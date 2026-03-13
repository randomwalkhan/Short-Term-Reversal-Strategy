from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import yfinance as yf
from reversal_universe import build_named_universe_map


def load_tickers_from_csv(csv_path: str | Path) -> list[str]:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Ticker csv not found -> {path}")

    df = pd.read_csv(path)
    if "ticker" not in df.columns:
        raise ValueError(f"{path}: expected a 'ticker' column")

    tickers = (
        df["ticker"]
        .astype(str)
        .str.strip()
        .str.upper()
    )
    return [ticker for ticker in tickers if ticker]


def ensure_qqq_only_filtered_csv(
    csv_path: str | Path,
    min_market_cap: float = 1e9,
    min_price: float = 10.0,
) -> list[str]:
    path = Path(csv_path)
    if path.exists():
        return load_tickers_from_csv(path)

    universe_map = build_named_universe_map(
        min_market_cap=min_market_cap,
        min_price=min_price,
    )
    qqq_only_filtered = universe_map["qqq_only_filtered"]
    pd.DataFrame({"ticker": qqq_only_filtered}).to_csv(path, index=False)
    return qqq_only_filtered


def download_reversal_data(ticker: str, start_date: str, end_date: str | None = None) -> pd.DataFrame:
    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
        threads=False,
    )

    if df.empty:
        return pd.DataFrame()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    required_cols = ["Open", "High", "Low", "Adj Close"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"{ticker}: missing required columns: {missing}")

    df = df[required_cols].copy().reset_index()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("Date").reset_index(drop=True)
    prev_adj_close = df["Adj Close"].shift(1)
    df["Max Drop"] = (prev_adj_close - df["Low"]) / prev_adj_close
    df = df.dropna(subset=["Date", "Open", "High", "Low", "Adj Close", "Max Drop"]).copy()
    df = df[["Date", "Open", "High", "Low", "Adj Close", "Max Drop"]]

    # Keep latest date first to match the rest of the project.
    return df.sort_values("Date", ascending=False).reset_index(drop=True)


def refresh_reversal_data(
    tickers: list[str],
    start_date: str = "2024-01-01",
    end_date: str | None = None,
    data_dir: str | Path = "reversal_data",
    skip_existing: bool = True,
) -> pd.DataFrame:
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []

    for ticker in tickers:
        out_path = data_path / f"{ticker}.csv"

        if skip_existing and out_path.exists():
            rows.append({
                "ticker": ticker,
                "status": "skipped_existing",
                "rows": pd.NA,
                "path": str(out_path),
            })
            continue

        try:
            df = download_reversal_data(ticker, start_date=start_date, end_date=end_date)
            if df.empty:
                rows.append({
                    "ticker": ticker,
                    "status": "empty",
                    "rows": 0,
                    "path": str(out_path),
                })
                continue

            df.to_csv(out_path, index=False)
            rows.append({
                "ticker": ticker,
                "status": "saved",
                "rows": len(df),
                "path": str(out_path),
            })
        except Exception as exc:
            rows.append({
                "ticker": ticker,
                "status": f"failed: {exc}",
                "rows": pd.NA,
                "path": str(out_path),
            })

    return pd.DataFrame(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download or refresh reversal CSV datasets.")
    parser.add_argument(
        "--tickers-csv",
        default="qqq_only_filtered_tickers.csv",
        help="CSV file with a ticker column.",
    )
    parser.add_argument(
        "--start-date",
        default="2024-01-01",
        help="Yahoo Finance start date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--end-date",
        default=None,
        help="Optional Yahoo Finance end date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--data-dir",
        default="reversal_data",
        help="Output directory for per-ticker CSV files.",
    )
    parser.add_argument(
        "--refresh-all",
        action="store_true",
        help="Refresh existing files instead of skipping them.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tickers = ensure_qqq_only_filtered_csv(args.tickers_csv)
    summary = refresh_reversal_data(
        tickers=tickers,
        start_date=args.start_date,
        end_date=args.end_date,
        data_dir=args.data_dir,
        skip_existing=not args.refresh_all,
    )

    print(summary.to_string(index=False))
    print("\nStatus counts:")
    print(summary["status"].value_counts(dropna=False).to_string())


if __name__ == "__main__":
    main()

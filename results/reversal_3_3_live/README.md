# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 14:45:01 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,772.50`
- Equity: `$16,772.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
    ZS           81.58               38            0.89              0.85        135.71                65.17            True
   XEL           90.00               10            1.40              0.78         79.15                20.53            True
   CSX           80.00               15            1.26              0.40         45.06                28.77            True
  CRWD           82.86               35            1.06              3.38        453.54                53.30            True
  FAST           84.62               13            2.20              0.69         44.38                39.66            True
  SNPS           93.55               31            1.28              4.32        482.04                50.93            True
  MSFT           80.95               21            1.32              3.97        427.55                30.07            True
  UPRO           90.32               31            1.14              1.00        125.26                42.06            True
  SHOP           95.12               41            0.73              0.63        121.78                56.59            True
  AVGO           92.11               38            0.51              1.42        399.22                43.25            True
   HON           84.62               13            1.53              2.29        211.95                25.70            True
  ADSK           88.89               36            0.82              1.35        234.27                45.23            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-29T14:40:03.710393-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-29T14:35:04.143140-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-29T14:30:01.439060-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-29T14:25:04.993410-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-29T14:10:06.997817-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T14:05:05.131403-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T14:00:12.028983-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T13:55:05.166783-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T13:40:10.019029-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:35:08.054699-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429144501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429144501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429144501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429144501)

</details>

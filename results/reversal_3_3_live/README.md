# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 10:35:07 EDT`
Last processed slot: `manage_1030`

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
  CDNS          100.00               12            2.73              6.21        322.67                53.80            True
   KDP           87.50               24            0.68              0.14         28.76                36.44            True
   XEL           94.12               17            1.01              0.56         79.24                20.53            True
  FAST           85.71               21            1.53              0.48         44.47                39.66            True
  SNPS           96.00               25            1.93              6.52        481.09                50.93            True
  ADSK           86.21               29            1.03              1.70        234.12                45.23            True
  WDAY           81.82               33            1.73              1.47        120.55                63.12            True
  MSFT           80.00               25            0.85              2.57        428.15                30.07            True
  DDOG           90.32               31            1.28              1.18        131.05                52.25            True
   WMT           86.36               22            1.07              0.95        127.18                26.10            True
   CSX           89.29               28            0.64              0.20         45.14                28.77            True
  TSLA           86.49               37            0.67              1.76        375.27                46.49            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-29T10:35:07.394496-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:30:03.700381-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:25:04.185468-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:20:03.810424-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "INTC260529C00084000", "fill_price": 8.85, "pnl": 1775.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.09, "ticker": "INTC"}
2026-04-29T10:10:03.767251-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:05:08.240355-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:00:04.620825-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:55:04.061412-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:40:03.886159-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:35:04.233499-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429103507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429103507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429103507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429103507)

</details>

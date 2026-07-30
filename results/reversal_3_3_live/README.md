# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 09:55:02 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           80.00               10            1.69              0.37         31.29                34.46         0.598          pass              0.060              0.0                           0.170                2.18              0.007                  ok            True                  False
   CSX           94.12               17            0.97              0.34         50.59                28.82         0.583          pass              0.481              0.0                           0.183                1.66              0.274                  ok            True                  False
  GILD           90.91               11            1.83              1.70        132.00                34.28         0.574          pass              0.435             26.6                           0.355                0.20             -0.131                  ok            True                  False
  VRTX           84.62               13            1.59              5.38        481.03                33.19         0.574          pass              0.323             40.9                           0.270               -0.14             -0.017                  ok            True                  False
  MNST           94.12               17            0.89              0.61         96.97                25.74         0.566          pass              0.697             72.3                           0.473               -1.68             -0.255                  ok            True                  False
   MAR          100.00               11            1.87              4.99        378.98                28.18         0.564          pass              0.593             43.3                           0.261                2.97              0.326                  ok            True                  False
  BKNG           88.24               17            2.24              3.16        199.95                45.62         0.556          pass              0.366             14.7                           0.227               12.55              0.731                  ok            True                  False
  ABNB           95.45               22            1.52              1.62        152.31                40.20         0.549          pass              0.661             42.1                           0.228                2.83              0.086                  ok            True                  False
  AMGN           93.75               16            1.47              4.00        385.93                27.22         0.542          pass              0.544             27.7                           0.295                7.51              0.726                  ok            True                  False
   HON           84.21               19            1.05              1.76        240.36                39.75         0.537          pass              0.310             27.9                           0.216                7.15              1.064                  ok            True                  False
  DASH           96.30               27            1.66              2.25        192.56                53.51         0.531          pass              0.657             30.3                           0.264                1.34             -0.053                  ok            True                  False
  ROST           88.46               26            0.79              1.39        251.36                27.49         0.517          pass              0.508             41.2                           0.294               13.14              1.047                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-30T09:55:02.964620-04:00      manage_1000               exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "FAST260918C00045000", "fill_price": 3.465, "pnl": -1732.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "FAST"}
2026-07-29T15:10:04.505433-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T15:05:04.399519-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T15:00:04.380256-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T14:55:04.522646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T14:50:04.497983-04:00       entry_1500              entry {"allocated_cash": 17325.0, "asset_type": "option", "contract_symbol": "FAST260918C00045000", "contracts": 45, "early_entry_score": 0.745, "entry_mode": "regular", "entry_option_price": 3.85, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 324.0, "option_spread_pct": 7.79, "option_volume": 33.0, "success_rate": 100.0, "ticker": "FAST", "timing_score": 0.573}
2026-07-29T14:50:04.497983-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-29", "training_samples": 5497, "window": 5}
2026-07-29T12:00:04.480323-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:55:04.538258-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:50:05.595902-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730095502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730095502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730095502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730095502)

</details>

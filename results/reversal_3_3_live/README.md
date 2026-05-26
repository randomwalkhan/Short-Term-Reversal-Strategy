# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 15:40:02 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26       30.350     36.1500  2320.0   19.110379 take_profit_day2_hit_at_scan
  SBUX     option         option SBUX260717C00105000     38          2026-05-22         2026-05-26        3.625      3.2625 -1377.5  -10.000000        stop_loss_hit_at_scan
  TTWO     option         option TTWO260717C00230000     15          2026-05-26         2026-05-26        9.800     11.3500  2325.0   15.816327 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.48               42            0.92              0.55         85.18               109.49         0.667          pass              0.777             77.0                           0.387               -3.06              0.037                                 ok            True                  False
  CSCO           81.82               11            1.71              1.44        119.79                52.25         0.634          pass              0.232             37.9                           0.654               19.88              1.890                                 ok            True                  False
  AMGN           92.86               14            1.03              2.44        338.26                27.24         0.585          pass              0.473             15.1                           0.322                2.66              0.208                                 ok            True                  False
  MELI           94.12               34            1.03             12.04       1659.26                60.80         0.566          pass              0.785             64.1                           0.509                5.77              0.719                                 ok            True                  False
  CTSH           82.35               17            1.78              0.66         52.47                46.65         0.545          pass              0.293             43.0                           0.335                5.94              1.309                                 ok            True                  False
   ROP           83.33               12            1.89              4.34        325.08                26.18         0.527          pass              0.178              7.8                           0.136               -2.45              0.039                                 ok            True                  False
  ROST           94.29               35            0.51              0.84        234.45                38.50         0.501          pass              0.799             67.1                           0.485                8.88              0.769                                 ok            True                  False
  SBUX          100.00                7            1.90              1.37        102.52                33.02         0.617          pass              0.507             15.2                           0.271               -3.78             -0.297            downtrend_blocked_slope           False                  False
   WMT           90.00               10            1.47              1.24        119.74                34.37         0.602          pass              0.401             24.7                           0.510               -7.12             -0.851 downtrend_blocked_slope_and_streak           False                  False
   AEP           76.47               17            0.40              0.37        131.43                25.20         0.597          pass              0.299             64.2                           0.441                0.28              0.069                                 ok           False                  False
   TRI           62.50                8            2.75              1.65         85.15                55.00         0.564          pass              0.061              1.7                           0.197               -5.70              0.040                                 ok           False                  False
  ORLY           83.33                6            2.42              1.55         91.07                38.39         0.558          pass              0.310             55.1                           0.765               -2.00              0.069                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-26T15:10:03.526476-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
2026-05-26T12:00:02.390044-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:45:01.347976-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526154002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526154002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526154002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526154002)

</details>

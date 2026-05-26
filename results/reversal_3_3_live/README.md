# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 15:05:01 EDT`
Last processed slot: `entry_1500`

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
  MELI           94.59               37            0.69              8.01       1660.99                60.80         0.569          pass              0.854             76.1                           0.718                6.14              0.735                                 ok            True                   True
  AMGN           87.50               16            0.99              2.35        338.29                27.24         0.567          pass              0.328             10.4                           0.304                2.70              0.210                                 ok            True                  False
   ADP          100.00               11            2.52              3.97        223.61                37.70         0.545          pass              0.483              7.4                           0.254                3.77              0.634                                 ok            True                  False
  CTSH           85.00               20            1.58              0.58         52.50                46.65         0.540          pass              0.402             49.4                           0.420                6.15              1.318                                 ok            True                  False
   ROP           88.89               18            1.55              3.55        325.42                26.18         0.514          pass              0.415             24.6                           0.519               -2.11              0.055                                 ok            True                  False
  TEAM           91.11               45            0.40              0.24         85.32               109.49         0.680          pass              0.834             90.1                           0.584               -2.55              0.061                                 ok           False                  False
  CSCO           80.00                5            2.57              2.17        119.48                52.25         0.621          pass              0.082              6.6                           0.151               18.84              1.851                                 ok           False                  False
  SBUX          100.00                7            1.92              1.39        102.52                33.02         0.616          pass              0.504             14.1                           0.327               -3.80             -0.298            downtrend_blocked_slope           False                  False
   TRI           78.57               14            1.97              1.19         85.35                55.00         0.595          pass              0.165             26.3                           0.275               -4.95              0.076                                 ok           False                  False
   AEP           75.00               16            0.53              0.49        131.38                25.20         0.594          pass              0.257             52.7                           0.339                0.15              0.063                                 ok           False                  False
   WMT           88.89                9            1.78              1.50        119.63                34.37         0.587          pass              0.322              8.7                           0.179               -7.42             -0.865 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00               48            0.06              0.06        133.90                66.43         0.572          pass              0.952             98.3                           0.579               15.94              1.675                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
2026-05-26T12:00:02.390044-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:45:01.347976-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:40:05.359008-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526150501)

</details>

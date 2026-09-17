# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:35:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           80.95               21            0.96              0.72        107.19                39.87         0.584          pass              0.168              3.7                           0.173                0.36              0.072                                 ok            True                  False
   TRI           93.33               30            1.12              0.79        100.97                57.96         0.583          pass              0.634             29.1                           0.406               -5.38             -0.561 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.74               19            0.08              0.01         24.72                25.04         0.564          pass              0.676             55.6                           0.345               -4.40             -0.307                                 ok           False                  False
  ADSK           85.71               28            1.41              2.17        219.38                56.33         0.537          pass              0.368             14.1                           0.243              -10.14             -0.491 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.00               40            0.80              0.76        134.68                64.77         0.523          pass              0.610             30.3                           0.269              -15.76             -1.349 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.24              0.07         42.41                15.25         0.521          pass              0.682             50.0                           0.380               -2.79             -0.423 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.15               26            0.49              0.95        272.78                24.48         0.518          pass              0.766             69.3                           0.703               -2.70             -0.144                                 ok           False                  False
  ADBE           97.22               36            0.69              1.21        249.98                47.92         0.516          pass              0.823             66.1                           0.724              -11.09             -1.055 downtrend_blocked_slope_and_streak           False                  False
  VRSK           85.71               14            2.24              2.86        180.53                41.00         0.515          pass              0.253              7.5                           0.181               -5.32             -0.383            downtrend_blocked_slope           False                  False
  INTU          100.00               36            0.51              1.14        317.64                44.10         0.510          pass              0.810             62.0                           0.517               -7.71             -0.547 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           92.31               13            2.00              0.33         23.59                34.54         0.508          pass              0.428              9.5                           0.184              -13.26             -1.371 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               17            0.66              0.62        134.08                14.34         0.507          pass              0.333              5.4                           0.207               -4.01             -0.371            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:30:05.183690-04:00 early_entry_1030 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:25:03.246728-04:00 early_entry_1025 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:20:02.157972-04:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-16T15:35:01.538068-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "PYPL261016C00055000", "fill_price": 1.116, "pnl": -3434.8, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-09-16T15:05:01.537613-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917103501)

</details>

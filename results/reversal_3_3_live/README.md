# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:40:05 EDT`
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
   WMT           84.00               25            0.87              0.66        107.22                39.87         0.570          pass              0.300             12.1                           0.192                0.44              0.076                                 ok            True                  False
   ADP           95.45               22            0.62              1.18        272.68                24.48         0.534          pass              0.719             61.7                           0.505               -2.82             -0.149                                 ok            True                  False
   TRI           92.86               28            1.21              0.86        100.94                57.96         0.589          pass              0.591             23.1                           0.325               -5.47             -0.565 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.44               18            0.24              0.04         24.71                25.04         0.559          pass              0.583             29.4                           0.247               -4.55             -0.314            downtrend_blocked_slope           False                  False
   EXC           95.00               20            0.28              0.08         42.40                15.25         0.529          pass              0.640             40.0                           0.338               -2.84             -0.426 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.88               32            0.95              1.66        249.79                47.92         0.524          pass              0.760             53.5                           0.483              -11.32             -1.067 downtrend_blocked_slope_and_streak           False                  False
  CHTR           89.74               39            0.88              0.83        134.64                64.77         0.524          pass              0.575             23.2                           0.225              -15.83             -1.353 downtrend_blocked_slope_and_streak           False                  False
  ADSK           85.19               27            1.77              2.74        219.14                56.33         0.519          pass              0.304              0.0                           0.257              -10.48             -0.508 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               31            0.97              2.17        317.20                44.10         0.512          pass              0.675             27.9                           0.327               -8.14             -0.568 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               17            0.59              0.55        134.10                14.34         0.511          pass              0.365             15.9                           0.233               -3.94             -0.368            downtrend_blocked_slope           False                  False
  PAYX           86.96               23            0.91              0.74        116.40                25.45         0.501          pass              0.410             29.3                           0.375               -6.73             -0.613            downtrend_blocked_slope           False                  False
 CMCSA           85.71               14            1.88              0.31         23.60                34.54         0.500          pass              0.275             15.2                           0.241              -13.15             -1.365 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-09-17T10:40:05.311687-04:00 early_entry_1040 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:35:01.165987-04:00 early_entry_1035 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:30:05.183690-04:00 early_entry_1030 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:25:03.246728-04:00 early_entry_1025 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:20:02.157972-04:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-16T15:35:01.538068-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "PYPL261016C00055000", "fill_price": 1.116, "pnl": -3434.8, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917104005)

</details>

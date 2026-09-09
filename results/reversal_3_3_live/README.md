# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 12:40:04 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$39,968.10`
- Equity: `$74,223.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-2,925.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 34255.0         14.3          13.18      209.63        207.84          bid_ask_mid                      13.18                bid_ask_mid                    True         -2925.0                  -7.87         88.89               36              1.63         52.75           52.62                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           82.35               34            1.41              1.34        135.94               103.38         0.665          pass              0.433             48.0                           0.452                6.13              0.914                                 ok            True                  False
  CRWD           89.74               39            0.91              1.34        209.44                89.86         0.660          pass              0.599             26.7                           0.281               12.26              0.577                                 ok            True                  False
  PANW           85.71               42            0.61              1.44        336.36                67.50         0.561          pass              0.567             53.0                           0.381               -1.46             -0.813                                 ok            True                  False
  NVDA           90.91               33            0.71              1.12        225.25                44.12         0.540          pass              0.582             27.9                           0.310                5.20              0.631                                 ok            True                  False
  CPRT           85.71               21            1.79              0.41         32.42                44.55         0.523          pass              0.374             32.0                           0.435               -3.95             -0.103                                 ok            True                  False
   CEG           90.48               21            1.08              2.26        298.08                32.90         0.502          pass              0.589             62.0                           0.651                6.25              0.779                                 ok            True                  False
  UPRO           83.33               18            1.48              1.55        148.64                24.94         0.500          pass              0.266             24.6                           0.332               -1.90             -0.106                                 ok            True                  False
   KHC          100.00               14            0.38              0.07         24.87                28.58         0.620          pass              0.700             70.3                           0.703               -0.47              0.066                                 ok           False                  False
  PYPL           96.30               27            0.79              0.29         53.05                58.35         0.617          pass              0.796             73.8                           0.584              -15.06             -1.441 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.43               35            1.02              1.33        185.71                77.37         0.615          pass              0.624             30.4                           0.430               -5.16             -0.261            downtrend_blocked_slope           False                  False
  AMGN           96.55               29            0.48              1.32        392.60                44.47         0.586          pass              0.740             51.5                           0.313              -11.52             -0.891 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                7            1.23              1.19        137.94                16.46         0.571          pass              0.516             19.6                           0.484               -2.86             -0.215                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-09T12:00:03.976220-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:55:03.977367-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:50:04.576506-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:45:06.789046-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:40:01.867073-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:35:06.764095-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:30:02.001507-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:25:05.081609-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:20:06.529747-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:15:03.937186-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909124004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909124004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909124004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909124004)

</details>

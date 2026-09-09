# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 13:10:03 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$75,458.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-1,690.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 35490.0         14.3          13.65      209.63        208.37          bid_ask_mid                      13.65                bid_ask_mid                    True         -1690.0                  -4.55         88.89               36              1.63         52.75           53.85                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           82.35               34            1.32              1.26        135.98               103.38         0.670          pass              0.443             51.1                           0.410                6.22              0.918                                 ok            True                  False
  CRWD           90.24               41            0.81              1.20        209.51                89.86         0.655          pass              0.643             34.7                           0.413               12.37              0.582                                 ok            True                  False
   EXC          100.00               10            0.88              0.27         43.83                15.52         0.564          pass              0.513             18.9                           0.313               -0.75             -0.004                                 ok            True                  False
   AEP           83.33               12            0.92              0.81        125.07                16.51         0.545          pass              0.227             23.3                           0.333                1.22              0.199                                 ok            True                  False
  NVDA           90.91               33            0.72              1.14        225.24                44.12         0.540          pass              0.579             26.9                           0.394                5.19              0.631                                 ok            True                  False
  CPRT           85.71               21            1.89              0.43         32.42                44.55         0.518          pass              0.363             28.5                           0.310               -4.04             -0.107                                 ok            True                  False
   CEG           87.50               16            1.31              2.74        297.87                32.90         0.516          pass              0.453             53.8                           0.358                6.00              0.769                                 ok            True                  False
   XEL           91.67               12            1.55              0.83         76.52                17.22         0.512          pass              0.431             18.5                           0.335               -1.94             -0.183                                 ok            True                  False
  WDAY           91.43               35            0.91              1.19        185.77                77.37         0.622          pass              0.647             37.7                           0.450               -5.06             -0.256            downtrend_blocked_slope           False                  False
   KHC          100.00               13            0.46              0.08         24.87                28.58         0.621          pass              0.674             64.1                           0.561               -0.55              0.062                                 ok           False                  False
  AMGN          100.00               23            0.71              1.95        392.33                44.47         0.612          pass              0.633             28.4                           0.216              -11.73             -0.902 downtrend_blocked_slope_and_streak           False                  False
  PYPL           96.55               29            0.75              0.28         53.06                58.35         0.608          pass              0.812             75.0                           0.524              -15.03             -1.439 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909131003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909131003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909131003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909131003)

</details>

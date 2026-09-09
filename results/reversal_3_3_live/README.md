# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 13:15:06 EDT`
Last processed slot: `manual`

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
- Equity: `$74,873.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-2,275.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 34905.0         14.3          13.42      209.63        208.46          bid_ask_mid                      13.42                bid_ask_mid                    True         -2275.0                  -6.12         88.89               36              1.63         52.75           53.52                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               36            1.12              1.07        136.06               103.38         0.671          pass              0.505             58.7                           0.499                6.44              0.927                                 ok            True                  False
  CRWD           90.48               42            0.75              1.10        209.55                89.86         0.653          pass              0.666             40.3                           0.423               12.45              0.585                                 ok            True                  False
  NVDA           91.67               36            0.60              0.94        225.33                44.12         0.530          pass              0.655             39.3                           0.475                5.32              0.636                                 ok            True                  False
  CPRT           86.36               22            1.70              0.39         32.43                44.55         0.524          pass              0.408             35.5                           0.491               -3.86             -0.099                                 ok            True                  False
   XEL           91.67               12            1.55              0.84         76.52                17.22         0.512          pass              0.430             18.2                           0.381               -1.95             -0.183                                 ok            True                  False
   KHC          100.00               13            0.42              0.07         24.87                28.58         0.623          pass              0.684             67.2                           0.584               -0.51              0.064                                 ok           False                  False
  WDAY           91.43               35            0.94              1.22        185.76                77.37         0.620          pass              0.641             36.0                           0.394               -5.09             -0.257            downtrend_blocked_slope           False                  False
  PYPL           96.67               30            0.70              0.26         53.07                58.35         0.606          pass              0.825             76.9                           0.636              -14.98             -1.436 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                5            1.44              1.39        137.85                16.46         0.571          pass              0.475              6.1                           0.135               -3.06             -0.224                                 ok           False                  False
  PAYX          100.00               13            1.48              1.21        116.41                30.90         0.570          pass              0.512             11.7                           0.336               -7.83             -0.767            downtrend_blocked_slope           False                  False
   EXC          100.00                9            0.91              0.28         43.83                15.52         0.568          pass              0.504             15.8                           0.330               -0.78             -0.006                                 ok           False                  False
  PANW           86.05               43            0.50              1.18        336.48                67.50         0.562          pass              0.602             61.5                           0.437               -1.35             -0.808                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909131506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909131506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909131506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909131506)

</details>

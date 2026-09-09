# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 14:35:06 EDT`
Last processed slot: `manage_1430`

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
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 34255.0         14.3          13.18      209.63        207.83          bid_ask_mid                      13.18                bid_ask_mid                    True         -2925.0                  -7.87         88.89               36              1.63         52.75           52.89                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.65               31            1.92              1.83        135.73               103.38         0.651          pass              0.309             29.0                           0.220                5.57              0.890                                 ok            True                  False
  CRWD           89.74               39            1.10              1.62        209.33                89.86         0.649          pass              0.554             11.8                           0.216               12.05              0.569                                 ok            True                  False
  WDAY           91.89               37            0.55              0.72        185.97                77.37         0.632          pass              0.747             62.3                           0.622               -4.72             -0.240                                 ok            True                   True
   PEP           92.86               14            0.74              0.71        138.14                16.46         0.549          pass              0.580             51.9                           0.700               -2.37             -0.192                                 ok            True                  False
  NVDA           91.18               34            0.67              1.06        225.28                44.12         0.537          pass              0.607             31.8                           0.359                5.24              0.633                                 ok            True                  False
   AEP           91.30               23            0.50              0.44        125.23                16.51         0.511          pass              0.613             58.0                           0.598                1.65              0.218                                 ok            True                  False
  CPRT           81.48               27            1.30              0.30         32.47                44.55         0.511          pass              0.356             50.6                           0.669               -3.47             -0.080                                 ok            True                  False
   CEG           85.71               14            1.62              3.39        297.60                32.90         0.507          pass              0.358             42.9                           0.320                5.67              0.754                                 ok            True                  False
  PYPL           95.45               22            0.96              0.36         53.03                58.35         0.635          pass              0.748             68.1                           0.445              -15.21             -1.448 downtrend_blocked_slope_and_streak           False                  False
   STX           86.84               38            0.09              0.58        904.13                74.46         0.624          pass              0.717             95.2                           0.468                9.97              0.588                                 ok           False                  False
   KHC          100.00               17            0.30              0.05         24.88                28.58         0.606          pass              0.737             76.6                           0.513               -0.39              0.070                                 ok           False                  False
  AMGN           96.88               32            0.31              0.85        392.81                44.47         0.579          pass              0.811             68.9                           0.568              -11.37             -0.884 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909143506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909143506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909143506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909143506)

</details>

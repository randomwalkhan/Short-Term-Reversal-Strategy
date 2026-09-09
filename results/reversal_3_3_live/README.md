# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:20:01 EDT`
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

- Cash: `$39,968.10`
- Equity: `$78,838.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$1,690.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 38870.0         14.3          14.95      209.63        208.65          bid_ask_mid                      14.95                bid_ask_mid                    True          1690.0                   4.55         88.89               36              1.63         52.75           58.06                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           84.21               38            0.74              0.71        136.22               103.38         0.697          pass              0.369              0.0                           0.150                6.84              0.945                                 ok            True                  False
  CRWD           91.11               45            0.54              0.80        209.68                89.86         0.653          pass              0.637             25.0                           0.180               12.68              0.594                                 ok            True                  False
   PEP          100.00               11            0.82              0.79        138.11                16.46         0.576          pass              0.495             10.3                           0.199               -2.45             -0.195                                 ok            True                  False
  NVDA           90.62               32            0.92              1.46        225.11                44.12         0.534          pass              0.483              0.0                           0.163                4.98              0.621                                 ok            True                  False
  CPRT           86.36               22            1.61              0.37         32.44                44.55         0.529          pass              0.419             39.0                           0.615               -3.77             -0.094                                 ok            True                  False
  LRCX           80.00               35            0.91              2.04        319.54                52.73         0.522          pass              0.382             54.5                           0.482                0.90             -0.065                                 ok            True                  False
  TMUS           93.33               15            1.41              1.79        180.92                25.45         0.502          pass              0.512             24.4                           0.315               -0.80              0.199                                 ok            True                  False
  MSFT           88.89               27            0.73              2.52        492.87                23.28         0.501          pass              0.412              3.9                           0.088               -0.28             -0.091                                 ok            True                  False
   STX           86.84               38            0.10              0.63        904.11                74.46         0.629          pass              0.716             94.8                           0.660                9.96              0.588                                 ok           False                  False
  WDAY           91.43               35            0.79              1.03        185.84                77.37         0.629          pass              0.672             45.8                           0.435               -4.94             -0.251            downtrend_blocked_slope           False                  False
   KHC          100.00               13            0.46              0.08         24.87                28.58         0.621          pass              0.674             64.1                           0.695               -0.55              0.062                                 ok           False                  False
  PYPL           94.12               34            0.34              0.13         53.13                58.35         0.601          pass              0.863             88.8                           0.783              -14.68             -1.420 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-09T10:20:01.984247-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:15:03.852683-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-09-08T14:55:03.619621-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909102001)

</details>

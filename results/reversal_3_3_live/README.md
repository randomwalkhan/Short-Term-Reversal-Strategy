# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$53,034.30`
- Equity: `$103,221.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-1,925.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 50187.5         9.48           9.12      160.14        159.32          bid_ask_mid                       9.12                bid_ask_mid                    True         -1925.0                  -3.69         83.33               12               2.4         42.26           43.04                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           80.00               20            1.02              0.84        117.58                34.67         0.565          pass              0.136              4.4                           0.106               10.11              1.082                                 ok            True                  False
  SNPS           80.65               31            0.91              3.23        503.79                54.22         0.558          pass              0.289             25.3                           0.270               21.18              2.319                                 ok            True                  False
  UPRO           91.67               12            2.01              2.21        155.46                30.90         0.547          pass              0.391              4.0                           0.314                1.97              0.296                                 ok            True                  False
   KDP           94.74               19            0.98              0.21         31.04                26.61         0.534          pass              0.549             14.1                           0.282               -2.24             -0.194                                 ok            True                  False
  MPWR           83.33               18            2.97             30.62       1460.57                53.62         0.530          pass              0.280             28.3                           0.498                5.65              0.955                                 ok            True                  False
  DASH           80.95               21            2.11              2.87        192.39                42.81         0.515          pass              0.150              0.0                           0.288                0.13              0.182                                 ok            True                  False
  SHOP           86.49               37            1.02              1.18        163.93                52.70         0.502          pass              0.538             44.9                           0.545               14.34              1.481                                 ok            True                  False
    ZS           93.33               45            0.28              0.42        212.07                73.32         0.617          pass              0.833             71.8                           0.460               -1.30             -0.003                                 ok           False                  False
  SOXL           79.17               24            4.95              5.69        161.82               111.15         0.595          pass              0.263             36.7                           0.637                6.76              1.234                                 ok           False                  False
  QCOM           85.71               28            1.15              1.46        180.40                56.22         0.588          pass              0.480             49.6                           0.565               -9.28             -1.037 downtrend_blocked_slope_and_streak           False                  False
  META           58.33               12            2.08             10.76        734.27                55.45         0.587          pass              0.120             16.1                           0.368               -2.77             -0.333            downtrend_blocked_slope           False                  False
   STX           88.89               36            0.31              1.77        804.87                69.91         0.584          pass              0.738             89.8                           0.871              -13.00             -1.267            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T10:45:05.752801-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:40:04.683000-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:35:06.455720-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:30:05.764832-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:05.803343-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:20:04.740401-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:15:04.665736-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:05:05.843456-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:06.491610-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007104505)

</details>

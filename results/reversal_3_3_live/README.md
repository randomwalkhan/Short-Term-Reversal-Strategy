# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:40:04 EDT`
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

- Cash: `$53,034.30`
- Equity: `$102,671.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-2,475.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 49637.5         9.48           9.02      160.14        159.64          bid_ask_mid                       9.02                bid_ask_mid                    True         -2475.0                  -4.75         83.33               12               2.4         42.26           42.59                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.50               40            0.57              0.85        211.89                73.32         0.629          pass              0.724             42.7                           0.358               -1.59             -0.016                                 ok            True                  False
  CSCO           80.95               21            0.91              0.75        117.62                34.67         0.566          pass              0.201             15.1                           0.187               10.23              1.088                                 ok            True                  False
  SNPS           80.65               31            0.90              3.17        503.81                54.22         0.559          pass              0.293             26.6                           0.263               21.20              2.320                                 ok            True                  False
  MPWR           84.21               19            2.72             28.07       1461.66                53.62         0.539          pass              0.329             34.3                           0.655                5.92              0.967                                 ok            True                  False
   KDP           95.00               20            0.85              0.19         31.05                26.61         0.537          pass              0.590             23.2                           0.294               -2.11             -0.188                                 ok            True                  False
  UPRO           86.67               15            1.79              1.96        155.57                30.90         0.536          pass              0.294              9.7                           0.330                2.20              0.306                                 ok            True                  False
  SHOP           84.62               39            0.78              0.90        164.06                52.70         0.502          pass              0.541             58.2                           0.641               14.63              1.493                                 ok            True                  False
  SOXL           79.17               24            4.56              5.24        162.01               111.15         0.615          pass              0.280             41.7                           0.735                7.20              1.253                                 ok           False                  False
  QCOM           85.71               28            1.14              1.44        180.41                56.22         0.589          pass              0.482             50.3                           0.613               -9.26             -1.036 downtrend_blocked_slope_and_streak           False                  False
  META           58.33               12            2.14             11.05        734.14                55.45         0.584          pass              0.113             13.9                           0.314               -2.82             -0.336            downtrend_blocked_slope           False                  False
   STX           86.84               38            0.11              0.64        805.36                69.91         0.581          pass              0.716             96.3                           0.894              -12.83             -1.258            downtrend_blocked_slope           False                  False
   CEG           80.00                5            3.23              6.80        297.49                58.89         0.569          pass              0.149             30.7                           0.302               10.16              0.947                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T10:40:04.683000-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:35:06.455720-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:30:05.764832-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:05.803343-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:20:04.740401-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:15:04.665736-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:05:05.843456-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:06.491610-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T00:00:06.148407-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007104004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007104004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007104004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007104004)

</details>

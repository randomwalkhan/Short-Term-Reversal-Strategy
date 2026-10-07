# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 11:10:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$101,571.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-3,575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 48537.5         9.48           8.82      160.14        159.47          bid_ask_mid                       8.82                bid_ask_mid                    True         -3575.0                  -6.86         83.33               12               2.4         42.26            42.1                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           85.71               28            0.56              0.47        117.74                34.67         0.548          pass              0.480             51.1                           0.586               10.62              1.103                                 ok            True                  False
   KDP           95.00               20            0.85              0.19         31.05                26.61         0.536          pass              0.596             25.4                           0.332               -2.11             -0.188                                 ok            True                  False
  UPRO           86.67               15            1.79              1.96        155.57                30.90         0.535          pass              0.314             16.4                           0.355                2.20              0.306                                 ok            True                  False
  SNPS           82.50               40            0.56              1.98        504.32                54.22         0.527          pass              0.482             54.1                           0.517               21.61              2.335                                 ok            True                  False
  MPWR           80.00               15            3.51             36.18       1458.18                53.62         0.516          pass              0.131             15.3                           0.187                5.06              0.930                                 ok            True                  False
  DASH           80.00               25            1.82              2.47        192.56                42.81         0.505          pass              0.217             22.2                           0.345                0.43              0.196                                 ok            True                  False
    ZS           93.33               45            0.30              0.44        212.06                73.32         0.616          pass              0.828             70.1                           0.565               -1.32             -0.004                                 ok           False                  False
  META           61.54               13            1.93             10.01        734.59                55.45         0.593          pass              0.145             22.0                           0.481               -2.62             -0.327            downtrend_blocked_slope           False                  False
   CEG           85.71                7            2.83              5.95        297.85                58.89         0.585          pass              0.329             39.3                           0.473               10.62              0.966                                 ok           False                  False
  QCOM           84.00               25            1.55              1.97        180.19                56.22         0.581          pass              0.361             32.1                           0.215               -9.65             -1.055 downtrend_blocked_slope_and_streak           False                  False
  SOXL           79.17               24            5.31              6.11        161.64               111.15         0.575          pass              0.247             32.0                           0.410                6.35              1.217                                 ok           False                  False
   STX           88.89               36            0.49              2.79        804.44                69.91         0.573          pass              0.719             83.9                           0.628              -13.16             -1.275            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T11:10:05.726059-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:05:04.782833-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:00:05.677909-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:55:05.731047-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:50:04.594870-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:45:05.752801-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:40:04.683000-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:35:06.455720-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:30:05.764832-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:05.803343-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007111005)

</details>

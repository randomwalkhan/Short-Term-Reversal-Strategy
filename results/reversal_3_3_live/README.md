# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:20:04 EDT`
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
- Equity: `$103,084.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-2,062.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 50050.0         9.48            9.1      160.14        159.08          bid_ask_mid                        9.1                bid_ask_mid                    True         -2062.5                  -3.96         83.33               12               2.4         42.26           44.02                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           84.62               13            2.25              4.73        298.37                58.89         0.580          pass              0.356             51.7                           0.575               11.28              0.993                                 ok            True                  False
  CSCO           85.19               27            0.63              0.52        117.72                34.67         0.551          pass              0.430             41.3                           0.412               10.55              1.101                                 ok            True                  False
  UPRO           86.67               15            1.73              1.89        155.60                30.90         0.540          pass              0.304             12.9                           0.266                2.27              0.309                                 ok            True                  False
   KDP           94.74               19            0.98              0.21         31.04                26.61         0.536          pass              0.516              3.2                           0.041               -2.24             -0.194                                 ok            True                  False
  SNPS           82.50               40            0.51              1.80        504.40                54.22         0.529          pass              0.495             58.3                           0.398               21.68              2.338                                 ok            True                  False
  MPWR           82.35               17            3.11             32.11       1459.93                53.62         0.528          pass              0.237             24.8                           0.329                5.49              0.949                                 ok            True                  False
  CRWD           80.00               20            2.76              5.38        276.55                55.11         0.525          pass              0.192             24.2                           0.409                3.31              0.706                                 ok            True                  False
  DASH           80.00               25            1.91              2.59        192.51                42.81         0.503          pass              0.168              6.0                           0.128                0.35              0.192                                 ok            True                  False
  META           58.33               12            2.06             10.64        734.32                55.45         0.589          pass              0.104             10.5                           0.270               -2.74             -0.332            downtrend_blocked_slope           False                  False
  QCOM           85.71               28            1.18              1.50        180.39                56.22         0.586          pass              0.476             48.4                           0.697               -9.30             -1.038 downtrend_blocked_slope_and_streak           False                  False
  SOXL           79.17               24            5.12              5.89        161.74               111.15         0.586          pass              0.255             34.5                           0.674                6.56              1.226                                 ok           False                  False
   STX           87.88               33            1.01              5.69        803.19                69.91         0.561          pass              0.621             67.1                           0.752              -13.61             -1.299            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T10:20:04.740401-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:15:04.665736-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:05:05.843456-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:06.491610-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T00:00:06.148407-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
2026-10-06T15:10:04.494335-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-06T15:05:04.280902-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-06T15:00:04.457281-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-06T14:55:01.305987-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007102004)

</details>

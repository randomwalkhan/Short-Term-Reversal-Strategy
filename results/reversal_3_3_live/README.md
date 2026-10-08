# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 10:30:06 EDT`
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

- Cash: `$47,804.30`
- Equity: `$107,204.30`
- Realized PnL: `$89,916.80`
- Unrealized PnL: `$7,287.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 59400.0         9.48           10.8      160.14        162.65          bid_ask_mid                       10.8                bid_ask_mid                    True          7287.5                  13.98         83.33               12               2.4         42.26           44.28                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.14               28            2.76              3.07        157.59               112.38         0.656            pass              0.438             64.9                           0.875                5.60              1.109                                 ok            True                  False
  MPWR           89.29               28            1.32             13.14       1420.35                55.22         0.571            pass              0.601             58.7                           0.786                5.52              0.865                                 ok            True                  False
  MSTR           91.67               36            1.07              1.15        152.88                80.80         0.616            pass              0.758             70.7                           0.819               -6.11             -0.132           downtrend_blocked_streak           False                  False
  QCOM           87.50               24            1.65              2.05        176.24                56.66         0.586            pass              0.461             36.3                           0.615              -10.33             -1.097 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.89               27            0.44              0.36        117.23                34.80         0.567            pass              0.594             62.3                           0.521                9.68              1.210                                 ok           False                  False
   STX           87.88               33            1.39              7.84        804.21                69.74         0.558            pass              0.582             54.1                           0.658              -12.09             -1.542            downtrend_blocked_slope           False                  False
  INTC           88.57               35            1.53              1.21        112.60                69.90         0.531            pass              0.635             62.1                           0.869              -12.56             -1.002 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           90.48               21            0.19              0.03         20.93                21.76         0.523            pass              0.643             79.5                           0.571               -4.09             -0.338            downtrend_blocked_slope           False                  False
  AMAT           82.93               41            0.05              0.20        520.57                48.66         0.521            pass              0.625             98.3                           0.988                9.72              1.067                                 ok           False                  False
  REGN           75.00                4            2.37             12.32        736.84                27.38         0.512            pass              0.051              0.0                           0.150               -8.98             -0.783            downtrend_blocked_slope           False                  False
  GILD           84.62               13            1.36              1.39        146.25                18.65         0.505            pass              0.205              3.9                           0.049               -3.23             -0.504 downtrend_blocked_slope_and_streak           False                  False
   TRI           85.19               27            1.60              1.11         98.80                44.07         0.499 below_threshold              0.371             23.0                           0.237               -2.62             -0.070                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-10-08T10:30:06.096812-04:00 early_entry_1030 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:25:06.880454-04:00 early_entry_1025 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:20:05.114713-04:00 early_entry_1020 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:15:04.991008-04:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:10:05.110275-04:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:05:06.592020-04:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:00:03.810887-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T09:50:06.393850-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "NVDA261120C00235000", "fill_price": 11.7675, "pnl": -5230.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "NVDA"}
2026-10-08T00:00:04.872922-04:00     data_refresh       data_refresh                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-10-07T15:10:05.672351-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008103006)

</details>

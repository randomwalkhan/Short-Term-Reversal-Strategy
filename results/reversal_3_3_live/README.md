# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 11:05:04 EDT`
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
- Equity: `$103,359.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-1,787.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 50325.0         9.48           9.15      160.14        159.15          bid_ask_mid                       9.15                bid_ask_mid                    True         -1787.5                  -3.43         83.33               12               2.4         42.26           43.05                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.50               40            0.52              0.77        211.92                73.32         0.631          pass              0.739             47.6                           0.445               -1.54             -0.014                                 ok            True                  False
  CSCO           85.71               28            0.55              0.45        117.75                34.67         0.549          pass              0.485             52.6                           0.557               10.64              1.104                                 ok            True                  False
  UPRO           91.67               12            1.98              2.16        155.48                30.90         0.548          pass              0.402              7.6                           0.235                2.01              0.298                                 ok            True                  False
   KDP           94.74               19            1.00              0.22         31.04                26.61         0.533          pass              0.544             12.7                           0.247               -2.26             -0.195                                 ok            True                  False
  SNPS           81.58               38            0.67              2.37        504.16                54.22         0.531          pass              0.418             45.2                           0.439               21.48              2.330                                 ok            True                  False
  MPWR           80.00               15            3.37             34.78       1458.78                53.62         0.523          pass              0.141             18.6                           0.237                5.21              0.936                                 ok            True                  False
  DASH           80.95               21            2.05              2.78        192.43                42.81         0.517          pass              0.188             12.6                           0.201                0.20              0.185                                 ok            True                  False
  NVDA           91.30               23            0.93              1.55        238.57                24.15         0.511          pass              0.499             19.9                           0.175                5.10              0.673                                 ok            True                  False
  META           58.33               12            1.97             10.17        734.52                55.45         0.594          pass              0.135             20.8                           0.458               -2.65             -0.328            downtrend_blocked_slope           False                  False
   STX           88.57               35            0.52              2.91        804.38                69.91         0.578          pass              0.703             83.2                           0.678              -13.18             -1.277            downtrend_blocked_slope           False                  False
  QCOM           84.00               25            1.71              2.17        180.10                56.22         0.572          pass              0.339             25.2                           0.180               -9.79             -1.062 downtrend_blocked_slope_and_streak           False                  False
   CEG           80.00                5            3.23              6.78        297.49                58.89         0.569          pass              0.149             30.8                           0.259               10.17              0.947                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T11:05:04.782833-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:00:05.677909-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:55:05.731047-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:50:04.594870-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:45:05.752801-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:40:04.683000-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:35:06.455720-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:30:05.764832-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:05.803343-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:20:04.740401-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007110504)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 10:45:02 EDT`
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

- Cash: `$19,710.25`
- Equity: `$29,655.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$570.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  9945.0        46.88          49.72      660.72        671.54          bid_ask_mid                      49.72                bid_ask_mid                    True           570.0                   6.08         81.82               22              1.27         53.38            51.9                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           88.24               17            2.66              5.70        303.11                65.52         0.559          pass              0.346              7.9                           0.103               -0.22              0.226                                 ok            True                  False
   LIN          100.00               13            1.17              4.29        520.70                20.66         0.558          pass              0.561             28.3                           0.364               -0.49             -0.298                                 ok            True                  False
   ADI           84.00               25            1.58              4.35        390.89                55.85         0.558          pass              0.341             26.2                           0.232               -2.68              0.061                                 ok            True                  False
   CSX           87.50               16            0.95              0.33         49.78                19.08         0.556          pass              0.398             34.0                           0.477                4.03              0.352                                 ok            True                  False
  NXPI           86.96               23            1.82              3.62        282.32                58.07         0.548          pass              0.404             25.6                           0.199               -0.83              0.234                                 ok            True                  False
   WBD           83.33               12            1.09              0.21         27.39                20.00         0.536          pass              0.216             20.0                           0.226                1.95              0.268                                 ok            True                  False
  KLAC           75.00               12            4.30              6.93        227.40               109.33         0.591          pass              0.104             10.4                           0.137              -26.93             -2.108 downtrend_blocked_slope_and_streak           False                  False
  AMAT           80.00               15            3.34             13.91        589.74                98.89         0.589          pass              0.149             19.1                           0.213              -20.36             -1.405 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.44               36            0.12              1.45       1775.02                66.00         0.587          pass              0.885             89.4                           0.460              -10.85             -0.714            downtrend_blocked_slope           False                  False
  QCOM           84.85               33            0.84              1.04        177.65                61.79         0.581          pass              0.446             35.0                           0.241               -4.43             -0.082           downtrend_blocked_streak           False                  False
  MCHP           96.00               25            2.24              1.36         86.53                68.63         0.555          pass              0.597             13.7                           0.154               -6.62             -0.297            downtrend_blocked_slope           False                  False
  MPWR           79.17               24            2.87             27.64       1364.57                84.79         0.552          pass              0.196             15.7                           0.157               -3.29              0.100                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-15T10:45:02.900716-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:40:04.846319-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:35:02.734120-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:30:03.936476-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:25:06.040216-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:20:02.772383-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:15:05.965611-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:10:03.001163-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:05:02.748975-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715104502)

</details>

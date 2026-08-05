# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:45:01 EDT`
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

- Cash: `$17,080.75`
- Equity: `$33,080.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 16000.0          4.1            4.0      138.68        139.11          bid_ask_mid                        4.0                bid_ask_mid                    True          -400.0                  -2.44         83.33               24              0.68          24.5           22.91                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
 CMCSA           83.33               12            1.40              0.25         24.82                44.00         0.617          pass              0.273             36.4                           0.639                4.51              1.002                       ok            True                  False
  CTAS           92.59               27            0.90              1.29        203.10                37.77         0.574          pass              0.619             37.6                           0.598                0.22             -0.099                       ok            True                  False
  VRSK           94.44               36            0.54              0.74        192.49                43.54         0.534          pass              0.781             56.3                           0.464               -0.28             -0.293                       ok            True                  False
  CPRT           82.61               23            1.58              0.33         29.26                38.86         0.507          pass              0.306             33.1                           0.490                6.50              0.628                       ok            True                  False
   WDC           82.86               35            0.22              0.85        548.19                99.34         0.713          pass              0.571             85.5                           0.373               -1.68              0.189 downtrend_blocked_streak           False                  False
  DRAM           77.42               31            1.51              0.58         54.64               109.93         0.687          pass              0.394             61.9                           0.332               -6.42             -0.619 downtrend_blocked_streak           False                  False
  TMUS           80.00                5            2.83              3.51        175.70                55.59         0.630          pass              0.111             16.1                           0.322               -9.82             -0.467  downtrend_blocked_slope           False                  False
  AMAT           88.00               25            2.32              8.89        542.81                87.24         0.619          pass              0.427             17.3                           0.176               -3.61             -0.352 downtrend_blocked_streak           False                  False
  SOXL           78.57               28            5.71              5.59        137.51               182.46         0.588          pass              0.218             13.2                           0.142              -18.06             -1.929 downtrend_blocked_streak           False                  False
  MSFT           81.58               38            0.34              1.17        492.31                57.86         0.568          pass              0.496             70.2                           0.655               25.82              3.090                       ok           False                  False
  LRCX           83.33               24            2.95              6.55        314.93                92.33         0.566          pass              0.278             12.9                           0.178               -3.42             -0.179 downtrend_blocked_streak           False                  False
  AMZN           83.33               48            0.04              0.08        277.39                61.32         0.562          pass              0.629             94.5                           0.703               13.26              2.050                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T10:45:01.734892-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:40:05.699069-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:35:01.163054-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:30:06.205244-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:25:05.700806-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:20:05.967417-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:00:04.700543-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805104501)

</details>

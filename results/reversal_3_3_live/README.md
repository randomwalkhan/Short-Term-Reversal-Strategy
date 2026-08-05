# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:50:01 EDT`
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

- Cash: `$17,080.75`
- Equity: `$33,680.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 16600.0          4.1           4.15      138.68        138.73          bid_ask_mid                       4.15                bid_ask_mid                    True           200.0                   1.22         83.33               24              0.68          24.5           24.92                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  CTAS           91.30               23            1.04              1.48        203.01                37.77         0.590          pass              0.532             28.1                           0.395                0.08             -0.105                       ok            True                  False
  PAYX          100.00               13            1.08              0.90        118.28                35.13         0.587          pass              0.674             65.0                           0.404                7.10              0.749                       ok            True                  False
  MRVL           80.00               35            1.82              2.78        217.40               100.52         0.578          pass              0.375             50.3                           0.288                1.72              0.258                       ok            True                  False
   KDP           80.00               20            0.68              0.15         31.04                28.75         0.558          pass              0.276             51.2                           0.496                2.28              0.458                       ok            True                  False
  VRSK           94.12               34            0.94              1.26        192.26                43.54         0.520          pass              0.663             24.8                           0.272               -0.67             -0.311                       ok            True                  False
  CPRT           85.00               20            1.90              0.39         29.23                38.86         0.511          pass              0.309             19.4                           0.346                6.15              0.613                       ok            True                  False
  DRAM           76.47               34            0.89              0.34         54.74               109.93         0.706          pass              0.463             77.5                           0.511               -5.83             -0.590 downtrend_blocked_streak           False                  False
  TEAM           85.37               41            0.01              0.01        110.31                86.98         0.642          pass              0.704             98.8                           0.512               29.15              2.885                       ok           False                  False
  SOXL           78.57               28            4.96              4.85        137.82               182.46         0.641          pass              0.258             24.6                           0.214              -17.41             -1.893 downtrend_blocked_streak           False                  False
  AMAT           89.29               28            1.81              6.92        543.66                87.24         0.636          pass              0.538             35.6                           0.288               -3.10             -0.328 downtrend_blocked_streak           False                  False
  TMUS           80.00                5            3.05              3.78        175.59                55.59         0.616          pass              0.090              9.6                           0.253              -10.02             -0.477  downtrend_blocked_slope           False                  False
 CMCSA           77.78                9            1.87              0.33         24.79                44.00         0.598          pass              0.106             15.5                           0.357                4.02              0.981                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T10:50:01.771343-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:45:01.734892-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:40:05.699069-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:35:01.163054-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:30:06.205244-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:25:05.700806-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:20:05.967417-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805105001)

</details>

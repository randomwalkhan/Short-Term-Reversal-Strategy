# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:20:05 EDT`
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

- Cash: `$17,080.75`
- Equity: `$33,680.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 16600.0          4.1           4.15      138.68        138.54          bid_ask_mid                       4.15                bid_ask_mid                    True           200.0                   1.22         83.33               24              0.68          24.5           25.85                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            1.05              1.60        217.90               100.52         0.632          pass              0.444             71.3                           0.434                2.52              0.294                       ok            True                  False
 CMCSA           81.82               11            1.70              0.30         24.80                44.00         0.602          pass              0.183             22.7                           0.293                4.19              0.988                       ok            True                  False
  MDLZ           94.74               19            0.71              0.31         61.95                31.68         0.598          pass              0.627             38.0                           0.351                1.28              0.290                       ok            True                  False
  CTAS           91.67               24            1.00              1.43        203.04                37.77         0.586          pass              0.555             30.7                           0.353                0.12             -0.103                       ok            True                  False
   KDP           80.00               20            0.69              0.15         31.04                28.75         0.557          pass              0.272             50.0                           0.409                2.27              0.457                       ok            True                  False
  CPRT           85.71               21            1.77              0.36         29.24                38.86         0.514          pass              0.353             25.2                           0.266                6.29              0.619                       ok            True                  False
  GILD           90.91               11            2.09              1.98        134.40                28.84         0.506          pass              0.403             18.2                           0.192                1.60              0.205                       ok            True                  False
  SOXL           80.00               35            2.27              2.23        138.95               182.46         0.773          pass              0.431             62.4                           0.375              -15.08             -1.766 downtrend_blocked_streak           False                  False
  DRAM           75.00               36            0.20              0.08         54.86               109.93         0.734          pass              0.532             95.0                           0.749               -5.18             -0.559 downtrend_blocked_streak           False                  False
  AMAT           91.43               35            0.86              3.30        545.20                87.24         0.666          pass              0.705             55.6                           0.333               -2.17             -0.285 downtrend_blocked_streak           False                  False
  LRCX           86.67               30            1.39              3.09        316.41                92.33         0.650          pass              0.494             39.2                           0.261               -1.87             -0.107 downtrend_blocked_streak           False                  False
  TMUS           80.00                5            2.84              3.53        175.70                55.59         0.631          pass              0.099             11.8                           0.194               -9.83             -0.467  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T10:20:05.967417-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:00:04.700543-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T00:00:04.689271-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-04T15:10:06.388254-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-04T15:05:01.446900-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-04T15:00:05.343102-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-08-04T14:55:02.363501-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805102005)

</details>

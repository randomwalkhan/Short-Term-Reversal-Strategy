# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:35:01 EDT`
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
- Equity: `$33,080.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 16000.0          4.1            4.0      138.68         138.7          bid_ask_mid                        4.0                bid_ask_mid                    True          -400.0                  -2.44         83.33               24              0.68          24.5           23.89                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           83.33               12            1.56              0.27         24.81                44.00         0.606          pass              0.250             29.1                           0.424                4.34              0.995                                 ok            True                  False
  CTAS           91.30               23            1.01              1.43        203.04                37.77         0.592          pass              0.539             30.5                           0.411                0.12             -0.103                                 ok            True                  False
   KDP           80.00               20            0.68              0.15         31.04                28.75         0.558          pass              0.276             51.2                           0.452                2.28              0.458                                 ok            True                  False
  PAYX          100.00               23            0.51              0.42        118.48                35.13         0.557          pass              0.793             83.6                           0.606                7.72              0.775                                 ok            True                  False
  CPRT           85.00               20            1.80              0.37         29.24                38.86         0.517          pass              0.323             23.7                           0.414                6.26              0.618                                 ok            True                  False
  DRAM           76.47               34            0.97              0.37         54.73               109.93         0.702          pass              0.457             75.7                           0.557               -5.90             -0.594           downtrend_blocked_streak           False                  False
  SOXL           79.31               29            4.32              4.23        138.09               182.46         0.683          pass              0.280             28.5                           0.171              -16.86             -1.863           downtrend_blocked_streak           False                  False
  AMAT           88.46               26            1.98              7.57        543.37                87.24         0.644          pass              0.414              5.8                           0.137               -3.27             -0.336           downtrend_blocked_streak           False                  False
  TMUS           83.33                6            2.70              3.35        175.78                55.59         0.637          pass              0.213             20.1                           0.260               -9.69             -0.460            downtrend_blocked_slope           False                  False
  MDLZ           91.67               24            0.31              0.13         62.02                31.68         0.586          pass              0.683             73.2                           0.690                1.69              0.308                                 ok           False                  False
  AAPL           96.00               25            0.82              1.79        308.61                38.19         0.582          pass              0.679             40.4                           0.309               -5.85             -0.845 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            2.01              3.07        217.27               100.52         0.570          pass              0.352             45.1                           0.260                1.52              0.249                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T10:35:01.163054-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:30:06.205244-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:25:05.700806-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:20:05.967417-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:00:04.700543-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T00:00:04.689271-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-04T15:10:06.388254-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805103501)

</details>

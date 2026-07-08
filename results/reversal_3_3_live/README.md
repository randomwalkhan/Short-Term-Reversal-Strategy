# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-08 11:17:31 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$13,056.75`
- Equity: `$25,881.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260821C00047500       2026-07-07                   1     54     12690.0                 12825.0         2.35           2.38       48.48         48.12          bid_ask_mid                       2.38                bid_ask_mid                    True           135.0                   1.06          91.3               23              0.68         28.35           32.89                  21.52                2967.0           20.0               0.09                      ok
```

## Today's Closed Trades (2026-07-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ASML           94.12               34            0.58              7.13       1744.23                75.63         0.627            pass              0.824             75.0                           0.418               -2.33             -0.208                      ok            True                  False
   KDP          100.00               15            0.73              0.16         31.42                33.17         0.566            pass              0.693             67.6                           0.580                1.98              0.071                      ok            True                  False
   ADP           91.67               12            1.60              2.76        244.42                31.95         0.556            pass              0.465             28.4                           0.291                9.60              1.285                      ok            True                  False
  PAYX          100.00               15            1.54              1.17        107.62                32.70         0.553            pass              0.628             46.5                           0.422                8.63              1.171                      ok            True                  False
  PCAR           90.00               10            2.23              1.94        123.63                37.78         0.553            pass              0.325              1.1                           0.207                4.20              0.499                      ok            True                  False
  GILD           88.46               26            0.64              0.61        136.10                35.29         0.540            pass              0.546             53.2                           0.400                8.35              0.845                      ok            True                  False
   CSX           90.00               20            0.79              0.27         48.39                21.11         0.523            pass              0.386              0.0                           0.150                4.26              0.508                      ok            True                  False
  GOOG           81.82               22            1.41              3.58        362.08                34.43         0.508            pass              0.214             11.7                           0.198                3.59              0.656                      ok            True                  False
  IDXX           90.91               11            2.68             10.71        565.66                37.15         0.500            pass              0.427             26.6                           0.486                2.52              0.323                      ok            True                  False
   KHC           80.00               30            0.85              0.15         25.24                37.35         0.500 below_threshold              0.297             38.0                           0.295               11.64              1.163                      ok            True                  False
  SOXL           90.00               30            1.64              1.90        164.47               233.51         0.831            pass              0.737             84.7                           0.454              -29.75             -3.900 downtrend_blocked_slope           False                  False
  DRAM           86.36               22            2.48              1.05         60.14               122.15         0.709            pass              0.521             66.9                           0.384              -14.63             -2.099 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-08T11:17:31.826171-04:00 early_entry_1115      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-08T10:00:23.726420-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "entry_ask": 24.2, "entry_bid": 21.6, "entry_mode": "early", "entry_option_price": 22.9, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 53.0, "option_spread_pct": 11.35, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "matched_signals": 43, "recovery_stability_score": 0.607, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T00:00:05.492385-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-07-07T15:10:01.115389-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-07T15:05:02.177767-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-07T15:00:05.200618-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-07T14:55:05.093959-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-07T14:50:02.270348-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"allocated_cash": 12690.0, "asset_type": "option", "contract_symbol": "CSX260821C00047500", "contracts": 54, "early_entry_score": 0.601, "entry_mode": "regular", "entry_option_price": 2.35, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 2967.0, "option_spread_pct": 8.51, "option_volume": 20.0, "success_rate": 91.3, "ticker": "CSX", "timing_score": 0.525}
2026-07-07T14:50:02.270348-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.524, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 36.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.594}
2026-07-07T14:50:02.270348-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-07", "training_samples": 5385, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260708111731)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260708111731)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260708111731)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260708111731)

</details>

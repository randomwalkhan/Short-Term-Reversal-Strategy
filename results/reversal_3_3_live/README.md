# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 15:40:06 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$1,421.80`
- Equity: `$128,764.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-8,927.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 60000.0         20.0          18.75      220.60        218.99          bid_ask_mid                      18.75                bid_ask_mid                    True         -4000.0                  -6.25         100.0               12              3.08         70.90           70.22                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 67342.5          1.1           1.02       44.42         44.53          bid_ask_mid                       1.02                bid_ask_mid                    True         -4927.5                  -6.82          80.0               15              0.97         20.09           21.07                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   ROP           81.25               16            1.41              4.36        439.78                39.00         0.558          pass              0.265             45.3                           0.536               18.19              2.018                      ok            True                  False
   WMT           80.00               15            1.05              0.88        119.91                23.89         0.544          pass              0.141             17.6                           0.348                6.01              0.467                      ok            True                  False
  TEAM          100.00               21            1.98              3.10        222.09                43.78         0.540          pass              0.561             11.2                           0.171                5.26              0.855                      ok            True                  False
   MAR           86.67               15            1.19              3.29        393.34                21.92         0.522          pass              0.468             68.1                           0.769                4.99              0.545                      ok            True                  False
  FAST           91.67               12            1.55              0.57         52.23                20.88         0.520          pass              0.480             34.5                           0.653                0.44              0.220                      ok            True                  False
  ORLY           94.12               17            1.27              0.81         90.70                20.34         0.505          pass              0.557             28.0                           0.464                4.49              0.477                      ok            True                  False
  GEHC           80.00               20            1.28              0.64         71.70                26.81         0.504          pass              0.265             49.2                           0.539                3.36              0.416                      ok            True                  False
  TMUS           86.49               37            0.33              0.34        146.78                64.06         0.640          pass              0.622             68.4                           0.446               -4.74             -0.686 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.14              0.50         62.76                25.86         0.600          pass              0.339             26.3                           0.476                1.23              0.139                      ok           False                  False
 CMCSA           87.50                8            1.34              0.21         21.96                26.02         0.568          pass              0.297             13.2                           0.295                4.19              0.552                      ok           False                  False
   KHC           80.00                5            2.63              0.46         24.53                34.80         0.554          pass              0.062              2.3                           0.226                7.36              0.925                      ok           False                  False
   PEP           50.00                2            1.98              1.88        134.66                25.06         0.541          pass              0.082              9.5                           0.311                4.30              0.621                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-27T15:10:03.998420-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T15:05:06.800261-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T15:00:05.952985-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T14:55:05.068283-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-27T14:50:03.992702-04:00       entry_1500      entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
2026-10-27T14:50:03.992702-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-27", "training_samples": 6196, "window": 5}
2026-10-27T12:00:05.676478-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.822, "early_reclaim_pct": 78.5, "matched_signals": 42, "recovery_stability_score": 0.692, "success_rate": 92.86, "ticker": "WDAY", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T11:55:06.030396-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:50:05.158961-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T11:45:04.083038-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027154006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027154006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027154006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027154006)

</details>

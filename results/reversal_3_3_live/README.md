# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-26 10:15:51 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$18,092.50`
- Equity: `$27,462.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$-3,150.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260821C00380000       2026-06-25                   1      4     12520.0                  9370.0         31.3          23.42      379.69        369.45          bid_ask_mid                      23.42                bid_ask_mid                    True         -3150.0                 -25.16         87.88               33              0.63         52.09           48.87                  76.92                2270.0         1394.0               0.03                      ok
```

## Today's Closed Trades (2026-06-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  DRAM           93.33               15            3.41              1.83         76.10               122.54         0.742          pass              0.623             53.3                           0.816               14.05              1.323                      ok            True                  False
    MU           88.00               25            2.19             18.56       1205.60               127.35         0.736          pass              0.602             71.8                           0.874               19.20              1.659                      ok            True                  False
  KLAC           90.91               11            3.77              6.82        255.88                93.32         0.648          pass              0.465             34.1                           0.653                3.27              0.195                      ok            True                  False
  INTC           91.67               24            2.13              1.98        132.02                97.28         0.638          pass              0.653             61.7                           0.842               11.19              1.157                      ok            True                  False
  AMAT           91.67               12            3.22             15.04        661.55                87.16         0.627          pass              0.542             51.8                           0.811               16.99              1.448                      ok            True                  False
  SOXL           91.67               12           10.51             18.59        244.64               236.70         0.593          pass              0.475             30.5                           0.702                0.92              0.112                      ok            True                  False
  LRCX           92.86               14            3.78             10.64        397.26                86.42         0.567          pass              0.560             44.6                           0.776                6.72              0.624                      ok            True                  False
  PCAR           80.00               20            1.18              1.01        121.25                36.28         0.540          pass              0.303             60.8                           0.575                2.26              0.070                      ok            True                  False
  MRVL          100.00               19            3.58              7.05        278.24               155.27         0.818          pass              0.667             41.8                           0.760               -3.39             -0.378 downtrend_blocked_slope           False                  False
  AVGO           78.57               14            2.47              6.54        376.11                76.91         0.677          pass              0.187             30.9                           0.624               -4.00             -0.270 downtrend_blocked_slope           False                  False
   TXN           88.89                9            3.13              6.82        308.89                63.36         0.622          pass              0.352             17.5                           0.318                1.67              0.191                      ok           False                  False
  ASML           95.24               21            2.33             30.05       1828.30                66.48         0.611          pass              0.659             41.6                           0.750               -5.33             -0.483 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-26T10:15:51.250947-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T00:00:07.288133-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
2026-06-25T15:10:04.366784-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:05:03.502084-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:00:05.541289-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:55:02.526574-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:50:05.514440-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 12520.0, "asset_type": "option", "contract_symbol": "AVGO260821C00380000", "contracts": 4, "early_entry_score": 0.654, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 2270.0, "option_spread_pct": 3.19, "option_volume": 1394.0, "success_rate": 87.88, "ticker": "AVGO", "timing_score": 0.668}
2026-06-25T14:50:05.514440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-25", "training_samples": 5306, "window": 5}
2026-06-25T11:55:33.596906-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260821C00175000", "current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "entry_ask": 18.3, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 17.95, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 954.0, "option_spread_pct": 3.9, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "matched_signals": 42, "recovery_stability_score": 0.556, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-25T11:12:19.435736-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260626101551)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260626101551)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260626101551)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260626101551)

</details>

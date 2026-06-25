# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-25 15:45:01 EDT`
Last processed slot: `manual`

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
- Equity: `$29,682.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$-930.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260821C00380000       2026-06-25                   0      4     12520.0                 11590.0         31.3          28.98      379.69        378.49          bid_ask_mid                      28.98                bid_ask_mid                    True          -930.0                  -7.43         87.88               33              0.63         52.09           50.13                  76.92                2270.0         1394.0               0.03                      ok
```

## Today's Closed Trades (2026-06-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AVGO           86.21               29            0.92              2.46        381.03                76.92         0.673          pass              0.547             62.6                           0.410                1.90              0.123                                 ok            True                  False
  INTC           94.44               36            0.82              0.76        131.59                97.48         0.624          pass              0.871             83.4                           0.682               22.23              1.806                                 ok            True                   True
  UPRO           88.46               26            0.59              0.56        134.46                51.32         0.620          pass              0.571             58.9                           0.306                2.68             -0.096                                 ok            True                  False
  CSCO           96.77               31            0.96              0.81        119.39                40.01         0.526          pass              0.734             47.2                           0.353               -0.18             -0.050                                 ok            True                  False
  SNPS           84.21               19            2.24              7.28        460.90                46.83         0.511          pass              0.308             28.4                           0.293               -1.50              0.092                                 ok            True                  False
  MPWR           91.18               34            0.18              1.85       1434.16                84.45         0.655          pass              0.811             95.7                           0.631               -2.77             -0.871            downtrend_blocked_slope           False                  False
   WBD           88.89                9            0.79              0.15         27.14                20.10         0.618          pass              0.306              2.3                           0.214                2.88              0.159                                 ok           False                  False
   PEP          100.00                3            1.82              1.81        141.49                19.15         0.598          pass              0.492             10.7                           0.213               -3.22             -0.324            downtrend_blocked_slope           False                  False
  CDNS           92.59               27            1.32              3.45        370.92                55.72         0.596          pass              0.638             43.1                           0.417               -4.59             -0.391            downtrend_blocked_slope           False                  False
  META           66.67                6            2.36              9.23        553.84                45.69         0.589          pass              0.134             25.0                           0.259               -4.53             -0.426 downtrend_blocked_slope_and_streak           False                  False
   TRI           82.35               34            0.27              0.15         80.92                56.19         0.587          pass              0.537             85.1                           0.568               -1.46             -0.177                                 ok           False                  False
   MAR           93.33               15            1.29              3.45        382.08                26.43         0.551          pass              0.464              6.8                           0.178               -1.97             -0.406            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-06-25T15:10:04.366784-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:05:03.502084-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T15:00:05.541289-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:55:02.526574-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-25T14:50:05.514440-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 12520.0, "asset_type": "option", "contract_symbol": "AVGO260821C00380000", "contracts": 4, "early_entry_score": 0.654, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 2270.0, "option_spread_pct": 3.19, "option_volume": 1394.0, "success_rate": 87.88, "ticker": "AVGO", "timing_score": 0.668}
2026-06-25T14:50:05.514440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-25", "training_samples": 5306, "window": 5}
2026-06-25T11:55:33.596906-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260821C00175000", "current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "entry_ask": 18.3, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 17.95, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 954.0, "option_spread_pct": 3.9, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.857, "early_reclaim_pct": 70.1, "matched_signals": 42, "recovery_stability_score": 0.556, "success_rate": 95.24, "ticker": "DASH", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-25T11:12:19.435736-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-25T10:28:17.676892-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-25T09:18:02.513254-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260625154501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260625154501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260625154501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260625154501)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 15:15:05 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KDP           95.65               23            0.74              0.18         34.55                29.04         0.553            pass              0.737             65.1                           0.350               12.56              1.275                      ok            True                  False
  GILD           90.00               10            1.69              1.85        155.72                26.70         0.534            pass              0.454             44.8                           0.686                4.77              0.596                      ok            True                  False
   KHC           80.00               15            1.68              0.28         23.71                25.26         0.504            pass              0.098              4.8                           0.188                6.60              0.741                      ok            True                  False
  INTU           88.24               34            0.58              1.37        334.70                37.42         0.501            pass              0.588             52.9                           0.306               12.66              1.291                      ok            True                  False
  TMUS           60.00               10            2.40              2.65        156.61                56.37         0.586            pass              0.176             39.2                           0.601               -8.17             -0.449 downtrend_blocked_slope           False                  False
  MDLZ          100.00                1            2.44              1.09         63.52                19.17         0.547            pass              0.465              3.3                           0.192                5.14              0.634                      ok           False                  False
 CMCSA           75.00                4            1.95              0.30         22.23                21.50         0.508            pass              0.185             44.6                           0.492                4.70              0.702                      ok           False                  False
  MELI           79.17               24            1.67             21.94       1870.10                40.36         0.506            pass              0.200             18.7                           0.220               -1.31             -0.155                      ok           False                  False
  ORLY          100.00               16            1.44              0.91         89.63                13.90         0.495 below_threshold              0.514              8.2                           0.215                4.86              0.543                      ok           False                  False
  GEHC           70.00               10            2.02              0.99         69.80                23.16         0.487 below_threshold              0.070              7.2                           0.114                6.40              0.838                      ok           False                  False
  ABNB           82.35               17            1.91              2.37        175.92                39.60         0.477 below_threshold              0.186              9.6                           0.186                8.05              0.955                      ok           False                  False
   ROP           88.24               34            0.61              1.70        397.48                26.56         0.476 below_threshold              0.587             53.3                           0.352               10.38              1.023                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-21T15:10:06.687584-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-21T14:55:05.525520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-21T14:50:04.709155-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_trade_after_option_and_timing_filters"}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"early_entry_score": 0.216, "option_liquidity_status": "no_two_sided_quote,wide_spread", "option_open_interest": 112.0, "option_spread_pct": null, "option_volume": 63.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.504}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.255, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 40.0, "option_spread_pct": 10.41, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.508}
2026-10-21T14:50:04.709155-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-21", "training_samples": 6158, "window": 5}
2026-10-21T12:00:03.696470-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:55:05.704920-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 61.1, "entry_ask": 32.2, "entry_bid": 27.2, "entry_mode": "early", "entry_option_price": 29.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 16.84, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 61.1, "matched_signals": 39, "recovery_stability_score": 0.62, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021151505)

</details>

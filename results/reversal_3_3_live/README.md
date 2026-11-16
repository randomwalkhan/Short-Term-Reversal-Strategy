# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 09:55:03 EST`
Last processed slot: `manage_1000`

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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  FTNT           81.08               37            1.32              1.18        126.71                93.31         0.671          pass              0.358             27.5                           0.249               -0.53              0.070                      ok            True                  False
  ABNB           83.33               24            1.40              1.83        186.00                54.57         0.582          pass              0.415             58.0                           0.566                7.63              0.914                      ok            True                  False
  ISRG           90.62               32            0.83              2.57        442.49                45.74         0.561          pass              0.518             10.6                           0.230                0.70             -0.276                      ok            True                  False
   CEG           84.62               39            0.53              1.04        279.33                61.55         0.560          pass              0.604             77.2                           0.748                8.18              1.273                      ok            True                  False
  ALNY           76.47               34            1.23              1.42        164.43               110.81         0.739          pass              0.322             29.4                           0.233                3.17              0.192                      ok           False                  False
  INTC           63.64               11            5.56              2.32         58.66               143.21         0.700          pass              0.133             18.8                           0.419               -6.05              0.151                      ok           False                  False
  UPRO           88.89                9            2.72              2.64        137.37                68.17         0.646          pass              0.335             11.0                           0.207               -3.17             -0.092                      ok           False                  False
   BKR           63.64               11            2.08              0.72         49.13                57.94         0.611          pass              0.142             24.8                           0.238               -8.31             -0.525 downtrend_blocked_slope           False                  False
   TRI           87.50               40            0.33              0.25        109.19                62.00         0.609          pass              0.561             33.3                           0.261              -10.88             -0.928 downtrend_blocked_slope           False                  False
 GOOGL           70.00               10            2.34              4.84        293.69                54.19         0.595          pass              0.101             13.9                           0.159                3.53              0.524                      ok           False                  False
  GOOG           70.00               10            2.28              4.67        290.52                52.39         0.592          pass              0.106             15.6                           0.166                2.81              0.443                      ok           False                  False
   ADI           66.67                9            2.93              8.15        394.48                66.18         0.580          pass              0.154             31.8                           0.467               -6.42             -0.177                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:05:05.959531-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:00:05.889317-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:55:04.803922-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:50:04.935495-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 61380.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "contracts": 198, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 3.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 3966.0, "option_spread_pct": 6.45, "option_volume": 43.0, "success_rate": 93.33, "ticker": "MDLZ", "timing_score": 0.574}
2026-11-06T14:50:04.935495-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-06", "training_samples": 6334, "window": 5}
2026-11-06T12:00:04.909641-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:55:04.780197-05:00 early_entry_1155 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "entry_ask": 4.3, "entry_bid": 4.05, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 5.99, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "matched_signals": 38, "recovery_stability_score": 0.712, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116095503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116095503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116095503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116095503)

</details>

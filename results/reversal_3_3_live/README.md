# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 10:15:01 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC          100.00               11            0.65              0.20         43.08                14.68         0.555            pass              0.515             17.6                           0.142               -1.46             -0.078                                 ok            True                  False
   AEP           84.62               13            0.89              0.77        123.00                16.49         0.524            pass              0.249             17.9                           0.215               -0.07              0.056                                 ok            True                  False
  PYPL           94.44               36            0.30              0.11         53.67                58.55         0.610            pass              0.753             44.6                           0.222                0.06             -0.001                                 ok           False                  False
   KHC           92.86               14            0.41              0.07         24.57                26.10         0.587            pass              0.570             47.4                           0.216               -3.15             -0.453            downtrend_blocked_slope           False                  False
  SNPS           72.73               22            1.89              5.26        395.12                60.55         0.573            pass              0.188             16.8                           0.315              -11.92             -1.219            downtrend_blocked_slope           False                  False
  AMGN           97.06               34            0.10              0.27        377.23                44.95         0.571            pass              0.838             73.6                           0.300              -12.82             -1.804 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.12               17            1.51              1.56        147.35                26.03         0.526            pass              0.595             39.7                           0.653               -3.95             -0.338 downtrend_blocked_slope_and_streak           False                  False
  NVDA           88.89                9            3.14              4.80        216.23                43.68         0.526            pass              0.370             26.7                           0.625               -2.70             -0.164           downtrend_blocked_streak           False                  False
  CDNS           57.14                7            2.72              5.52        287.01                43.36         0.507            pass              0.051              0.0                           0.193              -17.30             -1.893 downtrend_blocked_slope_and_streak           False                  False
  CHTR           89.74               39            1.35              1.38        145.18                68.13         0.504            pass              0.664             53.3                           0.290               -6.40             -0.917            downtrend_blocked_slope           False                  False
  MELI           96.67               30            0.98             13.04       1891.78                37.25         0.500            pass              0.622             12.8                           0.204               -4.45             -0.513 downtrend_blocked_slope_and_streak           False                  False
   CSX           81.82               22            0.53              0.18         48.87                18.07         0.492 below_threshold              0.365             62.3                           0.357               -4.79             -0.329            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-14T10:15:01.117814-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "matched_signals": 35, "recovery_stability_score": 0.743, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:10:06.027535-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "matched_signals": 31, "recovery_stability_score": 0.68, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:05:06.288532-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:00:06.059973-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914101501)

</details>

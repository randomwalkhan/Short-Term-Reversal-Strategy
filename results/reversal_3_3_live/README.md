# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:15:05 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  VRSK           91.30               23            1.49              1.83        174.63                39.25         0.503            pass              0.523             28.4                           0.315               -6.75             -0.238                                 ok            True                  False
   PEP          100.00               10            0.93              0.84        129.39                15.76         0.556            pass              0.551             31.9                           0.440               -6.60             -0.644 downtrend_blocked_slope_and_streak           False                  False
   KHC           95.00               20            0.20              0.04         24.41                22.04         0.552            pass              0.734             70.6                           0.486               -1.89             -0.113                                 ok           False                  False
  CHTR           88.89               27            1.85              1.66        127.46                64.18         0.550            pass              0.489             28.0                           0.335              -17.23             -1.440 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.42              0.73        248.61                46.23         0.531            pass              0.873             77.7                           0.806               -6.99             -0.441            downtrend_blocked_slope           False                  False
  ADSK           88.37               43            0.06              0.09        216.91                55.58         0.528            pass              0.766             96.7                           0.886               -0.50              0.344                                 ok           False                  False
   ADP           94.74               19            0.84              1.60        270.53                22.01         0.524            pass              0.634             42.9                           0.312               -2.51              0.119           downtrend_blocked_streak           False                  False
  INTU          100.00               29            1.19              2.52        302.11                42.64         0.504            pass              0.744             55.5                           0.703               -9.95             -0.615 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.50                8            2.41              2.83        166.97                33.56         0.491 below_threshold              0.357             36.0                           0.632               -9.58             -0.930            downtrend_blocked_slope           False                  False
  PAYX           82.35               17            1.36              1.10        115.67                23.92         0.491 below_threshold              0.190             10.4                           0.176               -5.87             -0.215           downtrend_blocked_streak           False                  False
  SBUX           71.43                7            1.71              1.15         95.34                22.99         0.489 below_threshold              0.126             25.6                           0.239               -9.84             -0.846 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               30            0.01              0.01         72.30                19.27         0.486 below_threshold              0.874             97.5                           0.736               -3.76             -0.521            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-21T10:15:05.893967-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:10:06.043789-04:00 early_entry_1010      early_entry_shadow {"contract_symbol": "CTAS261030C00195000", "current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "entry_ask": 10.1, "entry_bid": 7.4, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 40, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 30.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T10:05:06.363886-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:00:04.768791-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T09:20:04.809937-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-18T15:10:04.788288-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921101505)

</details>

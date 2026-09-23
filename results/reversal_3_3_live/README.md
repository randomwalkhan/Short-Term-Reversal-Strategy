# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:50:05 EDT`
Last processed slot: `manage_1100`

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

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           92.86               28            2.31              2.70        166.17               109.59         0.700          pass              0.622             29.7                           0.396               23.19              2.830                                 ok            True                  False
  PYPL           88.89               18            1.51              0.56         52.65                57.12         0.631          pass              0.431             25.9                           0.310               -0.15             -0.185                                 ok            True                  False
  NVDA           91.30               23            1.42              2.28        227.89                44.57         0.582          pass              0.493             15.6                           0.324                0.98              0.451                                 ok            True                  False
  ADSK           81.82               33            0.89              1.37        219.03                55.47         0.558          pass              0.391             44.4                           0.441                5.35              0.316                                 ok            True                  False
  UPRO           88.24               17            1.78              1.92        152.92                31.44         0.524          pass              0.350             10.5                           0.248                2.59              0.468                                 ok            True                  False
  AMGN           86.11               36            0.27              0.78        409.91                46.69         0.564          pass              0.600             69.3                           0.346                4.56              0.632                                 ok           False                  False
   XEL          100.00                6            1.18              0.60         71.80                15.29         0.561          pass              0.520             21.3                           0.352               -5.78             -0.559 downtrend_blocked_slope_and_streak           False                  False
  MRVL           75.76               33            1.74              3.19        260.99                69.87         0.551          pass              0.272             21.2                           0.314                9.70              1.471                                 ok           False                  False
   WBD           92.68               41            0.10              0.02         30.82                38.24         0.539          pass              0.852             86.6                           0.626               10.35              1.013                                 ok           False                  False
   KHC           93.33               15            0.98              0.16         23.93                22.23         0.525          pass              0.577             45.3                           0.538               -3.43             -0.219           downtrend_blocked_streak           False                  False
   CEG           83.33               30            0.79              1.46        262.83                42.63         0.507          pass              0.456             61.0                           0.711              -11.07             -1.150 downtrend_blocked_slope_and_streak           False                  False
  VRSK           90.00               40            0.08              0.09        171.90                39.26         0.502          pass              0.798             93.6                           0.812               -3.22             -0.435 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-23T10:50:05.940190-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:45:05.446928-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:40:01.660057-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:35:05.492268-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:30:06.224797-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:25:06.407969-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:20:05.981567-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:15:04.258896-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:10:06.450659-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "entry_ask": 5.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 41.86, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.742, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "matched_signals": 33, "recovery_stability_score": 0.742, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:05:05.428675-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923105005)

</details>

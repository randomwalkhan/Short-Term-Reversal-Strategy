# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:20:05 EDT`
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
  MSTR           92.86               28            2.28              2.67        166.19               109.59         0.706          pass              0.584             16.8                           0.242               23.23              2.831                                 ok            True                  False
  PYPL           88.89               18            1.54              0.57         52.65                57.12         0.629          pass              0.427             24.5                           0.182               -0.18             -0.186                                 ok            True                  False
  NVDA           91.30               23            1.50              2.41        227.84                44.57         0.577          pass              0.468              7.3                           0.187                0.90              0.447                                 ok            True                  False
  ADSK           81.82               33            0.85              1.31        219.06                55.47         0.561          pass              0.393             45.1                           0.330                5.39              0.318                                 ok            True                  False
  UPRO           88.89               18            1.67              1.80        152.97                31.44         0.528          pass              0.349              1.9                           0.157                2.71              0.474                                 ok            True                  False
  MRVL           75.76               33            1.81              3.32        260.94                69.87         0.547          pass              0.252             14.7                           0.229                9.62              1.468                                 ok           False                  False
   XEL           85.71                7            1.12              0.57         71.82                15.29         0.541          pass              0.281             25.0                           0.372               -5.73             -0.557 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.68               41            0.10              0.02         30.82                38.24         0.539          pass              0.849             85.7                           0.569               10.35              1.012                                 ok           False                  False
   KHC           92.86               14            1.08              0.18         23.92                22.23         0.524          pass              0.541             39.5                           0.294               -3.54             -0.224           downtrend_blocked_streak           False                  False
   CEG           75.00               20            1.34              2.47        262.40                42.63         0.523          pass              0.221             34.1                           0.452              -11.56             -1.175 downtrend_blocked_slope_and_streak           False                  False
   ADP          100.00                6            1.90              3.58        268.11                21.61         0.509          pass              0.673             74.0                           0.447                0.38              0.029                                 ok           False                  False
  CHTR           85.37               41            0.84              0.69        116.97                65.60         0.509          pass              0.630             78.7                           0.791              -13.15             -1.995 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-23T10:20:05.981567-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:15:04.258896-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:10:06.450659-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "entry_ask": 5.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 41.86, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.742, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "matched_signals": 33, "recovery_stability_score": 0.742, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:05:05.428675-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:00:05.505875-04:00 early_entry_1000 early_entry_shadow  {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "entry_ask": 5.3, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 32.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "matched_signals": 33, "recovery_stability_score": 0.713, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T09:35:04.357346-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923102005)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:45:06 EDT`
Last processed slot: `early_entry_1045`

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
  WDAY           93.75               32            1.06              1.44        193.25                50.60         0.531            pass              0.589              7.5                           0.133               -2.03              0.289                                 ok            True                  False
   KHC           95.00               20            0.25              0.04         24.41                22.04         0.549            pass              0.716             64.7                           0.492               -1.93             -0.115                                 ok           False                  False
  CHTR           88.89               27            2.15              1.93        127.34                64.18         0.533            pass              0.452             16.3                           0.223              -17.48             -1.454 downtrend_blocked_slope_and_streak           False                  False
  ADSK           88.37               43            0.06              0.10        216.91                55.58         0.528            pass              0.765             96.5                           0.704               -0.50              0.343                                 ok           False                  False
  ADBE           97.37               38            0.53              0.92        248.53                46.23         0.524            pass              0.855             72.0                           0.459               -7.09             -0.446            downtrend_blocked_slope           False                  False
   ADP           94.44               18            0.98              1.87        270.42                22.01         0.521            pass              0.590             33.2                           0.244               -2.65              0.112           downtrend_blocked_streak           False                  False
   PEP           88.24               17            0.65              0.59        129.50                15.76         0.513            pass              0.474             52.3                           0.692               -6.34             -0.631 downtrend_blocked_slope_and_streak           False                  False
  TMUS           88.89                9            2.07              2.43        167.14                33.56         0.506            pass              0.423             45.1                           0.645               -9.26             -0.914            downtrend_blocked_slope           False                  False
  VRSK           85.71               14            2.16              2.65        174.27                39.25         0.506            pass              0.279             16.3                           0.237               -7.38             -0.269            downtrend_blocked_slope           False                  False
  INTU          100.00               36            0.60              1.28        302.64                42.64         0.497 below_threshold              0.855             77.4                           0.720               -9.42             -0.588 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.30               27            0.08              0.02         42.06                15.92         0.496 below_threshold              0.844             93.6                           0.665               -3.68             -0.457 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               28            0.08              0.04         72.28                19.27         0.494 below_threshold              0.828             86.3                           0.654               -3.82             -0.524            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:35:04.666862-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:30:01.878721-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:20:05.839585-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:15:05.893967-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:10:06.043789-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261030C00195000", "current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "entry_ask": 10.1, "entry_bid": 7.4, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 40, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 30.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T10:05:06.363886-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:00:04.768791-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921104506)

</details>

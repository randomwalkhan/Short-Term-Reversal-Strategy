# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:55:06 EDT`
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

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           94.12               17            0.43              0.07         24.40                22.04         0.555            pass              0.593             38.2                           0.328               -2.11             -0.123                                 ok           False                  False
  ADBE           97.37               38            0.26              0.46        248.72                46.23         0.540            pass              0.899             86.0                           0.663               -6.85             -0.434            downtrend_blocked_slope           False                  False
  CHTR           88.89               27            2.02              1.81        127.39                64.18         0.540            pass              0.469             21.4                           0.212              -17.37             -1.448 downtrend_blocked_slope_and_streak           False                  False
  WDAY           94.74               38            0.44              0.60        193.61                50.60         0.533            pass              0.817             61.3                           0.330               -1.42              0.318                                 ok           False                  False
   PEP           93.33               15            0.73              0.66        129.47                15.76         0.528            pass              0.582             46.6                           0.636               -6.41             -0.635 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.00               20            0.71              1.35        270.64                22.01         0.527            pass              0.675             51.8                           0.390               -2.38              0.125           downtrend_blocked_streak           False                  False
  TMUS           92.31               13            1.52              1.78        167.42                33.56         0.518            pass              0.579             59.7                           0.746               -8.75             -0.889            downtrend_blocked_slope           False                  False
  VRSK           89.47               19            1.75              2.15        174.49                39.25         0.505            pass              0.460             32.2                           0.436               -6.99             -0.250            downtrend_blocked_slope           False                  False
   XEL          100.00               26            0.10              0.05         72.28                19.27         0.504            pass              0.805             82.5                           0.633               -3.84             -0.525            downtrend_blocked_slope           False                  False
  SBUX           81.82               11            1.41              0.94         95.43                22.99         0.499 below_threshold              0.221             38.8                           0.499               -9.56             -0.832 downtrend_blocked_slope_and_streak           False                  False
  PAYX           84.21               19            1.09              0.89        115.76                23.92         0.496 below_threshold              0.328             35.2                           0.549               -5.62             -0.202           downtrend_blocked_streak           False                  False
  INTU          100.00               41            0.26              0.56        302.95                42.64         0.487 below_threshold              0.919             90.1                           0.782               -9.11             -0.573 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:45:06.703596-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:40:05.776403-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:35:04.666862-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:30:01.878721-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:20:05.839585-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:15:05.893967-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:10:06.043789-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261030C00195000", "current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "entry_ask": 10.1, "entry_bid": 7.4, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 40, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 30.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921105506)

</details>

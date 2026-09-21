# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:25:03 EDT`
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

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   PEP          100.00               13            0.79              0.72        129.44                15.76         0.546            pass              0.600             41.8                           0.645               -6.47             -0.638 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.30              0.52        248.70                46.23         0.538            pass              0.893             84.3                           0.814               -6.88             -0.435            downtrend_blocked_slope           False                  False
   ADP           95.00               20            0.73              1.39        270.63                22.01         0.526            pass              0.671             50.5                           0.362               -2.40              0.124           downtrend_blocked_streak           False                  False
  CHTR           89.19               37            1.28              1.15        127.68                64.18         0.524            pass              0.628             50.2                           0.683              -16.75             -1.413 downtrend_blocked_slope_and_streak           False                  False
  VRSK           89.47               19            1.84              2.26        174.44                39.25         0.504            pass              0.398             11.5                           0.259               -7.08             -0.254            downtrend_blocked_slope           False                  False
  SBUX           81.82               11            1.43              0.96         95.42                22.99         0.498 below_threshold              0.218             37.7                           0.425               -9.58             -0.834 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.50                8            2.34              2.75        167.00                33.56         0.494 below_threshold              0.363             37.9                           0.676               -9.51             -0.927            downtrend_blocked_slope           False                  False
  PAYX           84.21               19            1.15              0.94        115.74                23.92         0.494 below_threshold              0.293             23.9                           0.369               -5.68             -0.205           downtrend_blocked_streak           False                  False
  INTU          100.00               41            0.23              0.49        302.98                42.64         0.489 below_threshold              0.923             91.3                           0.874               -9.08             -0.571 downtrend_blocked_slope_and_streak           False                  False
   BKR           94.74               38            0.37              0.15         57.19                30.72         0.482 below_threshold              0.834             68.7                           0.695              -10.17             -1.343 downtrend_blocked_slope_and_streak           False                  False
   ADI           89.74               39            0.06              0.16        375.65                32.48         0.479 below_threshold              0.787             95.3                           0.761                3.66              0.229                                 ok           False                  False
  NXPI           82.35               34            0.49              0.78        227.65                36.05         0.478 below_threshold              0.388             39.1                           0.365                0.02              0.059                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-21T10:25:03.822733-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:20:05.839585-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:15:05.893967-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:10:06.043789-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261030C00195000", "current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "entry_ask": 10.1, "entry_bid": 7.4, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 40, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 30.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T10:05:06.363886-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:00:04.768791-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T09:20:04.809937-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-18T15:10:04.788288-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921102503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921102503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921102503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921102503)

</details>

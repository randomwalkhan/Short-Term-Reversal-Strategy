# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 15:25:05 EDT`
Last processed slot: `manage_1530`

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

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           93.55               31            0.92              1.23        191.39                50.40         0.524            pass              0.728             58.1                           0.443                2.08              0.431                                 ok            True                  False
   KHC           91.67               12            1.33              0.23         24.27                22.03         0.519            pass              0.413             12.2                           0.383               -3.43             -0.163                                 ok            True                  False
  TEAM          100.00               18            3.09              4.24        193.85                58.22         0.507            pass              0.624             40.0                           0.514                7.48              0.974                                 ok            True                  False
  FTNT           90.00               40            0.84              1.03        174.79                58.27         0.501            pass              0.729             70.6                           0.497               10.35              1.216                                 ok            True                  False
  CRWD           88.64               44            0.28              0.49        249.14                96.94         0.675            pass              0.753             84.9                           0.599               18.39              2.119                                 ok           False                  False
  MSFT           96.43               28            0.58              2.02        500.74                22.55         0.492 below_threshold              0.760             63.7                           0.608                0.97              0.104                                 ok           False                  False
  VRSK           91.89               37            0.29              0.35        171.87                39.65         0.462 below_threshold              0.829             95.3                           0.605               -2.00             -0.222           downtrend_blocked_streak           False                  False
  ADBE           83.33                6            4.33              7.56        246.28                45.94         0.430 below_threshold              0.197             21.8                           0.279               -7.20             -0.466            downtrend_blocked_slope           False                  False
   BKR           88.89               18            1.30              0.52         57.61                31.14         0.397 below_threshold              0.452             40.5                           0.402              -10.70             -1.049 downtrend_blocked_slope_and_streak           False                  False
  TTWO           78.26               23            1.64              2.41        208.89                37.71         0.397 below_threshold              0.243             38.7                           0.589               -3.19             -0.405 downtrend_blocked_slope_and_streak           False                  False
  AMZN           77.42               31            1.01              1.83        257.66                26.96         0.394 below_threshold              0.396             72.2                           0.662               -0.44              0.018                                 ok           False                  False
   APP           76.74               43            0.72              1.67        329.46                44.90         0.385 below_threshold              0.428             63.3                           0.713                5.06              0.421                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-22T15:10:06.051324-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.689, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 24.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.507}
2026-09-22T14:50:01.294026-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
2026-09-22T12:00:04.192622-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.559, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:55:04.534124-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922152505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922152505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922152505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922152505)

</details>

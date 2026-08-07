# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:40:02 EDT`
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

- Cash: `$32,694.50`
- Equity: `$32,694.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TMUS           90.91               33            0.65              0.82        179.62                57.01         0.609            pass              0.697             64.1                           0.711               -0.72             -0.138                                 ok            True                   True
  INTC           84.62               39            0.68              0.48         99.61                86.24         0.583            pass              0.560             61.8                           0.468                7.38              1.441                                 ok            True                  False
    MU           82.76               29            2.99             18.47        873.55               110.38         0.551            pass              0.326             23.4                           0.332               -7.15              0.113                                 ok            True                  False
  INSM           66.67               18            2.56              2.37        131.53               110.04         0.728            pass              0.177             17.0                           0.274               20.80              1.472                                 ok           False                  False
  MRVL           81.08               37            0.06              0.08        210.50                99.17         0.665            pass              0.568             97.6                           0.729                8.34              1.851                                 ok           False                  False
  ALNY           86.49               37            0.87              1.32        215.56               128.30         0.618            pass              0.615             66.6                           0.616              -21.17             -3.060            downtrend_blocked_slope           False                  False
   CSX           88.24               17            1.08              0.38         50.54                29.04         0.565            pass              0.365             14.1                           0.167               -5.79             -0.330 downtrend_blocked_slope_and_streak           False                  False
  GOOG           78.38               37            0.73              1.82        355.84                50.46         0.535            pass              0.288             18.1                           0.297               10.95              1.312                                 ok           False                  False
   MAR           93.10               29            0.77              1.93        358.84                38.09         0.526            pass              0.651             40.9                           0.228               -4.68             -0.862 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           75.00               36            0.84              2.12        356.84                51.28         0.524            pass              0.272             15.6                           0.266               10.94              1.340                                 ok           False                  False
  DRAM           76.00               25            4.42              1.59         50.76               108.98         0.498 below_threshold              0.194             14.7                           0.282               -7.58              0.239                                 ok           False                  False
  ROST           95.00               40            0.03              0.06        254.29                22.77         0.490 below_threshold              0.942             97.6                           0.821                6.42              0.461                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-07T10:40:02.462299-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.73, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "matched_signals": 37, "recovery_stability_score": 0.73, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 64.1, "matched_signals": 33, "recovery_stability_score": 0.711, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.609, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T10:35:01.485619-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:30:01.589091-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:25:02.606392-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "entry_ask": 3.7, "entry_bid": 2.95, "entry_mode": "early", "entry_option_price": 3.325, "hypothetical_budget": 16347.25, "hypothetical_contracts": 49, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 22.56, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.808, "shadow_only": true, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "matched_signals": 38, "recovery_stability_score": 0.808, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:20:01.443231-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:20:01.443231-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "INTC260918C00100000", "fill_price": 10.0575, "pnl": -1676.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "INTC"}
2026-08-07T10:15:06.143326-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:10:01.433730-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                             {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:05:05.478835-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                             {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807104002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807104002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807104002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807104002)

</details>

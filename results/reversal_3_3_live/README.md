# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 11:20:02 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           85.19               27            1.06              3.73        500.91                52.43         0.571            pass              0.489             60.1                           0.416               19.78              1.506                                 ok            True                  False
  CSCO           88.24               17            1.00              0.81        114.99                34.19         0.558            pass              0.488             55.2                           0.332                7.19              0.902                                 ok            True                  False
  MDLZ           93.75               16            0.67              0.29         61.67                19.83         0.554            pass              0.546             27.8                           0.470                4.38              0.648                                 ok            True                  False
  INTC           88.57               35            1.17              0.83        100.99                67.41         0.568            pass              0.638             61.9                           0.543              -13.60             -1.879 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.77               31            0.05              0.01         32.75                30.00         0.539            pass              0.877             94.2                           0.714                5.49              0.657                                 ok           False                  False
  MPWR           85.71               21            1.99             18.42       1311.34                51.39         0.539            pass              0.354             24.9                           0.337               -4.51             -0.360            downtrend_blocked_slope           False                  False
  UPRO           85.29               34            0.39              0.42        155.28                28.94         0.514            pass              0.463             36.8                           0.293                4.66              0.589                                 ok           False                  False
  SHOP           86.05               43            0.17              0.22        179.13                48.43         0.509            pass              0.695             94.3                           0.790               20.67              2.099                                 ok           False                  False
   STX           85.00               20            3.37             17.74        745.65                70.16         0.501            pass              0.434             61.1                           0.684              -20.31             -2.535            downtrend_blocked_slope           False                  False
  MCHP           96.00               25            1.46              0.75         73.51                37.42         0.492 below_threshold              0.673             41.3                           0.299               -7.65             -0.829            downtrend_blocked_slope           False                  False
   PEP           82.14               28            0.22              0.20        126.60                21.61         0.492 below_threshold              0.429             67.4                           0.542               -1.78             -0.054                                 ok           False                  False
  NVDA           87.50               24            0.70              1.11        225.84                22.13         0.491 below_threshold              0.496             51.2                           0.285               -1.09             -0.134                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-13T11:20:02.638996-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                               {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.752, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "matched_signals": 42, "recovery_stability_score": 0.752, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:15:05.483725-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                             {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "matched_signals": 42, "recovery_stability_score": 0.736, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:10:06.032401-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:05:06.217854-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00425000", "current_drop_pct": 0.98, "early_entry_score": 0.723, "early_reclaim_pct": 62.8, "entry_ask": 22.3, "entry_bid": 19.5, "entry_mode": "early", "entry_option_price": 20.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 34, "matched_signals": 30, "option_liquidity_status": "low_volume", "option_open_interest": 281.0, "option_spread_pct": 13.4, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.795, "shadow_only": true, "success_rate": 93.33, "ticker": "ISRG", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.723, "early_reclaim_pct": 62.8, "matched_signals": 30, "recovery_stability_score": 0.795, "success_rate": 93.33, "ticker": "ISRG", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.71, "early_reclaim_pct": 63.9, "matched_signals": 42, "recovery_stability_score": 0.73, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:00:04.704921-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                             {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.59, "early_entry_score": 0.715, "early_reclaim_pct": 65.3, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.714, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.715, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.714, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T10:55:05.723244-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:50:05.695677-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:45:04.655740-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:40:05.951817-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:35:04.412949-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013112002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013112002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013112002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013112002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 11:00:04 EDT`
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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           91.18               34            0.59              6.11       1477.27                53.63         0.574            pass              0.728             70.8                           0.589                6.72              0.822                                 ok            True                   True
  DRAM           84.00               25            1.58              0.68         61.38                49.40         0.563            pass              0.352             29.6                           0.487               -4.60             -0.167                                 ok            True                  False
  ASML           81.25               32            0.54              6.97       1856.87                40.48         0.544            pass              0.401             55.4                           0.589                5.84              0.797                                 ok            True                  False
  TMUS           85.71               28            0.66              0.76        164.31                30.04         0.527            pass              0.402             25.6                           0.209                0.70             -0.079                                 ok            True                  False
  ABNB           85.71               28            1.15              1.32        163.50                40.56         0.521            pass              0.392             22.4                           0.316                0.23              0.599                                 ok            True                  False
  META           85.71               42            0.12              0.63        741.63                55.50         0.580            pass              0.659             82.7                           0.579                0.60             -0.214                                 ok           False                  False
  QCOM           88.57               35            0.52              0.66        180.51                57.17         0.578            pass              0.559             35.2                           0.326               -9.29             -1.100 downtrend_blocked_slope_and_streak           False                  False
  INTC           88.89               36            1.20              0.98        115.77                74.54         0.568            pass              0.584             38.8                           0.424               -7.32             -0.732 downtrend_blocked_slope_and_streak           False                  False
  AMGN           81.25               16            1.18              3.34        401.55                46.96         0.513            pass              0.219             31.6                           0.355               -2.93             -0.209           downtrend_blocked_streak           False                  False
  AMAT           82.76               29            1.98              7.53        539.05                48.32         0.497 below_threshold              0.306             18.7                           0.372               12.50              1.580                                 ok           False                  False
  LRCX           75.00               24            2.77              6.71        342.92                55.68         0.491 below_threshold              0.206             21.1                           0.420                8.23              1.304                                 ok           False                  False
  TEAM          100.00               38            0.97              1.34        196.08                55.00         0.487 below_threshold              0.663              9.2                           0.129                3.23              0.130                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-10-06T11:00:04.190693-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "MPWR261120C01480000", "current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "entry_ask": 123.5, "entry_bid": 110.0, "entry_mode": "early", "entry_option_price": 116.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 4, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 60.0, "option_spread_pct": 11.56, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "matched_signals": 34, "recovery_stability_score": 0.589, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:55:04.412071-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:50:01.197576-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:45:05.848219-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:40:06.064214-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:35:04.353804-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:30:05.477700-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:25:05.769883-04:00 early_entry_1025 early_entry_shadow                                     {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "entry_ask": 13.6, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 13.33, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:20:05.384079-04:00 early_entry_1020 early_entry_shadow                                            {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "entry_ask": 13.1, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 52573.4, "hypothetical_contracts": 42, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 9.6, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.723, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.723, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:15:05.337195-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006110004)

</details>

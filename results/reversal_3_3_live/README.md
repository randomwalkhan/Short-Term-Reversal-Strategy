# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 11:45:06 EST`
Last processed slot: `early_entry_1145`

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

- Cash: `$126,926.55`
- Equity: `$126,926.55`
- Realized PnL: `$116,926.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-02)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     30          2026-10-30         2026-11-02         19.4       22.65 9750.0   16.752577 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           80.95               21            0.83              0.30         51.86                27.38         0.537            pass              0.192             13.1                           0.226                7.69              0.866                                 ok            True                  False
  GILD           88.89               18            1.18              1.41        170.07                29.81         0.525            pass              0.502             53.0                           0.623               10.18              1.003                                 ok            True                  False
  AAPL           92.86               14            1.31              3.17        343.27                14.54         0.500 below_threshold              0.449              9.8                           0.170               -0.83              0.031                                 ok            True                  False
  SOXL           74.19               31            1.73              0.93         76.65               161.32         0.768            pass              0.295             26.0                           0.231              -23.24             -1.422            downtrend_blocked_slope           False                  False
  INTC           58.33               12            4.57              2.10         64.86               126.81         0.706            pass              0.106              7.3                           0.222              -31.81             -2.705            downtrend_blocked_slope           False                  False
  ALNY           76.19               21            2.43              2.81        163.80               108.44         0.643            pass              0.304             55.4                           0.779              -30.99             -3.556            downtrend_blocked_slope           False                  False
  FTNT           62.50                8            3.64              3.47        134.59                91.18         0.621            pass              0.135             24.4                           0.635              -23.55             -2.624 downtrend_blocked_slope_and_streak           False                  False
  CSCO           72.22               18            1.22              0.90        104.13                35.63         0.532            pass              0.159             17.4                           0.161               -3.07             -0.052           downtrend_blocked_streak           False                  False
  TEAM          100.00               39            0.58              0.78        191.39                55.13         0.511            pass              0.879             78.3                           0.869              -11.24             -1.391            downtrend_blocked_slope           False                  False
  LRCX           65.52               29            1.87              3.13        237.77                61.33         0.505            pass              0.197              6.8                           0.172              -13.80             -0.876 downtrend_blocked_slope_and_streak           False                  False
  META           80.56               36            0.48              2.08        614.10                38.01         0.499 below_threshold              0.359             40.5                           0.369              -13.24             -1.525 downtrend_blocked_slope_and_streak           False                  False
    MU           77.27               22            2.62             16.20        877.80                60.34         0.499 below_threshold              0.146              5.4                           0.168               -4.79              0.094                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-11-02T11:45:06.353234-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:40:04.764399-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:35:05.778212-05:00 early_entry_1135 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "entry_ask": 3.0, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 2.8, "hypothetical_budget": 63463.28, "hypothetical_contracts": 226, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 14.29, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.589, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:30:05.925389-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:25:05.711228-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:20:05.561484-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:15:06.056353-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:10:06.789885-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:05:06.412913-05:00 early_entry_1105 early_entry_shadow              {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.564, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "matched_signals": 41, "recovery_stability_score": 0.564, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:00:05.740483-05:00 early_entry_1100 early_entry_shadow            {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "matched_signals": 35, "recovery_stability_score": 0.551, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102114506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102114506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102114506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102114506)

</details>

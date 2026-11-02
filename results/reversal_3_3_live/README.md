# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 11:05:06 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           83.33               18            0.92              0.30         46.03                22.23         0.537          pass              0.264             22.7                           0.270                7.84              0.776                                 ok            True                  False
   AEP           83.33               18            0.80              0.73        129.90                19.46         0.530          pass              0.299             34.7                           0.423                3.56              0.255                                 ok            True                  False
   CSX           80.00               25            0.72              0.26         51.88                27.38         0.518          pass              0.190             12.8                           0.155                7.80              0.871                                 ok            True                  False
   XEL           83.33               18            0.84              0.47         79.62                18.77         0.507          pass              0.415             74.1                           0.690                5.34              0.422                                 ok            True                  False
  INTC           65.00               20            3.22              1.48         65.13               126.81         0.749          pass              0.173             10.4                           0.193              -30.84             -2.641            downtrend_blocked_slope           False                  False
  ALNY           62.50                8            3.38              3.91        163.33               108.44         0.651          pass              0.179             38.0                           0.592              -31.66             -3.600            downtrend_blocked_slope           False                  False
  FTNT           62.50                8            3.72              3.55        134.56                91.18         0.616          pass              0.130             22.8                           0.397              -23.61             -2.628 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.50                8            1.84              2.19        169.74                29.81         0.549          pass              0.336             27.1                           0.374                9.46              0.972                                 ok           False                  False
  LRCX           69.77               43            0.24              0.41        238.93                61.33         0.536          pass              0.435             60.5                           0.351              -12.37             -0.801 downtrend_blocked_slope_and_streak           False                  False
  CSCO           77.27               22            0.93              0.68        104.22                35.63         0.529          pass              0.244             37.1                           0.277               -2.78             -0.038           downtrend_blocked_streak           False                  False
    MU           74.19               31            1.35              8.35        881.16                60.34         0.528          pass              0.237             14.6                           0.160               -3.55              0.153                                 ok           False                  False
  TEAM          100.00               28            1.56              2.10        190.82                55.13         0.520          pass              0.697             41.6                           0.488              -12.12             -1.436            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-02T11:05:06.412913-05:00 early_entry_1105 early_entry_shadow             {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.564, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "matched_signals": 41, "recovery_stability_score": 0.564, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:00:05.740483-05:00 early_entry_1100 early_entry_shadow           {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "matched_signals": 35, "recovery_stability_score": 0.551, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:55:06.162888-05:00 early_entry_1055 early_entry_shadow           {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "matched_signals": 41, "recovery_stability_score": 0.627, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:50:05.775893-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:45:05.694757-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:40:04.730319-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:35:05.961580-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:30:04.618613-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:25:05.872809-05:00 early_entry_1025 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "matched_signals": 41, "recovery_stability_score": 0.632, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:20:04.868575-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.768, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102110506)

</details>

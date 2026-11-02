# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 11:10:06 EST`
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
  GILD           90.00               10            1.57              1.88        169.88                29.81         0.554          pass              0.435             37.7                           0.467                9.75              0.985                                 ok            True                  False
   EXC           86.36               22            0.78              0.25         46.05                22.23         0.523          pass              0.406             34.5                           0.396                7.99              0.783                                 ok            True                  False
   AEP           85.00               20            0.74              0.68        129.92                19.46         0.523          pass              0.370             39.4                           0.502                3.62              0.258                                 ok            True                  False
   XEL           83.33               18            0.81              0.46         79.62                18.77         0.509          pass              0.418             74.9                           0.726                5.36              0.424                                 ok            True                  False
  INTC           61.54               13            4.19              1.93         64.93               126.81         0.729          pass              0.093              0.0                           0.150              -31.54             -2.687            downtrend_blocked_slope           False                  False
  ALNY           66.67               12            2.92              3.37        163.56               108.44         0.658          pass              0.219             46.6                           0.743              -31.33             -3.578            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.58              4.36        134.21                91.18         0.603          pass              0.075              5.0                           0.275              -24.29             -2.669 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               20            2.01              2.70        190.56                55.13         0.544          pass              0.596             25.0                           0.379              -12.52             -1.457            downtrend_blocked_slope           False                  False
  LRCX           66.67               39            0.67              1.12        238.63                61.33         0.530          pass              0.257              3.6                           0.065              -12.74             -0.821 downtrend_blocked_slope_and_streak           False                  False
  CSCO           77.27               22            0.99              0.72        104.20                35.63         0.526          pass              0.233             33.5                           0.255               -2.84             -0.041           downtrend_blocked_streak           False                  False
    MU           77.78               27            1.83             11.33        879.88                60.34         0.525          pass              0.166              0.0                           0.183               -4.02              0.131                                 ok           False                  False
  META           80.00               35            0.53              2.30        614.00                38.01         0.501          pass              0.319             34.1                           0.202              -13.29             -1.528 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-02T11:10:06.789885-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:05:06.412913-05:00 early_entry_1105 early_entry_shadow             {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.564, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "matched_signals": 41, "recovery_stability_score": 0.564, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:00:05.740483-05:00 early_entry_1100 early_entry_shadow           {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "matched_signals": 35, "recovery_stability_score": 0.551, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:55:06.162888-05:00 early_entry_1055 early_entry_shadow           {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "matched_signals": 41, "recovery_stability_score": 0.627, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:50:05.775893-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:45:05.694757-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:40:04.730319-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:35:05.961580-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:30:04.618613-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:25:05.872809-05:00 early_entry_1025 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "matched_signals": 41, "recovery_stability_score": 0.632, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102111006)

</details>

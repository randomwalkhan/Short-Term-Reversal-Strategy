# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 11:20:05 EST`
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
   EXC           87.50               24            0.65              0.21         46.07                22.23         0.519          pass              0.482             45.5                           0.531                8.13              0.789                                 ok            True                  False
  SOXL           75.68               37            0.20              0.11         77.00               161.32         0.820          pass              0.465             67.7                           0.264              -22.05             -1.352            downtrend_blocked_slope           False                  False
  INTC           61.54               13            4.19              1.93         64.93               126.81         0.725          pass              0.122              9.8                           0.164              -31.54             -2.687            downtrend_blocked_slope           False                  False
  ALNY           57.14                7            3.63              4.19        163.20               108.44         0.638          pass              0.164             33.4                           0.718              -31.84             -3.612            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.20              4.00        134.37                91.18         0.625          pass              0.101             13.0                           0.321              -23.98             -2.650 downtrend_blocked_slope_and_streak           False                  False
  GILD           88.89                9            1.73              2.06        169.80                29.81         0.551          pass              0.387             31.5                           0.391                9.58              0.978                                 ok           False                  False
  CSCO           77.27               22            0.94              0.69        104.21                35.63         0.529          pass              0.242             36.5                           0.299               -2.79             -0.039           downtrend_blocked_streak           False                  False
  LRCX           64.86               37            0.87              1.46        238.49                61.33         0.526          pass              0.262             10.0                           0.087              -12.92             -0.830 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               26            1.71              2.30        190.73                55.13         0.524          pass              0.667             36.0                           0.406              -12.25             -1.443            downtrend_blocked_slope           False                  False
    MU           77.78               27            1.82             11.29        879.90                60.34         0.524          pass              0.185              6.5                           0.100               -4.01              0.131                                 ok           False                  False
  META           80.00               30            0.78              3.35        613.55                38.01         0.517          pass              0.197              4.0                           0.065              -13.50             -1.539 downtrend_blocked_slope_and_streak           False                  False
  AMGN           77.27               22            0.97              3.18        464.65                24.52         0.504          pass              0.159              9.4                           0.219                8.60              0.765                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-02T11:20:05.561484-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:15:06.056353-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:10:06.789885-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:05:06.412913-05:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.564, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.818, "early_reclaim_pct": 76.9, "matched_signals": 41, "recovery_stability_score": 0.564, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T11:00:05.740483-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.802, "early_reclaim_pct": 67.8, "matched_signals": 35, "recovery_stability_score": 0.551, "success_rate": 94.29, "ticker": "BKR", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:55:06.162888-05:00 early_entry_1055 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "matched_signals": 41, "recovery_stability_score": 0.627, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:50:05.775893-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:45:05.694757-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:40:04.730319-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:35:05.961580-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102112005)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 10:55:06 EST`
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
  GILD           90.00               10            1.67              1.99        169.83                29.81         0.549          pass              0.423             33.7                           0.405                9.64              0.980                                 ok            True                  False
   EXC           81.25               16            1.00              0.32         46.02                22.23         0.543          pass              0.177             16.4                           0.201                7.76              0.773                                 ok            True                  False
   XEL           80.00               15            0.98              0.55         79.58                18.77         0.515          pass              0.294             69.7                           0.569                5.18              0.416                                 ok            True                  False
   AEP           86.36               22            0.73              0.66        129.93                19.46         0.513          pass              0.424             40.9                           0.361                3.64              0.259                                 ok            True                  False
  AAPL           94.12               17            0.98              2.36        343.62                14.54         0.501          pass              0.572             32.8                           0.463               -0.49              0.046                                 ok            True                  False
  INTC           66.67               21            3.16              1.45         65.14               126.81         0.750          pass              0.160              3.9                           0.123              -30.80             -2.638            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.12              3.93        134.40                91.18         0.629          pass              0.106             14.5                           0.277              -23.92             -2.647 downtrend_blocked_slope_and_streak           False                  False
  ALNY           66.67                3            5.19              5.99        162.43               108.44         0.580          pass              0.073              4.9                           0.182              -32.94             -3.686            downtrend_blocked_slope           False                  False
  LRCX           69.77               43            0.18              0.30        238.98                61.33         0.541          pass              0.446             64.0                           0.350              -12.31             -0.798 downtrend_blocked_slope_and_streak           False                  False
    MU           76.47               34            0.90              5.56        882.36                60.34         0.539          pass              0.343             43.2                           0.316               -3.11              0.174                                 ok           False                  False
  TEAM          100.00               17            2.44              3.27        190.32                55.13         0.538          pass              0.527              9.0                           0.163              -12.90             -1.477            downtrend_blocked_slope           False                  False
  CSCO           79.17               24            0.87              0.64        104.24                35.63         0.523          pass              0.269             41.3                           0.364               -2.72             -0.036           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-02T10:55:06.162888-05:00 early_entry_1055 early_entry_shadow           {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "entry_ask": 3.0, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 2.875, "hypothetical_budget": 63463.28, "hypothetical_contracts": 220, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1017.0, "option_spread_pct": 8.7, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 74.8, "matched_signals": 41, "recovery_stability_score": 0.627, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:50:05.775893-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:45:05.694757-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:40:04.730319-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:35:05.961580-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:30:04.618613-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:25:05.872809-05:00 early_entry_1025 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "matched_signals": 41, "recovery_stability_score": 0.632, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:20:04.868575-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.768, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:20:04.868575-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "CEG261218C00260000", "fill_price": 22.65, "pnl": 9750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.75, "ticker": "CEG"}
2026-11-02T10:15:01.964431-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102105506)

</details>

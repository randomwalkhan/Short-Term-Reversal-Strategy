# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 10:40:04 EST`
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
  GILD           90.00               10            1.62              1.93        169.85                29.81         0.552            pass              0.429             35.8                           0.313                9.70              0.983                                 ok            True                  False
   EXC           81.25               16            0.94              0.30         46.03                22.23         0.548            pass              0.136              2.5                           0.163                7.82              0.775                                 ok            True                  False
    MU           80.00               40            0.54              3.32        883.32                60.34         0.528            pass              0.451             66.1                           0.549               -2.75              0.190                                 ok            True                  False
  INTC           68.18               22            2.97              1.36         65.18               126.81         0.757            pass              0.172              5.3                           0.223              -30.66             -2.629            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.09              3.90        134.41                91.18         0.631            pass              0.105             14.0                           0.339              -23.90             -2.645 downtrend_blocked_slope_and_streak           False                  False
  ALNY           57.14                7            4.12              4.76        162.96               108.44         0.612            pass              0.124             20.8                           0.295              -32.19             -3.635            downtrend_blocked_slope           False                  False
  TEAM          100.00               20            2.04              2.74        190.55                55.13         0.542            pass              0.592             23.8                           0.357              -12.54             -1.458            downtrend_blocked_slope           False                  False
   AEP           76.92               13            1.07              0.97        129.79                19.46         0.541            pass              0.098              7.9                           0.188                3.29              0.243                                 ok           False                  False
   XEL           75.00               12            1.15              0.64         79.54                18.77         0.519            pass              0.259             64.5                           0.501                5.00              0.408                                 ok           False                  False
  CSCO           83.33               30            0.46              0.34        104.37                35.63         0.514            pass              0.481             69.0                           0.734               -2.32             -0.017           downtrend_blocked_streak           False                  False
   KDP           96.88               32            0.10              0.02         35.83                21.81         0.507            pass              0.872             91.5                           0.674                3.90              0.355                                 ok           False                  False
  AAPL           94.12               17            1.06              2.55        343.54                14.54         0.496 below_threshold              0.555             27.4                           0.378               -0.57              0.043                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-02T10:40:04.730319-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:35:05.961580-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:30:04.618613-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:25:05.872809-05:00 early_entry_1025 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.816, "early_reclaim_pct": 76.2, "matched_signals": 41, "recovery_stability_score": 0.632, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:20:04.868575-05:00 early_entry_1020 early_entry_shadow {"contract_symbol": "BKR261218C00055000", "current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 63463.28, "hypothetical_contracts": 235, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1017.0, "option_spread_pct": 22.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.813, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.768, "success_rate": 92.68, "ticker": "BKR", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-02T10:20:04.868575-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "CEG261218C00260000", "fill_price": 22.65, "pnl": 9750.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.75, "ticker": "CEG"}
2026-11-02T10:15:01.964431-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:10:04.210177-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:05:01.515738-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:00:05.841210-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102104004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102104004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102104004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102104004)

</details>

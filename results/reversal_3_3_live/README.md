# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 10:20:04 EDT`
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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.78               37            0.75              0.81        153.73               126.50         0.797          pass              0.581             73.4                           0.578               46.65              5.193                  ok            True                  False
  PYPL           92.59               27            0.98              0.41         58.83                59.96         0.665          pass              0.687             57.0                           0.517                0.12              0.216                  ok            True                  False
  SHOP           96.77               31            1.54              1.65        151.90                81.89         0.653          pass              0.641             12.0                           0.239               16.33              2.896                  ok            True                  False
  ABNB          100.00               10            2.58              3.35        183.55                64.05         0.631          pass              0.501             12.8                           0.113               17.77              2.254                  ok            True                  False
 CMCSA           88.24               17            1.23              0.22         25.56                42.38         0.621          pass              0.398             23.2                           0.311                7.03              0.684                  ok            True                  False
  GEHC           91.67               24            1.21              0.62         72.49                54.33         0.619          pass              0.615             49.4                           0.642               -0.04              0.328                  ok            True                  False
   ROP          100.00               21            1.34              3.76        397.89                44.32         0.606          pass              0.670             45.3                           0.557                1.25              0.193                  ok            True                  False
  PAYX          100.00               13            1.55              1.32        120.74                33.26         0.575          pass              0.576             32.9                           0.387                2.66              0.367                  ok            True                  False
  FAST          100.00               22            0.61              0.22         52.28                25.01         0.565          pass              0.705             56.2                           0.326               11.57              1.205                  ok            True                  False
  MDLZ           88.46               26            0.52              0.22         61.68                29.90         0.560          pass              0.576             62.6                           0.701               -2.57             -0.194                  ok            True                  False
   ADP           95.83               24            1.27              2.41        270.06                32.74         0.536          pass              0.648             33.6                           0.519                1.43              0.133                  ok            True                  False
   PEP           81.82               22            0.92              0.89        138.03                20.92         0.522          pass              0.254             24.4                           0.452               -2.18             -0.203                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-12T10:20:04.811080-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "matched_signals": 34, "recovery_stability_score": 0.643, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T10:15:04.787408-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:10:02.811881-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:05:01.817084-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:00:04.707045-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "REGN260918C00790000", "current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "entry_ask": 32.7, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 28.85, "hypothetical_budget": 17549.0, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 45.0, "option_spread_pct": 26.69, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "matched_signals": 38, "recovery_stability_score": 0.62, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.698, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.591, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T09:50:02.620693-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "LRCX260918C00310000", "fill_price": 34.9, "pnl": 4025.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 29.98, "ticker": "LRCX"}
2026-08-12T09:35:01.769154-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:30:01.771593-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:25:01.593760-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-08-12T09:20:03.729351-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812102004)

</details>

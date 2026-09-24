# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 10:55:04 EDT`
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

- Cash: `$67,953.30`
- Equity: `$67,953.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            2.04              2.32        161.21               109.59         0.741          pass              0.691             46.9                           0.307               19.74              2.701                  ok            True                  False
  NVDA           90.91               22            1.72              2.71        224.35                44.57         0.571          pass              0.465             12.3                           0.250               -0.80              0.370                  ok            True                  False
   WMT           81.82               11            1.49              1.16        110.03                21.22         0.536          pass              0.130              7.0                           0.140                2.88              0.269                  ok            True                  False
   ADP           95.00               20            0.70              1.29        263.13                21.61         0.529          pass              0.587             22.4                           0.249               -0.64             -0.017                  ok            True                  False
    MU           90.00               30            1.89             14.14       1065.82                49.67         0.529          pass              0.562             36.4                           0.373                2.33              0.936                  ok            True                  False
  MPWR           84.00               25            2.32             21.98       1346.05                51.84         0.526          pass              0.337             25.9                           0.270               10.00              1.187                  ok            True                  False
  MSFT          100.00               20            1.23              4.32        498.74                22.42         0.514          pass              0.620             34.2                           0.607                0.56              0.086                  ok            True                  False
  DRAM           82.14               28            2.37              1.03         61.46                51.34         0.512          pass              0.264             12.0                           0.202               -1.87              0.485                  ok            True                  False
  UPRO           84.00               25            1.22              1.29        149.75                31.44         0.507          pass              0.407             49.7                           0.460                0.86              0.391                  ok            True                  False
  CRWD           88.64               44            0.17              0.31        262.36                96.70         0.721          pass              0.768             88.7                           0.873               26.10              2.260                  ok           False                  False
    ZS           97.78               45            0.13              0.19        214.37                79.52         0.647          pass              0.946             93.8                           0.710               28.95              2.776                  ok           False                  False
  PYPL           89.47               38            0.29              0.10         52.47                57.12         0.611          pass              0.691             63.4                           0.493                0.36             -0.161                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-24T10:55:04.808112-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:50:06.565866-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:45:04.775481-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:40:03.659687-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:35:04.814352-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:30:06.608889-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:25:04.755958-04:00 early_entry_1025 early_entry_shadow            {"contract_symbol": "TEAM261023C00195000", "current_drop_pct": 0.57, "early_entry_score": 0.878, "early_reclaim_pct": 77.8, "entry_ask": 12.8, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.05, "hypothetical_budget": 33976.65, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 3.0, "option_spread_pct": 12.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.579, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.878, "early_reclaim_pct": 77.8, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.579, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-24T10:20:05.835034-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:15:06.803201-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:10:01.731428-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261030C00192500", "current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "entry_ask": 12.7, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 11.0, "hypothetical_budget": 33976.65, "hypothetical_contracts": 30, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 30.91, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "matched_signals": 35, "recovery_stability_score": 0.594, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924105504)

</details>

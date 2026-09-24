# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 14:05:04 EDT`
Last processed slot: `manage_1400`

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
  MSTR           94.29               35            0.90              1.02        161.76               109.59         0.764          pass              0.854             76.6                           0.369               21.13              2.753                  ok            True                  False
  CRWD           88.64               44            0.52              0.96        262.08                96.70         0.699          pass              0.696             65.2                           0.422               25.66              2.244                  ok            True                  False
  SOXL           80.65               31            3.14              3.21        144.87               119.42         0.664          pass              0.401             59.0                           0.418               12.62              2.345                  ok            True                  False
  PANW           80.49               41            0.70              1.94        392.47                79.07         0.628          pass              0.476             66.6                           0.456               16.54              1.356                  ok            True                  False
  PYPL           90.32               31            0.79              0.29         52.39                57.12         0.619          pass              0.591             38.1                           0.469               -0.14             -0.184                  ok            True                  False
  NVDA           89.66               29            0.89              1.40        224.91                44.57         0.578          pass              0.606             54.6                           0.505                0.04              0.408                  ok            True                  False
  TEAM          100.00               38            0.92              1.25        194.54                58.95         0.557          pass              0.835             64.3                           0.414                8.75              0.855                  ok            True                  False
  MPWR           86.21               29            1.59             15.08       1349.01                51.84         0.545          pass              0.494             49.2                           0.416               10.81              1.221                  ok            True                  False
    MU           86.84               38            0.79              5.96       1069.33                49.67         0.534          pass              0.642             73.2                           0.467                3.46              0.986                  ok            True                  False
   WMT           80.00               10            1.60              1.24        110.00                21.22         0.529          pass              0.125             24.1                           0.465                2.77              0.264                  ok            True                  False
  WDAY           93.75               32            1.01              1.37        191.79                50.68         0.527          pass              0.771             68.3                           0.425                2.35              0.302                  ok            True                  False
  MSFT           95.45               22            1.10              3.85        498.94                22.42         0.506          pass              0.654             41.3                           0.489                0.70              0.093                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-09-24T12:00:04.840325-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:55:06.286422-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:50:04.896304-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:45:04.623722-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:40:06.370244-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:35:05.981561-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:30:04.769449-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "MSTR261030C00160000", "current_drop_pct": 1.05, "early_entry_score": 0.841, "early_reclaim_pct": 72.6, "entry_ask": 14.25, "entry_bid": 13.65, "entry_mode": "early", "entry_option_price": 13.95, "hypothetical_budget": 33976.65, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 590.0, "option_spread_pct": 4.3, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.758, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.841, "early_reclaim_pct": 72.6, "matched_signals": 35, "recovery_stability_score": 0.604, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.758, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-24T11:25:06.367252-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "MSTR261030C00160000", "current_drop_pct": 0.89, "early_entry_score": 0.855, "early_reclaim_pct": 76.9, "entry_ask": 13.85, "entry_bid": 13.5, "entry_mode": "early", "entry_option_price": 13.675, "hypothetical_budget": 33976.65, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 590.0, "option_spread_pct": 2.56, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.764, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.855, "early_reclaim_pct": 76.9, "matched_signals": 35, "recovery_stability_score": 0.615, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.764, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-24T11:20:06.692131-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T11:15:04.671941-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924140504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924140504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924140504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924140504)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 12:30:02 EDT`
Last processed slot: `manage_1230`

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
  SOXL           81.82               33            2.34              2.39        145.23               119.42         0.701          pass              0.480             69.5                           0.806               13.55              2.382                  ok            True                  False
  PYPL           90.62               32            0.69              0.25         52.40                57.12         0.620          pass              0.631             46.3                           0.514               -0.04             -0.180                  ok            True                  False
  NVDA           92.59               27            0.96              1.51        224.86                44.57         0.589          pass              0.661             51.1                           0.689               -0.03              0.405                  ok            True                  False
  MPWR           86.67               30            1.18             11.18       1350.68                51.84         0.564          pass              0.554             62.3                           0.697               11.28              1.240                  ok            True                  False
  DRAM           82.76               29            1.50              0.65         61.62                51.34         0.555          pass              0.395             46.2                           0.692               -0.99              0.526                  ok            True                  False
  ADSK           81.48               27            1.66              2.52        216.07                55.47         0.545          pass              0.307             33.3                           0.305                3.35              0.229                  ok            True                  False
    MU           87.18               39            0.60              4.50       1069.95                49.67         0.543          pass              0.678             79.8                           0.786                3.67              0.995                  ok            True                  False
  WDAY           94.29               35            0.57              0.77        192.05                50.68         0.538          pass              0.848             82.1                           0.422                2.81              0.322                  ok            True                  False
   ADP           95.45               22            0.61              1.13        263.20                21.61         0.523          pass              0.629             32.2                           0.297               -0.56             -0.013                  ok            True                  False
  MSFT           95.45               22            1.04              3.63        499.03                22.42         0.510          pass              0.665             44.6                           0.536                0.76              0.095                  ok            True                  False
   STX           83.78               37            0.92              5.93        921.32                53.68         0.503          pass              0.556             75.0                           0.552                3.33              0.616                  ok            True                  False
   ADI           89.29               28            0.83              2.25        384.27                33.19         0.500          pass              0.633             71.8                           0.736                4.64              0.572                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924123002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924123002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924123002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924123002)

</details>

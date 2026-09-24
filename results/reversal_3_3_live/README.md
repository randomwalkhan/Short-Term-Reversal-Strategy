# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 10:50:06 EDT`
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
  MSTR           94.29               35            0.84              0.96        161.79               109.59         0.766          pass              0.858             78.0                           0.467               21.20              2.756                  ok            True                  False
  NVDA           91.30               23            1.53              2.42        224.47                44.57         0.577          pass              0.512             21.9                           0.343               -0.61              0.379                  ok            True                  False
  ADSK           81.25               32            1.05              1.59        216.47                55.47         0.555          pass              0.409             58.0                           0.677                4.00              0.258                  ok            True                  False
   WMT           81.82               11            1.41              1.09        110.06                21.22         0.541          pass              0.146             12.1                           0.171                2.97              0.272                  ok            True                  False
  MPWR           85.19               27            1.98             18.75       1347.44                51.84         0.534          pass              0.415             36.8                           0.476               10.38              1.203                  ok            True                  False
   ADP           95.00               20            0.70              1.30        263.12                21.61         0.529          pass              0.585             21.9                           0.225               -0.65             -0.017                  ok            True                  False
  DRAM           82.14               28            2.13              0.92         61.51                51.34         0.526          pass              0.293             21.2                           0.313               -1.62              0.497                  ok            True                  False
    MU           84.85               33            1.57             11.76       1066.84                49.67         0.522          pass              0.476             47.2                           0.608                2.66              0.951                  ok            True                  False
  CTSH          100.00               13            2.59              1.07         58.68                40.91         0.508          pass              0.503             10.8                           0.249               -1.01             -0.185                  ok            True                  False
  MSFT           95.45               22            1.09              3.81        498.96                22.42         0.506          pass              0.656             41.9                           0.659                0.71              0.093                  ok            True                  False
  UPRO           82.14               28            0.91              0.96        149.89                31.44         0.506          pass              0.416             62.7                           0.568                1.18              0.406                  ok            True                  False
   STX           84.21               38            0.80              5.20        921.63                53.68         0.504          pass              0.584             78.0                           0.540                3.44              0.621                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-24T10:50:06.565866-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:45:04.775481-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:40:03.659687-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:35:04.814352-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:30:06.608889-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:25:04.755958-04:00 early_entry_1025 early_entry_shadow            {"contract_symbol": "TEAM261023C00195000", "current_drop_pct": 0.57, "early_entry_score": 0.878, "early_reclaim_pct": 77.8, "entry_ask": 12.8, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.05, "hypothetical_budget": 33976.65, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 3.0, "option_spread_pct": 12.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.579, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.878, "early_reclaim_pct": 77.8, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.579, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-24T10:20:05.835034-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:15:06.803201-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:10:01.731428-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261030C00192500", "current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "entry_ask": 12.7, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 11.0, "hypothetical_budget": 33976.65, "hypothetical_contracts": 30, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 30.91, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "matched_signals": 35, "recovery_stability_score": 0.594, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-24T10:05:06.327033-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924105006)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 10:25:06 EDT`
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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INTU           82.35               34            1.01              2.15        304.59               100.92         0.719          pass              0.486             63.7                           0.326               -0.63             -0.486                       ok            True                  False
  CSCO           92.31               13            1.69              1.47        123.52                58.94         0.666          pass              0.531             38.7                           0.303                3.14              0.520                       ok            True                  False
  PANW           91.43               35            0.90              1.67        265.61                58.75         0.568          pass              0.730             67.1                           0.542                2.80              0.446                       ok            True                  False
   WMT           86.67               30            0.70              0.59        119.58                36.35         0.536          pass              0.493             42.9                           0.452                0.35              0.104                       ok            True                  False
  ADBE           82.35               34            1.10              1.88        244.18                49.77         0.520          pass              0.391             38.8                           0.262                0.75              0.180                       ok            True                  False
   BKR           80.00               25            1.09              0.49         64.63                39.67         0.519          pass              0.206             18.0                           0.191               -3.89             -0.097                       ok            True                  False
  WDAY           84.62               13            3.87              3.90        142.09                70.13         0.518          pass              0.225             10.0                           0.178               11.43              1.258                       ok            True                  False
    ZS           80.00               25            1.75              1.58        128.57               157.94         0.898          pass              0.224             11.4                           0.168              -31.21             -1.797  downtrend_blocked_slope           False                  False
  TEAM           95.35               43            0.10              0.07         97.86                87.01         0.648          pass              0.955             96.8                           0.621               15.16              0.933                       ok           False                  False
  AVGO           89.47               38            0.43              1.19        396.09                69.53         0.607          pass              0.689             62.9                           0.332               -6.42             -0.881  downtrend_blocked_slope           False                  False
  CRWD           83.33               18            1.81              8.36        655.21                61.55         0.592          pass              0.315             37.9                           0.296               -3.68             -0.166 downtrend_blocked_streak           False                  False
  MRVL          100.00                7            5.53             11.19        284.05               136.27         0.585          pass              0.524             21.9                           0.213               31.02              4.354                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:15:04.004316-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:10:02.035934-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "entry_ask": 13.8, "entry_bid": 12.25, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.722, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:05:03.054973-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "entry_ask": 14.25, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "matched_signals": 37, "recovery_stability_score": 0.761, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:00:05.039106-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:00:05.039106-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.325, "pnl": -1572.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-09T00:00:03.806421-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-06-08T15:10:01.789141-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-06-08T15:05:04.798011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609102506)

</details>

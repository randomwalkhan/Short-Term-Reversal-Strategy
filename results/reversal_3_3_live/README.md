# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 10:35:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTU           82.86               35            0.97              2.07        304.62               100.92         0.716          pass              0.510             65.1                           0.318               -0.59             -0.484                      ok            True                  False
  PANW           89.29               28            1.32              2.46        265.27                58.75         0.587          pass              0.581             51.5                           0.370                2.36              0.427                      ok            True                  False
   WDC           96.55               29            1.53              5.63        524.52                73.41         0.571          pass              0.641             19.0                           0.136               -1.07              0.048                      ok            True                  False
   STX           95.65               23            1.69             10.35        872.34                63.66         0.544          pass              0.589             16.0                           0.134                1.92              0.119                      ok            True                  False
   WMT           84.38               32            0.50              0.42        119.65                36.35         0.532          pass              0.494             59.2                           0.623                0.56              0.113                      ok            True                  False
  ADBE           81.25               32            1.28              2.19        244.05                49.77         0.520          pass              0.318             28.7                           0.235                0.57              0.171                      ok            True                  False
  WDAY           84.62               13            3.87              3.90        142.09                70.13         0.518          pass              0.225              9.9                           0.215               11.43              1.258                      ok            True                  False
    ZS           78.26               23            1.95              1.77        128.49               157.94         0.896          pass              0.214             12.6                           0.169              -31.35             -1.807 downtrend_blocked_slope           False                  False
  SOXL           93.75               32            0.38              0.56        211.20               192.77         0.862          pass              0.818             72.9                           0.318               -6.71             -0.513 downtrend_blocked_slope           False                  False
  CSCO           85.71                7            1.88              1.64        123.45                58.94         0.684          pass              0.316             31.7                           0.362                2.94              0.511                      ok           False                  False
  TEAM           95.24               42            0.39              0.27         97.78                87.01         0.636          pass              0.927             87.9                           0.618               14.83              0.920                      ok           False                  False
  AVGO           89.66               29            1.13              3.14        395.26                69.53         0.621          pass              0.460              4.5                           0.043               -7.08             -0.913 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:30:02.001966-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:15:04.004316-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:10:02.035934-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "entry_ask": 13.8, "entry_bid": 12.25, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.722, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:05:03.054973-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "entry_ask": 14.25, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "matched_signals": 37, "recovery_stability_score": 0.761, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:00:05.039106-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:00:05.039106-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.325, "pnl": -1572.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-09T00:00:03.806421-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609103506)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 14:05:02 EDT`
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

- Cash: `$31,794.75`
- Equity: `$31,794.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     16          2026-06-05         2026-06-08         9.85       8.865 -1576.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           94.29               35            1.29              0.90         99.08                86.36         0.639          pass              0.796             61.6                           0.451               14.94              1.823                      ok            True                  False
  PAYX          100.00               15            1.04              0.73        100.22                33.39         0.608          pass              0.633             46.4                           0.387                2.56              0.554                      ok            True                  False
  CRWD           83.33               18            1.93              9.07        667.13                64.90         0.591          pass              0.279             26.0                           0.405                1.52              0.950                      ok            True                  False
  ROST           92.59               27            0.94              1.51        229.72                43.36         0.586          pass              0.586             25.9                           0.475               -2.81             -0.158                      ok            True                  False
  PANW           86.96               23            1.65              3.15        270.70                60.15         0.575          pass              0.453             41.1                           0.420                5.79              1.189                      ok            True                  False
  MSFT           87.50               24            1.09              3.19        415.30                34.82         0.560          pass              0.481             43.9                           0.713               -1.54              0.119                      ok            True                  False
  AMGN           90.00               10            1.32              3.23        348.19                22.27         0.532          pass              0.530             70.0                           0.501                1.67              0.296                      ok            True                  False
  FAST           94.74               19            1.18              0.38         46.63                21.36         0.526          pass              0.581             25.3                           0.336                5.23              0.685                      ok            True                  False
  WDAY           89.47               38            0.70              0.71        143.98                69.97         0.508          pass              0.693             67.7                           0.461               11.81              1.873                      ok            True                  False
  DASH           85.71               21            2.44              2.68        155.65                51.66         0.507          pass              0.366             29.8                           0.218               -3.95             -0.129                      ok            True                  False
   ADP           96.67               30            0.90              1.46        231.33                32.55         0.500          pass              0.739             51.8                           0.433                2.02              0.600                      ok            True                  False
    ZS           82.05               39            0.56              0.51        130.56               157.69         0.894          pass              0.565             76.0                           0.664              -28.69             -2.382 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:50:04.863668-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:45:02.732022-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:40:03.636153-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:35:06.615496-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:30:04.779379-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:25:01.866024-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "entry_ask": 9.7, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 20.45, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.609, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "matched_signals": 36, "recovery_stability_score": 0.609, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T11:20:06.683285-04:00 early_entry_1120 early_entry_shadow                           {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "entry_ask": 18.45, "entry_bid": 17.55, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 5.0, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "matched_signals": 36, "recovery_stability_score": 0.644, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608140502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608140502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608140502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608140502)

</details>

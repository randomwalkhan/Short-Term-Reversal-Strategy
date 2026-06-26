# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-26 14:15:01 EDT`
Last processed slot: `manual`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AVGO     option         option AVGO260821C00380000      4          2026-06-25         2026-06-26         31.3       28.17 -1252.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           91.67               12            4.76              2.56         75.79               122.54         0.677          pass              0.496             34.8                           0.354               12.45              1.259                                 ok            True                  False
    MU           90.91               11            4.96             42.16       1195.49               127.35         0.653          pass              0.471             35.9                           0.225               15.81              1.528                                 ok            True                  False
   WBD           91.67               12            0.67              0.13         26.93                20.23         0.619          pass              0.423             12.3                           0.211               -0.22              0.071                                 ok            True                  False
  AMAT           91.67               12            3.79             17.70        660.41                87.16         0.589          pass              0.513             43.2                           0.293               16.30              1.421                                 ok            True                  False
  INTC           90.00               20            3.70              3.44        131.40                97.28         0.554          pass              0.489             33.4                           0.219                9.40              1.083                                 ok            True                  False
  PCAR           82.61               23            1.02              0.87        121.31                36.28         0.533          pass              0.408             66.3                           0.484                2.43              0.077                                 ok            True                  False
  MRVL          100.00               10            5.51             10.86        276.61               155.27         0.762          pass              0.532             18.6                           0.201               -5.33             -0.471            downtrend_blocked_slope           False                  False
  AVGO           81.25               16            2.29              6.08        376.30                76.91         0.678          pass              0.250             36.2                           0.387               -3.83             -0.262            downtrend_blocked_slope           False                  False
  ASML           91.67               12            3.30             42.55       1822.95                66.48         0.604          pass              0.437             17.3                           0.164               -6.27             -0.528            downtrend_blocked_slope           False                  False
  KLAC           85.71                7            5.12              9.28        254.82                93.32         0.575          pass              0.257             15.6                           0.187                1.81              0.130                                 ok           False                  False
  NVDA           81.82               33            0.66              0.90        195.35                47.09         0.559          pass              0.472             71.6                           0.586               -5.08             -0.635 downtrend_blocked_slope_and_streak           False                  False
  CSCO           83.33                6            2.64              2.20        118.03                39.88         0.553          pass              0.245             33.6                           0.555               -4.92             -0.248           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-26T12:00:02.704488-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "entry_ask": 17.3, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.75, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 6.57, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "matched_signals": 35, "recovery_stability_score": 0.58, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-26T11:53:23.382476-04:00 early_entry_1150 early_entry_shadow  {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "entry_ask": 17.0, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.6, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 4.82, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.78, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "matched_signals": 35, "recovery_stability_score": 0.78, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-26T11:10:57.327815-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T10:35:51.274137-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T10:35:51.274137-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "AVGO260821C00380000", "fill_price": 28.17, "pnl": -1252.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AVGO"}
2026-06-26T10:15:51.250947-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-26T00:00:07.288133-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-06-25T15:10:04.366784-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-25T15:05:03.502084-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-25T15:00:05.541289-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260626141501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260626141501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260626141501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260626141501)

</details>

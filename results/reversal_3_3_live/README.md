# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 10:35:03 EDT`
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

- Cash: `$30,858.00`
- Equity: `$30,858.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  AAPL     option         option AAPL260821C00325000     15          2026-07-22         2026-07-23       10.850      9.7650 -1627.50       -10.0 stop_loss_hit_at_scan
  PYPL     option         option PYPL260821C00055000     55          2026-07-21         2026-07-23        3.075      2.7675 -1691.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.10               31            0.59              0.23         55.41                61.85         0.666          pass              0.524             42.6                           0.481               21.76              2.334                      ok            True                  False
  MDLZ          100.00               10            1.20              0.51         60.64                31.72         0.641          pass              0.545             27.0                           0.321                3.14              0.343                      ok            True                  False
  AAPL           94.44               18            1.11              2.54        324.80                37.45         0.613          pass              0.633             44.5                           0.661                1.91              0.378                      ok            True                  False
   PEP           84.62               13            1.09              1.04        135.21                30.61         0.610          pass              0.273             22.9                           0.315               -2.68             -0.227                      ok            True                  False
   KHC           92.31               13            1.25              0.23         25.86                31.13         0.604          pass              0.459             16.7                           0.246                3.87              0.462                      ok            True                  False
  MPWR           82.86               35            1.00              9.77       1394.27                64.79         0.550          pass              0.508             69.9                           0.395                0.75              0.251                      ok            True                  False
   ADP           96.15               26            0.73              1.25        242.59                36.25         0.549          pass              0.649             29.1                           0.255                0.02              0.058                      ok            True                  False
  GILD           91.67               24            0.91              0.83        129.99                35.55         0.545          pass              0.629             56.8                           0.736               -4.21             -0.143                      ok            True                  False
   MAR          100.00               10            2.09              5.41        367.48                21.19         0.530          pass              0.508             18.3                           0.201               -2.79             -0.142                      ok            True                  False
  AVGO           80.65               31            0.90              2.50        395.74                43.16         0.501          pass              0.361             51.2                           0.427               -1.96             -0.209                      ok            True                  False
  SOXL           84.85               33            1.74              1.96        160.15               181.21         0.823          pass              0.591             75.4                           0.625              -17.80             -2.299 downtrend_blocked_slope           False                  False
  MRVL           86.11               36            0.37              0.55        210.75                89.79         0.655          pass              0.663             86.9                           0.469              -13.57             -1.511 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-23T10:35:03.078129-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "REGN260821C00600000", "current_drop_pct": 0.71, "early_entry_score": 0.696, "early_reclaim_pct": 80.9, "entry_ask": 59.7, "entry_bid": 53.0, "entry_mode": "early", "entry_option_price": 56.35, "hypothetical_budget": 15429.0, "hypothetical_contracts": 2, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 549.0, "option_spread_pct": 11.89, "option_volume": 131.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.791, "shadow_only": true, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.696, "early_reclaim_pct": 80.9, "matched_signals": 36, "recovery_stability_score": 0.791, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-23T10:30:04.030785-04:00 early_entry_1030 early_entry_shadow  {"contract_symbol": "REGN260821C00600000", "current_drop_pct": 0.68, "early_entry_score": 0.699, "early_reclaim_pct": 81.8, "entry_ask": 58.3, "entry_bid": 53.0, "entry_mode": "early", "entry_option_price": 55.65, "hypothetical_budget": 15429.0, "hypothetical_contracts": 2, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 549.0, "option_spread_pct": 9.52, "option_volume": 131.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.772, "shadow_only": true, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.699, "early_reclaim_pct": 81.8, "matched_signals": 36, "recovery_stability_score": 0.772, "success_rate": 88.89, "ticker": "REGN", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-23T10:25:02.098761-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:20:02.100648-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:15:04.110282-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:10:06.093555-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "PYPL260821C00055000", "fill_price": 2.7675, "pnl": -1691.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-07-23T10:00:05.051160-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T09:55:06.076284-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "AAPL260821C00325000", "fill_price": 9.765, "pnl": -1627.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AAPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723103503)

</details>

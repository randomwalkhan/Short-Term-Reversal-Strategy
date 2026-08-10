# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 12:45:02 EDT`
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

- Cash: `$31,073.00`
- Equity: `$31,073.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.67               24            1.04              0.43         58.89                60.12         0.684          pass              0.556             27.6                           0.215                4.25              0.332                      ok            True                  False
  LRCX           87.10               31            1.11              2.42        310.31                90.05         0.654          pass              0.517             40.9                           0.302                5.58              1.426                      ok            True                  False
  AMAT           89.29               28            1.77              6.68        536.28                85.88         0.631          pass              0.494             20.9                           0.226                2.46              1.258                      ok            True                  False
 CMCSA           87.50               16            1.30              0.23         25.26                44.15         0.621          pass              0.433             43.6                           0.668                9.78              0.774                      ok            True                  False
  TMUS           90.91               33            0.74              0.92        176.80                55.81         0.610          pass              0.709             68.0                           0.746               -0.75             -0.138                      ok            True                   True
  MDLZ           91.67               12            1.61              0.71         62.31                30.17         0.562          pass              0.437             18.8                           0.342                1.53             -0.036                      ok            True                  False
  BKNG           95.00               20            1.79              2.69        213.27                46.72         0.557          pass              0.601             26.2                           0.247               12.73              1.023                      ok            True                  False
  ORLY           86.96               23            1.51              0.99         93.11                35.75         0.526          pass              0.382             19.2                           0.291                1.69              0.398                      ok            True                  False
  PCAR           96.77               31            0.61              0.57        132.87                29.28         0.520          pass              0.698             35.2                           0.346               -0.85             -0.196                      ok            True                  False
   PEP           80.00               25            0.63              0.62        138.76                22.07         0.513          pass              0.283             43.9                           0.554               -1.18             -0.272                      ok            True                  False
   HON           86.36               22            1.11              1.91        245.39                29.28         0.506          pass              0.449             49.6                           0.365               -0.92              0.008                      ok            True                  False
  ALNY           88.64               44            0.20              0.31        219.07               128.37         0.806          pass              0.744             77.6                           0.644              -21.42             -2.611 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-08-10T12:00:04.535713-04:00 early_entry_1200 early_entry_shadow                                          {"contract_symbol": "LRCX260918C00310000", "current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "entry_ask": 28.45, "entry_bid": 26.4, "entry_mode": "early", "entry_option_price": 27.425, "hypothetical_budget": 15536.5, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 7.47, "option_volume": 47.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "matched_signals": 37, "recovery_stability_score": 0.687, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T11:55:01.643754-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:50:01.638195-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:45:06.232412-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:40:01.623818-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:35:01.707228-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:30:06.173236-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:25:02.712869-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:20:04.669365-04:00 early_entry_1120 early_entry_shadow   {"contract_symbol": "HON260911C00245000", "current_drop_pct": 0.58, "early_entry_score": 0.738, "early_reclaim_pct": 73.6, "entry_ask": 9.4, "entry_bid": 6.7, "entry_mode": "early", "entry_option_price": 8.05, "hypothetical_budget": 15536.5, "hypothetical_contracts": 19, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 33.54, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 91.43, "ticker": "HON", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.738, "early_reclaim_pct": 73.6, "matched_signals": 35, "recovery_stability_score": 0.743, "success_rate": 91.43, "ticker": "HON", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T11:15:01.972299-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "HON260911C00245000", "current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "entry_ask": 9.4, "entry_bid": 6.7, "entry_mode": "early", "entry_option_price": 8.05, "hypothetical_budget": 15536.5, "hypothetical_contracts": 19, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 33.54, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "matched_signals": 32, "recovery_stability_score": 0.713, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810124502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810124502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810124502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810124502)

</details>

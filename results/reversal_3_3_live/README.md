# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 12:10:03 EDT`
Last processed slot: `manage_1200`

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
  SOXL           80.65               31            3.84              3.77        138.63               179.06         0.683          pass              0.296             23.7                           0.462                5.24              2.559                      ok            True                  False
  LRCX           87.88               33            0.84              1.83        310.56                90.05         0.660          pass              0.595             55.2                           0.592                5.87              1.438                      ok            True                  False
  PYPL           93.94               33            0.74              0.31         58.94                60.12         0.650          pass              0.735             48.2                           0.454                4.57              0.345                      ok            True                  False
  AMAT           90.00               30            1.42              5.34        536.85                85.88         0.643          pass              0.575             36.8                           0.522                2.83              1.274                      ok            True                  False
 CMCSA           92.31               13            1.48              0.26         25.25                44.15         0.637          pass              0.520             36.1                           0.558                9.59              0.766                      ok            True                  False
  TMUS           92.86               28            1.00              1.24        176.66                55.81         0.629          pass              0.696             56.9                           0.624               -1.01             -0.150                      ok            True                  False
  MDLZ           91.67               12            1.65              0.72         62.30                30.17         0.560          pass              0.432             17.2                           0.278                1.50             -0.038                      ok            True                  False
  BKNG           95.83               24            1.40              2.10        213.52                46.72         0.557          pass              0.676             42.4                           0.671               13.19              1.042                      ok            True                  False
  ORLY           87.50               24            1.43              0.94         93.13                35.75         0.525          pass              0.415             23.2                           0.203                1.77              0.401                      ok            True                  False
   PEP           80.00               25            0.62              0.60        138.76                22.07         0.514          pass              0.287             45.2                           0.492               -1.17             -0.272                      ok            True                  False
   HON           88.46               26            0.84              1.44        245.59                29.28         0.500          pass              0.568             61.9                           0.527               -0.65              0.021                      ok            True                  False
  ALNY           88.64               44            0.36              0.55        218.96               128.37         0.799          pass              0.689             59.7                           0.468              -21.55             -2.618 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810121003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810121003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810121003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810121003)

</details>

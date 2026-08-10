# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 10:55:01 EDT`
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
  TEAM           84.62               39            0.76              0.80        148.73               133.30         0.801          pass              0.612             72.0                           0.541               54.30              3.916                      ok            True                  False
 CMCSA           92.86               14            1.44              0.26         25.25                44.15         0.634          pass              0.546             37.6                           0.671                9.63              0.768                      ok            True                  False
  TMUS           92.86               28            0.94              1.17        176.69                55.81         0.633          pass              0.704             59.3                           0.756               -0.95             -0.147                      ok            True                  False
  AMAT           88.46               26            2.00              7.55        535.90                85.88         0.630          pass              0.399              1.4                           0.162                2.22              1.247                      ok            True                  False
  LRCX           86.21               29            1.76              3.83        309.71                90.05         0.624          pass              0.355              0.0                           0.163                4.89              1.396                      ok            True                  False
   STX           91.18               34            0.53              3.02        811.47                91.44         0.592          pass              0.769             83.9                           0.452               -1.05              0.515                      ok            True                  False
  MDLZ           92.86               14            1.31              0.57         62.36                30.17         0.571          pass              0.529             34.1                           0.611                1.85             -0.022                      ok            True                  False
  BKNG           95.00               20            1.69              2.53        213.33                46.72         0.564          pass              0.615             30.5                           0.435               12.85              1.028                      ok            True                  False
  ORLY           88.89               27            1.14              0.75         93.21                35.75         0.526          pass              0.519             38.7                           0.568                2.06              0.414                      ok            True                  False
  MCHP           84.00               25            2.79              1.65         83.98                76.06         0.512          pass              0.260              0.8                           0.038                5.69              0.912                      ok            True                  False
   HON           86.96               23            1.04              1.80        245.44                29.28         0.505          pass              0.480             52.6                           0.616               -0.86              0.011                      ok            True                  False
  ALNY           88.64               44            0.21              0.32        219.06               128.37         0.807          pass              0.715             67.8                           0.402              -21.43             -2.612 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-10T10:55:01.620992-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:50:05.624699-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "PYPL260918C00060000", "current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "entry_ask": 1.59, "entry_bid": 1.52, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 15536.5, "hypothetical_contracts": 99, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 8780.0, "option_spread_pct": 4.5, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:45:01.632821-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-08-10T10:30:04.655219-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:25:03.677192-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:20:04.656698-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:15:05.996593-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810105501)

</details>

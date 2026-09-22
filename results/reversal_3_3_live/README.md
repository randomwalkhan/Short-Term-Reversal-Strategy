# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 11:55:04 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           86.84               38            1.26              2.19        248.41                96.94         0.651            pass              0.532             32.5                           0.329               17.24              2.075                                 ok            True                  False
   KHC           94.44               18            0.55              0.09         24.33                22.03         0.539            pass              0.585             30.8                           0.306               -2.67             -0.128                                 ok            True                  False
  MSFT          100.00               14            1.53              5.38        499.31                22.55         0.522            pass              0.479              0.0                           0.245               -0.00              0.060                                 ok            True                  False
  FTNT           85.71               28            1.75              2.15        174.31                58.27         0.511            pass              0.439             38.4                           0.450                9.33              1.173                                 ok            True                  False
  WDAY           92.31               26            1.65              2.21        190.97                50.40         0.507            pass              0.560             24.8                           0.370                1.33              0.397                                 ok            True                  False
  PANW           77.14               35            1.42              3.70        370.17                79.39         0.568            pass              0.329             35.3                           0.332                8.75              1.187                                 ok           False                  False
   TRI           92.31               26            1.54              1.03         94.99                58.54         0.560            pass              0.493              0.7                           0.180               -4.91             -0.325 downtrend_blocked_slope_and_streak           False                  False
   WBD           93.33               45            0.00              0.00         30.80                38.22         0.525            pass              0.908            100.0                           0.564                9.53              0.745                                 ok           False                  False
  UPRO           83.33               36            0.32              0.35        153.92                31.53         0.500            pass              0.479             55.8                           0.310                2.86              0.306                                 ok           False                  False
  ADBE           90.00               10            3.44              6.01        246.94                45.94         0.467 below_threshold              0.427             37.8                           0.264               -6.35             -0.424            downtrend_blocked_slope           False                  False
  TEAM          100.00                9            4.85              6.64        192.82                58.22         0.457 below_threshold              0.464              5.9                           0.203                5.53              0.891                                 ok           False                  False
  VRSK           91.43               35            0.65              0.78        171.68                39.65         0.451 below_threshold              0.785             89.4                           0.441               -2.35             -0.238           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-22T11:55:04.534124-04:00 early_entry_1155 early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:50:04.129679-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.25, "hypothetical_budget": 35735.4, "hypothetical_contracts": 25, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.23, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:45:05.185045-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:40:04.072289-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:35:05.251125-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:30:06.235648-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:25:05.068681-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                               {"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "matched_signals": 31, "recovery_stability_score": 0.684, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:20:05.152954-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                 {"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "matched_signals": 31, "recovery_stability_score": 0.652, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:14:41.644035-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:55:06.218660-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922115504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922115504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922115504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922115504)

</details>

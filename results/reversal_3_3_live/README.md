# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 11:20:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.65              1.83        157.83               104.19         0.711            pass              0.688             46.8                           0.420               13.92              2.449                                 ok            True                  False
  SHOP           84.62               26            1.65              1.65        141.54                62.03         0.543            pass              0.461             59.1                           0.836                4.49              1.144                                 ok            True                  False
   CEG           81.25               16            1.89              3.48        261.78                41.90         0.532            pass              0.174             15.7                           0.267               -2.37             -0.002                                 ok            True                  False
  PYPL           88.24               17            1.60              0.62         54.78                60.08         0.509            pass              0.491             58.1                           0.588                0.24              0.081                                 ok            True                  False
  MSFT          100.00               18            1.32              4.78        514.12                25.07         0.502            pass              0.657             51.1                           0.714                0.78              0.232                                 ok            True                  False
   TRI           88.24               34            0.76              0.53         98.76                56.74         0.590            pass              0.648             69.9                           0.663               -7.16             -0.502 downtrend_blocked_slope_and_streak           False                  False
   WBD           95.65               46            0.02              0.00         30.86                38.15         0.546            pass              0.936             93.7                           0.663                9.80              1.281                                 ok           False                  False
  ASML           83.78               37            0.26              3.23       1742.56                41.71         0.526            pass              0.598             88.1                           0.503               10.42              1.141                                 ok           False                  False
   KHC           96.15               26            0.02              0.00         23.63                20.56         0.502            pass              0.848             97.2                           0.462               -2.66             -0.472 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.89                9            2.50              2.66        151.06                32.02         0.501            pass              0.334             15.7                           0.336                1.83              0.529                                 ok           False                  False
   ADI           87.50               24            1.18              3.25        392.21                35.26         0.498 below_threshold              0.516             57.6                           0.400                7.74              0.945                                 ok           False                  False
   BKR           92.31               39            0.01              0.00         57.83                32.19         0.493 below_threshold              0.869             99.2                           0.582                1.84              0.246                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T11:20:06.180521-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:15:05.555577-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:10:06.397628-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:05:04.918839-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:00:06.419831-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:55:05.016465-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:50:06.030235-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:45:06.952611-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:35:06.564944-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.688, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928112006)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 11:45:04 EDT`
Last processed slot: `early_entry_1145`

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
  MSTR           93.75               32            1.49              1.66        157.90               104.19         0.705            pass              0.739             51.8                           0.423               14.10              2.456                                 ok            True                  False
  SHOP           85.71               35            1.12              1.11        141.77                62.03         0.526            pass              0.589             72.3                           0.794                5.06              1.169                                 ok            True                  False
   CEG           80.00               15            2.06              3.79        261.64                41.90         0.524            pass              0.110              8.0                           0.227               -2.54             -0.010                                 ok            True                  False
  MSFT          100.00               17            1.38              5.00        514.03                25.07         0.504            pass              0.644             48.8                           0.606                0.72              0.229                                 ok            True                  False
   TRI           88.24               34            0.74              0.51         98.77                56.74         0.591            pass              0.651             70.7                           0.725               -7.14             -0.501 downtrend_blocked_slope_and_streak           False                  False
   WBD           95.65               46            0.02              0.00         30.86                38.15         0.546            pass              0.936             93.7                           0.637                9.80              1.281                                 ok           False                  False
  CHTR           79.55               44            0.11              0.08        112.87                64.54         0.522            pass              0.538             95.3                           0.645              -21.32             -2.605 downtrend_blocked_slope_and_streak           False                  False
  UPRO          100.00                8            2.58              2.74        151.02                32.02         0.512            pass              0.490             13.1                           0.301                1.75              0.526                                 ok           False                  False
  LRCX           70.37               27            2.27              5.02        313.06                61.39         0.504            pass              0.295             43.6                           0.481               12.75              1.774                                 ok           False                  False
   KHC           96.00               25            0.11              0.02         23.62                20.56         0.501            pass              0.808             86.0                           0.509               -2.74             -0.476 downtrend_blocked_slope_and_streak           False                  False
   ADI           88.89               27            0.93              2.58        392.50                35.26         0.499 below_threshold              0.599             66.4                           0.530                8.01              0.956                                 ok           False                  False
  PYPL           80.00               10            2.33              0.90         54.66                60.08         0.496 below_threshold              0.167             39.0                           0.296               -0.50              0.047                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-09-28T11:45:04.059310-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:40:05.053761-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "entry_ask": 30.1, "entry_bid": 28.7, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.76, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "matched_signals": 30, "recovery_stability_score": 0.556, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:35:05.945998-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:30:05.957358-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:25:05.958568-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:20:06.180521-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:15:05.555577-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:10:06.397628-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:05:04.918839-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:00:06.419831-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928114504)

</details>

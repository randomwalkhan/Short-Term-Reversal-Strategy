# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:55:02 EDT`
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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.50               32            0.51              0.20         56.47                61.55         0.634          pass              0.642             77.3                           0.756               24.79              2.836                                 ok            True                  False
   WBD           83.33               12            0.95              0.18         26.79                20.40         0.581          pass              0.205             15.0                           0.182                1.90              0.378                                 ok            True                  False
  PAYX          100.00               31            0.58              0.46        114.19                33.31         0.526          pass              0.783             63.5                           0.753                7.91              0.831                                 ok            True                   True
  ORLY           80.77               26            1.30              0.78         85.71                41.23         0.522          pass              0.254             24.8                           0.294                0.82             -0.005                                 ok            True                  False
  PCAR           83.33               24            1.13              0.99        125.77                30.30         0.520          pass              0.234              0.0                           0.188               -0.90              0.094                                 ok            True                  False
  MNST          100.00               25            0.55              0.38         97.34                20.09         0.515          pass              0.766             71.6                           0.436               -0.42              0.161                                 ok            True                  False
  GILD           92.86               28            0.57              0.54        134.05                34.72         0.515          pass              0.628             37.9                           0.371                3.01              0.047                                 ok            True                  False
  BKNG           85.71               21            1.73              2.20        180.74                41.44         0.514          pass              0.359             27.3                           0.353               -1.38              0.144                                 ok            True                  False
   CSX           91.30               23            0.62              0.22         50.66                17.40         0.511          pass              0.532             30.9                           0.215                3.33              0.446                                 ok            True                  False
   ADP           96.30               27            0.77              1.37        254.68                34.14         0.508          pass              0.726             54.1                           0.672                5.77              0.625                                 ok            True                  False
  TEAM           85.00               40            0.81              0.53         93.06                69.60         0.507          pass              0.629             81.8                           0.730                8.22              0.790                                 ok            True                  False
  KLAC           85.71               28            1.25              1.87        211.95               107.27         0.708          pass              0.361              5.8                           0.102               -9.95             -0.607 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-20T10:55:02.013692-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "PAYX260821C00110000", "current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 63.5, "entry_ask": 5.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 15705.88, "hypothetical_contracts": 28, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1044.0, "option_spread_pct": 7.27, "option_volume": 102.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 63.5, "matched_signals": 31, "recovery_stability_score": 0.753, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-20T10:50:05.022185-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:45:02.099135-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:40:04.090335-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:35:05.083590-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:30:04.102843-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:25:04.012806-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:20:01.111901-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720105502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720105502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720105502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720105502)

</details>

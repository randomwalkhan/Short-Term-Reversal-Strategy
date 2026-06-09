# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:30:02 EDT`
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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.23              0.71         82.87                69.62         0.693          pass              0.271             19.7                           0.123               -1.86             -0.116                                 ok            True                  False
  CDNS           92.31               26            1.27              3.50        392.74                58.79         0.572          pass              0.520              9.4                           0.260                1.96              0.453                                 ok            True                  False
  CTSH           93.55               31            0.77              0.29         52.87                51.28         0.564          pass              0.723             54.9                           0.262                1.49             -0.116                                 ok            True                  False
  TEAM           95.24               21            3.96              2.72         96.73                87.01         0.537          pass              0.531              1.3                           0.160               10.70              0.754                                 ok            True                  False
   CSX           92.00               25            0.59              0.20         47.03                21.30         0.517          pass              0.634             54.1                           0.297                0.78              0.172                                 ok            True                  False
   WDC          100.00               17            3.44             12.69        521.49                73.41         0.511          pass              0.509              3.7                           0.283               -3.00             -0.042                                 ok            True                  False
    ZS           72.73               11            4.13              3.74        127.65               157.94         0.851          pass              0.098              2.0                           0.144              -32.88             -1.909            downtrend_blocked_slope           False                  False
  DRAM          100.00               13            2.54              1.08         60.06               103.58         0.721          pass              0.517              8.3                           0.263               -2.53             -0.349            downtrend_blocked_slope           False                  False
  INTU           75.00               20            2.39              5.10        303.32               100.92         0.715          pass              0.180             14.0                           0.154               -2.01             -0.550 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                2            3.45              3.00        122.87                58.94         0.635          pass              0.472              2.7                           0.222                1.30              0.438                                 ok           False                  False
  MSFT           83.33                6            1.94              5.59        409.34                36.13         0.622          pass              0.160              2.8                           0.173               -2.95             -0.371            downtrend_blocked_slope           False                  False
   ADI          100.00               16            2.03              5.74        401.43                49.72         0.585          pass              0.519              6.7                           0.205               -5.52             -0.325            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:10:02.019874-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "WDC260717C00520000", "current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "entry_ask": 61.05, "entry_bid": 54.7, "entry_mode": "early", "entry_option_price": 57.875, "hypothetical_budget": 15111.13, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 457.0, "option_spread_pct": 10.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "matched_signals": 32, "recovery_stability_score": 0.618, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-09T11:05:04.976190-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:00:04.007300-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:55:02.016087-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:45:01.973366-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609113002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609113002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609113002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609113002)

</details>

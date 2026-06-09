# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:20:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TRI           86.36               22            0.85              0.49         82.97                69.62         0.694          pass              0.453             44.5                           0.215               -1.49             -0.098                      ok            True                  False
    MU           82.76               29            1.55             10.32        944.86               111.98         0.691          pass              0.394             41.5                           0.404                4.32              0.175                      ok            True                  False
  TEAM           96.55               29            2.51              1.72         97.15                87.01         0.590          pass              0.651             21.7                           0.146               12.38              0.822                      ok            True                  False
   WDC           96.55               29            1.31              4.84        524.85                73.41         0.567          pass              0.768             61.7                           0.657               -0.86              0.057                      ok            True                  False
  CTSH           93.55               31            0.73              0.27         52.87                51.28         0.567          pass              0.731             57.7                           0.286                1.53             -0.114                      ok            True                  False
   STX           96.43               28            1.46              8.96        872.93                63.66         0.511          pass              0.736             54.9                           0.629                2.15              0.129                      ok            True                  False
    ZS           76.47               17            3.01              2.72        128.08               157.94         0.874          pass              0.185             16.9                           0.326              -32.09             -1.856 downtrend_blocked_slope           False                  False
  INTU           79.17               24            1.83              3.92        303.83               100.92         0.728          pass              0.268             34.0                           0.295               -1.46             -0.524                      ok           False                  False
  SOXL           94.74               19            4.59              6.79        208.53               192.77         0.668          pass              0.617             32.4                           0.342              -10.65             -0.709 downtrend_blocked_slope           False                  False
  CSCO           83.33                6            2.70              2.34        123.15                58.94         0.634          pass              0.196             14.5                           0.268                2.09              0.473                      ok           False                  False
  PANW           78.57               14            2.42              4.51        264.40                58.75         0.598          pass              0.120             11.2                           0.150                1.22              0.376                      ok           False                  False
   ADI           96.55               29            0.75              2.13        402.98                49.72         0.590          pass              0.666             26.8                           0.262               -4.29             -0.266 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:10:02.019874-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "WDC260717C00520000", "current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "entry_ask": 61.05, "entry_bid": 54.7, "entry_mode": "early", "entry_option_price": 57.875, "hypothetical_budget": 15111.13, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 457.0, "option_spread_pct": 10.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.829, "early_reclaim_pct": 74.8, "matched_signals": 32, "recovery_stability_score": 0.618, "success_rate": 96.88, "ticker": "WDC", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-09T11:05:04.976190-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:00:04.007300-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:55:02.016087-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:45:01.973366-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:40:03.961827-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609112006)

</details>

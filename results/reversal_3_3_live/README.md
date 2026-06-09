# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:05:04 EDT`
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
    MU           80.00               25            2.17             14.44        943.09               111.98         0.675          pass              0.222             18.1                           0.166                3.66              0.147                      ok            True                  False
  TEAM           93.33               30            2.30              1.58         97.21                87.01         0.592          pass              0.633             28.3                           0.166               12.62              0.832                      ok            True                  False
   WDC           96.15               26            2.17              8.02        523.49                73.41         0.529          pass              0.669             36.6                           0.299               -1.72              0.018                      ok            True                  False
   STX           95.00               20            2.24             13.76        870.87                63.66         0.512          pass              0.610             30.7                           0.275                1.34              0.093                      ok            True                  False
    ZS           75.00               16            3.20              2.89        128.01               157.94         0.871          pass              0.162             11.8                           0.158              -32.22             -1.865 downtrend_blocked_slope           False                  False
  DRAM          100.00               20            0.47              0.20         60.43               103.58         0.801          pass              0.754             69.0                           0.386               -0.45             -0.253                      ok           False                  False
  INTU           79.17               24            1.82              3.90        303.84               100.92         0.728          pass              0.269             34.3                           0.191               -1.45             -0.524                      ok           False                  False
   TRI           89.29               28            0.26              0.15         83.11                69.62         0.694          pass              0.685             82.7                           0.356               -0.91             -0.072                      ok           False                  False
  CSCO          100.00                3            2.99              2.60        123.04                58.94         0.662          pass              0.474              2.6                           0.080                1.78              0.459                      ok           False                  False
  PAYX          100.00               26            0.03              0.02         98.91                34.09         0.622          pass              0.863             98.2                           0.678                4.31              0.511                      ok           False                  False
  AVGO           85.00               20            2.00              5.54        394.22                69.53         0.600          pass              0.336             25.4                           0.251               -7.90             -0.953 downtrend_blocked_slope           False                  False
  PANW           78.57               14            2.46              4.58        264.37                58.75         0.596          pass              0.116              9.8                           0.121                1.18              0.374                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-09T11:05:04.976190-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:00:04.007300-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:55:02.016087-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:45:01.973366-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:40:03.961827-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:30:02.001966-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609110504)

</details>

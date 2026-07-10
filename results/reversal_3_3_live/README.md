# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 11:19:23 EDT`
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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  GILD     option         option GILD260821C00135000     24          2026-07-09         2026-07-10         5.85       5.265 -1404.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           95.65               23            0.76              1.68        315.50                35.27         0.586          pass              0.667             40.6                           0.532               14.05              1.466                                 ok            True                  False
  SOXL           86.67               30            2.21              2.98        191.17               230.34         0.909          pass              0.620             72.8                           0.749              -25.50             -3.547            downtrend_blocked_slope           False                  False
  DRAM           83.33               24            1.82              0.82         64.01               119.54         0.780          pass              0.447             62.3                           0.711              -17.82             -2.073            downtrend_blocked_slope           False                  False
   WDC           86.49               37            0.16              0.66        577.77               123.00         0.779          pass              0.716             95.0                           0.767              -14.55             -1.594            downtrend_blocked_slope           False                  False
    MU           81.25               32            1.08              7.53        988.41               119.39         0.765          pass              0.463             68.7                           0.714              -19.16             -2.381            downtrend_blocked_slope           False                  False
  KLAC           91.43               35            0.54              0.87        229.12               118.44         0.743          pass              0.801             85.1                           0.738              -11.80             -2.213 downtrend_blocked_slope_and_streak           False                  False
  LRCX           92.59               27            1.64              4.05        351.44               104.85         0.698          pass              0.704             61.6                           0.683              -13.55             -2.109 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.18               34            0.52              6.54       1801.45                72.45         0.655          pass              0.749             75.1                           0.642               -2.51             -0.512            downtrend_blocked_slope           False                  False
  MRVL           92.31               26            2.93              4.99        241.13               107.78         0.620          pass              0.607             36.6                           0.570              -16.04             -2.169            downtrend_blocked_slope           False                  False
  MPWR           78.57               28            2.01             19.36       1365.83                84.23         0.600          pass              0.332             50.7                           0.608               -6.24             -0.253                                 ok           False                  False
  QCOM           82.76               29            1.41              1.88        190.30                71.74         0.569          pass              0.407             50.1                           0.573               -8.04             -0.375           downtrend_blocked_streak           False                  False
  CTSH           78.79               33            0.97              0.29         43.27                63.93         0.548          pass              0.256             16.0                           0.216                9.78              1.202                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-10T11:19:23.277635-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:46:53.268563-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00      manage_1000               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00135000", "fill_price": 5.265, "pnl": -1404.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-10T00:00:05.149826-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-07-09T15:10:06.797522-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:05:11.506156-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:00:11.129710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:55:10.687527-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:50:10.393351-04:00       entry_1500              entry {"allocated_cash": 14040.0, "asset_type": "option", "contract_symbol": "GILD260821C00135000", "contracts": 24, "early_entry_score": 0.621, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 8090.0, "option_spread_pct": 6.84, "option_volume": 34.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.541}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710111923)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710111923)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710111923)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710111923)

</details>

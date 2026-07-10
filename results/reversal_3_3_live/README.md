# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 13:30:01 EDT`
Last processed slot: `manage_1330`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MPWR           81.25               32            1.36             13.12       1368.51                84.23         0.620            pass              0.442             66.6                           0.595               -5.62             -0.223                       ok            True                  False
  AAPL           96.43               28            0.56              1.23        315.69                35.27         0.570            pass              0.747             56.5                           0.548               14.29              1.475                       ok            True                  False
  DRAM           83.33               24            1.49              0.67         64.07               119.54         0.794            pass              0.469             69.0                           0.678              -17.54             -2.058  downtrend_blocked_slope           False                  False
  MRVL           93.10               29            1.82              3.10        241.94               107.78         0.672            pass              0.725             60.6                           0.717              -15.08             -2.117  downtrend_blocked_slope           False                  False
  INTC           90.62               32            1.63              1.29        111.99                93.93         0.611            pass              0.683             63.9                           0.788              -16.69             -2.255  downtrend_blocked_slope           False                  False
  QCOM           84.85               33            0.92              1.23        190.58                71.74         0.579            pass              0.543             67.5                           0.728               -7.58             -0.353 downtrend_blocked_streak           False                  False
  CPRT          100.00                7            2.63              0.52         28.11                43.96         0.539            pass              0.454              0.0                           0.205               -8.20             -0.534  downtrend_blocked_slope           False                  False
  WDAY           82.93               41            0.30              0.29        138.22                60.14         0.518            pass              0.452             40.6                           0.319               21.24              1.909                       ok           False                  False
  MSFT           78.95               38            0.06              0.15        384.29                37.55         0.509            pass              0.514             92.3                           0.487                8.87              0.684                       ok           False                  False
  VRTX           85.71                7            2.19              7.62        493.24                34.73         0.503            pass              0.234             10.6                           0.301                1.13              0.230                       ok           False                  False
  CTSH           68.18               22            2.28              0.69         43.10                63.93         0.503            pass              0.132              0.5                           0.075                8.33              1.142                       ok           False                  False
   ADP           96.77               31            0.27              0.46        241.08                32.25         0.499 below_threshold              0.873             94.5                           0.596               11.24              1.136                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-07-10T11:47:54.272841-04:00 early_entry_1145 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T11:19:23.277635-04:00 early_entry_1115 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:46:53.268563-04:00 early_entry_1045 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "GILD260821C00135000", "fill_price": 5.265, "pnl": -1404.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-10T00:00:05.149826-04:00     data_refresh       data_refresh                                                                                                                                                                     {'saved': 93}
2026-07-09T15:10:06.797522-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-07-09T15:05:11.506156-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-07-09T15:00:11.129710-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-07-09T14:55:10.687527-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710133001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710133001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710133001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710133001)

</details>

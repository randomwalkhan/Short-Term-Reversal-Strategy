# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 13:00:02 EDT`
Last processed slot: `manage_1300`

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
  MPWR           81.25               32            1.51             14.56       1367.89                84.23         0.611          pass              0.430             62.9                           0.580               -5.76             -0.230                                 ok            True                  False
  SOXL           87.50               32            0.55              0.74        192.13               230.34         0.938          pass              0.720             93.2                           0.683              -24.23             -3.470            downtrend_blocked_slope           False                  False
  DRAM           83.33               24            1.80              0.81         64.01               119.54         0.780          pass              0.448             62.6                           0.642              -17.80             -2.072            downtrend_blocked_slope           False                  False
    MU           81.82               33            0.81              5.65        989.22               119.39         0.771          pass              0.514             78.5                           0.734              -18.94             -2.368            downtrend_blocked_slope           False                  False
  LRCX           93.94               33            0.61              1.51        352.52               104.85         0.724          pass              0.854             85.6                           0.680              -12.64             -2.062 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.67               36            0.19              2.38       1803.23                72.45         0.664          pass              0.824             91.0                           0.720               -2.19             -0.497            downtrend_blocked_slope           False                  False
  MRVL           92.59               27            2.47              4.20        241.47               107.78         0.644          pass              0.654             46.7                           0.579              -15.64             -2.147            downtrend_blocked_slope           False                  False
  QCOM           82.76               29            1.40              1.87        190.31                71.74         0.570          pass              0.408             50.4                           0.476               -8.03             -0.375           downtrend_blocked_streak           False                  False
  AAPL           96.67               30            0.48              1.06        315.77                35.27         0.564          pass              0.778             62.7                           0.710               14.38              1.478                                 ok           False                  False
  INTC           89.66               29            2.69              2.12        111.63                93.93         0.561          pass              0.562             40.6                           0.593              -17.58             -2.304            downtrend_blocked_slope           False                  False
  AVGO           88.10               42            0.01              0.04        401.09                53.79         0.545          pass              0.767             98.9                           0.722                5.84              0.695                                 ok           False                  False
  CPRT           90.91               11            2.24              0.44         28.14                43.96         0.530          pass              0.380              9.9                           0.308               -7.84             -0.516            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710130002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710130002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710130002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710130002)

</details>

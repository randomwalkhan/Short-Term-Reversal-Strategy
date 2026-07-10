# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 15:50:05 EDT`
Last processed slot: `manage_1600`

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
  MPWR           81.25               32            1.12             10.77       1369.51                84.23         0.636          pass              0.461             72.6                           0.803               -5.39             -0.212                                 ok            True                  False
  SOXL           88.24               34            0.07              0.09        192.41               230.34         0.942          pass              0.771             99.2                           0.834              -23.87             -3.448            downtrend_blocked_slope           False                  False
    MU           81.82               33            0.80              5.52        989.27               119.39         0.767          pass              0.515             79.0                           0.543              -18.92             -2.367            downtrend_blocked_slope           False                  False
  DRAM           83.33               24            2.15              0.97         63.94               119.54         0.764          pass              0.425             55.3                           0.518              -18.10             -2.088            downtrend_blocked_slope           False                  False
  LRCX           93.94               33            0.61              1.50        352.53               104.85         0.725          pass              0.855             85.7                           0.700              -12.64             -2.061 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.67               36            0.12              1.57       1803.58                72.45         0.668          pass              0.833             94.0                           0.729               -2.13             -0.494            downtrend_blocked_slope           False                  False
  MRVL           92.59               27            2.62              4.46        241.36               107.78         0.634          pass              0.643             43.4                           0.651              -15.77             -2.154            downtrend_blocked_slope           False                  False
  INTC           89.66               29            2.49              1.96        111.70                93.93         0.574          pass              0.577             45.0                           0.513              -17.41             -2.294            downtrend_blocked_slope           False                  False
  QCOM           83.33               30            1.27              1.69        190.38                71.74         0.573          pass              0.445             55.1                           0.622               -7.91             -0.369           downtrend_blocked_streak           False                  False
  AVGO           87.18               39            0.27              0.76        400.78                53.79         0.545          pass              0.679             79.9                           0.649                5.57              0.683                                 ok           False                  False
  CPRT          100.00                7            2.54              0.50         28.11                43.96         0.544          pass              0.474              6.5                           0.143               -8.12             -0.530            downtrend_blocked_slope           False                  False
  CTSH           70.83               24            1.91              0.58         43.15                63.93         0.516          pass              0.211             22.1                           0.409                8.74              1.159                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-07-10T15:10:08.910811-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:05:06.429039-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:00:09.226035-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:55:05.716481-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:50:05.489745-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-07-10T14:50:05.489745-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-10", "training_samples": 5470, "window": 5}
2026-07-10T11:47:54.272841-04:00 early_entry_1145 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T11:19:23.277635-04:00 early_entry_1115 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:46:53.268563-04:00 early_entry_1045 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710155005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710155005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710155005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710155005)

</details>

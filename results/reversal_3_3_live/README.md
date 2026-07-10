# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 16:00:02 EDT`
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
  MPWR           80.65               31            1.60             15.39       1367.53                84.23         0.611          pass              0.401             60.8                           0.648               -5.85             -0.234                                 ok            True                  False
  SOXL           87.88               33            0.19              0.25        192.34               230.34         0.941          pass              0.751             97.7                           0.730              -23.96             -3.454            downtrend_blocked_slope           False                  False
  DRAM           83.33               24            2.00              0.90         63.97               119.54         0.771          pass              0.434             58.4                           0.486              -17.97             -2.081            downtrend_blocked_slope           False                  False
    MU           80.65               31            1.31              9.06        987.76               119.39         0.751          pass              0.429             65.5                           0.452              -19.34             -2.391            downtrend_blocked_slope           False                  False
  LRCX           92.86               28            0.79              1.95        352.33               104.85         0.739          pass              0.781             81.4                           0.620              -12.80             -2.070 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.18               34            0.40              5.11       1802.06                72.45         0.662          pass              0.766             80.6                           0.700               -2.40             -0.507            downtrend_blocked_slope           False                  False
  MRVL           92.31               26            3.12              5.31        240.99               107.78         0.608          pass              0.593             32.5                           0.374              -16.21             -2.177            downtrend_blocked_slope           False                  False
  INTC           89.66               29            2.42              1.90        111.72                93.93         0.579          pass              0.582             46.6                           0.504              -17.35             -2.291            downtrend_blocked_slope           False                  False
  QCOM           83.87               31            1.11              1.48        190.47                71.74         0.578          pass              0.483             60.7                           0.645               -7.76             -0.361           downtrend_blocked_streak           False                  False
  AVGO           87.18               39            0.28              0.78        400.77                53.79         0.545          pass              0.677             79.3                           0.652                5.56              0.683                                 ok           False                  False
  CPRT          100.00                5            2.88              0.57         28.09                43.96         0.533          pass              0.464              3.6                           0.156               -8.44             -0.545            downtrend_blocked_slope           False                  False
  AAPL           97.30               37            0.37              0.81        315.87                35.27         0.526          pass              0.847             71.4                           0.604               14.50              1.484                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710160002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710160002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710160002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710160002)

</details>

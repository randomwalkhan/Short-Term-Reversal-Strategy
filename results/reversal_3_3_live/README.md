# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 13:05:04 EDT`
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
  MPWR           80.65               31            1.57             15.12       1367.65                84.23         0.612          pass              0.403             61.5                           0.547               -5.82             -0.233                                 ok            True                  False
  AAPL           96.43               28            0.52              1.14        315.73                35.27         0.573          pass              0.756             59.6                           0.695               14.33              1.477                                 ok            True                  False
  SOXL           87.10               31            0.78              1.05        192.00               230.34         0.935          pass              0.694             90.4                           0.637              -24.41             -3.481            downtrend_blocked_slope           False                  False
  DRAM           83.33               24            2.19              0.99         63.94               119.54         0.762          pass              0.422             54.5                           0.553              -18.13             -2.090            downtrend_blocked_slope           False                  False
    MU           80.65               31            1.25              8.69        987.92               119.39         0.758          pass              0.434             66.9                           0.640              -19.30             -2.388            downtrend_blocked_slope           False                  False
  LRCX           93.10               29            0.74              1.83        352.39               104.85         0.737          pass              0.798             82.6                           0.624              -12.76             -2.068 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.67               36            0.20              2.48       1803.19                72.45         0.664          pass              0.823             90.6                           0.679               -2.20             -0.497            downtrend_blocked_slope           False                  False
  MRVL           92.59               27            2.70              4.61        241.30               107.78         0.629          pass              0.637             41.5                           0.498              -15.85             -2.158            downtrend_blocked_slope           False                  False
  QCOM           82.76               29            1.37              1.83        190.33                71.74         0.572          pass              0.412             51.6                           0.470               -8.00             -0.373           downtrend_blocked_streak           False                  False
  INTC           89.66               29            2.60              2.05        111.66                93.93         0.567          pass              0.568             42.5                           0.571              -17.50             -2.300            downtrend_blocked_slope           False                  False
  AVGO           88.10               42            0.03              0.08        401.08                53.79         0.544          pass              0.764             98.0                           0.689                5.83              0.694                                 ok           False                  False
  CTSH           70.83               24            1.85              0.56         43.16                63.93         0.525          pass              0.180             11.5                           0.350                8.80              1.162                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710130504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710130504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710130504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710130504)

</details>

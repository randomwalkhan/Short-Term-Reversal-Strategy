# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 12:40:05 EDT`
Last processed slot: `manage_1230`

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
  MPWR           81.25               32            1.06             10.15       1369.78                84.23         0.640          pass              0.466             74.2                           0.793               -5.33             -0.209                                 ok            True                  False
  AAPL           96.15               26            0.63              1.40        315.62                35.27         0.577          pass              0.716             50.6                           0.647               14.20              1.471                                 ok            True                  False
  DRAM           83.33               24            1.86              0.84         64.00               119.54         0.777          pass              0.444             61.3                           0.706              -17.86             -2.075            downtrend_blocked_slope           False                  False
    MU           81.25               32            0.99              6.89        988.69               119.39         0.767          pass              0.478             73.8                           0.798              -19.09             -2.376            downtrend_blocked_slope           False                  False
  LRCX           94.44               36            0.15              0.37        353.01               104.85         0.734          pass              0.921             96.5                           0.862              -12.24             -2.041 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.67               36            0.07              0.85       1803.88                72.45         0.671          pass              0.842             96.8                           0.830               -2.07             -0.492            downtrend_blocked_slope           False                  False
  MRVL           92.59               27            2.41              4.11        241.51               107.78         0.647          pass              0.657             47.8                           0.654              -15.59             -2.144            downtrend_blocked_slope           False                  False
  QCOM           83.87               31            1.19              1.59        190.43                71.74         0.572          pass              0.474             58.0                           0.608               -7.84             -0.365           downtrend_blocked_streak           False                  False
  INTC           89.66               29            2.60              2.05        111.66                93.93         0.567          pass              0.568             42.4                           0.679              -17.51             -2.300            downtrend_blocked_slope           False                  False
  CPRT           87.50                8            2.45              0.49         28.12                43.96         0.531          pass              0.257              1.4                           0.123               -8.04             -0.526            downtrend_blocked_slope           False                  False
  CTSH           70.83               24            1.92              0.58         43.15                63.93         0.520          pass              0.170              8.2                           0.169                8.72              1.158                                 ok           False                  False
  WDAY           83.72               43            0.22              0.21        138.25                60.14         0.513          pass              0.484             44.4                           0.321               21.33              1.912                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710124005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710124005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710124005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710124005)

</details>

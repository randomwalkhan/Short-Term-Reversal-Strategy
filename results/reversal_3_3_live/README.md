# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 10:46:53 EDT`
Last processed slot: `early_entry_1045`

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
  AAPL           94.44               18            1.08              2.39        315.19                35.27         0.592          pass              0.544             15.6                           0.199               13.68              1.451                                 ok            True                  False
  VRTX           90.91               11            1.76              6.12        493.88                34.73         0.514          pass              0.406             18.8                           0.301                1.58              0.249                                 ok            True                  False
  SOXL           84.62               26            3.09              4.16        190.67               230.34         0.897          pass              0.506             62.0                           0.703              -26.17             -3.588            downtrend_blocked_slope           False                  False
   WDC           84.85               33            0.56              2.28        577.07               123.00         0.777          pass              0.609             82.8                           0.554              -14.90             -1.612            downtrend_blocked_slope           False                  False
  DRAM           82.61               23            2.44              1.10         63.89               119.54         0.754          pass              0.380             49.4                           0.631              -18.34             -2.102            downtrend_blocked_slope           False                  False
    MU           78.57               28            1.77             12.31        986.37               119.39         0.747          pass              0.341             48.8                           0.507              -19.72             -2.412            downtrend_blocked_slope           False                  False
  KLAC           90.32               31            0.93              1.50        228.85               118.44         0.741          pass              0.712             74.3                           0.773              -12.15             -2.231 downtrend_blocked_slope_and_streak           False                  False
  LRCX           92.00               25            2.09              5.16        350.96               104.85         0.683          pass              0.641             51.0                           0.647              -13.94             -2.130 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.18               34            0.52              6.57       1801.43                72.45         0.654          pass              0.749             75.0                           0.717               -2.52             -0.512            downtrend_blocked_slope           False                  False
  MPWR           78.57               28            2.03             19.52       1365.76                84.23         0.599          pass              0.331             50.3                           0.695               -6.26             -0.254                                 ok           False                  False
  MRVL           91.67               24            3.66              6.23        240.60               107.78         0.586          pass              0.526             20.9                           0.206              -16.67             -2.203            downtrend_blocked_slope           False                  False
  QCOM           80.00               25            1.96              2.63        189.98                71.74         0.554          pass              0.246             30.3                           0.382               -8.56             -0.401           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-10T10:46:53.268563-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00      manage_1000               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00135000", "fill_price": 5.265, "pnl": -1404.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-10T00:00:05.149826-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-07-09T15:10:06.797522-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:05:11.506156-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T15:00:11.129710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:55:10.687527-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-09T14:50:10.393351-04:00       entry_1500              entry {"allocated_cash": 14040.0, "asset_type": "option", "contract_symbol": "GILD260821C00135000", "contracts": 24, "early_entry_score": 0.621, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 8090.0, "option_spread_pct": 6.84, "option_volume": 34.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.541}
2026-07-09T14:50:10.393351-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-09", "training_samples": 5465, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710104653)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710104653)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710104653)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710104653)

</details>

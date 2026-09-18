# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:10:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           96.77               31            1.90              2.62        196.35                82.85         0.608          pass              0.667             22.2                           0.216                8.95              1.823                                 ok            True                  False
  CTSH          100.00               17            2.17              0.94         61.48                39.55         0.532          pass              0.553             17.5                           0.237               -6.34              0.001                                 ok            True                  False
  FTNT           84.62               13            2.81              3.40        171.12                57.60         0.530          pass              0.206              3.2                           0.125                7.27              1.147                                 ok            True                  False
  MSFT           95.83               24            0.93              3.24        496.36                21.82         0.501          pass              0.581             12.6                           0.236               -3.33             -0.145                                 ok            True                  False
   WBD           85.71               14            0.92              0.18         28.16                10.21         0.501          pass              0.300             23.5                           0.157               -1.37             -0.064                                 ok            True                  False
  CRWD           63.64               11            3.72              6.40        242.96                97.92         0.620          pass              0.093              8.0                           0.162               10.04              1.721                                 ok           False                  False
  PYPL           91.43               35            0.34              0.13         52.89                57.74         0.616          pass              0.755             73.9                           0.754               -6.92             -0.418            downtrend_blocked_slope           False                  False
  MRVL           80.49               41            0.33              0.56        240.52                74.50         0.602          pass              0.490             72.3                           0.435               14.91              0.814                                 ok           False                  False
   EXC          100.00                6            1.14              0.34         42.49                15.46         0.568          pass              0.495             12.7                           0.125               -4.43             -0.463 downtrend_blocked_slope_and_streak           False                  False
   TRI           90.91               11            3.03              2.11         98.58                55.72         0.568          pass              0.381              8.8                           0.192              -13.68             -0.627 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               38            0.47              0.64        192.26                58.58         0.564          pass              0.869             75.4                           0.686               -1.57              0.374                                 ok           False                  False
  ADSK           86.49               37            0.51              0.78        218.31                55.63         0.549          pass              0.578             56.8                           0.357               -8.42             -0.047           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-09-18T10:10:02.340504-04:00 early_entry_1010 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "WMT261023C00108000", "fill_price": 3.05, "pnl": 6159.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.91, "ticker": "WMT"}
2026-09-18T10:05:06.381889-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:00:06.717363-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T00:00:09.864377-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-17T15:10:01.182099-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T15:05:01.143983-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T15:00:04.868136-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T14:55:01.186160-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T14:50:04.102358-04:00       entry_1500     timing_overlay                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-17", "training_samples": 5767, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918101002)

</details>

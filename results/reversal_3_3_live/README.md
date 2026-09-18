# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:15:05 EDT`
Last processed slot: `early_entry_1015`

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
    ZS           96.67               30            1.99              2.74        196.29                82.85         0.609          pass              0.650             18.7                           0.179                8.86              1.819                                 ok            True                  False
  TEAM          100.00               38            0.79              1.06        192.07                58.58         0.545          pass              0.818             58.9                           0.481               -1.89              0.360                                 ok            True                  False
  CTSH          100.00               19            2.10              0.91         61.49                39.55         0.524          pass              0.572             20.0                           0.279               -6.28              0.004                                 ok            True                  False
  INTC           82.50               40            0.62              0.47        108.60                60.44         0.515          pass              0.379             20.2                           0.135               17.96              0.931                                 ok            True                  False
  MSFT          100.00               22            1.12              3.89        496.08                21.82         0.508          pass              0.531              0.0                           0.175               -3.51             -0.153                                 ok            True                  False
  FTNT           80.00               10            3.33              4.02        170.86                57.60         0.508          pass              0.053              0.9                           0.064                6.70              1.122                                 ok            True                  False
   WBD           84.62               13            0.94              0.19         28.16                10.21         0.505          pass              0.260             22.1                           0.149               -1.39             -0.065                                 ok            True                  False
  PYPL           94.12               34            0.52              0.19         52.86                57.74         0.614          pass              0.778             60.1                           0.668               -7.08             -0.426            downtrend_blocked_slope           False                  False
  CRWD           66.67                9            4.19              7.21        242.61                97.92         0.608          pass              0.069              2.7                           0.157                9.50              1.699                                 ok           False                  False
  MRVL           80.49               41            0.37              0.63        240.49                74.50         0.600          pass              0.479             68.8                           0.396               14.86              0.812                                 ok           False                  False
   TRI           91.67               12            2.86              2.00         98.62                55.72         0.572          pass              0.423             13.6                           0.278              -13.54             -0.619 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00                7            1.08              0.32         42.50                15.46         0.566          pass              0.508             17.2                           0.159               -4.38             -0.461 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-09-18T10:15:05.598179-04:00 early_entry_1015 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00 early_entry_1010 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "WMT261023C00108000", "fill_price": 3.05, "pnl": 6159.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.91, "ticker": "WMT"}
2026-09-18T10:05:06.381889-04:00 early_entry_1005 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:00:06.717363-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T00:00:09.864377-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-17T15:10:01.182099-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T15:05:01.143983-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T15:00:04.868136-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-09-17T14:55:01.186160-04:00       entry_1500       slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918101505)

</details>

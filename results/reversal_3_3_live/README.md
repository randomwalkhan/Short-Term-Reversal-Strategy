# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:45:04 EDT`
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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           85.71               28            1.01              3.57        500.98                52.43         0.568            pass              0.515             61.8                           0.344               19.83              1.509                                 ok            True                  False
  MDLZ           93.33               15            0.70              0.30         61.66                19.83         0.559            pass              0.478             11.2                           0.220                4.35              0.647                                 ok            True                  False
  CSCO           92.31               26            0.57              0.46        115.14                34.19         0.534            pass              0.712             74.4                           0.534                7.65              0.922                                 ok            True                  False
  SHOP           83.33               36            0.77              0.96        178.81                48.43         0.515            pass              0.537             74.6                           0.591               19.95              2.072                                 ok            True                  False
  INTC           85.37               41            0.55              0.39        101.18                67.41         0.565            pass              0.646             82.2                           0.718              -13.06             -1.850 downtrend_blocked_slope_and_streak           False                  False
  MPWR           82.35               17            2.31             21.29       1310.10                51.39         0.543            pass              0.203             13.2                           0.127               -4.81             -0.375            downtrend_blocked_slope           False                  False
   CEG           86.49               37            0.36              0.74        293.57                56.17         0.533            pass              0.663             85.7                           0.601               10.68              1.663                                 ok           False                  False
   STX           82.61               23            2.77             14.59        747.00                70.16         0.514            pass              0.412             68.0                           0.870              -19.82             -2.507            downtrend_blocked_slope           False                  False
  UPRO           83.78               37            0.17              0.19        155.38                28.94         0.508            pass              0.548             72.1                           0.487                4.89              0.599                                 ok           False                  False
   XEL           85.19               27            0.33              0.17         74.10                18.13         0.488 below_threshold              0.512             70.5                           0.587                4.58              0.572                                 ok           False                  False
  MCHP           96.55               29            1.18              0.61         73.57                37.42         0.484 below_threshold              0.732             52.5                           0.353               -7.39             -0.816            downtrend_blocked_slope           False                  False
  NVDA           90.32               31            0.19              0.29        226.19                22.13         0.482 below_threshold              0.725             87.1                           0.671               -0.58             -0.111                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-13T10:45:04.655740-04:00 early_entry_1045 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:40:05.951817-04:00 early_entry_1040 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:35:04.412949-04:00 early_entry_1035 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00 early_entry_1030 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "CEG261120C00290000", "fill_price": 21.65, "pnl": 9300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.09, "ticker": "CEG"}
2026-10-13T10:25:06.600262-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:20:06.700982-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:15:06.623973-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:10:05.811238-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:05:05.477631-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013104504)

</details>

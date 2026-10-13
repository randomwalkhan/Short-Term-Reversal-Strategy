# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:50:05 EDT`
Last processed slot: `manage_1100`

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
  MDLZ           92.86               14            0.84              0.36         61.63                19.83         0.556            pass              0.425              0.0                           0.048                4.20              0.640                                 ok            True                  False
  SNPS           85.29               34            0.69              2.43        501.47                52.43         0.551            pass              0.578             74.0                           0.441               20.23              1.523                                 ok            True                  False
  CSCO           91.67               24            0.67              0.54        115.11                34.19         0.540            pass              0.669             70.2                           0.557                7.55              0.918                                 ok            True                  False
  SHOP           84.62               39            0.56              0.70        178.92                48.43         0.510            pass              0.612             81.5                           0.623               20.21              2.081                                 ok            True                  False
  INTC           88.89               36            0.94              0.66        101.07                67.41         0.576            pass              0.677             69.6                           0.661              -13.40             -1.868 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.55               29            0.17              0.04         32.73                30.00         0.544            pass              0.818             78.8                           0.743                5.37              0.651                                 ok           False                  False
  MPWR           85.71               21            2.14             19.78       1310.75                51.39         0.531            pass              0.337             19.4                           0.157               -4.65             -0.367            downtrend_blocked_slope           False                  False
   CEG           88.10               42            0.12              0.25        293.78                56.17         0.518            pass              0.753             95.1                           0.634               10.94              1.674                                 ok           False                  False
  ABNB           92.68               41            0.02              0.02        163.49                38.50         0.510            pass              0.878             96.2                           0.445                4.15              0.329                                 ok           False                  False
  UPRO           86.11               36            0.28              0.31        155.33                28.94         0.509            pass              0.547             53.4                           0.406                4.77              0.594                                 ok           False                  False
   PEP           78.26               23            0.36              0.32        126.54                21.61         0.509            pass              0.277             46.5                           0.450               -1.92             -0.060                                 ok           False                  False
   STX           85.00               20            3.41             17.97        745.55                70.16         0.498 below_threshold              0.432             60.7                           0.784              -20.35             -2.537            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-13T10:50:05.695677-04:00 early_entry_1050 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:45:04.655740-04:00 early_entry_1045 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:40:05.951817-04:00 early_entry_1040 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:35:04.412949-04:00 early_entry_1035 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00 early_entry_1030 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "CEG261120C00290000", "fill_price": 21.65, "pnl": 9300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.09, "ticker": "CEG"}
2026-10-13T10:25:06.600262-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:20:06.700982-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:15:06.623973-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:10:05.811238-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013105005)

</details>

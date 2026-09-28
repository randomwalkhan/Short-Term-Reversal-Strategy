# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 09:55:06 EDT`
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               25            4.83              5.12        149.26               120.87         0.559          pass              0.277             40.3                           0.269               42.62              4.605                                 ok            True                  False
   CEG           86.36               22            1.16              2.14        262.35                41.90         0.553          pass              0.437             43.9                           0.477               -1.65              0.031                                 ok            True                  False
  MPWR           85.19               27            1.52             14.57       1361.19                54.48         0.528          pass              0.485             60.3                           0.403               17.79              2.194                                 ok            True                  False
  AMAT           85.00               40            0.60              2.02        484.13                51.73         0.523          pass              0.634             82.7                           0.605               13.65              1.744                                 ok            True                  False
  PYPL           88.89               18            1.47              0.57         54.80                60.08         0.512          pass              0.526             61.4                           0.630                0.37              0.087                                 ok            True                  False
   STX           87.88               33            1.47              9.46        912.77                54.25         0.511          pass              0.567             50.7                           0.363               12.23              1.870                                 ok            True                  False
    MU           92.86               28            1.87             14.18       1076.20                50.18         0.508          pass              0.606             30.7                           0.241               14.93              1.850                                 ok            True                  False
  UPRO           82.61               23            1.27              1.36        151.65                32.02         0.506          pass              0.294             28.9                           0.412                3.13              0.587                                 ok            True                  False
  NXPI           87.10               31            0.88              1.46        237.45                39.27         0.502          pass              0.597             72.6                           0.442                5.72              0.685                                 ok            True                  False
  MSFT          100.00               14            1.69              6.12        513.55                25.07         0.501          pass              0.589             37.3                           0.539                0.40              0.215                                 ok            True                  False
   TRI           83.33               18            2.33              1.62         98.30                56.74         0.575          pass              0.221              7.2                           0.087               -8.64             -0.575 downtrend_blocked_slope_and_streak           False                  False
  LRCX           79.55               44            0.25              0.55        314.97                61.39         0.546          pass              0.536             93.8                           0.770               15.09              1.867                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                              detail
2026-09-28T09:50:05.886543-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-28T03:00:06.642645-04:00   data_refresh  data_refresh                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00 share_ext_0255 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00 share_ext_0250 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00 share_ext_0245 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:40:05.820539-04:00 share_ext_0240 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:35:05.219756-04:00 share_ext_0235 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:30:04.108962-04:00 share_ext_0230 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:25:06.088084-04:00 share_ext_0225 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:20:05.261496-04:00 share_ext_0220 market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928095506)

</details>

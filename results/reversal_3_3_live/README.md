# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 14:22:12 EDT`
Last processed slot: `manage_1430`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   ADP           92.00               25            0.94              1.41        212.39                34.95         0.527            pass              0.630             52.4                           0.495                6.97              0.482                      ok            True                  False
  ASML           80.00               25            1.93             21.46       1582.82                48.89         0.491 below_threshold              0.318             56.3                           0.712                9.00              1.268                      ok           False                  False
  ADBE           66.67               12            2.95              5.22        250.80                45.04         0.468 below_threshold              0.078              5.8                           0.254                2.62              0.450                      ok           False                  False
  AMGN           77.42               31            0.89              2.08        330.81                25.13         0.456 below_threshold              0.296             36.8                           0.242               -3.36             -0.396 downtrend_blocked_slope           False                  False
  ADSK           87.50                8            3.39              5.80        242.02                39.96         0.439 below_threshold              0.254              3.4                           0.211                0.51              0.404                      ok           False                  False
   APP           84.09               44            0.29              0.96        468.14                60.71         0.399 below_threshold              0.630             93.6                           0.820                1.50              0.668                      ok           False                  False
  ABNB           95.65               23            1.81              1.79        140.72                21.69         0.379 below_threshold              0.540              5.0                           0.172               -1.51             -0.021                      ok           False                  False
  ALNY           78.57               14            2.71              5.60        292.65                34.74         0.368 below_threshold              0.086              7.6                           0.215               -6.96             -0.485 downtrend_blocked_slope           False                  False
  BKNG           66.67                3            5.35              6.22        163.33                39.12         0.356 below_threshold              0.039              1.2                           0.193              -11.50             -0.769 downtrend_blocked_slope           False                  False
  AAPL           85.00               40            0.32              0.66        292.98                26.17         0.340 below_threshold              0.659             97.1                           0.794                9.23              0.980                      ok           False                  False
  AMZN           93.55               31            0.81              1.55        272.02                21.04         0.319 below_threshold              0.816             94.3                           0.521                3.58              0.505                      ok           False                  False
  AVGO           90.70               43            0.09              0.28        429.88                38.44         0.284 below_threshold              0.812             99.5                           0.726                2.72              0.482                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511142212)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511142212)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511142212)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511142212)

</details>

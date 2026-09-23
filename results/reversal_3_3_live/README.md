# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 09:40:04 EDT`
Last processed slot: `manage_0930`

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

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               30            3.98              4.23        150.15               119.42         0.629          pass              0.234             12.7                           0.318               16.00              2.479                                 ok            True                  False
  DRAM           82.14               28            1.78              0.79         63.33                51.34         0.549          pass              0.243              3.8                           0.236                1.55              0.641                                 ok            True                  False
  INTC           83.33               36            1.57              1.36        123.28                67.82         0.530          pass              0.419             34.6                           0.370               14.75              2.110                                 ok            True                  False
  MPWR           85.19               27            1.91             18.49       1372.70                51.84         0.521          pass              0.304              0.0                           0.252               12.50              1.290                                 ok            True                  False
   ADI           88.00               25            1.11              3.04        389.07                33.19         0.514          pass              0.407             14.3                           0.240                5.74              0.619                                 ok            True                  False
  NVDA           91.43               35            0.27              0.43        228.68                44.57         0.590          pass              0.713             61.0                           0.578                2.16              0.503                                 ok           False                  False
  ADSK           85.37               41            0.17              0.26        219.51                55.47         0.569          pass              0.630             76.6                           0.424                6.11              0.349                                 ok           False                  False
   XEL           88.89                9            0.92              0.47         71.86                15.29         0.547          pass              0.322             10.1                           0.131               -5.54             -0.547 downtrend_blocked_slope_and_streak           False                  False
  CHTR           85.71               42            0.61              0.50        117.05                65.60         0.540          pass              0.521             38.4                           0.235              -12.95             -1.985 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.68               41            0.10              0.02         30.82                38.24         0.539          pass              0.852             86.6                           0.542               10.35              1.013                                 ok           False                  False
   PEP           91.30               23            0.23              0.21        131.10                15.28         0.518          pass              0.523             27.7                           0.241               -4.24             -0.591 downtrend_blocked_slope_and_streak           False                  False
   CEG           72.22               18            1.65              3.05        262.15                42.63         0.512          pass              0.160             18.5                           0.240              -11.84             -1.190 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                 detail
2026-09-23T09:35:04.357346-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00   entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923094004)

</details>

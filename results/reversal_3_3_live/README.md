# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 10:05:07 EDT`
Last processed slot: `manage_1000`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$26,462.75`
- Equity: `$26,462.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               37            0.77              0.69        127.34                70.74         0.623          pass              0.818             58.4                           0.496               40.81              2.620                                 ok            True                  False
  PAYX           90.91               11            1.14              0.76         94.16                29.36         0.567          pass              0.547             64.1                           0.683                3.53              0.204                                 ok            True                  False
  AMGN           86.67               15            0.95              2.19        329.81                26.77         0.545          pass              0.468             67.6                           0.469               -0.31             -0.013                                 ok            True                  False
 GOOGL           86.21               29            0.87              2.35        386.65                41.27         0.523          pass              0.344              0.0                           0.170               -3.45             -0.212                                 ok            True                  False
   HON           84.62               26            0.70              1.07        216.69                24.50         0.504          pass              0.348             22.6                           0.262               -0.02              0.061                                 ok            True                  False
  ADSK           90.48               21            1.57              2.68        243.01                38.52         0.502          pass              0.598             65.0                           0.822               -1.13             -0.164                                 ok            True                  False
   TXN           93.94               33            0.08              0.18        302.23                69.06         0.645          pass              0.883             97.9                           0.535                4.36              0.593                                 ok           False                  False
  TEAM           88.57               35            1.69              1.03         86.18               114.61         0.619          pass              0.658             66.9                           0.806               -4.10             -0.532 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.55               29            0.29              0.22        106.29                31.99         0.555          pass              0.787             68.2                           0.524                0.24              0.192                                 ok           False                  False
   WMT          100.00                3            2.28              2.14        133.28                20.68         0.541          pass              0.551             32.5                           0.203                1.01              0.291                                 ok           False                  False
  GOOG           85.71               28            0.89              2.40        383.87                41.08         0.516          pass              0.324              0.0                           0.163               -3.46             -0.223           downtrend_blocked_streak           False                  False
  SNPS           93.75               16            2.24              7.75        490.55                41.71         0.511          pass              0.592             44.8                           0.714               -4.29             -0.433 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                         detail
2026-05-20T10:05:07.673831-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                     {"reason": "no_candidate"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                         {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,no_two_sided_quote,wide_spread", "option_open_interest": 29.0, "option_spread_pct": null, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped          {"early_entry_score": 0.821, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 15.38, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.44}
2026-05-20T09:18:59.431991-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                  {'saved': 92}
2026-05-19T15:10:04.056831-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-19T15:05:05.027114-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-19T15:00:02.089036-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-19T14:55:06.057081-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-19T14:50:01.084215-04:00       entry_1500          timing_overlay                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-19", "training_samples": 5044, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520100507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520100507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520100507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520100507)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 15:15:01 EDT`
Last processed slot: `manual`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               13            1.11              0.63         81.40                20.22         0.557          pass              0.565             29.8                           0.409                0.35              0.133                                 ok            True                  False
   STX           89.47               19            4.03             24.06        841.38               103.51         0.528          pass              0.519             51.3                           0.806               -5.04              0.436                                 ok            True                  False
   WDC           90.00               20            4.38             15.95        512.96               113.75         0.517          pass              0.544             53.0                           0.801              -10.54             -0.090                                 ok            True                  False
   AEP           82.35               17            1.23              1.17        135.04                20.37         0.502          pass              0.238             26.1                           0.324               -1.30             -0.020                                 ok            True                  False
  PYPL           88.64               44            0.01              0.00         56.15                61.92         0.613          pass              0.789             99.3                           0.499               17.83              1.312                                 ok           False                  False
  DRAM           78.57               28            2.10              0.78         52.87                97.77         0.597          pass              0.367             62.5                           0.828               -9.10             -0.524            downtrend_blocked_slope           False                  False
  TMUS           88.89               27            0.86              1.09        179.62                59.26         0.586          pass              0.558             49.7                           0.238               -5.24             -0.648            downtrend_blocked_slope           False                  False
  INTC           87.50               40            0.31              0.20         92.23                79.50         0.565          pass              0.741             94.7                           0.975              -10.75             -0.897 downtrend_blocked_slope_and_streak           False                  False
  KLAC           85.71               21            3.33              4.91        208.42                94.03         0.563          pass              0.441             53.1                           0.832               -8.43             -0.805 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.49              0.16         47.46                24.01         0.556          pass              0.759             74.5                           0.418                0.44              0.127                                 ok           False                  False
  MPWR           84.21               38            0.47              4.41       1331.92                65.61         0.539          pass              0.614             87.1                           0.883                2.80              0.324                                 ok           False                  False
   WBD           71.43                7            1.53              0.28         25.65                22.96         0.537          pass              0.126             24.0                           0.375               -6.33             -0.859            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-07-27T15:10:06.692175-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:05:03.663832-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:00:02.669579-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:55:05.984850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:50:01.830454-04:00       entry_1500           entry_skipped                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.242, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 375.0, "option_spread_pct": 15.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.504}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.544, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 216.0, "option_spread_pct": 14.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.558}
2026-07-27T14:50:01.830454-04:00       entry_1500          timing_overlay                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-27", "training_samples": 5518, "window": 5}
2026-07-27T12:00:02.583905-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727151501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727151501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727151501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727151501)

</details>

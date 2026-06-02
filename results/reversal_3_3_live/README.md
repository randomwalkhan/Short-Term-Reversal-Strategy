# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 14:50:05 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$36,331.75`
- Equity: `$36,331.75`
- Realized PnL: `$26,331.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AMZN     option         option AMZN260717C00260000     15          2026-06-02         2026-06-02         10.8      12.575 2662.5   16.435185 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           96.97               33            0.64              0.40         88.93                49.60         0.586            pass              0.820             69.5                           0.728               -0.01              0.211                                 ok            True                   True
  INTC           95.65               23            1.98              1.52        108.68                88.85         0.562            pass              0.717             57.9                           0.527               -0.93             -0.140                                 ok            True                  False
  INSM           66.67               21            2.62              1.95        105.20               110.78         0.717            pass              0.293             49.2                           0.654               -3.64             -0.259            downtrend_blocked_slope           False                  False
  MELI           85.71                7            3.61             43.68       1712.26                60.28         0.577            pass              0.236              8.6                           0.401                5.21              0.637                                 ok           False                  False
  FTNT          100.00               46            0.27              0.27        147.02                71.69         0.576            pass              0.939             93.8                           0.791               16.01              1.316                                 ok           False                  False
   WMT           83.33               18            1.13              0.91        114.21                32.65         0.563            pass              0.273             25.0                           0.334              -15.03             -1.699 downtrend_blocked_slope_and_streak           False                  False
    ZS           66.67                3            8.58              9.36        151.70               157.27         0.541            pass              0.099             14.9                           0.300              -18.52             -2.797            downtrend_blocked_slope           False                  False
  PAYX           88.89                9            1.76              1.26        101.90                33.30         0.526            pass              0.453             54.3                           0.659                6.51              0.639                                 ok           False                  False
  REGN           90.24               41            0.18              0.76        600.33                42.53         0.522            pass              0.790             88.1                           0.792               -4.64             -0.613 downtrend_blocked_slope_and_streak           False                  False
  ISRG           83.33               12            2.38              6.87        409.31                38.26         0.505            pass              0.264             37.0                           0.580               -8.52             -0.917 downtrend_blocked_slope_and_streak           False                  False
  CRWD           80.00               10            2.92             15.97        775.32                48.77         0.488 below_threshold              0.163             38.0                           0.565               22.71              2.151                                 ok           False                  False
  GILD           75.00                8            2.16              1.98        130.25                23.89         0.485 below_threshold              0.138             29.8                           0.426               -1.08              0.118                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:40:01.271913-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:30:04.237556-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00 early_entry_1125  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602145005)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 15:00:02 EDT`
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
  MNST           96.55               29            0.68              0.43         88.92                49.60         0.610            pass              0.790             67.4                           0.713               -0.06              0.209                                 ok            True                  False
  INTC           96.15               26            1.80              1.38        108.74                88.85         0.555            pass              0.748             61.9                           0.530               -0.74             -0.132                                 ok            True                  False
  INSM           72.00               25            2.27              1.69        105.31               110.78         0.720            pass              0.340             55.9                           0.686               -3.29             -0.243                                 ok           False                  False
  FTNT          100.00               46            0.25              0.26        147.03                71.69         0.577            pass              0.940             94.2                           0.809               16.03              1.317                                 ok           False                  False
  MELI           80.00                5            3.75             45.42       1711.52                60.28         0.574            pass              0.072              5.0                           0.271                5.06              0.631                                 ok           False                  False
   WMT           84.21               19            1.01              0.81        114.25                32.65         0.566            pass              0.329             33.2                           0.460              -14.92             -1.693 downtrend_blocked_slope_and_streak           False                  False
    ZS           66.67                3            8.49              9.25        151.75               157.27         0.547            pass              0.102             15.9                           0.256              -18.43             -2.792            downtrend_blocked_slope           False                  False
  PAYX           88.89                9            1.82              1.30        101.88                33.30         0.522            pass              0.448             52.8                           0.638                6.45              0.636                                 ok           False                  False
  REGN           90.70               43            0.05              0.22        600.56                42.53         0.518            pass              0.827             96.5                           0.861               -4.52             -0.607 downtrend_blocked_slope_and_streak           False                  False
  ISRG           83.33               12            2.41              6.94        409.28                38.26         0.503            pass              0.262             36.3                           0.581               -8.54             -0.918 downtrend_blocked_slope_and_streak           False                  False
  PANW           76.92               13            2.30              4.84        298.41                51.15         0.497 below_threshold              0.246             58.6                           0.391               18.59              1.944                                 ok           False                  False
  CRWD           80.00               10            2.90             15.87        775.37                48.77         0.490 below_threshold              0.164             38.4                           0.538               22.73              2.152                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:40:01.271913-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602150002)

</details>

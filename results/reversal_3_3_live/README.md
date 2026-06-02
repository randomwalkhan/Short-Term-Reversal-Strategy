# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 15:25:01 EDT`
Last processed slot: `manage_1530`

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
  MNST           96.00               25            0.84              0.53         88.87                49.60         0.625            pass              0.742             59.9                           0.526               -0.21              0.202                                 ok            True                  False
  INTC           96.00               25            1.92              1.47        108.70                88.85         0.553            pass              0.733             59.3                           0.579               -0.87             -0.137                                 ok            True                  False
  INSM           73.08               26            2.25              1.67        105.31               110.78         0.716            pass              0.347             56.3                           0.620               -3.28             -0.242                                 ok           False                  False
   WMT           76.92               13            1.33              1.07        114.14                32.65         0.576            pass              0.113             11.8                           0.181              -15.20             -1.708 downtrend_blocked_slope_and_streak           False                  False
  MELI           85.71                7            3.63             43.97       1712.13                60.28         0.575            pass              0.234              8.0                           0.260                5.19              0.636                                 ok           False                  False
    ZS           50.00                4            7.95              8.67        151.99               157.27         0.557            pass              0.119             21.2                           0.591              -17.95             -2.766            downtrend_blocked_slope           False                  False
  PAYX           88.89                9            1.62              1.16        101.94                33.30         0.536            pass              0.464             57.9                           0.662                6.66              0.645                                 ok           False                  False
  CDNS           94.87               39            0.21              0.60        413.90                44.19         0.496 below_threshold              0.920             93.4                           0.848               19.45              1.804                                 ok           False                  False
  CRWD           78.57               14            2.40             13.11        776.55                48.77         0.492 below_threshold              0.223             49.1                           0.713               23.37              2.175                                 ok           False                  False
  IDXX           81.82               11            2.37              9.42        562.75                30.08         0.491 below_threshold              0.178             24.7                           0.358                1.38              0.278                                 ok           False                  False
  DXCM           78.26               23            1.74              0.91         74.48                46.68         0.488 below_threshold              0.266             43.5                           0.466               13.03              1.037                                 ok           False                  False
  ISRG           81.82               11            2.70              7.79        408.92                38.26         0.488 below_threshold              0.190             28.6                           0.311               -8.82             -0.931 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-02T15:10:01.501174-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602152501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602152501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602152501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602152501)

</details>

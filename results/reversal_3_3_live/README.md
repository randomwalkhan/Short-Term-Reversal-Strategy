# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 15:50:02 EDT`
Last processed slot: `manage_1600`

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
  MELI           90.00               10            3.20             38.82       1714.34                60.28         0.588            pass              0.382             18.8                           0.509                5.65              0.656                                 ok            True                  False
  MNST           96.97               33            0.64              0.40         88.93                49.60         0.586            pass              0.820             69.5                           0.685               -0.01              0.211                                 ok            True                   True
  INTC           95.83               24            1.94              1.48        108.69                88.85         0.559            pass              0.726             58.9                           0.515               -0.89             -0.138                                 ok            True                  False
  PAYX           90.91               11            1.39              0.99        102.01                33.30         0.540            pass              0.543             64.0                           0.701                6.91              0.656                                 ok            True                  False
  CRWD           81.25               16            1.73              9.49        778.10                48.77         0.525            pass              0.315             63.2                           0.783               24.21              2.206                                 ok            True                  False
  INSM           71.43               28            1.74              1.29        105.48               110.78         0.733            pass              0.392             66.2                           0.777               -2.77             -0.218                                 ok           False                  False
    ZS           50.00                4            7.58              8.27        152.17               157.27         0.583            pass              0.133             24.8                           0.634              -17.63             -2.748            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.32              1.06        114.15                32.65         0.577            pass              0.120             14.2                           0.263              -15.19             -1.707 downtrend_blocked_slope_and_streak           False                  False
  SBUX           86.67               15            1.04              0.70         96.21                19.05         0.515            pass              0.275              4.3                           0.242              -10.41             -1.117 downtrend_blocked_slope_and_streak           False                  False
  ISRG           81.82               11            2.55              7.37        409.10                38.26         0.498 below_threshold              0.202             32.4                           0.528               -8.68             -0.925 downtrend_blocked_slope_and_streak           False                  False
  GOOG          100.00                1            3.49              9.11        368.67                25.52         0.493 below_threshold              0.527             25.9                           0.188               -8.53             -0.559            downtrend_blocked_slope           False                  False
  PANW           88.00               25            1.35              2.85        299.26                51.15         0.489 below_threshold              0.589             75.7                           0.796               19.74              1.988                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602155002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602155002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602155002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602155002)

</details>

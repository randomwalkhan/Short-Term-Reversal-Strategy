# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 15:15:05 EDT`
Last processed slot: `manual`

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
  MNST           96.43               28            0.70              0.43         88.91                49.60         0.616            pass              0.782             66.8                           0.627               -0.07              0.208                                 ok            True                  False
  INTC           96.15               26            1.78              1.37        108.74                88.85         0.556            pass              0.749             62.2                           0.634               -0.73             -0.131                                 ok            True                  False
  INSM           70.83               24            2.49              1.85        105.24               110.78         0.712            pass              0.320             51.7                           0.602               -3.51             -0.253            downtrend_blocked_slope           False                  False
  MELI           80.00                5            3.81             46.18       1711.19                60.28         0.570            pass              0.067              3.4                           0.174                4.99              0.628                                 ok           False                  False
   WMT           82.35               17            1.22              0.98        114.18                32.65         0.563            pass              0.224             19.4                           0.255              -15.10             -1.703 downtrend_blocked_slope_and_streak           False                  False
    ZS           50.00                4            8.12              8.86        151.91               157.27         0.546            pass              0.113             19.5                           0.364              -18.11             -2.774            downtrend_blocked_slope           False                  False
  PAYX           88.89                9            1.70              1.22        101.92                33.30         0.530            pass              0.458             55.8                           0.616                6.57              0.642                                 ok           False                  False
  ISRG           81.82               11            2.56              7.39        409.09                38.26         0.498 below_threshold              0.202             32.3                           0.382               -8.69             -0.925 downtrend_blocked_slope_and_streak           False                  False
  CRWD           78.57               14            2.41             13.19        776.52                48.77         0.492 below_threshold              0.222             48.8                           0.698               23.35              2.175                                 ok           False                  False
   ADP           91.67               24            1.18              1.93        232.91                34.26         0.486 below_threshold              0.656             67.6                           0.636                3.61              0.355                                 ok           False                  False
  CDNS           94.59               37            0.56              1.61        413.47                44.19         0.485 below_threshold              0.865             82.5                           0.805               19.04              1.788                                 ok           False                   True
  DXCM           81.48               27            1.44              0.76         74.55                46.68         0.484 below_threshold              0.360             53.0                           0.635               13.37              1.051                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602151505)

</details>

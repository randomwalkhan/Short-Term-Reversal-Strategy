# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:05:05 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               28            1.84              1.56        119.94               109.00         0.641          pass              0.698             38.0                           0.193               24.94              3.110                                 ok            True                  False
  TEAM           88.89               18            4.33              2.58         83.90               115.69         0.610          pass              0.421             23.3                           0.245               15.36              1.351                                 ok            True                  False
  QCOM           92.31               26            1.22              1.80        209.54                94.36         0.580          pass              0.511              6.2                           0.062               33.17              3.232                                 ok            True                  False
  SNPS           97.14               35            0.68              2.45        512.16                43.23         0.546          pass              0.785             54.7                           0.480                5.92              0.705                                 ok            True                  False
   ADP          100.00               10            2.40              3.60        212.27                33.54         0.544          pass              0.573             39.6                           0.241               -2.97             -0.108                                 ok            True                  False
   XEL           95.83               24            0.75              0.42         79.72                27.12         0.529          pass              0.704             52.8                           0.583                0.61             -0.227                                 ok            True                  False
  CHTR           71.43               14            3.05              3.16        146.57               118.13         0.768          pass              0.159             18.6                           0.231               -9.61             -1.377            downtrend_blocked_slope           False                  False
 CMCSA           92.86               28            0.46              0.08         24.87                62.10         0.687          pass              0.738             68.9                           0.721               -7.38             -0.997 downtrend_blocked_slope_and_streak           False                  False
  INSM           76.47               34            1.14              0.93        115.60               110.65         0.594          pass              0.420             66.9                           0.631              -15.07             -2.854 downtrend_blocked_slope_and_streak           False                  False
  GEHC           70.59               34            0.96              0.42         62.11                57.10         0.562          pass              0.377             53.5                           0.650                3.72              0.358                                 ok           False                  False
  SHOP           80.00               20            2.84              1.99         98.99                84.62         0.558          pass              0.219             32.2                           0.395              -20.01             -2.544 downtrend_blocked_slope_and_streak           False                  False
  LRCX           82.93               41            0.06              0.13        289.19                52.22         0.533          pass              0.579             82.5                           0.421               16.20              1.757                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T10:05:05.859086-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513100505)

</details>

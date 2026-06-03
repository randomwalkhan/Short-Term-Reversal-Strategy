# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 16:00:05 EDT`
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

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   TXN     option         option TXN260717C00310000      8          2026-06-03         2026-06-03         22.0        19.8 -1760.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               25            1.59              1.65        148.15                71.83         0.610          pass              0.740             59.7                           0.491               14.78              1.493                                 ok            True                  False
  MELI           89.47               19            2.07             24.25       1662.44                61.01         0.610          pass              0.434             20.0                           0.464                2.72              0.314                                 ok            True                  False
  CSCO           95.65               23            1.12              1.00        127.57                53.71         0.609          pass              0.727             59.7                           0.307                9.70              0.905                                 ok            True                  False
  NXPI           96.97               33            0.53              1.20        323.11                50.93         0.569          pass              0.809             66.4                           0.566                9.39              0.691                                 ok            True                   True
  WDAY           85.29               34            1.33              1.39        148.29                75.59         0.541          pass              0.554             66.1                           0.718               13.58              2.146                                 ok            True                  False
   WBD           94.44               18            0.57              0.11         27.13                 9.03         0.541          pass              0.519              8.8                           0.211               -0.24             -0.028                                 ok            True                  False
  AAPL           90.91               11            1.57              3.47        313.71                17.72         0.523          pass              0.416             21.9                           0.373                3.77              0.364                                 ok            True                  False
   ROP           90.00               20            1.42              3.35        335.07                35.89         0.517          pass              0.536             50.2                           0.699                0.85              0.341                                 ok            True                  False
  CTSH           80.00               10            2.92              1.13         54.66                50.18         0.500          pass              0.139             29.7                           0.588                5.21              0.871                                 ok            True                  False
    ZS           50.00                4            6.79              6.85        141.21               159.87         0.660          pass              0.089              7.8                           0.312              -23.33             -2.960            downtrend_blocked_slope           False                  False
  INTU           70.59               17            3.32              7.49        318.93               101.75         0.642          pass              0.139              9.2                           0.260              -22.08             -1.296            downtrend_blocked_slope           False                  False
   AEP           66.67               15            0.51              0.46        126.91                27.13         0.585          pass              0.158             22.2                           0.181               -1.91             -0.354 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T15:10:03.976623-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:05:05.758809-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:00:06.248089-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:55:06.012322-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:50:06.341439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
2026-06-03T12:00:06.118457-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603160005)

</details>

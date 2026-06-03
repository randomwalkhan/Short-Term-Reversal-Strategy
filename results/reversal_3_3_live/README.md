# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 14:55:06 EDT`
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
  MELI           92.86               14            2.44             28.58       1660.58                61.01         0.625          pass              0.432              0.0                           0.157                2.33              0.297                                 ok            True                  False
  FTNT          100.00               27            1.44              1.50        148.22                71.83         0.605          pass              0.764             63.5                           0.540               14.95              1.500                                 ok            True                  False
  NXPI           96.97               33            0.53              1.20        323.10                50.93         0.568          pass              0.809             66.2                           0.415                9.39              0.691                                 ok            True                  False
   ROP           81.82               11            2.16              5.09        334.32                35.89         0.521          pass              0.180             24.3                           0.306                0.10              0.307                                 ok            True                  False
  AAPL           90.91               11            1.73              3.81        313.56                17.72         0.514          pass              0.391             14.2                           0.386                3.61              0.357                                 ok            True                  False
  UPRO           95.65               23            1.53              1.62        150.18                28.22         0.509          pass              0.641             34.6                           0.459                8.72              0.884                                 ok            True                  False
  WDAY           83.87               31            2.14              2.23        147.93                75.59         0.505          pass              0.430             45.5                           0.457               12.65              2.108                                 ok            True                  False
  CRWD           82.35               17            2.17             11.68        763.95                51.19         0.505          pass              0.273             37.8                           0.508               21.95              2.200                                 ok            True                  False
   CEG           80.95               21            2.35              4.49        270.73                55.62         0.503          pass              0.190             13.6                           0.425                2.14             -0.303                                 ok            True                  False
  INSM           78.57               42            0.41              0.30        103.60               108.46         0.751          pass              0.514             79.5                           0.439               -3.83             -0.402 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            6.06              6.11        141.53               159.87         0.708          pass              0.124             17.8                           0.471              -22.73             -2.924            downtrend_blocked_slope           False                  False
  INTU           72.22               18            3.20              7.22        319.04               101.75         0.645          pass              0.155             12.5                           0.278              -21.99             -1.291            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-03T14:55:06.012322-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:50:06.341439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
2026-06-03T12:00:06.118457-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603145506)

</details>

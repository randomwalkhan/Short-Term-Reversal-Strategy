# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 11:35:06 EDT`
Last processed slot: `manage_1130`

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
  MELI           92.00               25            1.72             20.18       1664.18                61.01         0.603          pass              0.508              9.3                           0.134                3.08              0.330                                 ok            True                  False
  MCHP          100.00               23            1.20              0.82         96.61                44.80         0.528          pass              0.721             60.5                           0.422                4.86              0.377                                 ok            True                  False
  WDAY           81.82               22            2.73              2.85        147.66                75.59         0.525          pass              0.272             30.3                           0.382               11.96              2.080                                 ok            True                  False
  CRWD           87.50               24            1.29              6.94        765.97                51.19         0.519          pass              0.534             63.0                           0.712               23.04              2.241                                 ok            True                  False
  AAPL           94.12               17            1.15              2.53        314.11                17.72         0.517          pass              0.553             26.0                           0.372                4.22              0.383                                 ok            True                  False
  UPRO           95.65               23            1.55              1.64        150.17                28.22         0.513          pass              0.591             17.8                           0.234                8.70              0.883                                 ok            True                  False
   ADP          100.00               13            2.31              3.73        229.58                34.09         0.510          pass              0.512             13.8                           0.184                2.45              0.421                                 ok            True                  False
  SNPS          100.00               10            2.95             10.51        503.84                42.98         0.503          pass              0.488             12.4                           0.160               -0.11             -0.276                                 ok            True                  False
  INSM           79.07               43            0.39              0.28        103.61               108.46         0.747          pass              0.518             81.0                           0.541               -3.80             -0.401 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.62              5.67        141.72               159.87         0.742          pass              0.113             12.9                           0.362              -22.37             -2.903            downtrend_blocked_slope           False                  False
    MU           82.86               35            0.10              0.77       1063.77               101.17         0.737          pass              0.604             95.7                           0.587               52.13              4.598                                 ok           False                  False
  INTU           73.68               19            2.95              6.64        319.29               101.75         0.656          pass              0.184             19.5                           0.361              -21.78             -1.278            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T11:35:06.204353-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:10:06.071222-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:05:06.061538-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:00:05.946994-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603113506)

</details>

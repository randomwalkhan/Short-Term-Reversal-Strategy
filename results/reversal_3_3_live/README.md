# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:50:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.25               32            1.61              1.74        153.34               126.50         0.778          pass              0.386             42.9                           0.500               45.38              5.153                  ok            True                  False
  PYPL           92.00               25            1.03              0.43         58.82                59.96         0.673          pass              0.652             54.8                           0.673                0.07              0.214                  ok            True                  False
  SHOP           97.14               35            1.00              1.06        152.15                81.89         0.662          pass              0.757             41.5                           0.445               16.97              2.921                  ok            True                  False
 CMCSA           92.86               14            1.56              0.28         25.53                42.38         0.626          pass              0.439              2.4                           0.105                6.68              0.669                  ok            True                  False
  GEHC           94.12               17            1.90              0.97         72.33                54.33         0.624          pass              0.547             20.4                           0.170               -0.74              0.296                  ok            True                  False
  ABNB           94.74               19            1.81              2.34        183.98                64.05         0.615          pass              0.631             38.9                           0.352               18.71              2.290                  ok            True                  False
   ROP          100.00               18            1.63              4.55        397.55                44.32         0.608          pass              0.615             33.7                           0.373                0.96              0.180                  ok            True                  False
  TMUS           88.57               35            0.57              0.71        178.28                55.82         0.604          pass              0.563             35.8                           0.302                2.44              0.273                  ok            True                  False
  ISRG           86.49               37            0.69              1.94        400.40                69.94         0.593          pass              0.473             20.2                           0.226               12.89              1.321                  ok            True                  False
  PAYX          100.00               13            1.60              1.36        120.72                33.26         0.577          pass              0.512             11.6                           0.234                2.60              0.365                  ok            True                  False
  MDLZ           91.30               23            0.75              0.33         61.64                29.90         0.568          pass              0.582             45.6                           0.439               -2.80             -0.205                  ok            True                  False
   ADP           95.45               22            1.37              2.60        269.98                32.74         0.546          pass              0.580             15.1                           0.287                1.33              0.128                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                 detail
2026-08-12T09:50:02.620693-04:00  manage_1000         exit {"asset_type": "option", "contract_symbol": "LRCX260918C00310000", "fill_price": 34.9, "pnl": 4025.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 29.98, "ticker": "LRCX"}
2026-08-12T09:35:01.769154-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:30:01.771593-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:25:01.593760-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:20:03.729351-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:15:01.696450-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:10:04.748220-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:05:02.776077-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T09:00:03.695691-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-12T08:55:02.907270-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812095002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812095002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812095002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812095002)

</details>

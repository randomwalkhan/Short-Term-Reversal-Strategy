# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:55:05 EDT`
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
  TEAM           81.25               32            1.64              1.77        153.32               126.50         0.776          pass              0.383             41.7                           0.329               45.33              5.151                  ok            True                  False
  PYPL           91.67               24            1.04              0.43         58.82                59.96         0.678          pass              0.636             54.4                           0.590                0.06              0.213                  ok            True                  False
  SHOP           97.06               34            1.12              1.20        152.10                81.89         0.661          pass              0.729             34.2                           0.311               16.82              2.915                  ok            True                  False
  ABNB           94.74               19            1.74              2.25        184.02                64.05         0.620          pass              0.639             41.4                           0.463               18.80              2.294                  ok            True                  False
  GEHC           95.24               21            1.59              0.81         72.40                54.33         0.620          pass              0.636             33.6                           0.352               -0.42              0.311                  ok            True                  False
 CMCSA           88.24               17            1.24              0.22         25.55                42.38         0.620          pass              0.395             22.2                           0.212                7.02              0.684                  ok            True                  False
  TMUS           90.91               33            0.66              0.82        178.24                55.82         0.614          pass              0.585             26.4                           0.277                2.35              0.270                  ok            True                  False
   ROP          100.00               18            1.67              4.66        397.50                44.32         0.606          pass              0.610             32.1                           0.392                0.92              0.178                  ok            True                  False
  ISRG           86.49               37            0.59              1.64        400.53                69.94         0.599          pass              0.539             42.1                           0.265               13.01              1.326                  ok            True                  False
  PAYX          100.00               11            1.85              1.57        120.63                33.26         0.574          pass              0.464              0.0                           0.230                2.34              0.353                  ok            True                  False
  MDLZ           92.00               25            0.57              0.24         61.68                29.90         0.568          pass              0.654             59.1                           0.564               -2.62             -0.197                  ok            True                  False
  FAST          100.00               23            0.57              0.21         52.29                25.01         0.561          pass              0.719             58.9                           0.360               11.62              1.206                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812095505)

</details>

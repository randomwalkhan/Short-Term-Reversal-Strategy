# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 13:45:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               21            1.72              1.79        148.09                71.83         0.628          pass              0.705             56.4                           0.369               14.62              1.487                      ok            True                  False
  MELI           92.31               26            1.50             17.51       1665.32                61.01         0.611          pass              0.560             21.3                           0.292                3.32              0.340                      ok            True                  False
  NXPI           96.88               32            0.56              1.27        323.08                50.93         0.573          pass              0.797             64.4                           0.515                9.36              0.690                      ok            True                  False
  MCHP           96.15               26            0.70              0.48         96.76                44.80         0.537          pass              0.791             76.9                           0.671                5.40              0.400                      ok            True                  False
  WDAY           84.38               32            1.83              1.91        148.06                75.59         0.520          pass              0.475             53.3                           0.598               13.00              2.122                      ok            True                  False
  UPRO           95.24               21            1.68              1.77        150.11                28.22         0.513          pass              0.610             28.5                           0.467                8.56              0.877                      ok            True                  False
   ROP           88.24               17            1.79              4.21        334.69                35.89         0.511          pass              0.429             37.3                           0.611                0.48              0.324                      ok            True                  False
   CEG           80.95               21            2.29              4.37        270.78                55.62         0.508          pass              0.191             13.9                           0.371                2.20             -0.300                      ok            True                  False
  INTU           73.68               19            2.93              6.61        319.31               101.75         0.657          pass              0.186             19.9                           0.413              -21.77             -1.278 downtrend_blocked_slope           False                  False
    ZS           50.00                4            7.05              7.11        141.10               159.87         0.644          pass              0.077              4.3                           0.264              -23.54             -2.972 downtrend_blocked_slope           False                  False
  PAYX           87.50                8            2.15              1.52        100.14                33.97         0.554          pass              0.349             31.3                           0.581                4.38              0.647                      ok           False                  False
  CDNS          100.00                9            2.74              7.99        412.96                43.85         0.532          pass              0.530             25.7                           0.525               19.77              1.824                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-03T12:00:06.118457-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:45:06.164113-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:40:05.582974-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:35:06.204353-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:30:06.209772-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:25:03.345818-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:20:06.172120-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-03T11:15:06.996321-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603134506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603134506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603134506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603134506)

</details>

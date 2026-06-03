# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 14:45:05 EDT`
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
  FTNT          100.00               23            1.65              1.71        148.13                71.83         0.619          pass              0.723             58.2                           0.492               14.71              1.490                      ok            True                  False
  MELI           89.47               19            2.08             24.34       1662.40                61.01         0.615          pass              0.382              2.5                           0.108                2.71              0.313                      ok            True                  False
  NXPI           96.88               32            0.59              1.34        323.05                50.93         0.571          pass              0.791             62.5                           0.426                9.32              0.688                      ok            True                  False
  AAPL           90.00               10            1.78              3.94        313.51                17.72         0.516          pass              0.353             11.4                           0.353                3.55              0.354                      ok            True                  False
  WDAY           84.38               32            1.95              2.03        148.01                75.59         0.511          pass              0.465             50.3                           0.550               12.87              2.117                      ok            True                  False
  UPRO           95.65               23            1.51              1.59        150.19                28.22         0.510          pass              0.645             35.7                           0.480                8.75              0.885                      ok            True                  False
   ROP           85.71               14            2.08              4.89        334.40                35.89         0.510          pass              0.312             27.2                           0.443                0.18              0.311                      ok            True                  False
   CEG           80.95               21            2.25              4.30        270.81                55.62         0.510          pass              0.201             17.3                           0.449                2.24             -0.298                      ok            True                  False
  CRWD           80.00               15            2.32             12.49        763.60                51.19         0.507          pass              0.185             33.5                           0.374               21.76              2.193                      ok            True                  False
    ZS           50.00                4            6.32              6.38        141.42               159.87         0.689          pass              0.112             14.2                           0.440              -22.94             -2.937 downtrend_blocked_slope           False                  False
  INTU           73.68               19            3.00              6.76        319.24               101.75         0.653          pass              0.179             18.1                           0.404              -21.82             -1.281 downtrend_blocked_slope           False                  False
  MSFT          100.00                2            2.91              8.99        437.46                33.05         0.551          pass              0.529             24.7                           0.526                2.87              0.721                      ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603144505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603144505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603144505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603144505)

</details>

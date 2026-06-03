# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 12:40:06 EDT`
Last processed slot: `manage_1230`

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
  MELI           92.00               25            1.70             19.93       1664.29                61.01         0.604          pass              0.512             10.5                           0.238                3.10              0.331                                 ok            True                  False
  FTNT          100.00               27            1.47              1.53        148.20                71.83         0.603          pass              0.762             62.6                           0.589               14.91              1.498                                 ok            True                  False
  NXPI           96.77               31            0.78              1.77        322.86                50.93         0.565          pass              0.747             50.3                           0.304                9.11              0.679                                 ok            True                  False
  MCHP           96.00               25            0.88              0.59         96.71                44.80         0.532          pass              0.767             71.2                           0.550                5.21              0.392                                 ok            True                  False
  AAPL           90.91               11            1.75              3.87        313.54                17.72         0.514          pass              0.367              6.0                           0.112                3.58              0.355                                 ok            True                  False
   ROP           85.71               14            2.02              4.76        334.46                35.89         0.514          pass              0.318             29.2                           0.642                0.24              0.314                                 ok            True                  False
  WDAY           84.38               32            1.95              2.03        148.01                75.59         0.511          pass              0.465             50.3                           0.649               12.87              2.117                                 ok            True                  False
   ADP          100.00               15            2.11              3.42        229.72                34.09         0.508          pass              0.547             21.0                           0.419                2.66              0.430                                 ok            True                  False
  SNPS          100.00               10            2.91             10.35        503.92                42.98         0.506          pass              0.492             13.8                           0.386               -0.06             -0.274                                 ok            True                  False
  INSM           80.43               46            0.10              0.07        103.70               108.46         0.748          pass              0.572             95.2                           0.736               -3.52             -0.388 downtrend_blocked_slope_and_streak           False                  False
    MU           82.86               35            0.02              0.16       1064.03               101.17         0.741          pass              0.614             99.1                           0.703               52.26              4.602                                 ok           False                  False
    ZS           50.00                4            6.72              6.78        141.25               159.87         0.671          pass              0.071              1.4                           0.151              -23.27             -2.956            downtrend_blocked_slope           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603124006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603124006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603124006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603124006)

</details>

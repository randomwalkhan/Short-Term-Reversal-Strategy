# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 13:20:02 EDT`
Last processed slot: `manage_1330`

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
    MU           81.82               33            0.67              4.98       1061.97               101.17         0.716          pass              0.490             72.2                           0.404               51.27              4.573                      ok            True                  False
  FTNT          100.00               19            1.77              1.85        148.07                71.83         0.638          pass              0.689             54.9                           0.282               14.56              1.484                      ok            True                  False
  MELI           92.31               26            1.54             18.04       1665.10                61.01         0.608          pass              0.552             18.9                           0.330                3.27              0.338                      ok            True                  False
  NXPI           96.55               29            1.09              2.47        322.56                50.93         0.558          pass              0.674             30.5                           0.230                8.77              0.665                      ok            True                  False
  MCHP          100.00               20            1.39              0.94         96.56                44.80         0.536          pass              0.684             54.4                           0.340                4.67              0.368                      ok            True                  False
   ROP           86.67               15            1.94              4.58        334.54                35.89         0.513          pass              0.358             31.9                           0.591                0.32              0.317                      ok            True                  False
  SNPS          100.00               14            2.38              8.49        504.71                42.98         0.512          pass              0.566             29.3                           0.555                0.48             -0.250                      ok            True                  False
  WDAY           84.38               32            2.03              2.11        147.98                75.59         0.506          pass              0.459             48.4                           0.584               12.78              2.113                      ok            True                  False
  UPRO           94.74               19            2.07              2.19        149.93                28.22         0.501          pass              0.538             11.6                           0.315                8.12              0.859                      ok            True                  False
   CEG           80.00               20            2.49              4.75        270.61                55.62         0.501          pass              0.125              2.9                           0.258                1.99             -0.309                      ok            True                  False
  INTU           73.68               19            3.16              7.12        319.09               101.75         0.643          pass              0.165             13.7                           0.246              -21.95             -1.288 downtrend_blocked_slope           False                  False
    ZS           50.00                4            7.10              7.16        141.08               159.87         0.642          pass              0.070              2.0                           0.196              -23.58             -2.975 downtrend_blocked_slope           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603132002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603132002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603132002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603132002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 10:05:05 EDT`
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

- Cash: `$33,480.75`
- Equity: `$33,480.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-04)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00050000    106          2026-08-03         2026-08-04         1.65       1.485 -1749.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.96              0.42         61.55                32.17         0.608          pass              0.602             44.9                           0.582                2.13              0.386                      ok            True                  False
   ROP           92.00               25            1.18              3.23        391.19                47.45         0.578          pass              0.616             46.1                           0.395               10.63              1.469                      ok            True                  False
  DXCM           88.89               36            0.71              0.43         87.12                57.42         0.553          pass              0.597             43.6                           0.339               15.97              1.961                      ok            True                  False
  CTAS           91.67               24            0.95              1.35        203.43                37.98         0.546          pass              0.614             51.7                           0.518                0.83              0.135                      ok            True                  False
   WBD           91.67               24            0.65              0.12         26.04                24.14         0.545          pass              0.516             19.0                           0.188                0.35              0.078                      ok            True                  False
   PEP           83.33               24            0.74              0.72        139.32                26.13         0.540          pass              0.413             58.8                           0.716                2.67              0.387                      ok            True                  False
  PAYX          100.00               13            1.19              0.98        117.25                35.86         0.531          pass              0.725             83.9                           0.689                4.93              0.777                      ok            True                  False
  MNST           92.00               25            0.69              0.45         93.36                26.29         0.516          pass              0.597             42.0                           0.353               -1.65              0.021                      ok            True                  False
  ISRG           69.23               13            2.26              5.94        372.87                72.79         0.664          pass              0.086              0.0                           0.150                4.82              0.808                      ok           False                  False
  TMUS           90.00               20            1.24              1.53        176.43                55.96         0.658          pass              0.417              6.0                           0.091               -8.32             -0.680 downtrend_blocked_slope           False                  False
  PYPL           93.18               44            0.06              0.02         57.86                60.15         0.635          pass              0.901             95.2                           0.752                3.55              0.453                      ok           False                  False
   KHC           92.00               25            0.17              0.03         26.41                32.72         0.617          pass              0.735             84.4                           0.690                2.27              0.315                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-08-04T10:05:05.202403-04:00 early_entry_1005 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:05:05.202403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.485, "pnl": -1749.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-04T10:00:02.269549-04:00 early_entry_1000 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T08:05:01.281633-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T08:00:06.156963-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T07:55:05.413752-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T07:50:01.172793-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T07:45:05.958919-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T07:40:04.165148-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-04T07:35:01.120189-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804100505)

</details>

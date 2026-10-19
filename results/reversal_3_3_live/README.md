# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 09:50:04 EDT`
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

- Cash: `$131,531.80`
- Equity: `$131,531.80`
- Realized PnL: `$121,531.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     35          2026-10-16         2026-10-19        17.05       19.65 9100.0   15.249267 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KDP           95.65               23            0.58              0.14         34.56                30.61         0.573          pass              0.753             69.7                           0.646               11.43              1.316                      ok            True                  False
   CEG           88.89               27            1.11              2.11        270.46                59.14         0.570          pass              0.426              6.2                           0.134                0.27             -0.633                      ok            True                  False
 CMCSA           90.91               11            0.96              0.15         21.84                21.89         0.562          pass              0.469             38.2                           0.421                2.12              0.310                      ok            True                  False
  CTAS           91.67               24            0.91              1.36        213.11                23.07         0.514          pass              0.541             28.3                           0.267                8.37              0.976                      ok            True                  False
  CTSH           94.44               36            0.70              0.32         65.89                41.45         0.512          pass              0.733             41.0                           0.358               12.72              1.557                      ok            True                  False
   ADP           92.86               28            0.57              1.16        288.40                21.32         0.510          pass              0.712             66.2                           0.405               10.37              1.094                      ok            True                  False
   KHC           86.36               22            1.12              0.19         23.60                22.28         0.503          pass              0.373             24.3                           0.331                7.21              0.760                      ok            True                  False
  TMUS           80.77               26            0.88              0.98        158.68                56.39         0.630          pass              0.228             12.5                           0.164               -4.22             -0.646 downtrend_blocked_slope           False                  False
  PAYX           75.00               28            1.08              0.85        111.27                41.41         0.558          pass              0.222             15.4                           0.151               10.66              1.147                      ok           False                  False
   EXC           75.00                8            1.36              0.41         43.32                17.09         0.536          pass              0.054              0.0                           0.167                5.12              0.497                      ok           False                  False
  ABNB           92.31               39            0.35              0.42        173.52                41.37         0.529          pass              0.727             50.9                           0.291                5.50              0.796                      ok           False                  False
  MDLZ           96.15               26            0.30              0.13         63.85                19.69         0.526          pass              0.757             66.1                           0.672                8.94              0.877                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                                detail
2026-10-19T09:50:04.852472-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 19.65, "pnl": 9100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.25, "ticker": "CEG"}
2026-10-19T03:00:04.169170-04:00   data_refresh  data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-17T02:55:05.454730-04:00 share_ext_0255 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:50:06.805476-04:00 share_ext_0250 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:45:05.931268-04:00 share_ext_0245 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:40:05.272709-04:00 share_ext_0240 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:35:06.507747-04:00 share_ext_0235 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:30:06.058985-04:00 share_ext_0230 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:25:05.586713-04:00 share_ext_0225 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:20:06.484266-04:00 share_ext_0220 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019095004)

</details>

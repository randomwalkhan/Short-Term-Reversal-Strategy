# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 10:00:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           90.00               10            1.07              0.16         21.83                21.89         0.561          pass              0.415             30.9                           0.395                2.00              0.305                                 ok            True                  False
   CEG           85.00               20            1.94              3.69        269.79                59.14         0.553          pass              0.255              0.0                           0.150               -0.57             -0.672                                 ok            True                  False
  CTAS           92.59               27            0.78              1.16        213.19                23.07         0.505          pass              0.615             38.6                           0.455                8.51              0.982                                 ok            True                  False
   KHC           88.00               25            0.87              0.14         23.62                22.28         0.502          pass              0.488             41.4                           0.559                7.49              0.772                                 ok            True                  False
  TMUS           82.76               29            0.62              0.69        158.80                56.39         0.630          pass              0.378             38.1                           0.329               -3.97             -0.634            downtrend_blocked_slope           False                  False
   KDP           96.15               26            0.43              0.10         34.58                30.61         0.564          pass              0.795             77.3                           0.753               11.59              1.322                                 ok           False                  False
  PAYX           78.12               32            0.70              0.55        111.40                41.41         0.561          pass              0.339             45.5                           0.501               11.09              1.165                                 ok           False                  False
   EXC           75.00                4            1.52              0.46         43.30                17.09         0.547          pass              0.074              6.4                           0.147                4.95              0.489                                 ok           False                  False
  META           84.62               13            1.69              8.39        705.73                56.19         0.523          pass              0.214              6.2                           0.118               -6.01             -0.277 downtrend_blocked_slope_and_streak           False                  False
  CTSH           94.87               39            0.45              0.21         65.94                41.45         0.509          pass              0.826             61.7                           0.577               13.00              1.568                                 ok           False                  False
  MDLZ           93.55               31            0.08              0.03         63.90                19.69         0.507          pass              0.825             91.1                           0.805                9.18              0.887                                 ok           False                  False
   XEL           88.00               25            0.47              0.25         76.20                16.32         0.507          pass              0.427             20.9                           0.218                6.24              0.609                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-19T10:00:05.134811-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T09:50:04.852472-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 19.65, "pnl": 9100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.25, "ticker": "CEG"}
2026-10-19T03:00:04.169170-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-17T02:55:05.454730-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:50:06.805476-04:00   share_ext_0250      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:45:05.931268-04:00   share_ext_0245      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:40:05.272709-04:00   share_ext_0240      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:35:06.507747-04:00   share_ext_0235      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:30:06.058985-04:00   share_ext_0230      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:25:05.586713-04:00   share_ext_0225      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019100005)

</details>

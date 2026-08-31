# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 10:05:01 EDT`
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

- Cash: `$50,178.10`
- Equity: `$50,178.10`
- Realized PnL: `$40,178.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-31)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00155000     29          2026-08-28         2026-08-31          9.0         8.1 -2610.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ABNB          100.00               13            2.11              2.80        188.23                62.79         0.681          pass              0.510              7.4                           0.155                3.42              0.290                  ok            True                  False
  MELI          100.00               14            2.00             27.50       1954.46                48.83         0.619          pass              0.520             10.4                           0.136                7.80              0.798                  ok            True                  False
   TRI           93.33               30            1.13              0.84        105.86                60.45         0.586          pass              0.777             76.3                           0.634                6.71              0.432                  ok            True                   True
  PAYX          100.00               22            0.81              0.72        126.73                24.67         0.558          pass              0.628             30.6                           0.269                6.30              0.607                  ok            True                  False
  SBUX           93.75               16            0.93              0.70        107.55                22.68         0.555          pass              0.516             18.0                           0.188               -0.99              0.142                  ok            True                  False
   KDP           87.50               16            1.79              0.40         32.01                30.92         0.539          pass              0.294              0.0                           0.002                4.38              0.452                  ok            True                  False
  CHTR           88.89               27            1.86              2.00        152.76                53.40         0.530          pass              0.417              4.7                           0.066                4.62              0.361                  ok            True                  False
  VRTX           97.06               34            0.63              2.39        540.67                33.03         0.526          pass              0.804             64.0                           0.675                4.41              0.297                  ok            True                   True
 CMCSA           93.75               16            1.64              0.31         26.93                25.33         0.523          pass              0.462              1.1                           0.049                4.09              0.342                  ok            True                  False
  WDAY           86.96               23            3.19              4.57        202.76                72.83         0.510          pass              0.353             10.1                           0.113                3.66              0.268                  ok            True                  False
  UPRO           82.61               23            1.31              1.39        151.18                30.93         0.506          pass              0.248             13.9                           0.230               -2.99             -0.089                  ok            True                  False
  MDLZ           92.31               26            0.83              0.36         62.21                19.95         0.503          pass              0.485              0.0                           0.177               -0.54             -0.170                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-31T10:05:01.432627-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "entry_ask": 24.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 21.65, "hypothetical_budget": 25089.05, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 39.0, "option_spread_pct": 30.02, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "matched_signals": 34, "recovery_stability_score": 0.675, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.777, "early_reclaim_pct": 76.3, "matched_signals": 30, "recovery_stability_score": 0.634, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.586, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:00:05.270470-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T09:50:01.420574-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-29T02:55:05.202083-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:30:05.313779-04:00   share_ext_0230      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831100501)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 10:10:04 EDT`
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

- Cash: `$16,479.50`
- Equity: `$33,352.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$658.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 16873.0         1.72            1.8       58.88         58.52          bid_ask_mid                        1.8                bid_ask_mid                    True           658.0                   4.06         94.12               17              1.51         27.86           33.86                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           93.10               29            0.93              0.38         58.91                60.12         0.663          pass              0.648             35.3                           0.326                4.37              0.337                      ok            True                  False
  TMUS           89.47               19            1.64              2.04        176.32                55.81         0.646          pass              0.391              4.6                           0.151               -1.65             -0.180                      ok            True                  False
  MCHP           84.85               33            1.40              0.83         84.33                76.06         0.561          pass              0.462             41.0                           0.480                7.20              0.976                      ok            True                  False
  MDLZ           91.67               12            1.65              0.72         62.30                30.17         0.560          pass              0.432             17.2                           0.230                1.50             -0.038                      ok            True                  False
  BKNG           93.75               16            2.19              3.29        213.01                46.72         0.557          pass              0.475              4.1                           0.067               12.28              1.005                      ok            True                  False
  ORLY           86.96               23            1.50              0.98         93.11                35.75         0.531          pass              0.325              0.0                           0.197                1.69              0.398                      ok            True                  False
  CTSH           86.11               36            0.88              0.36         57.52                54.30         0.510          pass              0.557             56.4                           0.512               21.49              1.501                      ok            True                  False
  MPWR           81.08               37            0.65              6.40       1398.80                61.17         0.505          pass              0.410             50.1                           0.365                3.98              0.713                      ok            True                  False
  TEAM           84.62               39            0.34              0.35        148.92               133.30         0.820          pass              0.662             87.7                           0.631               54.97              3.935                      ok           False                  False
  ALNY           88.64               44            0.36              0.55        218.96               128.37         0.800          pass              0.646             45.1                           0.294              -21.55             -2.618 downtrend_blocked_slope           False                  False
  LRCX           89.47               38            0.22              0.49        311.14                90.05         0.677          pass              0.757             83.3                           0.430                6.53              1.467                      ok           False                  False
 CMCSA           88.89                9            1.85              0.33         25.22                44.15         0.638          pass              0.307              2.1                           0.052                9.17              0.749                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-08-10T10:10:04.657796-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:05:05.873939-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "entry_ask": 21.95, "entry_bid": 19.4, "entry_mode": "early", "entry_option_price": 20.675, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 12.33, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "matched_signals": 41, "recovery_stability_score": 0.792, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:00:04.766738-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "entry_ask": 22.45, "entry_bid": 20.25, "entry_mode": "early", "entry_option_price": 21.35, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 10.3, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "matched_signals": 41, "recovery_stability_score": 0.847, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.772, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.761, "success_rate": 91.18, "ticker": "STX", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T03:00:02.466412-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 93}
2026-08-08T02:55:02.757209-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:50:05.752555-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:45:01.896094-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:40:05.765932-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:35:06.001208-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:30:03.730064-04:00   share_ext_0230      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810101004)

</details>

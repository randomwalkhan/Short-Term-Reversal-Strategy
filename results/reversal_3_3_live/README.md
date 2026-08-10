# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 10:05:05 EDT`
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
- Equity: `$33,258.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$564.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 16779.0         1.72           1.78       58.88         58.71          bid_ask_mid                       1.78                bid_ask_mid                    True           564.0                   3.48         94.12               17              1.51         27.86           33.01                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.08               37            1.48              1.46        139.63               179.06         0.801          pass              0.448             52.9                           0.368                7.82              2.669                      ok            True                  False
  LRCX           87.88               33            0.79              1.71        310.62                90.05         0.669          pass              0.555             41.5                           0.276                5.93              1.441                      ok            True                  False
  PYPL           94.12               34            0.61              0.25         58.96                60.12         0.653          pass              0.775             57.6                           0.481                4.71              0.351                      ok            True                  False
  TMUS           90.91               22            1.26              1.57        176.52                55.81         0.653          pass              0.516             26.6                           0.285               -1.28             -0.162                      ok            True                  False
 CMCSA           90.00               10            1.81              0.32         25.22                44.15         0.637          pass              0.330              0.0                           0.025                9.21              0.751                      ok            True                  False
  MDLZ           91.67               12            1.61              0.71         62.31                30.17         0.562          pass              0.437             18.8                           0.228                1.53             -0.036                      ok            True                  False
  BKNG           94.44               18            2.11              3.16        213.06                46.72         0.551          pass              0.500              2.1                           0.137               12.37              1.009                      ok            True                  False
  MCHP           84.85               33            1.71              1.01         84.26                76.06         0.540          pass              0.421             28.1                           0.258                6.86              0.962                      ok            True                  False
  ORLY           88.00               25            1.28              0.84         93.17                35.75         0.536          pass              0.372              1.6                           0.096                1.93              0.408                      ok            True                  False
  MPWR           81.08               37            0.64              6.30       1398.84                61.17         0.506          pass              0.412             50.9                           0.331                3.99              0.713                      ok            True                  False
  CHTR           90.48               21            2.44              2.61        151.45                48.91         0.501          pass              0.403              0.0                           0.197               13.10              1.281                      ok            True                  False
  ALNY           88.10               42            0.49              0.76        218.87               128.37         0.802          pass              0.568             24.1                           0.203              -21.65             -2.624 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-08-10T10:05:05.873939-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "entry_ask": 21.95, "entry_bid": 19.4, "entry_mode": "early", "entry_option_price": 20.675, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 12.33, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.876, "early_reclaim_pct": 76.7, "matched_signals": 41, "recovery_stability_score": 0.792, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:00:04.766738-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "DASH260918C00200000", "current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "entry_ask": 22.45, "entry_bid": 20.25, "entry_mode": "early", "entry_option_price": 21.35, "hypothetical_budget": 8239.75, "hypothetical_contracts": 3, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 1627.0, "option_spread_pct": 10.3, "option_volume": 81.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 82.1, "matched_signals": 41, "recovery_stability_score": 0.847, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.772, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.761, "success_rate": 91.18, "ticker": "STX", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T03:00:02.466412-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 93}
2026-08-08T02:55:02.757209-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:50:05.752555-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:45:01.896094-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:40:05.765932-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:35:06.001208-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:30:03.730064-04:00   share_ext_0230      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:25:01.945300-04:00   share_ext_0225      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810100505)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 10:00:02 EDT`
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

- Cash: `$17,610.75`
- Equity: `$33,290.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-80.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15680.0         9.85            9.8       98.17         99.14     last_price_stale                        NaN                unavailable                   False           -80.0                  -0.51         95.65               23              3.29          79.1            0.78                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.74              1.05         85.59                69.04         0.644          pass              0.325             39.5                           0.401               -1.53              0.158                       ok            True                  False
  PAYX          100.00               18            0.82              0.57        100.28                33.39         0.603          pass              0.688             58.2                           0.586                2.79              0.565                       ok            True                  False
  MSFT           87.50               24            1.11              3.25        415.28                34.82         0.567          pass              0.391             13.7                           0.206               -1.56              0.118                       ok            True                  False
  PANW           92.50               40            0.51              0.98        271.63                60.15         0.542          pass              0.833             81.7                           0.802                7.01              1.241                       ok            True                   True
  CTAS           86.36               22            1.31              1.64        179.14                23.69         0.503          pass              0.369             23.0                           0.363                2.64              0.521                       ok            True                  False
    ZS           81.58               38            0.65              0.59        130.53               157.69         0.894          pass              0.535             72.2                           0.598              -28.75             -2.387  downtrend_blocked_slope           False                  False
  TEAM           95.45               44            0.33              0.23         99.37                86.36         0.645          pass              0.935             90.1                           0.791               16.06              1.867                       ok           False                  False
   CEG           81.82               33            0.65              1.16        254.33                55.63         0.576          pass              0.454             64.8                           0.630              -11.42             -1.489  downtrend_blocked_slope           False                  False
  INSM           69.70               33            1.30              0.86         93.85                54.02         0.570          pass              0.339             43.0                           0.273              -12.47             -0.926  downtrend_blocked_slope           False                  False
  CRWD           93.02               43            0.17              0.82        670.67                64.90         0.563          pass              0.871             89.2                           0.459                3.34              1.030                       ok           False                  False
   EXC           75.00               12            0.72              0.23         45.65                19.68         0.560          pass              0.212             47.6                           0.266               -0.83             -0.186                       ok           False                  False
   AEP           60.00               15            0.71              0.64        128.86                24.28         0.554          pass              0.266             58.9                           0.343               -2.56             -0.234 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-06-08T10:00:02.881266-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.7, "entry_ask": 15.4, "entry_bid": 14.0, "entry_mode": "early", "entry_option_price": 14.7, "hypothetical_budget": 8805.38, "hypothetical_contracts": 5, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 1806.0, "option_spread_pct": 9.52, "option_volume": 195.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.802, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.7, "matched_signals": 40, "recovery_stability_score": 0.802, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.821, "early_reclaim_pct": 77.9, "matched_signals": 41, "recovery_stability_score": 0.585, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-06T02:55:05.037778-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:50:04.162002-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:45:02.082249-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:40:02.201062-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:35:06.145778-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:30:02.216838-04:00   share_ext_0230      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:25:03.009223-04:00   share_ext_0225      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:20:05.037850-04:00   share_ext_0220      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:15:06.052679-04:00   share_ext_0215      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608100002)

</details>

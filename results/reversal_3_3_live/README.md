# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-21 09:43:07 EDT`
Last processed slot: `manual`

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

- Cash: `$26,628.00`
- Equity: `$53,798.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$660.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261016C00180000       2026-08-20                   1     22     26510.0                 27170.0        12.05          12.35      185.18        184.99     last_price_stale                        NaN                unavailable                   False           660.0                   2.49         93.94               33              0.65         33.73             0.0                  63.87                 783.0           31.0               0.06                      ok
```

## Today's Closed Trades (2026-08-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           80.00               30            2.09              2.56        173.81               116.76         0.737          pass              0.239             10.5                           0.242               14.89              1.525                                 ok            True                  False
  MRVL           80.00               35            2.03              3.56        249.48                98.16         0.592          pass              0.268             14.0                           0.134               12.44              1.549                                 ok            True                  False
  PAYX          100.00               27            0.50              0.43        122.73                35.17         0.550          pass              0.782             71.1                           0.359                1.88              0.105                                 ok            True                  False
  AAPL           84.62               26            0.98              2.13        310.39                35.92         0.522          pass              0.346             21.2                           0.237               -1.53              0.117                                 ok            True                  False
   ROP          100.00               26            1.10              3.15        409.10                34.10         0.505          pass              0.734             59.0                           0.365                0.92              0.130                                 ok            True                  False
   WDC           83.33               36            0.37              1.23        468.52               103.26         0.710          pass              0.545             70.5                           0.376                7.60              0.973                                 ok           False                  False
  AMAT           91.43               35            0.72              2.50        495.14                84.07         0.677          pass              0.640             33.5                           0.246               -8.53             -0.858            downtrend_blocked_slope           False                  False
  SHOP           97.30               37            0.73              0.75        146.86                80.43         0.672          pass              0.846             66.3                           0.355               -3.60             -0.575            downtrend_blocked_slope           False                  False
  WDAY           84.62               39            0.31              0.43        197.14                83.43         0.662          pass              0.604             73.7                           0.396                9.50              0.992                                 ok           False                  False
   TRI           91.89               37            0.41              0.30        105.75                73.29         0.634          pass              0.671             36.8                           0.178                4.23              0.192                                 ok           False                  False
  KLAC           83.78               37            0.43              0.55        185.62                69.68         0.614          pass              0.342              0.0                           0.183               -6.48             -0.749 downtrend_blocked_slope_and_streak           False                  False
  AMZN           69.70               33            0.74              1.35        259.53                59.61         0.603          pass              0.325             37.2                           0.249               -5.94             -0.654 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-21T00:00:05.323227-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-20T14:55:07.817083-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 26510.0, "asset_type": "option", "contract_symbol": "ABNB261016C00180000", "contracts": 22, "early_entry_score": 0.826, "entry_mode": "regular", "entry_option_price": 12.05, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 783.0, "option_spread_pct": 5.81, "option_volume": 31.0, "success_rate": 93.94, "ticker": "ABNB", "timing_score": 0.625}
2026-08-20T14:55:07.817083-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"early_entry_score": 0.536, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 8.0, "option_spread_pct": 24.91, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.643}
2026-08-20T14:55:07.817083-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-20", "training_samples": 5707, "window": 5}
2026-08-20T11:40:03.908797-04:00 early_entry_1140      early_entry_shadow {"contract_symbol": "SHOP261016C00145000", "current_drop_pct": 0.62, "early_entry_score": 0.855, "early_reclaim_pct": 62.8, "entry_ask": 11.35, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.05, "hypothetical_budget": 26569.0, "hypothetical_contracts": 24, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 617.0, "option_spread_pct": 5.43, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 97.56, "ticker": "SHOP", "timing_score": 0.666, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.855, "early_reclaim_pct": 62.8, "matched_signals": 41, "recovery_stability_score": 0.651, "success_rate": 97.56, "ticker": "SHOP", "timing_score": 0.666, "trend_health_status": "ok"}, {"current_drop_pct": 0.74, "early_entry_score": 0.831, "early_reclaim_pct": 76.8, "matched_signals": 33, "recovery_stability_score": 0.748, "success_rate": 96.97, "ticker": "VRTX", "timing_score": 0.476, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-20T11:31:08.330243-04:00 early_entry_1130      early_entry_shadow {"contract_symbol": "SHOP261016C00145000", "current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "entry_ask": 11.45, "entry_bid": 10.35, "entry_mode": "early", "entry_option_price": 10.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 617.0, "option_spread_pct": 10.09, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.573, "shadow_only": true, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.841, "early_reclaim_pct": 60.2, "matched_signals": 39, "recovery_stability_score": 0.573, "success_rate": 97.44, "ticker": "SHOP", "timing_score": 0.674, "trend_health_status": "ok"}, {"current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 32, "recovery_stability_score": 0.782, "success_rate": 96.88, "ticker": "VRTX", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-20T10:57:29.950425-04:00 early_entry_1055      early_entry_shadow                                                                                                                                                                                                                               {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "entry_ask": 14.4, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 13.9, "hypothetical_budget": 26569.0, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 215.0, "option_spread_pct": 7.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.684, "early_reclaim_pct": 62.5, "matched_signals": 33, "recovery_stability_score": 0.636, "success_rate": 90.91, "ticker": "MAR", "timing_score": 0.521, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T10:38:39.121946-04:00 early_entry_1035      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-20T10:19:19.114673-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "entry_ask": 26.9, "entry_bid": 24.1, "entry_mode": "early", "entry_option_price": 25.5, "hypothetical_budget": 26569.0, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 92.0, "option_spread_pct": 10.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.796, "early_reclaim_pct": 71.3, "matched_signals": 30, "recovery_stability_score": 0.605, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-20T09:18:16.446091-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260821094307)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260821094307)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260821094307)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260821094307)

</details>

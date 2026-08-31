# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 10:25:01 EDT`
Last processed slot: `manage_1030`

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
  ABNB          100.00               14            1.95              2.59        188.32                62.79         0.684          pass              0.538             14.4                           0.302                3.59              0.297                  ok            True                  False
   TRI           94.12               34            0.61              0.45        106.03                60.45         0.595          pass              0.858             87.3                           0.841                7.28              0.456                  ok            True                   True
  MELI          100.00               31            0.96             13.21       1960.59                48.83         0.577          pass              0.769             57.0                           0.721                8.94              0.845                  ok            True                  False
  MSTR           83.78               37            1.04              0.93        126.91                81.68         0.567          pass              0.384             15.6                           0.166               28.98              3.293                  ok            True                  False
  AMGN          100.00               24            0.57              1.73        431.68                27.94         0.565          pass              0.734             61.4                           0.661                3.12              0.248                  ok            True                  False
  PAYX          100.00               28            0.53              0.47        126.84                24.67         0.537          pass              0.738             54.9                           0.639                6.61              0.620                  ok            True                  False
  VRTX           96.55               29            1.09              4.15        539.91                33.03         0.529          pass              0.692             37.3                           0.382                3.92              0.276                  ok            True                  False
  UPRO           87.50               16            1.78              1.89        150.97                30.93         0.528          pass              0.298              1.6                           0.206               -3.44             -0.111                  ok            True                  False
  CTAS           85.00               20            0.85              1.21        203.66                14.76         0.518          pass              0.327             24.9                           0.329                2.34              0.229                  ok            True                  False
  BKNG           94.74               19            1.99              2.86        204.40                35.32         0.517          pass              0.591             28.6                           0.598               -1.57             -0.246                  ok            True                  False
 CMCSA           90.00               20            1.24              0.23         26.96                25.33         0.515          pass              0.469             28.0                           0.413                4.52              0.361                  ok            True                  False
   KDP           82.61               23            1.35              0.30         32.05                30.92         0.512          pass              0.284             25.6                           0.339                4.84              0.472                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-31T10:25:01.260797-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.841, "shadow_only": true, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.858, "early_reclaim_pct": 87.3, "matched_signals": 34, "recovery_stability_score": 0.841, "success_rate": 94.12, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:20:06.273399-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                    {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.841, "early_reclaim_pct": 85.4, "matched_signals": 33, "recovery_stability_score": 0.783, "success_rate": 93.94, "ticker": "TRI", "timing_score": 0.595, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:15:05.509244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "TRI261016C00105000", "current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "entry_ask": 9.0, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 25089.05, "hypothetical_contracts": 32, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 35.0, "option_spread_pct": 33.77, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.801, "early_reclaim_pct": 80.2, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 93.55, "ticker": "TRI", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:10:04.381634-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T10:05:01.432627-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "entry_ask": 24.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 21.65, "hypothetical_budget": 25089.05, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 39.0, "option_spread_pct": 30.02, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "matched_signals": 34, "recovery_stability_score": 0.675, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.777, "early_reclaim_pct": 76.3, "matched_signals": 30, "recovery_stability_score": 0.634, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.586, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:00:05.270470-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T09:50:01.420574-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-29T02:55:05.202083-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831102501)

</details>

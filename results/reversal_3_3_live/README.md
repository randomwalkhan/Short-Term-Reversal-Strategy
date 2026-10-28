# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 11:35:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$68,764.30`
- Equity: `$133,404.30`
- Realized PnL: `$122,764.30`
- Unrealized PnL: `$640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 64640.0         20.0           20.2       220.6        220.56          bid_ask_mid                       20.2                bid_ask_mid                    True           640.0                    1.0         100.0               12              3.08          70.9           72.85                  47.89                 302.0           39.0                0.1                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            0.57              0.25         62.24                25.51         0.613          pass              0.564             51.4                           0.490               -0.92             -0.092                                 ok            True                  False
  MSTR           91.18               34            1.16              1.14        140.91                70.33         0.596          pass              0.601             27.7                           0.332               -2.43             -0.150                                 ok            True                  False
 CMCSA           90.00               10            1.03              0.16         21.77                26.07         0.582          pass              0.437             37.5                           0.391                2.68              0.234                                 ok            True                  False
   KHC           88.46               26            0.81              0.14         24.00                36.33         0.554          pass              0.486             32.7                           0.264                5.13              0.636                                 ok            True                  False
    ZS           92.11               38            0.55              0.99        259.72                56.99         0.543          pass              0.714             50.0                           0.241               17.18              2.371                                 ok            True                  False
   PEP           80.00               25            0.64              0.60        133.24                25.80         0.522          pass              0.297             48.4                           0.633                2.61              0.402                                 ok            True                  False
  MCHP           88.89               18            2.39              1.34         79.59                42.57         0.507          pass              0.371             10.1                           0.237                9.82              0.754                                 ok            True                  False
  CRWD           85.00               40            1.10              2.06        267.14                57.68         0.501          pass              0.402              6.4                           0.083                6.33              1.259                                 ok            True                  False
  TMUS           85.29               34            0.45              0.46        146.63                63.84         0.646          pass              0.616             83.4                           0.726               -7.36             -0.918            downtrend_blocked_slope           False                  False
   CEG           84.21               38            0.47              0.85        258.61                65.80         0.597          pass              0.578             73.1                           0.485               -7.79             -0.865 downtrend_blocked_slope_and_streak           False                  False
  MPWR           68.97               29            1.11              9.40       1207.86                59.51         0.568          pass              0.308             41.5                           0.490               -3.59             -0.610            downtrend_blocked_slope           False                  False
  PAYX           50.00                6            1.62              1.24        108.73                35.39         0.556          pass              0.147             30.6                           0.466                0.20              0.285                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-28T11:35:05.885505-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:30:05.433292-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:25:02.485358-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "entry_ask": 18.3, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.9, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.795, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.795, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:20:06.604106-04:00 early_entry_1120 early_entry_shadow   {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "entry_ask": 18.3, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.9, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 78.9, "matched_signals": 42, "recovery_stability_score": 0.803, "success_rate": 88.1, "ticker": "ALNY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:15:06.636724-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:10:06.028026-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T11:05:04.307484-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "entry_ask": 18.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.6, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.28, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "matched_signals": 43, "recovery_stability_score": 0.788, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:00:05.505760-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:55:05.346290-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:50:05.367637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028113505)

</details>

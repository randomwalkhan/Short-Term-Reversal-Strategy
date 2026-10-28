# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 10:55:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$133,244.30`
- Realized PnL: `$122,764.30`
- Unrealized PnL: `$480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 64480.0         20.0          20.15       220.6         221.8          bid_ask_mid                      20.15                bid_ask_mid                    True           480.0                   0.75         100.0               12              3.08          70.9           70.85                  47.89                 302.0           39.0                0.1                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.86               14            0.55              0.24         62.25                25.51         0.609            pass              0.591             53.4                           0.545               -0.89             -0.091                                 ok            True                  False
  MSTR           90.91               33            1.25              1.23        140.87                70.33         0.597            pass              0.570             22.0                           0.233               -2.51             -0.154                                 ok            True                  False
   KHC           90.00               30            0.54              0.09         24.02                36.33         0.547            pass              0.620             55.2                           0.596                5.42              0.648                                 ok            True                  False
   PEP           80.95               21            0.77              0.72        133.19                25.80         0.539            pass              0.265             37.4                           0.604                2.48              0.396                                 ok            True                  False
   KDP           96.15               26            0.50              0.12         34.81                24.92         0.532            pass              0.722             53.9                           0.691                4.73              0.337                                 ok            True                  False
  PANW           80.95               42            0.51              1.42        401.09                57.54         0.523            pass              0.478             66.8                           0.570                6.57              1.153                                 ok            True                  False
  MCHP           88.89               18            2.38              1.33         79.60                42.57         0.510            pass              0.349              2.6                           0.097                9.85              0.755                                 ok            True                  False
  MSFT           96.30               27            0.66              2.47        530.27                19.65         0.500 below_threshold              0.575              3.8                           0.114               -1.10             -0.137                                 ok            True                  False
  TMUS           80.00               25            0.93              0.96        146.42                63.84         0.664            pass              0.362             65.2                           0.560               -7.81             -0.940            downtrend_blocked_slope           False                  False
   CEG           88.57               35            0.79              1.43        258.37                65.80         0.601            pass              0.620             55.0                           0.413               -8.08             -0.880 downtrend_blocked_slope_and_streak           False                  False
  PAYX           62.50                8            1.32              1.01        108.83                35.39         0.583            pass              0.093             11.7                           0.168                0.51              0.299                                 ok           False                  False
 CMCSA           88.89                9            1.21              0.19         21.76                26.07         0.580            pass              0.311              5.4                           0.177                2.49              0.226                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-10-28T10:55:05.346290-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:50:05.367637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:45:06.466134-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:40:05.198297-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "CTAS261218C00200000", "current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "entry_ask": 19.2, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.25, "hypothetical_budget": 34382.15, "hypothetical_contracts": 18, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 648.0, "option_spread_pct": 10.41, "option_volume": 28.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "matched_signals": 34, "recovery_stability_score": 0.584, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.685, "early_reclaim_pct": 69.8, "matched_signals": 32, "recovery_stability_score": 0.566, "success_rate": 90.62, "ticker": "AEP", "timing_score": 0.456, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:35:05.723103-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:30:04.740302-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "entry_ask": 8.1, "entry_bid": 7.1, "entry_mode": "early", "entry_option_price": 7.6, "hypothetical_budget": 34382.15, "hypothetical_contracts": 45, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 817.0, "option_spread_pct": 13.16, "option_volume": 99.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "matched_signals": 34, "recovery_stability_score": 0.701, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:25:04.451776-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:20:06.172690-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                             {"contract_symbol": "MCHP261127C00079000", "current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "entry_ask": 6.0, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34382.15, "hypothetical_contracts": 62, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 18.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "matched_signals": 35, "recovery_stability_score": 0.759, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T10:15:06.401001-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:10:05.977135-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                            {"contract_symbol": "MCHP261127C00079000", "current_drop_pct": 0.92, "early_entry_score": 0.707, "early_reclaim_pct": 62.1, "entry_ask": 6.3, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.55, "hypothetical_budget": 34382.15, "hypothetical_contracts": 61, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 27.03, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.723, "shadow_only": true, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.707, "early_reclaim_pct": 62.1, "matched_signals": 35, "recovery_stability_score": 0.723, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028105505)

</details>

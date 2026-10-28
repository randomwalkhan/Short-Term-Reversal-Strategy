# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 11:05:04 EDT`
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
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 64480.0         20.0          20.15       220.6        220.33          bid_ask_mid                      20.15                bid_ask_mid                    True           480.0                   0.75         100.0               12              3.08          70.9           73.04                  47.89                 302.0           39.0                0.1                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.51              0.22         62.26                25.51         0.601          pass              0.637             56.8                           0.533               -0.86             -0.089                                 ok            True                  False
  MSTR           91.43               35            1.10              1.09        140.93                70.33         0.594          pass              0.624             31.2                           0.264               -2.37             -0.148                                 ok            True                  False
   KHC           89.66               29            0.60              0.10         24.02                36.33         0.549          pass              0.589             50.0                           0.518                5.35              0.646                                 ok            True                  False
   KDP           96.15               26            0.50              0.12         34.81                24.92         0.532          pass              0.722             53.9                           0.670                4.73              0.337                                 ok            True                  False
   PEP           80.00               25            0.64              0.60        133.24                25.80         0.522          pass              0.297             48.4                           0.675                2.61              0.402                                 ok            True                  False
  PANW           80.95               42            0.55              1.53        401.04                57.54         0.520          pass              0.470             64.2                           0.476                6.52              1.151                                 ok            True                  False
  CRWD           86.36               44            0.60              1.12        267.54                57.68         0.512          pass              0.480             19.6                           0.213                6.87              1.282                                 ok            True                  False
  MCHP           89.47               19            2.32              1.30         79.61                42.57         0.507          pass              0.392              9.7                           0.177                9.91              0.757                                 ok            True                  False
  MSFT           96.43               28            0.55              2.03        530.46                19.65         0.500          pass              0.633             20.8                           0.262               -0.99             -0.132                                 ok            True                  False
  TMUS           82.14               28            0.70              0.72        146.52                63.84         0.662          pass              0.465             73.9                           0.728               -7.60             -0.929            downtrend_blocked_slope           False                  False
   CEG           85.71               42            0.24              0.43        258.80                65.80         0.589          pass              0.671             86.4                           0.727               -7.57             -0.854 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           87.50                8            1.35              0.21         21.75                26.07         0.575          pass              0.281              7.8                           0.237                2.35              0.220                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-10-28T11:05:04.307484-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                          {"contract_symbol": "ALNY261218C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "entry_ask": 18.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.6, "hypothetical_budget": 34382.15, "hypothetical_contracts": 20, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 69.0, "option_spread_pct": 19.28, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.713, "early_reclaim_pct": 81.0, "matched_signals": 43, "recovery_stability_score": 0.788, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T11:00:05.505760-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:55:05.346290-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:50:05.367637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:45:06.466134-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:40:05.198297-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "CTAS261218C00200000", "current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "entry_ask": 19.2, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.25, "hypothetical_budget": 34382.15, "hypothetical_contracts": 18, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 648.0, "option_spread_pct": 10.41, "option_volume": 28.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "matched_signals": 34, "recovery_stability_score": 0.584, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.685, "early_reclaim_pct": 69.8, "matched_signals": 32, "recovery_stability_score": 0.566, "success_rate": 90.62, "ticker": "AEP", "timing_score": 0.456, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:35:05.723103-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:30:04.740302-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "entry_ask": 8.1, "entry_bid": 7.1, "entry_mode": "early", "entry_option_price": 7.6, "hypothetical_budget": 34382.15, "hypothetical_contracts": 45, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 817.0, "option_spread_pct": 13.16, "option_volume": 99.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "matched_signals": 34, "recovery_stability_score": 0.701, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:25:04.451776-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:20:06.172690-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                             {"contract_symbol": "MCHP261127C00079000", "current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "entry_ask": 6.0, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34382.15, "hypothetical_contracts": 62, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 18.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "matched_signals": 35, "recovery_stability_score": 0.759, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028110504)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-28 11:00:05 EDT`
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
  TEAM     option         option TEAM261218C00230000       2026-10-26                   2     32     64000.0                 64480.0         20.0          20.15       220.6         221.5          bid_ask_mid                      20.15                bid_ask_mid                    True           480.0                   0.75         100.0               12              3.08          70.9           71.81                  47.89                 302.0           39.0                0.1                      ok
```

## Today's Closed Trades (2026-10-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            0.61              0.27         62.24                25.51         0.611          pass              0.553             47.9                           0.404               -0.96             -0.094                                 ok            True                  False
  MSTR           91.18               34            1.19              1.18        140.90                70.33         0.595          pass              0.594             25.7                           0.219               -2.46             -0.152                                 ok            True                  False
   KHC           89.66               29            0.62              0.11         24.01                36.33         0.548          pass              0.584             48.3                           0.545                5.33              0.645                                 ok            True                  False
   KDP           96.15               26            0.50              0.12         34.81                24.92         0.532          pass              0.722             53.9                           0.705                4.73              0.337                                 ok            True                  False
  MCHP           88.89               18            2.39              1.34         79.59                42.57         0.508          pass              0.359              5.9                           0.176                9.82              0.754                                 ok            True                  False
  TMUS           80.00               25            0.94              0.97        146.42                63.84         0.664          pass              0.361             65.0                           0.562               -7.82             -0.940            downtrend_blocked_slope           False                  False
   CEG           88.57               35            0.81              1.46        258.35                65.80         0.600          pass              0.617             54.0                           0.424               -8.10             -0.880 downtrend_blocked_slope_and_streak           False                  False
  MPWR           65.22               23            1.55             13.11       1206.27                59.51         0.574          pass              0.199             18.4                           0.225               -4.02             -0.630            downtrend_blocked_slope           False                  False
 CMCSA           87.50                8            1.44              0.22         21.75                26.07         0.570          pass              0.257              0.0                           0.207                2.26              0.215                                 ok           False                  False
  PAYX           50.00                6            1.64              1.25        108.72                35.39         0.563          pass              0.056              0.0                           0.152                0.18              0.285                                 ok           False                  False
   STX           75.00               40            0.49              2.29        666.87                75.21         0.550          pass              0.534             92.9                           0.866               -6.86             -0.555                                 ok           False                  False
   ADP          100.00                3            2.52              5.17        290.90                27.84         0.548          pass              0.531             25.5                           0.230                1.93              0.445                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-10-28T11:00:05.505760-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:55:05.346290-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:50:05.367637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:45:06.466134-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:40:05.198297-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "CTAS261218C00200000", "current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "entry_ask": 19.2, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.25, "hypothetical_budget": 34382.15, "hypothetical_contracts": 18, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 648.0, "option_spread_pct": 10.41, "option_volume": 28.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.806, "early_reclaim_pct": 66.6, "matched_signals": 34, "recovery_stability_score": 0.584, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.459, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.685, "early_reclaim_pct": 69.8, "matched_signals": 32, "recovery_stability_score": 0.566, "success_rate": 90.62, "ticker": "AEP", "timing_score": 0.456, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:35:05.723103-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:30:04.740302-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "entry_ask": 8.1, "entry_bid": 7.1, "entry_mode": "early", "entry_option_price": 7.6, "hypothetical_budget": 34382.15, "hypothetical_contracts": 45, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 817.0, "option_spread_pct": 13.16, "option_volume": 99.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.767, "early_reclaim_pct": 60.1, "matched_signals": 34, "recovery_stability_score": 0.701, "success_rate": 94.12, "ticker": "MCHP", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-28T10:25:04.451776-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-28T10:20:06.172690-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                             {"contract_symbol": "MCHP261127C00079000", "current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "entry_ask": 6.0, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34382.15, "hypothetical_contracts": 62, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 18.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.705, "early_reclaim_pct": 61.4, "matched_signals": 35, "recovery_stability_score": 0.759, "success_rate": 91.43, "ticker": "MCHP", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-28T10:15:06.401001-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261028110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261028110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261028110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261028110005)

</details>

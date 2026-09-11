# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 09:30:03 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$35,166.10`
- Equity: `$69,606.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$-135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00130000       2026-09-10                   1     30     34575.0                 34440.0        11.52          11.48      129.47        130.71     last_price_stale                        NaN                unavailable                   False          -135.0                  -0.39          80.0               30              2.43          70.7             0.0                 104.12               13089.0          181.0               0.03                      ok
```

## Today's Closed Trades (2026-09-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.13               46            0.24              0.35        208.71                89.85         0.667              pass              0.665             51.5                           0.354               -8.60             -0.861            downtrend_blocked_slope           False                  False
  AMGN          100.00                1            2.25              6.16        388.63                44.93         0.655              pass              0.495              9.8                           0.247              -12.48             -1.517 downtrend_blocked_slope_and_streak           False                  False
  ADSK           86.67               30            1.04              1.54        210.95                52.16         0.534              pass              0.364              0.0                           0.230              -22.61             -2.910 downtrend_blocked_slope_and_streak           False                  False
  CTSH           94.87               39            0.03              0.01         58.32                38.70         0.522              pass              0.933             96.9                           0.511               -8.56             -1.149            downtrend_blocked_slope           False                  False
  ADBE           94.12               17            2.67              4.66        246.84                48.95         0.508              pass              0.598             41.3                           0.436              -16.24             -1.997 downtrend_blocked_slope_and_streak           False                  False
  FTNT           91.49               47            0.37              0.42        158.67                53.57         0.473   below_threshold              0.807             84.5                           0.457               -8.41             -0.827            downtrend_blocked_slope           False                  False
   LIN           82.35               34            0.08              0.27        461.50                14.54         0.463   below_threshold              0.443             58.1                           0.409               -4.66             -0.620 downtrend_blocked_slope_and_streak           False                  False
  AAPL             NaN                0            0.00              0.00        327.47                23.35           NaN no_signal_history                NaN              NaN                           0.668                4.10              0.182                                 ok           False                  False
  ABNB             NaN                0            0.00              0.00        169.99                32.53           NaN no_signal_history                NaN              NaN                           0.484               -7.81             -1.112 downtrend_blocked_slope_and_streak           False                  False
   ADI             NaN                0            0.00              0.00        363.06                22.82           NaN no_signal_history                NaN              NaN                           0.548               -2.76             -0.031                                 ok           False                  False
   ADP             NaN                0            0.00              0.00        267.33                25.58           NaN no_signal_history                NaN              NaN                           0.736               -6.09             -0.871            downtrend_blocked_slope           False                  False
   AEP             NaN                0            0.00              0.00        125.39                16.66           NaN no_signal_history                NaN              NaN                           0.380                2.18              0.225                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 93}
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T15:00:04.389376-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T14:55:01.338809-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-10T14:50:04.321187-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 34575.0, "asset_type": "option", "contract_symbol": "MSTR261016C00130000", "contracts": 30, "early_entry_score": 0.329, "entry_mode": "regular", "entry_option_price": 11.525, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 13089.0, "option_spread_pct": 3.04, "option_volume": 181.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.627}
2026-09-10T14:50:04.321187-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-10", "training_samples": 5765, "window": 5}
2026-09-10T12:00:03.311742-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:55:04.274439-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "entry_ask": 5.8, "entry_bid": 4.7, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 20.95, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "matched_signals": 37, "recovery_stability_score": 0.651, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:50:01.152194-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "entry_ask": 5.7, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 17.14, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "matched_signals": 41, "recovery_stability_score": 0.674, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.576, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911093003)

</details>

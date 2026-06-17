# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 09:50:02 EDT`
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

- Cash: `$13,363.25`
- Equity: `$24,838.25`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$-1,147.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 11475.0         7.43           6.75       68.52          70.5     last_price_stale                        NaN                unavailable                   False         -1147.5                  -9.09         90.91               11              3.59         94.78             0.0                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           83.33               24            0.88              0.74        120.71                34.81         0.571          pass              0.343             34.6                           0.288                6.11              0.501                                 ok            True                  False
   WBD           95.45               22            0.51              0.09         26.56                17.02         0.542          pass              0.605             23.6                           0.327               -2.63             -0.120                                 ok            True                  False
  MDLZ           95.65               23            0.87              0.38         61.99                20.23         0.532          pass              0.605             21.7                           0.244                0.88              0.230                                 ok            True                  False
  GOOG           81.25               16            1.66              4.31        369.25                27.92         0.526          pass              0.133              2.3                           0.089                2.67              0.087                                 ok            True                  False
   LIN           96.15               26            0.70              2.53        517.08                19.32         0.522          pass              0.698             46.4                           0.453                4.09              0.417                                 ok            True                  False
 GOOGL           80.00               15            1.65              4.30        371.41                28.01         0.504          pass              0.091              2.5                           0.094                1.51              0.012                                 ok            True                  False
    ZS           78.57               42            0.28              0.25        127.12               152.67         0.877          pass              0.552             88.1                           0.697               -5.57             -0.540 downtrend_blocked_slope_and_streak           False                  False
  INTU           78.05               41            0.49              0.96        280.58                99.11         0.721          pass              0.515             81.0                           0.642              -13.20             -1.461 downtrend_blocked_slope_and_streak           False                  False
   KHC           87.50                8            0.27              0.05         23.78                25.54         0.699          pass              0.495             75.0                           0.645                6.17              0.843                                 ok           False                  False
  MPWR           94.12               34            0.16              1.68       1498.05                71.82         0.696          pass              0.733             42.2                           0.312               -7.92             -0.523            downtrend_blocked_slope           False                  False
   PEP          100.00                6            1.13              1.15        145.63                20.43         0.648          pass              0.477              4.1                           0.159                2.81              0.394                                 ok           False                  False
   CSX           87.50                8            1.18              0.39         46.73                20.12         0.616          pass              0.291              9.8                           0.144                0.44              0.193                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-06-16T15:10:02.062608-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T15:05:05.056304-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T15:00:03.019624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T14:55:06.031514-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T14:50:02.059942-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"allocated_cash": 12622.5, "asset_type": "option", "contract_symbol": "DRAM260717C00069000", "contracts": 17, "early_entry_score": 0.434, "entry_mode": "regular", "entry_option_price": 7.425, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 846.0, "option_spread_pct": 6.06, "option_volume": 111.0, "success_rate": 90.91, "ticker": "DRAM", "timing_score": 0.657}
2026-06-16T14:50:02.059942-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-16", "training_samples": 5231, "window": 5}
2026-06-16T11:52:05.052043-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T11:10:06.057140-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T10:36:17.030970-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "MAR260717C00400000", "current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "entry_ask": 13.9, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 12992.88, "hypothetical_contracts": 10, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 400.0, "option_spread_pct": 18.9, "option_volume": 13.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "matched_signals": 32, "recovery_stability_score": 0.854, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-16T10:36:17.030970-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "ROST260717C00240000", "fill_price": 5.175, "pnl": -1322.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ROST"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617095002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617095002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617095002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617095002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:10:05 EDT`
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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           93.33               30            1.13              0.80        100.97                57.96         0.583            pass              0.633             28.7                           0.288               -5.38             -0.561 downtrend_blocked_slope_and_streak           False                  False
   WMT           85.71               35            0.37              0.28        107.38                39.87         0.546            pass              0.529             51.8                           0.566                0.95              0.099                                 ok           False                  False
  ADSK           84.85               33            0.73              1.12        219.83                56.33         0.546            pass              0.504             55.5                           0.499               -9.53             -0.460 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.48               42            0.52              0.49        134.79                64.77         0.531            pass              0.632             33.3                           0.263              -15.52             -1.337 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.21              0.06         42.41                15.25         0.524            pass              0.625             30.8                           0.227               -2.77             -0.422 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.88               32            0.96              1.69        249.78                47.92         0.523            pass              0.757             52.7                           0.520              -11.33             -1.068 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               20            0.27              0.26        134.23                14.34         0.517            pass              0.452             22.3                           0.196               -3.64             -0.353            downtrend_blocked_slope           False                  False
  INTU          100.00               32            0.83              1.85        317.34                44.10         0.515            pass              0.714             38.5                           0.279               -8.01             -0.561 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.30               27            0.47              0.90        272.81                24.48         0.514            pass              0.777             70.9                           0.672               -2.67             -0.143                                 ok           False                  False
  VRSK           93.10               29            1.14              1.45        181.13                41.00         0.508            pass              0.588             20.5                           0.224               -4.25             -0.332            downtrend_blocked_slope           False                  False
  CTSH          100.00               37            0.49              0.21         61.76                43.69         0.500 below_threshold              0.820             63.4                           0.419               -2.92             -0.103                                 ok           False                  False
 CMCSA           89.47               19            1.60              0.27         23.62                34.54         0.495 below_threshold              0.377              5.0                           0.137              -12.91             -1.353 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-09-16T15:35:01.538068-04:00      manage_1530               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "PYPL261016C00055000", "fill_price": 1.116, "pnl": -3434.8, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T15:05:01.537613-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T15:00:06.128176-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T14:55:02.603343-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-16T14:50:31.812161-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-16", "training_samples": 5761, "window": 5}
2026-09-16T14:50:31.812161-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 34348.0, "asset_type": "option", "contract_symbol": "PYPL261016C00055000", "contracts": 277, "early_entry_score": 0.302, "entry_mode": "regular", "entry_option_price": 1.24, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 7856.0, "option_spread_pct": 11.29, "option_volume": 1919.0, "success_rate": 86.67, "ticker": "PYPL", "timing_score": 0.657}
2026-09-16T11:50:05.471536-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "entry_ask": 14.9, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.07, "option_volume": 90.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.719, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "matched_signals": 31, "recovery_stability_score": 0.719, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917101005)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 10:10:06 EDT`
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

- Cash: `$128,734.80`
- Equity: `$128,734.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           84.38               32            0.56              2.90        736.30                55.15         0.581            pass              0.565             81.1                           0.770                1.03              0.175                                 ok            True                  False
  MSTR           86.67               30            1.89              1.90        142.43                78.69         0.560            pass              0.570             67.5                           0.759              -12.44             -1.348 downtrend_blocked_slope_and_streak           False                  False
  SNPS           71.43                7            2.96              9.95        475.67                52.37         0.554            pass              0.188             44.1                           0.615               -5.06             -0.274 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50                8            3.10              6.07        276.94                59.82         0.551            pass              0.337             27.4                           0.464                4.62              0.732                                 ok           False                  False
  MPWR           82.61               23            1.82             15.84       1236.32                56.61         0.536            pass              0.369             53.0                           0.478              -10.32             -1.569            downtrend_blocked_slope           False                  False
  CDNS           80.00               20            1.53              3.54        327.94                37.41         0.504            pass              0.305             62.7                           0.662               -7.51             -0.807 downtrend_blocked_slope_and_streak           False                  False
  AVGO           80.00               10            2.54              6.16        343.61                35.83         0.497 below_threshold              0.123             24.4                           0.444               -1.80             -0.356            downtrend_blocked_slope           False                  False
  CRWD           85.00               20            2.26              3.95        247.60                48.36         0.493 below_threshold              0.362             37.5                           0.430               -8.44             -0.882 downtrend_blocked_slope_and_streak           False                  False
  UPRO           86.21               29            0.74              0.78        150.03                30.64         0.485 below_threshold              0.532             63.7                           0.624                1.02              0.052                                 ok           False                  False
   AEP           75.00               16            0.92              0.81        125.78                12.92         0.479 below_threshold              0.151             21.0                           0.238                4.36              0.563                                 ok           False                  False
   XEL           87.10               31            0.19              0.10         75.32                17.56         0.473 below_threshold              0.467             30.0                           0.173                6.62              0.658                                 ok           False                  False
   ADI           88.46               26            0.82              2.31        402.58                27.65         0.472 below_threshold              0.574             64.9                           0.358               -1.07             -0.270                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-15T10:10:06.336303-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:05:05.165659-04:00 early_entry_1005 early_entry_shadow               {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "entry_ask": 17.4, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 2833.0, "option_spread_pct": 14.48, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "matched_signals": 37, "recovery_stability_score": 0.643, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:00:06.074428-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00217500", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "entry_ask": 17.75, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 16.325, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 17.46, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.617, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T09:50:06.230467-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 5.265, "pnl": -6727.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSCO"}
2026-10-15T00:00:06.592550-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-10-14T15:10:06.171047-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T15:05:05.885010-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T15:00:05.913118-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T14:55:05.778063-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T14:50:04.996677-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-14", "training_samples": 6059, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015101006)

</details>

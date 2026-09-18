# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 15:05:05 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           91.67               12            1.05              0.18         24.65                21.70         0.535          pass              0.544             55.2                           0.437               -2.20             -0.133                                 ok            True                  False
  CTSH          100.00               10            3.01              1.30         61.32                39.55         0.522          pass              0.486             11.4                           0.345               -7.15             -0.038                                 ok            True                  False
  CRWD           78.26               23            2.32              3.98        243.99                97.92         0.645          pass              0.293             47.3                           0.578               11.65              1.787                                 ok           False                  False
  PYPL           93.10               29            0.80              0.30         52.81                57.74         0.624          pass              0.654             38.4                           0.372               -7.35             -0.439            downtrend_blocked_slope           False                  False
  MRVL           78.95               38            1.01              1.70        240.03                74.50         0.571          pass              0.392             49.4                           0.528               14.13              0.783                                 ok           False                  False
   EXC          100.00                9            1.04              0.31         42.51                15.46         0.556          pass              0.529             24.6                           0.454               -4.34             -0.459 downtrend_blocked_slope_and_streak           False                  False
  ADSK           87.80               41            0.26              0.40        218.47                55.63         0.542          pass              0.696             77.8                           0.734               -8.19             -0.035           downtrend_blocked_streak           False                  False
  PANW           60.00               15            3.27              8.58        371.38                79.31         0.540          pass              0.195             35.7                           0.389                9.30              1.426                                 ok           False                  False
   AEP           77.78                9            1.12              0.96        121.21                17.28         0.530          pass              0.116             21.1                           0.338               -3.57             -0.425 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.97               33            1.02              1.80        251.90                46.08         0.522          pass              0.764             52.9                           0.624              -12.48             -0.792 downtrend_blocked_slope_and_streak           False                  False
  CHTR           84.21               19            3.03              2.83        132.16                63.68         0.509          pass              0.274             16.9                           0.319              -14.57             -1.285 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.88               32            0.14              0.27        272.12                22.18         0.504          pass              0.870             90.9                           0.730               -3.50             -0.016           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.508, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.515}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
2026-09-18T14:50:01.910301-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-18", "training_samples": 5785, "window": 5}
2026-09-18T12:00:05.801546-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:55:06.730103-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:50:03.921219-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "entry_ask": 14.2, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.525, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 9.98, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "matched_signals": 39, "recovery_stability_score": 0.586, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918150505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918150505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918150505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918150505)

</details>

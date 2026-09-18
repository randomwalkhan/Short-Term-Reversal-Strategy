# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 11:15:06 EDT`
Last processed slot: `early_entry_1115`

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
   KHC           93.33               15            0.67              0.12         24.68                21.70         0.543          pass              0.658             71.6                           0.806               -1.82             -0.115                                 ok            True                  False
  CTSH          100.00               16            2.41              1.04         61.43                39.55         0.523          pass              0.533             13.6                           0.360               -6.57             -0.010                                 ok            True                  False
  FTNT           83.33               12            2.94              3.56        171.06                57.60         0.519          pass              0.219             21.7                           0.509                7.12              1.140                                 ok            True                  False
  CRWD           75.00               16            3.28              5.64        243.28                97.92         0.628          pass              0.179             25.5                           0.545               10.55              1.742                                 ok           False                  False
    ZS           97.67               43            0.40              0.55        197.23                82.85         0.624          pass              0.913             83.6                           0.887               10.62              1.892                                 ok           False                  False
  PYPL           91.43               35            0.38              0.14         52.88                57.74         0.613          pass              0.746             71.0                           0.610               -6.95             -0.419            downtrend_blocked_slope           False                  False
  MRVL           78.95               38            0.95              1.60        240.07                74.50         0.582          pass              0.305             20.2                           0.279               14.19              0.785                                 ok           False                  False
   EXC          100.00                9            1.04              0.31         42.51                15.46         0.557          pass              0.523             22.5                           0.383               -4.33             -0.459 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.88              1.34        218.06                55.63         0.554          pass              0.395             25.3                           0.329               -8.76             -0.064           downtrend_blocked_streak           False                  False
   TRI           90.91               11            3.36              2.34         98.48                55.72         0.548          pass              0.361              2.9                           0.237              -13.98             -0.642 downtrend_blocked_slope_and_streak           False                  False
  PANW           62.50                8            4.27             11.22        370.25                79.31         0.528          pass              0.100             15.9                           0.383                8.16              1.378                                 ok           False                  False
  ADBE           96.97               33            0.99              1.75        251.92                46.08         0.524          pass              0.768             54.1                           0.675              -12.45             -0.791 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-18T11:15:06.591225-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:10:04.781289-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "entry_ask": 13.95, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 13.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 10.96, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.817, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "matched_signals": 39, "recovery_stability_score": 0.817, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:05:05.479852-04:00 early_entry_1105 early_entry_shadow  {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "entry_ask": 13.95, "entry_bid": 12.45, "entry_mode": "early", "entry_option_price": 13.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 11.36, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:00:06.440780-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:55:06.922976-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:50:04.964114-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:45:06.500204-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:40:04.793356-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:35:06.106609-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:30:04.878508-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918111506)

</details>

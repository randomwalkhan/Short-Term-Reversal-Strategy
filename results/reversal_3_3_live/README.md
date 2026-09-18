# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 11:10:04 EDT`
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
    ZS           97.44               39            0.57              0.79        197.13                82.85         0.637          pass              0.887             76.6                           0.817               10.43              1.884                                 ok            True                   True
  MRVL           80.00               40            0.64              1.07        240.30                74.50         0.589          pass              0.398             46.5                           0.425               14.55              0.800                                 ok            True                  False
   KHC           92.86               14            0.79              0.14         24.67                21.70         0.541          pass              0.623             66.4                           0.794               -1.94             -0.121                                 ok            True                  False
  CTSH          100.00               15            2.46              1.06         61.42                39.55         0.527          pass              0.522             11.9                           0.301               -6.62             -0.012                                 ok            True                  False
  FTNT           83.33               12            2.87              3.46        171.10                57.60         0.523          pass              0.226             23.7                           0.504                7.21              1.144                                 ok            True                  False
   WBD           83.33               12            1.06              0.21         28.15                10.21         0.501          pass              0.188             11.8                           0.123               -1.52             -0.071                                 ok            True                  False
  CRWD           77.78               18            3.13              5.38        243.39                97.92         0.629          pass              0.203             28.8                           0.561               10.72              1.749                                 ok           False                  False
  PYPL           91.43               35            0.43              0.16         52.87                57.74         0.610          pass              0.732             66.7                           0.620               -7.00             -0.422            downtrend_blocked_slope           False                  False
   EXC          100.00                6            1.17              0.35         42.49                15.46         0.566          pass              0.493             12.3                           0.297               -4.47             -0.465 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.24               41            0.00              0.00        219.34                45.58         0.564          pass              0.830            100.0                           0.661               -3.88             -0.623           downtrend_blocked_streak           False                  False
   TRI           90.91               11            3.13              2.18         98.55                55.72         0.562          pass              0.371              5.6                           0.209              -13.78             -0.632 downtrend_blocked_slope_and_streak           False                  False
  ADSK           83.87               31            1.07              1.63        217.94                55.63         0.547          pass              0.326              9.3                           0.243               -8.93             -0.072           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-18T11:10:04.781289-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "entry_ask": 13.95, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 13.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 10.96, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.817, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "matched_signals": 39, "recovery_stability_score": 0.817, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:05:05.479852-04:00 early_entry_1105 early_entry_shadow  {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "entry_ask": 13.95, "entry_bid": 12.45, "entry_mode": "early", "entry_option_price": 13.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 11.36, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:00:06.440780-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:55:06.922976-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:50:04.964114-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:45:06.500204-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:40:04.793356-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:35:06.106609-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:30:04.878508-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:25:05.756600-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918111004)

</details>

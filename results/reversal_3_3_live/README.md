# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 12:15:06 EDT`
Last processed slot: `manual`

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
   KHC           93.33               15            0.57              0.10         24.69                21.70         0.549          pass              0.671             75.9                           0.616               -1.72             -0.111                                 ok            True                  False
  FTNT           86.67               15            2.72              3.29        171.17                57.60         0.518          pass              0.346             27.6                           0.368                7.37              1.151                                 ok            True                  False
  CTSH          100.00               14            2.73              1.18         61.37                39.55         0.516          pass              0.495              5.6                           0.108               -6.88             -0.025                                 ok            True                  False
   WBD           83.33               12            1.04              0.21         28.15                10.21         0.502          pass              0.192             13.2                           0.225               -1.50             -0.070                                 ok            True                  False
  CRWD           77.78               18            3.06              5.26        243.44                97.92         0.632          pass              0.208             30.4                           0.422               10.80              1.752                                 ok           False                  False
    ZS           97.67               43            0.33              0.45        197.28                82.85         0.628          pass              0.922             86.5                           0.776               10.70              1.896                                 ok           False                  False
  PYPL           91.43               35            0.42              0.15         52.87                57.74         0.611          pass              0.737             68.1                           0.595               -6.99             -0.421            downtrend_blocked_slope           False                  False
   EXC          100.00                6            1.20              0.36         42.49                15.46         0.565          pass              0.497             13.6                           0.270               -4.49             -0.466 downtrend_blocked_slope_and_streak           False                  False
  MRVL           77.14               35            1.56              2.63        239.63                74.50         0.557          pass              0.245              7.6                           0.242               13.49              0.757                                 ok           False                  False
  ADSK           85.71               35            0.63              0.96        218.23                55.63         0.553          pass              0.514             46.7                           0.434               -8.53             -0.052           downtrend_blocked_streak           False                  False
   TRI           88.89                9            3.52              2.45         98.43                55.72         0.547          pass              0.297              1.6                           0.221              -14.12             -0.650 downtrend_blocked_slope_and_streak           False                  False
   AEP           77.78                9            1.09              0.92        121.22                17.28         0.532          pass              0.124             23.7                           0.303               -3.54             -0.423 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-18T12:00:05.801546-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:55:06.730103-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:50:03.921219-04:00 early_entry_1150 early_entry_shadow  {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "entry_ask": 14.2, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.525, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 9.98, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "matched_signals": 39, "recovery_stability_score": 0.586, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:45:06.412302-04:00 early_entry_1145 early_entry_shadow    {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 78.6, "entry_ask": 14.2, "entry_bid": 12.8, "entry_mode": "early", "entry_option_price": 13.5, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 10.37, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 78.6, "matched_signals": 39, "recovery_stability_score": 0.633, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:40:04.871951-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.67, "early_entry_score": 0.874, "early_reclaim_pct": 72.5, "entry_ask": 14.2, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.425, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 11.55, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.631, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.874, "early_reclaim_pct": 72.5, "matched_signals": 39, "recovery_stability_score": 0.659, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.631, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:35:05.972190-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.893, "early_reclaim_pct": 78.4, "entry_ask": 14.2, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.425, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 11.55, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.757, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.893, "early_reclaim_pct": 78.4, "matched_signals": 39, "recovery_stability_score": 0.757, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:30:04.777867-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:25:04.772895-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:20:06.499852-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:15:06.591225-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918121506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918121506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918121506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918121506)

</details>

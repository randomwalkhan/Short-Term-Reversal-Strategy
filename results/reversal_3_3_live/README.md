# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-06 11:40:04 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$16,083.25`
- Equity: `$33,820.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$1,980.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   1     55     15757.5                 17737.5         2.86           3.22       58.15         58.98          bid_ask_mid                       3.22                bid_ask_mid                    True          1980.0                  12.57         91.18               34              0.66         31.86           31.96                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           96.55               29            0.86              2.37        393.51                46.42         0.590          pass              0.674             29.5                           0.279               10.14              0.796                                 ok            True                  False
  MNST           88.24               17            0.91              0.60         94.20                25.70         0.570          pass              0.392             23.0                           0.193                0.05             -0.081                                 ok            True                  False
  WDAY           83.33               30            1.86              2.22        169.68                67.74         0.520          pass              0.468             64.7                           0.655               30.96              2.493                                 ok            True                  False
  AMGN          100.00               17            1.35              3.84        406.18                30.87         0.511          pass              0.534             12.2                           0.224                8.30              0.683                                 ok            True                  False
   PEP           83.33               24            0.79              0.77        138.45                25.05         0.511          pass              0.331             32.5                           0.312                2.02              0.067                                 ok            True                  False
  ADSK           83.33               36            0.61              1.03        239.59                45.93         0.509          pass              0.563             83.4                           0.726               16.22              1.244                                 ok            True                  False
  ALNY           86.21               29            1.25              2.00        227.86               127.65         0.823          pass              0.494             39.9                           0.466              -15.96             -2.864            downtrend_blocked_slope           False                  False
  ISRG           86.84               38            0.33              0.87        374.83                72.98         0.678          pass              0.630             64.3                           0.582               12.63              1.080                                 ok           False                  False
  GEHC           94.59               37            0.43              0.21         70.15                58.07         0.629          pass              0.745             37.5                           0.370               12.89              1.571                                 ok           False                  False
  DRAM           78.12               32            2.20              0.83         53.39               109.54         0.607          pass              0.436             76.2                           0.621               -9.85             -0.080           downtrend_blocked_streak           False                  False
  INTC           85.71               42            0.09              0.06        101.03                86.71         0.596          pass              0.707             98.4                           0.573                0.74              0.807                                 ok           False                  False
   MAR           94.74               19            1.22              3.08        359.99                38.12         0.580          pass              0.562             17.1                           0.257               -2.07             -0.712 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-06T11:40:04.059152-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:35:02.131091-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:30:05.087052-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:25:02.082331-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:20:02.141414-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:15:03.902464-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-06T11:10:04.141911-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                         {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "entry_ask": 32.9, "entry_bid": 31.7, "entry_mode": "early", "entry_option_price": 32.3, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 3.72, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.714, "early_reclaim_pct": 77.7, "matched_signals": 46, "recovery_stability_score": 0.657, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-06T11:05:02.141767-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "IDXX260918C00580000", "current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 67.4, "entry_ask": 29.2, "entry_bid": 23.1, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 8041.63, "hypothetical_contracts": 3, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 23.33, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.677, "shadow_only": true, "success_rate": 94.74, "ticker": "IDXX", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 67.4, "matched_signals": 38, "recovery_stability_score": 0.677, "success_rate": 94.74, "ticker": "IDXX", "timing_score": 0.425, "trend_health_status": "ok"}, {"current_drop_pct": 1.0, "early_entry_score": 0.714, "early_reclaim_pct": 78.0, "matched_signals": 46, "recovery_stability_score": 0.725, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.369, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-06T11:00:04.213482-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "PANW260918C00360000", "current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "entry_ask": 31.85, "entry_bid": 30.45, "entry_mode": "early", "entry_option_price": 31.15, "hypothetical_budget": 8041.63, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1808.0, "option_spread_pct": 4.49, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.767, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.719, "early_reclaim_pct": 79.4, "matched_signals": 46, "recovery_stability_score": 0.767, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-06T10:55:01.181311-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                   {"contract_symbol": "FTNT260918C00160000", "current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "entry_ask": 12.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.725, "hypothetical_budget": 8041.63, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1551.0, "option_spread_pct": 12.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "top_candidates": [{"current_drop_pct": 1.36, "early_entry_score": 0.737, "early_reclaim_pct": 63.5, "matched_signals": 38, "recovery_stability_score": 0.675, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.368, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260806114004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260806114004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260806114004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260806114004)

</details>

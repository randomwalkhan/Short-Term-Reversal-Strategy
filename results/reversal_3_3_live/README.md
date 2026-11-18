# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 11:20:05 EST`
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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           91.43               35            1.33              3.72        397.35               121.47         0.778          pass              0.635             28.6                           0.323               44.85              2.251                  ok            True                  False
   TXN           85.71               14            1.83              3.79        294.24                59.80         0.625          pass              0.242              0.0                           0.250               -6.76              0.151                  ok            True                  False
   BKR           85.71               28            0.80              0.27         47.35                58.51         0.619          pass              0.363              9.5                           0.119               -5.14             -0.042                  ok            True                  False
   ADI           90.00               30            1.08              2.90        382.43                67.50         0.613          pass              0.505             14.6                           0.205               -6.57              0.107                  ok            True                  False
  MDLZ           95.24               21            0.55              0.26         66.64                29.89         0.583          pass              0.719             62.6                           0.657               -1.48              0.020                  ok            True                  False
 CMCSA           91.67               24            0.73              0.13         25.25                34.73         0.564          pass              0.587             42.2                           0.305                1.11              0.284                  ok            True                  False
  REGN           83.78               37            0.66              4.40        955.87                53.86         0.561          pass              0.394             18.9                           0.169                2.23              0.559                  ok            True                  False
   WMT           80.00               15            1.12              1.00        127.09                25.55         0.554          pass              0.214             41.6                           0.356               -2.38             -0.014                  ok            True                  False
  COST           86.36               22            0.73              5.67       1107.65                22.66         0.541          pass              0.410             35.6                           0.333                5.30              0.624                  ok            True                  False
   ADP           86.96               23            1.07              2.31        307.30                28.72         0.535          pass              0.364             12.7                           0.116                0.48              0.179                  ok            True                  False
   CEG           90.91               33            1.41              2.64        266.94                61.66         0.528          pass              0.612             38.3                           0.283                7.72              1.119                  ok            True                  False
  META           80.77               26            1.30              5.65        616.45                41.87         0.526          pass              0.180              0.0                           0.231               -3.05             -0.012                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-18T11:20:05.157588-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:10:06.093723-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "entry_ask": 27.1, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 7.27, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "matched_signals": 44, "recovery_stability_score": 0.563, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:05:06.391620-05:00 early_entry_1105 early_entry_shadow                                          {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "entry_ask": 22.2, "entry_bid": 21.85, "entry_mode": "early", "entry_option_price": 22.025, "hypothetical_budget": 52959.4, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 1.59, "option_volume": 159.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "matched_signals": 32, "recovery_stability_score": 0.634, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.767, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.606, "success_rate": 91.89, "ticker": "CEG", "timing_score": 0.552, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T10:59:10.549422-05:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CEG261224C00265000", "current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "entry_ask": 19.0, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 52959.4, "hypothetical_contracts": 30, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 18.39, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "matched_signals": 38, "recovery_stability_score": 0.571, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.755, "early_reclaim_pct": 62.4, "matched_signals": 44, "recovery_stability_score": 0.576, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.765, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-18T10:59:10.549422-05:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "APP261218C00400000", "fill_price": 28.17, "pnl": -5321.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-18T00:00:06.344355-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118112005)

</details>

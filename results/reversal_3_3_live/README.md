# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 11:25:05 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               44            0.83              2.32        397.95               121.47         0.759          pass              0.733             55.5                           0.433               45.59              2.275                       ok            True                  False
   BKR           84.00               25            0.91              0.30         47.33                58.51         0.627          pass              0.335             21.8                           0.211               -5.24             -0.047                       ok            True                  False
   TXN           87.50               16            1.67              3.45        294.38                59.80         0.622          pass              0.356             18.0                           0.233               -6.60              0.158                       ok            True                  False
   ADI           90.00               30            1.07              2.88        382.44                67.50         0.612          pass              0.530             22.8                           0.285               -6.57              0.107                       ok            True                  False
  MDLZ           95.65               23            0.51              0.24         66.65                29.89         0.573          pass              0.741             65.7                           0.637               -1.44              0.022                       ok            True                  False
   ADP           87.50               24            0.85              1.84        307.50                28.72         0.543          pass              0.439             30.4                           0.206                0.70              0.188                       ok            True                  False
   CEG           90.91               33            1.23              2.31        267.08                61.66         0.539          pass              0.636             46.1                           0.318                7.92              1.127                       ok            True                  False
  COST           83.33               24            0.54              4.18       1108.29                22.66         0.537          pass              0.393             52.5                           0.450                5.51              0.633                       ok            True                  False
   WMT           85.00               20            1.00              0.89        127.14                25.55         0.535          pass              0.398             48.2                           0.394               -2.26             -0.008                       ok            True                  False
  META           82.14               28            0.97              4.22        617.06                41.87         0.535          pass              0.320             29.7                           0.279               -2.72              0.004                       ok            True                  False
  SOXL           61.54               26            3.10              1.06         48.61               265.73         0.922          pass              0.321             40.9                           0.292              -28.69             -0.502  downtrend_blocked_slope           False                  False
  INTC           66.67               27            2.37              0.92         54.78               143.31         0.802          pass              0.266             24.3                           0.260               -7.57             -0.144 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-18T11:25:05.812808-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:20:05.157588-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:10:06.093723-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "entry_ask": 27.1, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 7.27, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "matched_signals": 44, "recovery_stability_score": 0.563, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:05:06.391620-05:00 early_entry_1105 early_entry_shadow                                          {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "entry_ask": 22.2, "entry_bid": 21.85, "entry_mode": "early", "entry_option_price": 22.025, "hypothetical_budget": 52959.4, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 1.59, "option_volume": 159.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "matched_signals": 32, "recovery_stability_score": 0.634, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.767, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.606, "success_rate": 91.89, "ticker": "CEG", "timing_score": 0.552, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T10:59:10.549422-05:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CEG261224C00265000", "current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "entry_ask": 19.0, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 52959.4, "hypothetical_contracts": 30, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 18.39, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "matched_signals": 38, "recovery_stability_score": 0.571, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.755, "early_reclaim_pct": 62.4, "matched_signals": 44, "recovery_stability_score": 0.576, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.765, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-18T10:59:10.549422-05:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "APP261218C00400000", "fill_price": 28.17, "pnl": -5321.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-18T00:00:06.344355-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118112505)

</details>

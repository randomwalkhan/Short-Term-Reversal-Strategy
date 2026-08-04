# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 10:35:05 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$33,480.75`
- Equity: `$33,480.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-04)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00050000    106          2026-08-03         2026-08-04         1.65       1.485 -1749.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           94.74               19            0.78              0.34         61.59                32.17         0.602          pass              0.680             55.6                           0.639                2.32              0.395                      ok            True                  False
   ROP           92.00               25            1.20              3.30        391.16                47.45         0.576          pass              0.613             45.0                           0.373               10.60              1.467                      ok            True                  False
   PEP           85.00               20            0.91              0.89        139.25                26.13         0.559          pass              0.403             49.0                           0.535                2.49              0.379                      ok            True                  False
   EXC          100.00               18            0.83              0.27         45.52                21.77         0.555          pass              0.725             72.0                           0.658               -1.39             -0.312                      ok            True                  False
  DXCM           88.24               34            0.95              0.58         87.06                57.42         0.549          pass              0.508             24.5                           0.175               15.69              1.950                      ok            True                  False
  CTAS           92.59               27            0.90              1.29        203.46                37.98         0.530          pass              0.664             54.1                           0.474                0.88              0.137                      ok            True                  False
  PAYX          100.00               21            0.58              0.48        117.47                35.86         0.518          pass              0.802             92.2                           0.768                5.58              0.805                      ok            True                  False
  GILD           86.67               30            0.53              0.49        130.94                32.36         0.517          pass              0.532             56.5                           0.375                0.13              0.058                      ok            True                  False
  ALNY           83.33               24            1.75              2.70        219.17               126.96         0.813          pass              0.310             15.7                           0.219              -20.23             -2.939 downtrend_blocked_slope           False                  False
  ISRG           75.00               20            1.50              3.95        373.72                72.79         0.675          pass              0.250             38.5                           0.538                5.63              0.843                      ok           False                  False
  TMUS           89.66               29            0.84              1.04        176.64                55.96         0.622          pass              0.592             48.4                           0.637               -7.95             -0.662 downtrend_blocked_slope           False                  False
   KHC           92.00               25            0.13              0.02         26.41                32.72         0.619          pass              0.744             87.5                           0.741                2.31              0.317                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-04T10:35:05.771525-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:30:05.361830-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:25:01.416298-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.71, "early_entry_score": 0.756, "early_reclaim_pct": 63.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 93.75, "ticker": "CTAS", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.756, "early_reclaim_pct": 63.8, "matched_signals": 32, "recovery_stability_score": 0.577, "success_rate": 93.75, "ticker": "CTAS", "timing_score": 0.51, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.735, "early_reclaim_pct": 62.9, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.57, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:20:01.349464-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.53, "early_entry_score": 0.728, "early_reclaim_pct": 75.8, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.565, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.728, "early_reclaim_pct": 75.8, "matched_signals": 33, "recovery_stability_score": 0.659, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.565, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:15:05.517431-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:10:06.188010-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.5, "matched_signals": 30, "recovery_stability_score": 0.581, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:05:05.202403-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:05:05.202403-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.485, "pnl": -1749.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-04T10:00:02.269549-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T08:05:01.281633-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804103505)

</details>

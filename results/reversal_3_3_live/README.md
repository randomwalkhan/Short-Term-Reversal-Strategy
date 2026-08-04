# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 13:35:07 EDT`
Last processed slot: `manage_1330`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           93.33               30            0.93              2.56        391.47                47.45         0.562          pass              0.717             57.3                           0.527               10.90              1.480                                 ok            True                  False
   PEP           83.33               24            0.73              0.71        139.32                26.13         0.541          pass              0.414             59.2                           0.670                2.67              0.387                                 ok            True                  False
  CTSH           86.11               36            0.94              0.36         55.01                60.42         0.501          pass              0.592             68.5                           0.666               25.26              3.071                                 ok            True                  False
  ALNY           87.10               31            1.10              1.70        219.60               126.96         0.814          pass              0.568             52.5                           0.584              -19.70             -2.909            downtrend_blocked_slope           False                  False
  ISRG           69.23               13            2.41              6.34        372.69                72.79         0.651          pass              0.114              9.7                           0.205                4.66              0.801                                 ok           False                  False
  TMUS           88.24               34            0.43              0.53        176.86                55.96         0.614          pass              0.662             73.7                           0.677               -7.57             -0.643            downtrend_blocked_slope           False                  False
  AMZN           73.68               19            1.93              3.83        282.38                60.32         0.590          pass              0.245             41.9                           0.543               12.52              1.494                                 ok           False                  False
  DXCM           90.70               43            0.09              0.06         87.29                57.42         0.552          pass              0.819             92.7                           0.647               16.70              1.989                                 ok           False                  False
   MAR          100.00               31            0.60              1.45        346.21                34.81         0.541          pass              0.791             65.5                           0.741               -6.27             -0.465 downtrend_blocked_slope_and_streak           False                  False
  COST           70.59               17            1.02              6.83        951.15                24.00         0.523          pass              0.227             42.8                           0.617                1.79              0.327                                 ok           False                  False
  BKNG           92.50               40            0.24              0.33        192.57                44.49         0.519          pass              0.845             86.7                           0.587                7.16              1.128                                 ok           False                  False
  META           88.37               43            0.26              1.07        589.78                55.17         0.516          pass              0.744             89.7                           0.845               -8.56             -1.052 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-08-04T12:00:02.363319-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "matched_signals": 33, "recovery_stability_score": 0.74, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:55:01.364368-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.701, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:50:01.376014-04:00 early_entry_1150 early_entry_shadow               {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "entry_ask": 36.7, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.35, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 7.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.717, "early_reclaim_pct": 72.3, "matched_signals": 33, "recovery_stability_score": 0.747, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.56, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:45:01.424926-04:00 early_entry_1145 early_entry_shadow              {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "entry_ask": 37.4, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 9.52, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.752, "early_reclaim_pct": 68.4, "matched_signals": 30, "recovery_stability_score": 0.736, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.578, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:40:04.541695-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "entry_ask": 40.8, "entry_bid": 34.6, "entry_mode": "early", "entry_option_price": 37.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.741, "early_reclaim_pct": 64.9, "matched_signals": 30, "recovery_stability_score": 0.733, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:35:05.362040-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 30, "recovery_stability_score": 0.711, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:30:01.403472-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.585, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.585, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.3, "matched_signals": 30, "recovery_stability_score": 0.694, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:25:01.272769-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:20:01.453908-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:15:06.199893-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "matched_signals": 35, "recovery_stability_score": 0.657, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804133507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804133507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804133507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804133507)

</details>

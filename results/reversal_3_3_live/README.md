# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 10:40:01 EDT`
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
  GEHC           94.29               35            0.62              0.30         69.60                58.11         0.623          pass              0.778             56.1                           0.384               11.77              1.633                      ok            True                  False
  MDLZ           94.44               18            0.87              0.38         61.57                32.17         0.602          pass              0.649             50.0                           0.601                2.22              0.390                      ok            True                  False
   ROP           90.91               22            1.29              3.55        391.05                47.45         0.588          pass              0.552             40.8                           0.320               10.50              1.463                      ok            True                  False
   PEP           85.00               20            0.91              0.89        139.25                26.13         0.559          pass              0.404             49.4                           0.548                2.49              0.379                      ok            True                  False
   EXC          100.00               18            0.87              0.28         45.51                21.77         0.552          pass              0.721             70.9                           0.692               -1.43             -0.314                      ok            True                  False
  DXCM           88.89               36            0.81              0.50         87.10                57.42         0.546          pass              0.571             35.5                           0.226               15.85              1.956                      ok            True                  False
  CTAS           92.86               28            0.81              1.16        203.51                37.98         0.529          pass              0.692             58.7                           0.492                0.97              0.141                      ok            True                  False
  GILD           86.67               30            0.58              0.53        130.92                32.36         0.514          pass              0.522             53.1                           0.327                0.09              0.056                      ok            True                  False
  PAYX          100.00               23            0.52              0.43        117.49                35.86         0.509          pass              0.816             93.0                           0.780                5.64              0.808                      ok            True                  False
  ABNB           92.86               28            1.20              1.27        150.10                33.33         0.505          pass              0.528              4.7                           0.091                3.28              0.849                      ok            True                  False
  ALNY           76.47               17            2.07              3.19        218.96               126.96         0.820          pass              0.144              5.0                           0.168              -20.48             -2.954 downtrend_blocked_slope           False                  False
  ISRG           68.75               16            1.83              4.81        373.35                72.79         0.670          pass              0.182             25.0                           0.407                5.28              0.828                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-04T10:40:01.354459-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:35:05.771525-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:30:05.361830-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:25:01.416298-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.71, "early_entry_score": 0.756, "early_reclaim_pct": 63.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 93.75, "ticker": "CTAS", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.756, "early_reclaim_pct": 63.8, "matched_signals": 32, "recovery_stability_score": 0.577, "success_rate": 93.75, "ticker": "CTAS", "timing_score": 0.51, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.735, "early_reclaim_pct": 62.9, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.57, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:20:01.349464-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.53, "early_entry_score": 0.728, "early_reclaim_pct": 75.8, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.565, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.728, "early_reclaim_pct": 75.8, "matched_signals": 33, "recovery_stability_score": 0.659, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.565, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:15:05.517431-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:10:06.188010-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.5, "matched_signals": 30, "recovery_stability_score": 0.581, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:05:05.202403-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T10:05:05.202403-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.485, "pnl": -1749.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-04T10:00:02.269549-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804104001)

</details>

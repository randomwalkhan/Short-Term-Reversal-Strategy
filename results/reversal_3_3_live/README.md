# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 11:25:05 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           86.36               22            1.11              0.19         23.75                25.26         0.508            pass              0.360             19.7                           0.322                7.21              0.767                      ok            True                  False
  TMUS           55.56                9            2.75              3.04        156.45                56.37         0.566            pass              0.147             30.3                           0.350               -8.50             -0.465 downtrend_blocked_slope           False                  False
  MDLZ          100.00                1            2.13              0.96         63.58                19.17         0.565            pass              0.469              4.2                           0.206                5.46              0.648                      ok           False                  False
   KDP           96.88               32            0.16              0.04         34.61                29.04         0.536            pass              0.878             92.5                           0.614               13.21              1.301                      ok           False                  False
  GILD           88.89                9            1.74              1.91        155.69                26.70         0.536            pass              0.420             43.1                           0.559                4.72              0.594                      ok           False                  False
  DASH           75.00                8            3.19              4.28        189.83                49.85         0.512            pass              0.068              5.6                           0.168               -2.98             -0.228                      ok           False                  False
  INTU           89.19               37            0.16              0.36        335.13                37.42         0.509            pass              0.738             87.5                           0.776               13.15              1.311                      ok           False                  False
 CMCSA           75.00                4            2.10              0.33         22.22                21.50         0.499 below_threshold              0.170             40.1                           0.646                4.54              0.695                      ok           False                  False
  GEHC           72.73               11            1.90              0.93         69.83                23.16         0.491 below_threshold              0.094             12.7                           0.147                6.53              0.844                      ok           False                  False
  MSFT           93.94               33            0.22              0.82        531.52                21.62         0.488 below_threshold              0.822             82.8                           0.759                0.18              0.016                      ok           False                  False
  MELI           80.43               46            0.11              1.41       1878.90                40.36         0.482 below_threshold              0.529             89.7                           0.521                0.25             -0.084                      ok           False                  False
  ABNB           88.46               26            1.13              1.40        176.34                39.60         0.479 below_threshold              0.485             34.8                           0.202                8.91              0.991                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-21T11:25:05.346017-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "entry_ask": 31.0, "entry_bid": 27.8, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 22.0, "option_spread_pct": 10.88, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "matched_signals": 40, "recovery_stability_score": 0.6, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:20:06.788412-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:15:06.754370-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:10:03.902127-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:05:02.562193-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:00:06.521634-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:55:05.589543-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                          {"contract_symbol": "ABNB261120C00175000", "current_drop_pct": 0.52, "early_entry_score": 0.752, "early_reclaim_pct": 69.9, "entry_ask": 11.05, "entry_bid": 8.7, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 72415.9, "hypothetical_contracts": 73, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 728.0, "option_spread_pct": 23.8, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.752, "early_reclaim_pct": 69.9, "matched_signals": 37, "recovery_stability_score": 0.682, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:50:05.866905-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.67, "early_entry_score": 0.768, "early_reclaim_pct": 63.7, "entry_ask": 31.9, "entry_bid": 27.6, "entry_mode": "early", "entry_option_price": 29.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 14.45, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.768, "early_reclaim_pct": 63.7, "matched_signals": 40, "recovery_stability_score": 0.721, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.753, "early_reclaim_pct": 70.3, "matched_signals": 37, "recovery_stability_score": 0.699, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:45:05.723673-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.8, "entry_ask": 32.1, "entry_bid": 26.1, "entry_mode": "early", "entry_option_price": 29.1, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 20.62, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.8, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:40:06.184950-04:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 60.9, "entry_ask": 32.1, "entry_bid": 26.1, "entry_mode": "early", "entry_option_price": 29.1, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 20.62, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 60.9, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.74, "early_reclaim_pct": 66.0, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021112505)

</details>

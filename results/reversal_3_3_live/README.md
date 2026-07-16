# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 10:55:05 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           81.25               16            2.49              6.82        388.04                55.85         0.586          pass              0.210             26.1                           0.240               -4.02             -0.002                                 ok            True                  False
  MPWR           81.82               22            3.73             35.36       1337.51                84.79         0.580          pass              0.241             18.1                           0.214               -5.80             -0.020                                 ok            True                  False
  NXPI           80.00               15            3.18              6.21        276.35                58.07         0.547          pass              0.108              6.6                           0.168               -3.87              0.092                                 ok            True                  False
   WBD           87.50               16            0.72              0.14         27.21                20.00         0.537          pass              0.530             78.9                           0.482                1.56              0.251                                 ok            True                  False
  TEAM           81.25               32            1.63              1.05         91.32                73.34         0.521          pass              0.395             54.1                           0.662                8.54              1.022                                 ok            True                  False
  BKNG           88.24               34            0.60              0.77        182.47                43.83         0.514          pass              0.614             60.9                           0.622                1.94             -0.196                                 ok            True                  False
  CRWD           87.50               32            1.27              1.84        205.98                56.35         0.506          pass              0.579             60.7                           0.622                5.67              0.706                                 ok            True                  False
  KLAC           87.50               32            1.05              1.65        223.79               109.33         0.733          pass              0.644             74.6                           0.367              -26.37             -2.074 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.46               26            1.12              4.55        577.48                98.89         0.719          pass              0.629             74.9                           0.372              -20.76             -1.428 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.59               37            0.04              0.56       1815.03                66.00         0.642          pass              0.928             98.3                           0.517               -8.79             -0.610                                 ok           False                  False
  LRCX           84.21               19            3.13              7.35        332.28                98.70         0.619          pass              0.343             36.1                           0.224              -25.01             -1.890 downtrend_blocked_slope_and_streak           False                  False
    MU           81.25               16            5.15             32.57        890.32               112.73         0.603          pass              0.170             12.1                           0.124              -25.68             -1.669            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-16T10:55:05.410744-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:50:02.316903-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                             {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "entry_ask": 16.2, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 15.7, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 6.37, "option_volume": 41.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.699, "early_reclaim_pct": 70.4, "matched_signals": 38, "recovery_stability_score": 0.741, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:45:01.218260-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:40:01.176250-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:35:02.369345-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                               {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "entry_ask": 16.5, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 15.775, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 761.0, "option_spread_pct": 9.19, "option_volume": 68.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.812, "early_reclaim_pct": 61.7, "matched_signals": 37, "recovery_stability_score": 0.55, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T10:30:06.149838-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:25:02.335727-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:20:04.346056-04:00 early_entry_1020 early_entry_shadow  {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "entry_ask": 15.3, "entry_bid": 13.15, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 15.11, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "matched_signals": 37, "recovery_stability_score": 0.803, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.696, "early_reclaim_pct": 69.4, "matched_signals": 38, "recovery_stability_score": 0.831, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:15:01.181570-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "entry_ask": 15.35, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 42, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 17.73, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "matched_signals": 42, "recovery_stability_score": 0.786, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.754, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.827, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:10:01.416514-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "entry_ask": 15.6, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 19.33, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "matched_signals": 44, "recovery_stability_score": 0.725, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716105505)

</details>

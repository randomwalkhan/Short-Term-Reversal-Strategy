# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 10:20:04 EDT`
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
  META           81.48               27            0.97              4.62        679.33                54.55         0.598          pass              0.391             59.5                           0.645               10.08              1.364                                 ok            True                  False
   ADI           87.50               24            1.75              4.78        388.91                55.85         0.588          pass              0.497             48.2                           0.731               -3.28              0.033                                 ok            True                  False
  CTSH           81.58               38            0.78              0.23         43.08                65.21         0.579          pass              0.358             23.9                           0.230               10.62              0.868                                 ok            True                  False
  NXPI           83.33               18            2.86              5.58        276.62                58.07         0.551          pass              0.245             16.0                           0.360               -3.56              0.107                                 ok            True                  False
   WBD           89.47               19            0.66              0.13         27.22                20.00         0.523          pass              0.606             80.5                           0.448                1.61              0.253                                 ok            True                  False
  BKNG           85.71               28            1.15              1.47        182.17                43.83         0.513          pass              0.399             25.0                           0.192                1.38             -0.221                                 ok            True                  False
    MU           84.21               19            3.74             23.67        894.14               112.73         0.668          pass              0.348             36.2                           0.596              -24.58             -1.602            downtrend_blocked_slope           False                  False
  LRCX           88.89               27            1.65              3.87        333.77                98.70         0.664          pass              0.616             66.3                           0.798              -23.87             -1.821 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               18            9.10             10.54        161.03               219.49         0.629          pass              0.290             28.5                           0.568              -43.58             -3.482            downtrend_blocked_slope           False                  False
  MPWR           77.78               27            2.47             23.40       1342.63                84.79         0.620          pass              0.313             45.8                           0.743               -4.57              0.040                                 ok           False                  False
  MSTR           68.75               32            2.54              1.73         96.73               100.18         0.615          pass              0.311             34.4                           0.502                9.28              0.318                                 ok           False                  False
  DRAM           75.00               12            5.98              2.40         56.37               112.33         0.593          pass              0.138             21.9                           0.568              -18.06             -1.186            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-16T10:20:04.346056-04:00 early_entry_1020 early_entry_shadow  {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "entry_ask": 15.3, "entry_bid": 13.15, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 15.11, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.803, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.825, "early_reclaim_pct": 65.8, "matched_signals": 37, "recovery_stability_score": 0.803, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.696, "early_reclaim_pct": 69.4, "matched_signals": 38, "recovery_stability_score": 0.831, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:15:01.181570-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "entry_ask": 15.35, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 42, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 17.73, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "matched_signals": 42, "recovery_stability_score": 0.786, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.754, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.827, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:10:01.416514-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "entry_ask": 15.6, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 19.33, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "matched_signals": 44, "recovery_stability_score": 0.725, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:05:04.361041-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "entry_ask": 16.05, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 14.725, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 18.0, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.56, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "matched_signals": 37, "recovery_stability_score": 0.56, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:00:05.335836-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:00:05.335836-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "ADI260821C00380000", "fill_price": 31.635, "pnl": -1406.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ADI"}
2026-07-15T15:10:01.366399-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T15:00:06.972520-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T14:50:07.762689-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 14060.0, "asset_type": "option", "contract_symbol": "ADI260821C00380000", "contracts": 4, "early_entry_score": 0.523, "entry_mode": "regular", "entry_option_price": 35.15, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 129.0, "option_spread_pct": 5.41, "option_volume": 42.0, "success_rate": 86.21, "ticker": "ADI", "timing_score": 0.569}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716102004)

</details>

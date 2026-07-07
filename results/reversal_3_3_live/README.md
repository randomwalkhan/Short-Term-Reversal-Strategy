# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-07 12:40:05 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$25,746.75`
- Equity: `$25,746.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  AMAT     option         option AMAT260821C00600000      1          2026-07-06         2026-07-07       75.775     68.1975 -757.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           86.96               23            1.05              1.06        143.96                55.41         0.593            pass              0.505             57.8                           0.738                1.27              0.573                                 ok            True                  False
   CSX           86.67               15            0.95              0.33         48.67                21.52         0.559            pass              0.301             11.4                           0.255                4.64              0.603                                 ok            True                  False
  ASML           90.00               10            4.22             53.96       1801.94                78.10         0.528            pass              0.405             28.5                           0.560               -9.40             -0.249                                 ok            True                  False
   KDP          100.00               19            0.43              0.09         31.71                33.28         0.586            pass              0.724             68.6                           0.299                3.14              0.490                                 ok           False                  False
   TXN           71.43                7            3.45              7.33        300.36                69.17         0.544            pass              0.181             42.2                           0.629              -11.81             -0.714            downtrend_blocked_slope           False                  False
   ADI           80.00               15            2.64              7.18        385.75                61.47         0.541            pass              0.214             42.2                           0.587              -15.02             -1.264            downtrend_blocked_slope           False                  False
  QCOM           78.26               23            2.06              2.68        185.33                82.48         0.539            pass              0.287             48.7                           0.563              -17.69             -1.762 downtrend_blocked_slope_and_streak           False                  False
  PCAR           76.92               13            1.84              1.62        125.21                37.79         0.530            pass              0.142             22.9                           0.505                2.89              0.449                                 ok           False                  False
  CSCO           96.67               30            0.90              0.72        113.67                39.71         0.499 below_threshold              0.739             52.0                           0.613               -6.71             -0.691 downtrend_blocked_slope_and_streak           False                  False
    MU           77.78                9            6.55             45.13        965.41               132.57         0.490 below_threshold              0.141             30.7                           0.527              -24.02             -1.961            downtrend_blocked_slope           False                  False
  FAST           80.00                5            2.30              0.78         47.98                20.37         0.487 below_threshold              0.073              8.3                           0.229                2.34              0.499                                 ok           False                  False
  MCHP           85.71                7            4.50              2.76         86.41                74.72         0.479 below_threshold              0.303             34.2                           0.567              -18.56             -1.478            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-07T12:00:06.141276-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "entry_ask": 16.35, "entry_bid": 15.45, "entry_mode": "early", "entry_option_price": 15.9, "hypothetical_budget": 12873.38, "hypothetical_contracts": 8, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 770.0, "option_spread_pct": 5.66, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "top_candidates": [{"current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:55:03.609525-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "entry_ask": 16.35, "entry_bid": 15.45, "entry_mode": "early", "entry_option_price": 15.9, "hypothetical_budget": 12873.38, "hypothetical_contracts": 8, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 770.0, "option_spread_pct": 5.66, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "top_candidates": [{"current_drop_pct": 1.31, "early_entry_score": 0.792, "early_reclaim_pct": 68.2, "matched_signals": 32, "recovery_stability_score": 0.675, "success_rate": 96.88, "ticker": "FTNT", "timing_score": 0.41, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:50:02.135353-04:00 early_entry_1150 early_entry_shadow     {"contract_symbol": "FTNT260807C00152500", "current_drop_pct": 0.95, "early_entry_score": 0.851, "early_reclaim_pct": 76.9, "entry_ask": 18.25, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 12873.38, "hypothetical_contracts": 7, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 125.0, "option_spread_pct": 13.76, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.4, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.851, "early_reclaim_pct": 76.9, "matched_signals": 37, "recovery_stability_score": 0.751, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.4, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 78.6, "matched_signals": 38, "recovery_stability_score": 0.697, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.363, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:45:02.072009-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "FTNT260807C00152500", "current_drop_pct": 0.86, "early_entry_score": 0.858, "early_reclaim_pct": 79.2, "entry_ask": 18.25, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 12873.38, "hypothetical_contracts": 7, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 125.0, "option_spread_pct": 13.76, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.764, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.858, "early_reclaim_pct": 79.2, "matched_signals": 37, "recovery_stability_score": 0.764, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.767, "early_reclaim_pct": 85.9, "matched_signals": 41, "recovery_stability_score": 0.735, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T11:06:09.093047-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "CRWD260821C00197500", "current_drop_pct": 0.89, "early_entry_score": 0.701, "early_reclaim_pct": 75.3, "entry_ask": 18.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 12873.38, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 537.0, "option_spread_pct": 4.52, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.679, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.356, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.701, "early_reclaim_pct": 75.3, "matched_signals": 38, "recovery_stability_score": 0.679, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.356, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-07T10:46:12.062462-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-07T09:56:39.997866-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "AMAT260821C00600000", "fill_price": 68.1975, "pnl": -757.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AMAT"}
2026-07-07T00:00:02.324788-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-07-06T15:10:01.561163-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-06T15:05:05.496825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260707124005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260707124005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260707124005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260707124005)

</details>

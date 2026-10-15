# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 10:35:06 EDT`
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

- Cash: `$128,734.80`
- Equity: `$128,734.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           84.62               26            0.89              4.59        735.57                55.15         0.598            pass              0.500             70.2                           0.568                0.70              0.160                                 ok            True                  False
    ZS           92.31               26            1.93              2.99        219.51                59.94         0.528            pass              0.640             50.7                           0.335                8.92              1.346                                 ok            True                  False
  MSTR           86.67               30            1.88              1.88        142.43                78.69         0.560            pass              0.570             67.8                           0.790              -12.43             -1.347 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.89                9            2.94              5.76        277.07                59.82         0.555            pass              0.386             31.0                           0.579                4.79              0.740                                 ok           False                  False
  MPWR           82.61               23            1.63             14.15       1237.05                56.61         0.547            pass              0.385             58.0                           0.626              -10.15             -1.560            downtrend_blocked_slope           False                  False
  CDNS           75.00                8            2.80              6.47        326.69                37.41         0.502            pass              0.146             31.8                           0.335               -8.70             -0.866 downtrend_blocked_slope_and_streak           False                  False
  SNPS           60.00                5            4.01             13.48        474.15                52.37         0.498 below_threshold              0.123             24.3                           0.318               -6.09             -0.323 downtrend_blocked_slope_and_streak           False                  False
  UPRO           86.21               29            0.78              0.82        150.01                30.64         0.483 below_threshold              0.526             61.8                           0.722                0.97              0.050                                 ok           False                  False
  SHOP           85.29               34            0.96              1.15        172.01                48.53         0.480 below_threshold              0.596             82.2                           0.674               14.60              1.543                                 ok           False                  False
  AVGO           80.95               21            1.70              4.11        344.49                35.83         0.479 below_threshold              0.295             49.6                           0.762               -0.95             -0.317                                 ok           False                  False
   ADI           82.35               17            1.58              4.46        401.66                27.65         0.476 below_threshold              0.254             32.2                           0.190               -1.83             -0.305            downtrend_blocked_slope           False                  False
  CRWD           80.00               15            3.14              5.47        246.94                48.36         0.470 below_threshold              0.121             13.4                           0.166               -9.25             -0.923 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow                                                 {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:20:04.114099-04:00 early_entry_1020 early_entry_shadow                                                  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "entry_ask": 16.1, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.6, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.41, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "matched_signals": 36, "recovery_stability_score": 0.703, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:15:05.162285-04:00 early_entry_1015 early_entry_shadow                           {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "entry_ask": 15.6, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.825, "hypothetical_budget": 64367.4, "hypothetical_contracts": 43, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 2833.0, "option_spread_pct": 10.46, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "matched_signals": 37, "recovery_stability_score": 0.731, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:10:06.336303-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:05:05.165659-04:00 early_entry_1005 early_entry_shadow               {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "entry_ask": 17.4, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 2833.0, "option_spread_pct": 14.48, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "matched_signals": 37, "recovery_stability_score": 0.643, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:00:06.074428-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00217500", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "entry_ask": 17.75, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 16.325, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 17.46, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.617, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T09:50:06.230467-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 5.265, "pnl": -6727.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSCO"}
2026-10-15T00:00:06.592550-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015103506)

</details>

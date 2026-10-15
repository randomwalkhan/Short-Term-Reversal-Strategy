# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:15:06 EDT`
Last processed slot: `early_entry_1115`

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
    ZS           91.43               35            1.16              1.79        220.02                59.94         0.517            pass              0.734             70.4                           0.665                9.78              1.382                                 ok            True                   True
  META           84.85               33            0.41              2.11        736.63                55.15         0.585            pass              0.600             86.2                           0.792                1.18              0.182                                 ok           False                  False
  SNPS           71.43                7            2.83              9.49        475.86                52.37         0.561            pass              0.196             46.7                           0.631               -4.93             -0.267 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.89                9            2.96              5.80        277.05                59.82         0.554            pass              0.384             30.6                           0.455                4.76              0.739                                 ok           False                  False
  MPWR           86.05               43            0.04              0.37       1242.95                56.61         0.522            pass              0.710             98.9                           0.903               -8.70             -1.487            downtrend_blocked_slope           False                  False
  CDNS           77.78               18            1.71              3.95        327.77                37.41         0.504            pass              0.279             58.4                           0.688               -7.67             -0.815 downtrend_blocked_slope_and_streak           False                  False
  CRWD           85.00               20            2.37              4.13        247.52                48.36         0.486 below_threshold              0.362             37.7                           0.632               -8.53             -0.887 downtrend_blocked_slope_and_streak           False                  False
   AEP           62.50                8            1.34              1.18        125.62                12.92         0.486 below_threshold              0.103             18.2                           0.223                3.92              0.544                                 ok           False                  False
  INTC           85.71               14            3.80              2.61         97.00                68.27         0.472 below_threshold              0.388             54.0                           0.719              -21.34             -2.397            downtrend_blocked_slope           False                  False
  NVDA           86.67               15            1.78              2.76        220.12                25.52         0.467 below_threshold              0.418             53.3                           0.646               -5.85             -0.730 downtrend_blocked_slope_and_streak           False                  False
  AVGO           85.71               28            1.41              3.41        344.79                35.83         0.458 below_threshold              0.493             58.1                           0.612               -0.66             -0.303                                 ok           False                  False
   XEL           88.57               35            0.08              0.04         75.34                17.56         0.456 below_threshold              0.680             79.7                           0.420                6.73              0.663                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T11:15:06.283716-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "entry_ask": 15.15, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.525, "hypothetical_budget": 64367.4, "hypothetical_contracts": 44, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 8.61, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.665, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:10:05.939660-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "entry_ask": 14.15, "entry_bid": 13.6, "entry_mode": "early", "entry_option_price": 13.875, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.96, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "top_candidates": [{"current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:05:05.115302-04:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "entry_ask": 14.0, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 13.775, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.27, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015111506)

</details>

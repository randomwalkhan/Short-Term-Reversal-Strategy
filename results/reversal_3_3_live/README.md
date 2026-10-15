# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 12:10:06 EDT`
Last processed slot: `manage_1200`

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
  META           83.87               31            0.60              3.11        736.21                55.15         0.584            pass              0.541             79.7                           0.609                0.99              0.173                                 ok            True                  False
   CEG           81.82               11            2.58              5.06        277.37                59.82         0.557            pass              0.229             39.4                           0.619                5.17              0.757                                 ok            True                  False
    ZS           90.00               30            1.64              2.53        219.71                59.94         0.518            pass              0.627             58.2                           0.466                9.25              1.360                                 ok            True                  False
  MPWR           85.71               35            0.44              3.87       1241.45                56.61         0.545            pass              0.639             88.5                           0.729               -9.07             -1.506            downtrend_blocked_slope           False                  False
  SNPS           71.43                7            3.31             11.11        475.17                52.37         0.535            pass              0.166             37.6                           0.446               -5.40             -0.290 downtrend_blocked_slope_and_streak           False                  False
  CRWD           85.00               20            2.27              3.97        247.59                48.36         0.491 below_threshold              0.369             40.1                           0.664               -8.44             -0.883 downtrend_blocked_slope_and_streak           False                  False
  AVGO           81.25               16            2.03              4.92        344.14                35.83         0.490 below_threshold              0.241             39.6                           0.344               -1.29             -0.332                                 ok           False                  False
  CDNS           77.78               18            2.06              4.75        327.42                37.41         0.484 below_threshold              0.251             49.9                           0.469               -8.00             -0.831 downtrend_blocked_slope_and_streak           False                  False
   AEP           62.50                8            1.38              1.22        125.61                12.92         0.484 below_threshold              0.096             15.9                           0.282                3.87              0.542                                 ok           False                  False
   XEL           86.67               30            0.20              0.11         75.31                17.56         0.477 below_threshold              0.509             50.0                           0.390                6.61              0.657                                 ok           False                  False
  INTC           85.71               14            3.78              2.60         97.01                68.27         0.474 below_threshold              0.389             54.2                           0.686              -21.32             -2.396            downtrend_blocked_slope           False                  False
   ADI           88.46               26            0.87              2.46        402.52                27.65         0.469 below_threshold              0.567             62.6                           0.383               -1.12             -0.272                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T12:00:06.622764-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:55:05.998701-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:50:06.396498-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:45:05.042150-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:40:06.522445-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:35:05.966288-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:30:05.086968-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:25:06.119732-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:20:05.131214-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:15:06.283716-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "entry_ask": 15.15, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.525, "hypothetical_budget": 64367.4, "hypothetical_contracts": 44, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 8.61, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.665, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015121006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015121006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015121006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015121006)

</details>

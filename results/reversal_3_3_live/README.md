# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 12:00:06 EDT`
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
   CEG           83.33               12            2.44              4.77        277.50                59.82         0.561            pass              0.287             42.9                           0.666                5.33              0.763                                 ok            True                  False
    ZS           90.00               30            1.60              2.47        219.73                59.94         0.521            pass              0.630             59.2                           0.399                9.30              1.361                                 ok            True                  False
  META           85.29               34            0.39              2.04        736.67                55.15         0.580            pass              0.619             86.7                           0.688                1.20              0.182                                 ok           False                  False
  SNPS           71.43                7            3.28             11.01        475.21                52.37         0.537            pass              0.168             38.2                           0.397               -5.37             -0.289 downtrend_blocked_slope_and_streak           False                  False
  MPWR           86.49               37            0.42              3.65       1241.54                56.61         0.536            pass              0.674             89.1                           0.617               -9.04             -1.505            downtrend_blocked_slope           False                  False
  CDNS           77.78               18            2.00              4.62        327.48                37.41         0.488 below_threshold              0.256             51.3                           0.488               -7.94             -0.829 downtrend_blocked_slope_and_streak           False                  False
   XEL           85.71               28            0.36              0.19         75.28                17.56         0.478 below_threshold              0.346              8.5                           0.148                6.44              0.650                                 ok           False                  False
  AVGO           80.95               21            1.75              4.23        344.44                35.83         0.476 below_threshold              0.290             48.0                           0.493               -1.00             -0.319                                 ok           False                  False
   AEP           50.00                6            1.54              1.36        125.55                12.92         0.475 below_threshold              0.064              5.6                           0.200                3.70              0.534                                 ok           False                  False
  CRWD           85.00               20            2.62              4.56        247.33                48.36         0.472 below_threshold              0.341             31.2                           0.512               -8.76             -0.899 downtrend_blocked_slope_and_streak           False                  False
  NVDA           88.24               17            1.61              2.50        220.23                25.52         0.466 below_threshold              0.486             57.8                           0.688               -5.69             -0.722 downtrend_blocked_slope_and_streak           False                  False
  INTC           77.78               18            3.48              2.39         97.10                68.27         0.459 below_threshold              0.273             57.9                           0.719              -21.08             -2.381            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015120006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015120006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015120006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015120006)

</details>

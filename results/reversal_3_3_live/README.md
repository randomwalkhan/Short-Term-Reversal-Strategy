# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 11:35:06 EDT`
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

- Cash: `$28,399.25`
- Equity: `$28,399.25`
- Realized PnL: `$18,399.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   CSX     option         option  CSX260821C00047500     54          2026-07-07         2026-07-09        2.350      3.0750  3915.0   30.851064 take_profit_day2_hit_at_scan
  PAYX     option         option PAYX260821C00110000     50          2026-07-08         2026-07-09        2.525      2.2725 -1262.5  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           91.67               12            1.36              3.50        366.49                27.70         0.540          pass              0.395              5.5                           0.186                3.29              0.433                                 ok            True                  False
  GILD           92.86               14            1.58              1.51        135.17                35.14         0.537          pass              0.588             54.8                           0.327                6.80              0.891                                 ok            True                  False
   ADP           95.00               20            1.01              1.70        240.64                32.32         0.536          pass              0.702             60.7                           0.602                8.68              1.219                                 ok            True                  False
  GOOG           81.82               11            2.15              5.41        356.39                34.51         0.513          pass              0.176             23.1                           0.416                1.72              0.552                                 ok            True                  False
  MDLZ          100.00               13            0.71              0.30         59.35                30.45         0.596          pass              0.670             63.4                           0.673               -3.55             -0.208           downtrend_blocked_streak           False                  False
 CMCSA           63.64               11            0.41              0.07         23.16                30.42         0.575          pass              0.292             75.9                           0.717                3.40              0.290                                 ok           False                  False
   KDP          100.00                8            1.47              0.32         30.83                33.74         0.573          pass              0.532             24.8                           0.311               -2.13             -0.492 downtrend_blocked_slope_and_streak           False                  False
  CPRT           90.91               11            2.26              0.45         28.40                44.46         0.533          pass              0.358              2.3                           0.144               -8.08             -0.551            downtrend_blocked_slope           False                  False
  PAYX          100.00               33            0.07              0.05        106.56                32.56         0.531          pass              0.899             97.5                           0.743               10.60              1.197                                 ok           False                  False
   XEL          100.00               22            0.52              0.29         79.50                21.16         0.531          pass              0.647             38.1                           0.293               -2.78             -0.294            downtrend_blocked_slope           False                  False
  CTAS           72.73               11            1.72              2.17        179.24                32.70         0.528          pass              0.119             20.0                           0.251                3.59              0.699                                 ok           False                  False
  ADBE           72.50               40            0.16              0.25        220.83                49.87         0.500          pass              0.538             96.1                           0.769               12.22              1.413                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-09T11:35:06.621543-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:30:06.104076-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:25:02.920653-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:20:02.105470-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:15:03.120402-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:10:05.116017-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:05:04.917552-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T11:00:06.363633-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:55:06.732149-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-09T10:50:03.977506-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.54, "early_entry_score": 0.885, "early_reclaim_pct": 79.9, "entry_ask": 125.8, "entry_bid": 105.6, "entry_mode": "early", "entry_option_price": 115.7, "hypothetical_budget": 14199.63, "hypothetical_contracts": 1, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 107.0, "option_spread_pct": 17.46, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 95.0, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.885, "early_reclaim_pct": 79.9, "matched_signals": 40, "recovery_stability_score": 0.81, "success_rate": 95.0, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709113506)

</details>

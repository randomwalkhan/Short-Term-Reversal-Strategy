# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 11:00:03 EDT`
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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           90.48               21            0.50              0.11         30.86                36.31         0.608          pass              0.423              3.1                           0.059               -3.13             -0.244                                 ok            True                  False
  ASML           94.12               34            0.76              9.30       1743.59                63.09         0.588          pass              0.604              3.0                           0.084               -4.97             -0.206                                 ok            True                  False
   WBD           83.33               12            0.99              0.19         26.79                20.40         0.578          pass              0.195             11.7                           0.135                1.86              0.376                                 ok            True                  False
   CSX           87.50               16            0.92              0.33         50.61                17.40         0.535          pass              0.294              0.0                           0.191                3.02              0.432                                 ok            True                  False
  PAYX          100.00               31            0.52              0.42        114.21                33.31         0.529          pass              0.793             66.9                           0.796                7.97              0.833                                 ok            True                   True
  ORLY           82.14               28            1.19              0.71         85.74                41.23         0.518          pass              0.324             31.5                           0.354                0.94              0.000                                 ok            True                  False
  PCAR           84.00               25            1.07              0.94        125.80                30.30         0.517          pass              0.278              6.6                           0.149               -0.84              0.097                                 ok            True                  False
  GILD           92.86               28            0.60              0.56        134.04                34.72         0.513          pass              0.619             35.1                           0.385                2.98              0.046                                 ok            True                  False
  BKNG           85.71               21            1.75              2.23        180.73                41.44         0.512          pass              0.356             26.4                           0.361               -1.40              0.143                                 ok            True                  False
   ADP           96.43               28            0.65              1.16        254.77                34.14         0.509          pass              0.754             61.1                           0.749                5.90              0.630                                 ok            True                  False
  ABNB           97.06               34            0.57              0.58        145.73                32.96         0.506          pass              0.751             46.8                           0.399               -1.70             -0.051                                 ok            True                  False
  AMAT           91.18               34            0.29              1.09        529.19                99.49         0.709          pass              0.626             32.3                           0.158              -10.91             -0.777 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-20T11:00:03.075062-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "PAYX260821C00115000", "current_drop_pct": 0.52, "early_entry_score": 0.793, "early_reclaim_pct": 66.9, "entry_ask": 3.1, "entry_bid": 3.0, "entry_mode": "early", "entry_option_price": 3.05, "hypothetical_budget": 15705.88, "hypothetical_contracts": 51, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1721.0, "option_spread_pct": 3.28, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.796, "shadow_only": true, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.529, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.793, "early_reclaim_pct": 66.9, "matched_signals": 31, "recovery_stability_score": 0.796, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.529, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-20T10:55:02.013692-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "PAYX260821C00110000", "current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 63.5, "entry_ask": 5.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 15705.88, "hypothetical_contracts": 28, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1044.0, "option_spread_pct": 7.27, "option_volume": 102.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 63.5, "matched_signals": 31, "recovery_stability_score": 0.753, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-20T10:50:05.022185-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:45:02.099135-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:40:04.090335-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:35:05.083590-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:30:04.102843-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:25:04.012806-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:20:01.111901-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720110003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720110003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720110003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720110003)

</details>

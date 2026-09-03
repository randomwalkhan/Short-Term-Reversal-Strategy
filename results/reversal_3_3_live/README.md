# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 11:35:01 EDT`
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

- Cash: `$74,478.10`
- Equity: `$74,478.10`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CPRT     option         option CPRT261016C00032500    144          2026-09-01         2026-09-03        1.650       2.800 16560.0   69.696970 take_profit_day2_hit_at_scan
  MSTR     option         option MSTR261009C00122000     20          2026-09-02         2026-09-03       11.475      16.575 10200.0   44.444444 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           81.82               33            1.00              0.39         56.04                63.42         0.581            pass              0.473             70.9                           0.753               -3.35             -0.198                                 ok            True                  False
  REGN          100.00               16            1.32              7.87        848.66                27.66         0.544            pass              0.560             21.9                           0.419                1.71              0.039                                 ok            True                  False
  SBUX           95.45               22            0.64              0.48        106.52                21.58         0.526            pass              0.697             54.7                           0.630                1.97              0.045                                 ok            True                  False
    MU           86.84               38            0.51              3.38        954.63                51.19         0.511            pass              0.681             87.0                           0.750               -2.37             -0.037                                 ok            True                  False
 CMCSA           92.31               26            0.76              0.14         26.75                26.14         0.507            pass              0.587             33.9                           0.387                0.70             -0.085                                 ok            True                  False
  SOXL           83.78               37            0.47              0.35        106.20                96.37         0.639            pass              0.625             93.5                           0.977              -13.39             -1.330            downtrend_blocked_slope           False                  False
   STX           86.67               30            1.16              6.58        805.72                70.48         0.575            pass              0.606             79.1                           0.746               -6.01             -0.392 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.48               42            0.08              0.04         72.74                58.99         0.566            pass              0.828             97.4                           0.849               -3.53             -0.424            downtrend_blocked_slope           False                  False
   WDC           82.86               35            0.52              1.63        448.20                80.52         0.552            pass              0.573             91.7                           0.783               -4.79             -0.234           downtrend_blocked_streak           False                  False
  AMAT           86.49               37            0.48              1.48        437.82                43.96         0.512            pass              0.653             82.8                           0.853              -12.07             -1.374 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.00               40            0.20              0.41        288.15                47.62         0.504            pass              0.667             94.4                           0.887               -7.34             -0.948 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               35            0.05              0.05        123.98                25.89         0.496 below_threshold              0.895             92.8                           0.443                0.83              0.065                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-03T11:35:01.854924-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:30:01.782491-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:25:02.898390-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:20:03.788665-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:15:01.912684-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:10:01.959979-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:05:04.957756-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "entry_ask": 7.5, "entry_bid": 6.8, "entry_mode": "early", "entry_option_price": 7.15, "hypothetical_budget": 37239.05, "hypothetical_contracts": 52, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 9.79, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "matched_signals": 44, "recovery_stability_score": 0.687, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:59:54.471518-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:40:04.774963-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:35:03.916601-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903113501)

</details>

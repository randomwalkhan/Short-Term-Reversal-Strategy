# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 14:40:01 EDT`
Last processed slot: `manage_1430`

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
  REGN          100.00               15            1.37              8.18        848.52                27.66         0.547            pass              0.544             18.8                           0.157                1.66              0.037                                 ok            True                  False
  MNST           88.89               36            0.30              0.09         44.38               424.20         0.999            pass              0.643             44.1                           0.287               -6.75             -0.938 downtrend_blocked_slope_and_streak           False                  False
  DRAM           82.86               35            0.47              0.19         56.13                63.42         0.601            pass              0.562             86.2                           0.789               -2.84             -0.174                                 ok           False                  False
   STX           86.67               30            1.22              6.88        805.59                70.48         0.571            pass              0.603             78.2                           0.612               -6.06             -0.395 downtrend_blocked_slope_and_streak           False                  False
   WDC           81.08               37            0.39              1.21        448.38                80.52         0.545            pass              0.545             93.8                           0.771               -4.66             -0.228           downtrend_blocked_streak           False                  False
  MELI          100.00               36            0.48              6.77       2003.68                49.44         0.538            pass              0.742             38.2                           0.314                3.90              0.302                                 ok           False                  False
    MU           86.84               38            0.36              2.39        955.06                51.19         0.520            pass              0.694             90.8                           0.838               -2.22             -0.030                                 ok           False                  False
  SBUX           96.43               28            0.35              0.26        106.61                21.58         0.508            pass              0.797             75.3                           0.679                2.27              0.059                                 ok           False                  False
  CSCO           89.74               39            0.48              0.37        109.30                36.36         0.502            pass              0.718             71.4                           0.571               -0.61             -0.122                                 ok           False                  False
  AMAT           86.49               37            0.69              2.10        437.56                43.96         0.500 below_threshold              0.630             75.6                           0.665              -12.24             -1.383 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           94.29               35            0.02              0.00         26.81                26.14         0.499 below_threshold              0.893             98.4                           0.886                1.46             -0.051                                 ok           False                  False
  MDLZ           83.33               12            1.80              0.79         62.11                20.19         0.495 below_threshold              0.222             23.5                           0.575               -4.39             -0.488 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-03T12:00:04.745572-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "entry_ask": 9.55, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 9.425, "hypothetical_budget": 37239.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 365.0, "option_spread_pct": 2.65, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T11:55:01.936733-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:50:04.853534-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:45:06.281910-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:40:01.991176-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:35:01.854924-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:30:01.782491-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:25:02.898390-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:20:03.788665-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:15:01.912684-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903144001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903144001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903144001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903144001)

</details>

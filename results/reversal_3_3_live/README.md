# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 11:45:06 EDT`
Last processed slot: `early_entry_1145`

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
  DRAM           83.33               30            1.41              0.55         55.97                63.42         0.576            pass              0.457             59.0                           0.638               -3.75             -0.217                                 ok            True                  False
  REGN          100.00               20            1.22              7.26        848.92                27.66         0.525            pass              0.603             28.0                           0.402                1.82              0.044                                 ok            True                  False
 CMCSA           92.31               26            0.73              0.14         26.75                26.14         0.509            pass              0.597             37.1                           0.425                0.74             -0.083                                 ok            True                  False
    MU           85.29               34            0.99              6.61        953.25                51.19         0.505            pass              0.575             74.6                           0.646               -2.84             -0.059                                 ok            True                  False
  SOXL           83.33               36            0.84              0.63        106.08                96.37         0.622            pass              0.590             88.4                           0.883              -13.71             -1.347            downtrend_blocked_slope           False                  False
   STX           86.67               30            1.30              7.36        805.39                70.48         0.566            pass              0.598             76.6                           0.711               -6.14             -0.399 downtrend_blocked_slope_and_streak           False                  False
   WDC           81.82               33            0.87              2.73        447.73                80.52         0.542            pass              0.514             86.1                           0.786               -5.13             -0.250 downtrend_blocked_slope_and_streak           False                  False
  CSCO           90.48               42            0.01              0.01        109.45                36.36         0.515            pass              0.828             99.2                           0.824               -0.14             -0.101                                 ok           False                  False
  SBUX           96.15               26            0.50              0.37        106.56                21.58         0.511            pass              0.752             64.7                           0.706                2.12              0.052                                 ok           False                  False
  MPWR           84.62               39            0.04              0.32       1219.22                40.59         0.504            pass              0.662             98.5                           0.771               -7.00             -0.821            downtrend_blocked_slope           False                  False
  AMAT           86.11               36            0.77              2.35        437.45                43.96         0.500            pass              0.605             72.8                           0.698              -12.31             -1.387 downtrend_blocked_slope_and_streak           False                  False
  AMGN           97.06               34            0.02              0.05        442.82                21.97         0.497 below_threshold              0.905             98.5                           0.684                2.68              0.046                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-03T11:45:06.281910-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:40:01.991176-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:35:01.854924-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:30:01.782491-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:25:02.898390-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:20:03.788665-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:15:01.912684-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:10:01.959979-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T11:05:04.957756-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "entry_ask": 7.5, "entry_bid": 6.8, "entry_mode": "early", "entry_option_price": 7.15, "hypothetical_budget": 37239.05, "hypothetical_contracts": 52, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 9.79, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "matched_signals": 44, "recovery_stability_score": 0.687, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:59:54.471518-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903114506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903114506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903114506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903114506)

</details>

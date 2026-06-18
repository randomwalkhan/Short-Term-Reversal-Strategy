# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 11:15:05 EDT`
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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           86.67               30            0.58              0.48        117.92                34.58         0.554          pass              0.453             28.9                           0.322               -0.25              0.025                                 ok            True                  False
  MDLZ           92.86               14            1.21              0.51         60.64                21.28         0.551          pass              0.461             12.0                           0.216               -1.42             -0.169                                 ok            True                  False
  CRWD           87.18               39            0.57              2.72        681.80                64.33         0.537          pass              0.686             82.4                           0.521               -5.56              0.067                                 ok            True                  False
  VRTX           93.75               16            1.54              4.96        456.86                24.55         0.509          pass              0.509             17.1                           0.279                2.30              0.301                                 ok            True                  False
    ZS           77.14               35            1.03              0.90        124.00               152.31         0.873          pass              0.468             71.4                           0.569               -8.99             -0.554 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.06              0.17         23.13                27.50         0.683          pass              0.523             18.3                           0.238                4.01              0.385                                 ok           False                  False
  INTU           69.23               26            1.98              3.72        267.48                98.62         0.683          pass              0.313             46.0                           0.280              -12.66             -1.299 downtrend_blocked_slope_and_streak           False                  False
   TRI           77.27               22            0.97              0.54         79.02                52.51         0.598          pass              0.334             64.8                           0.483               -8.46             -0.816 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.83              4.37        339.79                27.62         0.570          pass              0.195             16.4                           0.259               -2.95             -0.126           downtrend_blocked_streak           False                  False
  PAYX          100.00               27            0.32              0.22         97.49                31.76         0.561          pass              0.812             80.9                           0.538               -2.22             -0.166                                 ok           False                  False
  COST           58.33               12            1.22              8.24        962.06                23.27         0.540          pass              0.163             31.9                           0.363               -1.91             -0.059                                 ok           False                  False
  GILD           83.33                6            2.24              1.97        124.61                29.17         0.535          pass              0.143              0.4                           0.039               -4.44             -0.265 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-18T11:15:05.288880-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:10:05.442470-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:05:02.437168-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:00:02.344024-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:55:03.314248-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:50:01.439897-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:45:03.283549-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:40:01.292114-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:35:03.329239-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:30:02.323229-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "entry_ask": 9.9, "entry_bid": 7.35, "entry_mode": "early", "entry_option_price": 8.625, "hypothetical_budget": 13257.25, "hypothetical_contracts": 15, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 29.57, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "matched_signals": 43, "recovery_stability_score": 0.694, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618111505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618111505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618111505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618111505)

</details>

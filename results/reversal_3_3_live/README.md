# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 11:00:02 EDT`
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
  MDLZ           91.67               12            1.31              0.56         60.62                21.28         0.558          pass              0.380              0.0                           0.048               -1.52             -0.174                                 ok            True                  False
   WMT           86.67               30            0.56              0.46        117.93                34.58         0.556          pass              0.456             29.8                           0.389               -0.23              0.027                                 ok            True                  False
  VRTX           92.31               13            1.79              5.75        456.53                24.55         0.513          pass              0.411              3.9                           0.164                2.05              0.290                                 ok            True                  False
    ZS           78.38               37            0.80              0.69        124.08               152.31         0.875          pass              0.501             77.9                           0.805               -8.78             -0.544 downtrend_blocked_slope_and_streak           False                  False
  INTU           75.00               36            1.09              2.05        268.20                98.62         0.683          pass              0.452             70.3                           0.567              -11.87             -1.258 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.08              0.17         23.13                27.50         0.682          pass              0.510             13.8                           0.177                3.99              0.384                                 ok           False                  False
   PEP          100.00               23            0.04              0.04        141.57                22.29         0.603          pass              0.816             89.8                           0.511                0.61              0.166                                 ok           False                  False
   TRI           80.65               31            0.29              0.16         79.18                52.51         0.586          pass              0.484             89.4                           0.715               -7.84             -0.785 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.76              4.20        339.86                27.62         0.575          pass              0.205             19.6                           0.218               -2.88             -0.122           downtrend_blocked_streak           False                  False
  GILD           85.71                7            2.03              1.78        124.69                29.17         0.546          pass              0.218              3.8                           0.108               -4.24             -0.255 downtrend_blocked_slope_and_streak           False                  False
  CRWD           87.50               40            0.45              2.17        682.03                64.33         0.539          pass              0.712             85.9                           0.719               -5.46              0.072                                 ok           False                  False
  COST           64.29               14            1.13              7.64        962.32                23.27         0.539          pass              0.191             36.9                           0.486               -1.82             -0.054                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-18T11:00:02.344024-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:55:03.314248-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:50:01.439897-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:45:03.283549-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:40:01.292114-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:35:03.329239-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:30:02.323229-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "entry_ask": 9.9, "entry_bid": 7.35, "entry_mode": "early", "entry_option_price": 8.625, "hypothetical_budget": 13257.25, "hypothetical_contracts": 15, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 29.57, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "matched_signals": 43, "recovery_stability_score": 0.694, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T10:25:02.315380-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:20:06.081546-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:15:06.113244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618110002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:40:05 EDT`
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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           87.50               24            1.52              3.26        304.15                65.52         0.588          pass              0.494             47.3                           0.550                0.95              0.279                                 ok            True                  False
   ADI           86.21               29            1.11              3.06        391.44                55.85         0.565          pass              0.493             48.1                           0.467               -2.21              0.083                                 ok            True                  False
   EXC           94.74               19            0.59              0.19         46.84                21.56         0.554          pass              0.666             52.6                           0.318                0.05             -0.045                                 ok            True                  False
  NXPI           84.62               26            1.43              2.84        282.65                58.07         0.552          pass              0.410             41.7                           0.446               -0.43              0.252                                 ok            True                  False
   WBD           83.33               12            0.93              0.18         27.40                20.00         0.547          pass              0.253             32.0                           0.440                2.12              0.276                                 ok            True                  False
  MDLZ           93.75               16            0.34              0.14         58.74                30.54         0.628          pass              0.704             78.2                           0.396                1.31             -0.076                                 ok           False                  False
  KLAC           76.92               13            3.90              6.29        227.67               109.33         0.612          pass              0.139             19.3                           0.409              -26.62             -2.090 downtrend_blocked_slope_and_streak           False                  False
  AMAT           80.00               15            3.34             13.94        589.72                98.89         0.587          pass              0.154             20.8                           0.357              -20.36             -1.406 downtrend_blocked_slope_and_streak           False                  False
   LIN          100.00                5            1.64              5.99        519.97                20.66         0.582          pass              0.458              0.0                           0.157               -0.96             -0.319                                 ok           False                  False
  QCOM           83.87               31            0.95              1.19        177.59                61.79         0.579          pass              0.447             48.5                           0.453               -4.54             -0.087           downtrend_blocked_streak           False                  False
   CSX           88.89                9            1.36              0.48         49.72                19.08         0.578          pass              0.312              5.6                           0.121                3.60              0.333                                 ok           False                  False
  MCHP           96.15               26            2.09              1.27         86.56                68.63         0.559          pass              0.621             19.5                           0.274               -6.48             -0.290            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-07-15T11:40:05.824741-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "entry_ask": 109.0, "entry_bid": 89.0, "entry_mode": "early", "entry_option_price": 99.0, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.2, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "matched_signals": 30, "recovery_stability_score": 0.731, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:35:03.044078-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:30:02.764880-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "entry_ask": 109.0, "entry_bid": 88.7, "entry_mode": "early", "entry_option_price": 98.85, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.54, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "matched_signals": 30, "recovery_stability_score": 0.806, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:25:06.537726-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:20:02.933836-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:15:06.015471-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:10:02.751788-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "META260821C00660000", "fill_price": 54.6, "pnl": 1545.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.48, "ticker": "META"}
2026-07-15T11:00:03.028836-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715114005)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 13:25:04 EST`
Last processed slot: `manage_1330`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           56.25               16            3.57              1.51         59.90               129.60         0.723            pass              0.241             42.9                           0.292              -37.19             -4.978            downtrend_blocked_slope           False                  False
    ZS           92.86               42            0.37              0.59        224.84                64.45         0.533            pass              0.846             83.2                           0.679               -3.06             -0.907 downtrend_blocked_slope_and_streak           False                  False
  REGN           66.67                3            3.24             22.09        963.89                48.26         0.515            pass              0.080              9.3                           0.272               16.90              2.076                                 ok           False                  False
  NVDA           77.78               18            1.28              1.85        205.90                32.59         0.507            pass              0.266             54.1                           0.639               -8.07             -0.712 downtrend_blocked_slope_and_streak           False                  False
  AVGO           75.00               28            1.13              2.62        331.01                44.04         0.502            pass              0.362             64.0                           0.431               -2.79             -0.035                                 ok           False                  False
  CSCO           82.76               29            0.48              0.35        102.82                32.31         0.496 below_threshold              0.423             57.7                           0.356               -4.46             -0.523 downtrend_blocked_slope_and_streak           False                  False
  TEAM           96.15               26            1.73              2.31        190.06                53.65         0.493 below_threshold              0.697             46.9                           0.408              -16.74             -2.277            downtrend_blocked_slope           False                  False
  SNPS           74.19               31            0.83              2.70        461.72                45.79         0.492 below_threshold              0.386             65.6                           0.379                1.74              0.711                                 ok           False                  False
  ASML           71.43                7            3.18             34.55       1537.33                44.05         0.487 below_threshold              0.146             32.6                           0.314              -10.25             -0.588            downtrend_blocked_slope           False                  False
  DRAM           61.54               13            4.02              1.34         47.07                69.30         0.486 below_threshold              0.165             32.1                           0.297               -6.99             -0.210                                 ok           False                  False
  PANW           82.22               45            0.16              0.39        350.03                58.95         0.485 below_threshold              0.589             93.7                           0.597                0.69             -0.400                                 ok           False                  False
   AEP           86.36               22            0.70              0.64        129.59                19.14         0.481 below_threshold              0.553             85.2                           0.718                1.22              0.054                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:45:05.372887-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:40:03.980969-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:35:05.266988-05:00 early_entry_1135 early_entry_shadow  {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "entry_ask": 9.15, "entry_bid": 8.25, "entry_mode": "early", "entry_option_price": 8.7, "hypothetical_budget": 64815.78, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 10.34, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "matched_signals": 31, "recovery_stability_score": 0.72, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:30:01.206100-05:00 early_entry_1130 early_entry_shadow {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "entry_ask": 9.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.025, "hypothetical_budget": 64815.78, "hypothetical_contracts": 71, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 11.63, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "matched_signals": 30, "recovery_stability_score": 0.671, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:25:01.112223-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104132504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104132504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104132504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104132504)

</details>

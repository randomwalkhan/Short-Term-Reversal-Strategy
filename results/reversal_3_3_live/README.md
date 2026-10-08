# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 11:45:05 EDT`
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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           88.46               26            1.48             14.75       1419.66                55.22         0.573          pass              0.550             53.6                           0.660                5.35              0.857                                 ok            True                  False
  CSCO           86.36               22            0.86              0.71        117.09                34.80         0.571          pass              0.387             26.8                           0.252                9.22              1.190                                 ok            True                  False
   CEG           84.21               19            1.99              4.17        297.80                58.54         0.553          pass              0.307             26.3                           0.281               12.24              1.417                                 ok            True                  False
  PANW           81.40               43            0.59              1.67        404.85                57.34         0.519          pass              0.397             36.1                           0.279                3.40              0.724                                 ok            True                  False
  UPRO           84.00               25            1.04              1.13        154.67                30.53         0.511          pass              0.385             42.3                           0.328                2.37              0.409                                 ok            True                  False
  MELI           82.14               28            1.61             21.08       1863.74                42.10         0.509          pass              0.247              6.3                           0.120                5.05              0.808                                 ok            True                  False
  MSTR           89.29               28            2.31              2.48        152.31                80.80         0.592          pass              0.536             36.6                           0.219               -7.29             -0.189           downtrend_blocked_streak           False                  False
  QCOM           87.50               24            1.95              2.42        176.08                56.66         0.570          pass              0.425             24.8                           0.259              -10.60             -1.111 downtrend_blocked_slope_and_streak           False                  False
  META           84.21               38            0.24              1.20        720.79                52.76         0.560          pass              0.609             84.7                           0.433               -7.46             -0.404            downtrend_blocked_slope           False                  False
  SOXL           79.17               24            5.24              5.83        156.41               112.38         0.542          pass              0.248             33.5                           0.408                2.91              0.991                                 ok           False                  False
   STX           87.50               24            2.66             15.03        801.13                69.74         0.539          pass              0.384             12.1                           0.157              -13.23             -1.601            downtrend_blocked_slope           False                  False
   WDC           82.86               35            1.24              3.52        403.91                65.89         0.537          pass              0.421             41.6                           0.233              -11.09             -1.365            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-08T11:45:05.150899-04:00 early_entry_1145 early_entry_shadow  {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "entry_ask": 3.5, "entry_bid": 3.2, "entry_mode": "early", "entry_option_price": 3.35, "hypothetical_budget": 54289.65, "hypothetical_contracts": 162, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.96, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "matched_signals": 34, "recovery_stability_score": 0.608, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:40:06.664778-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:35:04.845679-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:30:01.685924-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:25:05.197379-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:20:05.981785-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:15:06.509064-04:00 early_entry_1115 early_entry_shadow                {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "entry_ask": 27.4, "entry_bid": 24.5, "entry_mode": "early", "entry_option_price": 25.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "matched_signals": 37, "recovery_stability_score": 0.721, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:10:06.909250-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.61, "early_entry_score": 0.859, "early_reclaim_pct": 85.2, "entry_ask": 4.0, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.75, "hypothetical_budget": 54289.65, "hypothetical_contracts": 144, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.859, "early_reclaim_pct": 85.2, "matched_signals": 36, "recovery_stability_score": 0.623, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:05:04.028696-04:00 early_entry_1105 early_entry_shadow                                   {"contract_symbol": "ADI261120C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "entry_ask": 27.9, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 121.0, "option_spread_pct": 10.96, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "matched_signals": 33, "recovery_stability_score": 0.582, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-08T11:00:06.101046-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008114505)

</details>

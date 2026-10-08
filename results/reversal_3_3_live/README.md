# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 13:30:02 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           85.71               14            2.23              6.39        407.34                34.70         0.519            pass              0.271             13.3                           0.202                4.79              0.669                                 ok            True                  False
  MSFT          100.00               19            1.29              4.78        527.71                20.46         0.507            pass              0.558             15.8                           0.192                5.02              0.488                                 ok            True                  False
  MSTR           85.71               21            3.04              3.27        151.97                80.80         0.587            pass              0.351             22.0                           0.369               -7.99             -0.223           downtrend_blocked_streak           False                  False
  META           80.00               25            1.13              5.71        718.86                52.76         0.581            pass              0.240             27.4                           0.215               -8.29             -0.445            downtrend_blocked_slope           False                  False
  QCOM           78.57               14            2.85              3.53        175.61                56.66         0.564            pass              0.135             17.4                           0.266              -11.42             -1.153 downtrend_blocked_slope_and_streak           False                  False
  CSCO           75.00               12            1.68              1.38        116.80                34.80         0.564            pass              0.133             21.0                           0.357                8.31              1.153                                 ok           False                  False
  UPRO           88.89                9            2.36              2.56        154.06                30.53         0.531            pass              0.321             10.3                           0.211                1.01              0.348                                 ok           False                  False
  SNPS           84.44               45            0.13              0.46        502.47                54.49         0.525            pass              0.636             88.4                           0.398               18.15              2.285                                 ok           False                  False
  AMGN           50.00                6            1.91              5.51        410.72                28.61         0.506            pass              0.169             39.6                           0.590               -0.20             -0.258                                 ok           False                  False
  DASH           88.10               42            0.27              0.36        191.08                42.67         0.503            pass              0.716             83.2                           0.765                1.70              0.332                                 ok           False                  False
  CRWD           89.13               46            0.54              1.01        265.01                59.00         0.498 below_threshold              0.660             55.6                           0.413                1.67              0.547                                 ok           False                  False
  MELI           76.47               34            1.06             13.96       1866.80                42.10         0.497 below_threshold              0.326             38.9                           0.460                5.63              0.833                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-08T12:00:05.051219-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "entry_ask": 3.7, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.55, "hypothetical_budget": 54289.65, "hypothetical_contracts": 152, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "matched_signals": 36, "recovery_stability_score": 0.751, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:55:05.190220-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:50:07.100494-04:00 early_entry_1150 early_entry_shadow  {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.51, "early_entry_score": 0.897, "early_reclaim_pct": 87.8, "entry_ask": 3.5, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.4, "hypothetical_budget": 54289.65, "hypothetical_contracts": 159, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 5.88, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 94.87, "ticker": "CTSH", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.897, "early_reclaim_pct": 87.8, "matched_signals": 39, "recovery_stability_score": 0.727, "success_rate": 94.87, "ticker": "CTSH", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:45:05.150899-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "entry_ask": 3.5, "entry_bid": 3.2, "entry_mode": "early", "entry_option_price": 3.35, "hypothetical_budget": 54289.65, "hypothetical_contracts": 162, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.96, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "matched_signals": 34, "recovery_stability_score": 0.608, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:40:06.664778-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:35:04.845679-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:30:01.685924-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:25:05.197379-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:20:05.981785-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:15:06.509064-04:00 early_entry_1115 early_entry_shadow                 {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "entry_ask": 27.4, "entry_bid": 24.5, "entry_mode": "early", "entry_option_price": 25.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "matched_signals": 37, "recovery_stability_score": 0.721, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008133002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008133002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008133002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008133002)

</details>

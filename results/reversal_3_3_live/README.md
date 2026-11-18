# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 12:40:04 EST`
Last processed slot: `manage_1230`

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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   TXN           88.89               18            1.52              3.15        294.51                59.80         0.616          pass              0.471             39.6                           0.511               -6.46              0.165                       ok            True                  False
   ADI           92.11               38            0.59              1.57        383.00                67.50         0.591          pass              0.775             68.9                           0.643               -6.11              0.130                       ok            True                   True
  REGN           81.82               33            0.89              5.96        955.20                53.86         0.569          pass              0.259              0.0                           0.239                2.00              0.549                       ok            True                  False
   CEG           91.18               34            0.93              1.74        267.32                61.66         0.553          pass              0.692             59.4                           0.598                8.25              1.141                       ok            True                  False
  INSM           83.33               42            0.81              0.69        121.56                62.27         0.538          pass              0.545             67.4                           0.704                9.88              1.103                       ok            True                  False
  SOXL           69.70               33            0.96              0.33         48.93               265.73         0.949          pass              0.493             81.6                           0.826              -27.12             -0.403  downtrend_blocked_slope           False                  False
  INTC           70.27               37            0.83              0.32         55.03               143.31         0.827          pass              0.483             73.4                           0.818               -6.11             -0.073 downtrend_blocked_streak           False                  False
  ALNY           56.25               16            2.82              3.09        155.18               110.55         0.736          pass              0.182             22.8                           0.278               -5.58             -0.074                       ok           False                  False
  LRCX           68.29               41            0.04              0.05        210.67               104.84         0.709          pass              0.566             98.2                           0.807               -4.88              0.462 downtrend_blocked_streak           False                  False
  MRVL           75.86               29            2.20              2.29        147.76               124.48         0.692          pass              0.336             46.6                           0.608               -8.97              0.126                       ok           False                  False
  MPWR           72.73               33            0.84              7.74       1314.05                97.00         0.680          pass              0.408             62.3                           0.616                3.59              1.044                       ok           False                  False
  KLAC           75.68               37            0.22              0.22        144.46                90.42         0.675          pass              0.509             87.0                           0.654               -3.56              0.379                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:55:05.147885-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:50:04.203803-05:00 early_entry_1150 early_entry_shadow      {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "entry_ask": 6.3, "entry_bid": 5.7, "entry_mode": "early", "entry_option_price": 6.0, "hypothetical_budget": 52959.4, "hypothetical_contracts": 88, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 10.0, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "matched_signals": 39, "recovery_stability_score": 0.7, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:45:05.124213-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "entry_ask": 6.1, "entry_bid": 5.6, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 52959.4, "hypothetical_contracts": 90, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 8.55, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "matched_signals": 39, "recovery_stability_score": 0.694, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:40:04.319584-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:35:02.338548-05:00 early_entry_1135 early_entry_shadow    {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "entry_ask": 26.4, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 25.8, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 4.65, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "matched_signals": 46, "recovery_stability_score": 0.559, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:30:05.127022-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:25:05.812808-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:20:05.157588-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118124004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118124004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118124004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118124004)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 14:10:04 EST`
Last processed slot: `manage_1400`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           92.59               27            1.99              5.55        396.56               121.47         0.781          pass              0.580             17.4                           0.209               43.88              2.221                                 ok            True                  False
   ADI           85.71               21            1.64              4.41        381.78                67.50         0.624          pass              0.327             13.0                           0.169               -7.11              0.081                                 ok            True                  False
   TXN           83.33               12            2.06              4.27        294.03                59.80         0.614          pass              0.218             18.2                           0.197               -6.97              0.140                                 ok            True                  False
   BKR           87.10               31            0.63              0.21         47.37                58.51         0.609          pass              0.556             55.2                           0.400               -4.98             -0.034                                 ok            True                  False
  VRSK           83.33               30            0.97              1.40        204.71                46.89         0.549          pass              0.462             61.6                           0.692                2.76              0.198                                 ok            True                  False
   CEG           90.91               33            1.11              2.08        267.18                61.66         0.547          pass              0.653             51.5                           0.389                8.05              1.133                                 ok            True                  False
  INSM           81.08               37            1.28              1.09        121.39                62.27         0.538          pass              0.409             48.7                           0.341                9.37              1.082                                 ok            True                  False
  META           82.35               34            0.54              2.33        617.87                41.87         0.526          pass              0.459             61.1                           0.383               -2.30              0.023                                 ok            True                  False
  SOXL           64.29               28            2.58              0.89         48.69               265.73         0.929          pass              0.365             50.8                           0.324              -28.31             -0.478            downtrend_blocked_slope           False                  False
  INTC           68.97               29            1.83              0.71         54.87               143.31         0.818          pass              0.333             41.6                           0.303               -7.05             -0.119           downtrend_blocked_streak           False                  False
  DRAM           64.71               34            0.39              0.11         38.88               109.09         0.736          pass              0.460             75.3                           0.389              -14.03             -0.413 downtrend_blocked_slope_and_streak           False                  False
  LRCX           66.67               33            1.16              1.71        209.96               104.84         0.688          pass              0.350             42.5                           0.258               -5.96              0.410           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118141004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118141004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118141004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118141004)

</details>

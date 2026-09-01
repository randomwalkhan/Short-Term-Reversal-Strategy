# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 11:55:07 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$47,718.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           87.50               16            1.14              0.37         45.76               551.67         1.000          pass              0.340              0.0                           0.171               -0.27             -0.139                      ok            True                  False
  TEAM           82.61               23            3.15              4.28        192.34               115.35         0.715          pass              0.263             11.7                           0.233               15.37              1.401                      ok            True                  False
  DRAM           82.86               35            0.67              0.27         56.79                66.99         0.599          pass              0.534             77.1                           0.856                2.58              0.153                      ok            True                  False
   TRI           93.75               32            0.84              0.63        107.05                60.77         0.595          pass              0.714             46.9                           0.574                8.13              0.529                      ok            True                  False
  SHOP           92.31               13            3.38              3.49        145.88                69.51         0.592          pass              0.451             14.4                           0.274               -4.21              0.030                      ok            True                  False
  CSCO           81.48               27            1.19              0.92        110.09                40.87         0.553          pass              0.254             15.4                           0.319               -3.30             -0.104                      ok            True                  False
  PAYX          100.00               22            0.82              0.73        127.03                24.69         0.549          pass              0.632             32.3                           0.463                6.54              0.626                      ok            True                  False
  CPRT           80.00               25            1.52              0.35         32.84                40.13         0.514          pass              0.234             27.5                           0.394                2.49              0.087                      ok            True                  False
  IDXX           88.24               17            1.74              6.78        553.79                29.41         0.509          pass              0.416             33.1                           0.568                0.17             -0.041                      ok            True                  False
  INSM           81.82               22            1.78              1.52        121.17               109.80         0.799          pass              0.226              5.8                           0.227               -6.75             -0.735 downtrend_blocked_slope           False                  False
  ABNB           95.00               40            0.17              0.22        183.13                62.80         0.633          pass              0.934             90.3                           0.738                2.02              0.106                      ok           False                  False
   STX           86.11               36            0.53              3.09        827.06                71.45         0.611          pass              0.647             83.2                           0.721              -17.17             -1.164 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-01T11:55:07.200979-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:50:02.104495-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:45:02.019132-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "entry_ask": 12.75, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 12.225, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 39, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.59, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.718, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.843, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.718, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:40:05.886827-04:00 early_entry_1140 early_entry_shadow  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "entry_ask": 12.6, "entry_bid": 11.55, "entry_mode": "early", "entry_option_price": 12.075, "hypothetical_budget": 23859.05, "hypothetical_contracts": 19, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 8.7, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.869, "early_reclaim_pct": 76.4, "matched_signals": 40, "recovery_stability_score": 0.713, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:35:02.066939-04:00 early_entry_1135 early_entry_shadow      {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "entry_ask": 12.3, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 11.9, "hypothetical_budget": 23859.05, "hypothetical_contracts": 20, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 358.0, "option_spread_pct": 6.72, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.83, "early_reclaim_pct": 67.9, "matched_signals": 38, "recovery_stability_score": 0.626, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T11:30:06.192762-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:25:02.972583-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:20:06.559055-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:15:02.069821-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-01T11:10:03.158617-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901115507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901115507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901115507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901115507)

</details>

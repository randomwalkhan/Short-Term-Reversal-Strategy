# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 14:00:02 EDT`
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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           83.33               12            1.77              0.72         58.04                61.52         0.689          pass              0.289             39.2                           0.637                3.24              0.202                      ok            True                  False
   KDP           85.00               20            0.91              0.20         31.36                34.46         0.590          pass              0.410             50.4                           0.657                2.99              0.042                      ok            True                  False
   CSX           91.67               12            1.25              0.44         50.55                28.82         0.583          pass              0.484             33.9                           0.476                1.37              0.261                      ok            True                  False
  AAPL           91.67               12            1.45              3.43        336.72                28.00         0.580          pass              0.512             43.1                           0.657                1.77              0.198                      ok            True                  False
  VRTX           84.62               13            1.64              5.54        480.96                33.19         0.571          pass              0.317             39.1                           0.522               -0.19             -0.020                      ok            True                  False
   MAR          100.00               17            1.33              3.55        379.60                28.18         0.560          pass              0.682             59.7                           0.492                3.54              0.351                      ok            True                  False
  MNST           95.45               22            0.75              0.51         97.01                25.74         0.544          pass              0.765             76.9                           0.727               -1.54             -0.248                      ok            True                  False
  ABNB           96.67               30            1.07              1.15        152.52                40.20         0.527          pass              0.763             59.1                           0.523                3.30              0.106                      ok            True                  False
  AMGN           96.15               26            0.77              2.09        386.74                27.22         0.518          pass              0.763             68.3                           0.597                8.28              0.758                      ok            True                  False
  DXCM           83.33               24            1.67              0.88         74.76                45.20         0.517          pass              0.336             33.9                           0.448               -0.32             -0.323                      ok            True                  False
  IDXX           83.33               18            1.95              7.77        566.44                36.22         0.504          pass              0.279             28.7                           0.596                3.33             -0.025                      ok            True                  False
  ISRG           82.86               35            0.82              2.02        352.23                72.57         0.636          pass              0.476             56.6                           0.500               -9.96             -0.970 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-30T12:00:05.999997-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:55:01.696793-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "entry_ask": 15.45, "entry_bid": 14.6, "entry_mode": "early", "entry_option_price": 15.025, "hypothetical_budget": 16611.13, "hypothetical_contracts": 11, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 5.66, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.714, "shadow_only": true, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.831, "early_reclaim_pct": 62.3, "matched_signals": 39, "recovery_stability_score": 0.714, "success_rate": 97.44, "ticker": "DASH", "timing_score": 0.503, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T11:50:03.981372-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:45:03.023708-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:40:02.091678-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:35:05.117192-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:30:04.994647-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:25:01.766574-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:20:04.950564-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:15:04.858903-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730140002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730140002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730140002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730140002)

</details>

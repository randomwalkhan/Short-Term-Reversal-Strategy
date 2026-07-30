# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 14:45:04 EDT`
Last processed slot: `manual`

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
  AAPL           92.31               13            1.36              3.22        336.81                28.00         0.580          pass              0.546             46.5                           0.617                1.86              0.202                      ok            True                  False
   CSX           92.31               13            1.21              0.43         50.56                28.82         0.579          pass              0.514             35.9                           0.394                1.41              0.263                      ok            True                  False
  GILD           91.67               12            1.72              1.60        132.05                34.28         0.566          pass              0.527             48.8                           0.641                0.32             -0.126                      ok            True                  False
   MAR          100.00               17            1.34              3.56        379.59                28.18         0.559          pass              0.681             59.5                           0.553                3.54              0.351                      ok            True                  False
  VRTX           91.30               23            1.22              4.14        481.55                33.19         0.539          pass              0.605             54.4                           0.608                0.23             -0.001                      ok            True                  False
  DXCM           81.82               22            1.68              0.89         74.76                45.20         0.527          pass              0.281             33.4                           0.478               -0.33             -0.323                      ok            True                  False
  MNST           96.30               27            0.58              0.39         97.06                25.74         0.523          pass              0.812             82.2                           0.707               -1.37             -0.240                      ok            True                  False
   AEP           80.00               15            1.28              1.16        128.90                20.00         0.521          pass              0.146             20.2                           0.293               -5.34             -0.172                      ok            True                  False
  ABNB           93.94               33            0.81              0.87        152.64                40.20         0.520          pass              0.784             68.9                           0.606                3.57              0.118                      ok            True                   True
  IDXX           81.25               16            2.12              8.47        566.14                36.22         0.502          pass              0.190             22.2                           0.327                3.14             -0.033                      ok            True                  False
  PYPL           78.95               19            1.41              0.58         58.10                61.52         0.663          pass              0.280             51.3                           0.696                3.61              0.218                      ok           False                  False
  ISRG           84.62               39            0.58              1.43        352.49                72.57         0.629          pass              0.587             69.3                           0.687               -9.75             -0.959 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730144504)

</details>

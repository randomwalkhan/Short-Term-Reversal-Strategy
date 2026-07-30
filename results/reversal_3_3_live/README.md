# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 12:05:05 EDT`
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
   KDP           86.36               22            0.73              0.16         31.38                34.46         0.591          pass              0.489             60.0                           0.628                3.17              0.050                      ok            True                  False
   MAR          100.00               13            1.47              3.93        379.44                28.18         0.577          pass              0.644             55.4                           0.670                3.39              0.344                      ok            True                  False
  VRTX           84.62               13            1.65              5.59        480.93                33.19         0.570          pass              0.316             38.5                           0.553               -0.20             -0.020                      ok            True                  False
  MNST           94.12               17            0.91              0.62         96.97                25.74         0.566          pass              0.696             72.0                           0.703               -1.69             -0.255                      ok            True                  False
   XEL          100.00               19            0.74              0.41         78.58                19.80         0.554          pass              0.589             24.7                           0.292               -2.49              0.023                      ok            True                  False
  ABNB           95.65               23            1.46              1.56        152.34                40.20         0.547          pass              0.674             44.4                           0.562                2.89              0.089                      ok            True                  False
  AMGN           94.12               17            1.36              3.69        386.06                27.22         0.539          pass              0.609             44.1                           0.629                7.64              0.731                      ok            True                  False
  PCAR           88.24               17            1.53              1.43        133.26                29.38         0.534          pass              0.370             16.6                           0.264                6.36              0.900                      ok            True                  False
   HON           86.36               22            0.96              1.62        240.42                39.75         0.524          pass              0.417             38.3                           0.654                7.24              1.068                      ok            True                  False
  DASH           97.44               39            0.92              1.25        192.99                53.51         0.501          pass              0.827             61.3                           0.699                2.10             -0.019                      ok            True                   True
  ISRG           78.57               28            1.12              2.78        351.91                72.57         0.655          pass              0.306             40.3                           0.385              -10.24             -0.984 downtrend_blocked_slope           False                  False
  PYPL           75.00                8            2.62              1.07         57.89                61.52         0.653          pass              0.094              9.7                           0.313                2.34              0.162                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730120505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730120505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730120505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730120505)

</details>

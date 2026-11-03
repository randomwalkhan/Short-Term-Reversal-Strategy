# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 11:55:04 EST`
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

- Cash: `$136,446.55`
- Equity: `$136,446.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.91               11            1.18              0.55         66.15                28.20         0.595          pass              0.486             43.1                           0.446                2.52              0.255                                 ok            True                  False
 CMCSA           90.00               20            0.59              0.10         23.83                32.70         0.578          pass              0.590             66.4                           0.409                6.13              0.545                                 ok            True                  False
   PEP           81.82               11            1.45              1.43        139.81                26.86         0.567          pass              0.189             25.5                           0.342                3.25              0.221                                 ok            True                  False
   KHC           83.33               12            1.87              0.33         24.79                33.68         0.560          pass              0.237             26.2                           0.378                2.66              0.152                                 ok            True                  False
   ADP           89.66               29            0.51              1.06        298.32                27.85         0.513          pass              0.665             76.6                           0.652                1.54             -0.166                                 ok            True                  False
   EXC           86.36               22            0.80              0.26         46.34                22.18         0.513          pass              0.428             42.2                           0.447                7.09              0.730                                 ok            True                  False
  TMUS           63.64               11            1.92              2.16        159.23                68.40         0.664          pass              0.163             29.8                           0.360               -0.43              0.104                                 ok           False                  False
   CSX           75.00               12            1.17              0.42         51.44                27.65         0.558          pass              0.157             29.2                           0.293                6.10              0.583                                 ok           False                  False
   ROP           66.67                9            2.00              6.70        476.67                37.35         0.558          pass              0.110             18.0                           0.144               18.02              1.664                                 ok           False                  False
 GOOGL           88.10               42            0.14              0.27        278.87                50.76         0.557          pass              0.744             90.8                           0.658              -18.13             -2.170 downtrend_blocked_slope_and_streak           False                  False
  PAYX           76.92               26            0.21              0.17        115.42                35.36         0.557          pass              0.442             93.1                           0.810                3.37             -0.029                                 ok           False                  False
  GOOG           88.10               42            0.12              0.24        277.94                49.16         0.553          pass              0.746             91.6                           0.564              -17.45             -2.083 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-03T11:55:04.283382-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:50:06.620716-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:45:05.991467-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:40:01.980819-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:35:05.840286-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:05.077695-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:25:04.545060-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:20:06.072141-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:15:01.990433-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:10:06.114764-05:00 early_entry_1110 early_entry_shadow {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 68223.28, "hypothetical_contracts": 99, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103115504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103115504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103115504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103115504)

</details>

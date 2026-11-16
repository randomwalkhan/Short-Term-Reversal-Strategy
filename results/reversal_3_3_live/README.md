# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 13:25:03 EST`
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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           88.24               34            0.84              1.01        172.04                68.34         0.587          pass              0.641             67.7                           0.384                5.52              0.739                      ok            True                  False
   CEG           83.33               18            2.29              4.48        277.85                61.55         0.582          pass              0.205              1.7                           0.074                6.27              1.192                      ok            True                  False
   TXN           81.82               11            2.34              4.97        301.47                58.41         0.580          pass              0.261             49.3                           0.513               -1.83              0.089                      ok            True                  False
  CTAS           95.65               23            0.61              0.96        225.83                28.07         0.566          pass              0.614             23.5                           0.298                0.27              0.062                      ok            True                  False
  AAPL           95.65               23            0.76              1.90        355.45                27.52         0.555          pass              0.607             21.7                           0.404                4.58              0.583                      ok            True                  False
   HON           80.95               21            1.08              1.69        221.74                32.11         0.548          pass              0.157              1.2                           0.077               -1.35             -0.007                      ok            True                  False
  NXPI           95.45               22            1.80              3.35        263.66                48.08         0.518          pass              0.699             55.7                           0.505                1.19              0.334                      ok            True                  False
  ALNY           57.89               19            2.58              2.98        163.76               110.81         0.716          pass              0.178             15.5                           0.157                1.76              0.130                      ok           False                  False
  FTNT           45.45               11            3.29              2.93        125.97                93.31         0.651          pass              0.083              3.7                           0.240               -2.51             -0.021                      ok           False                  False
  INTC           50.00                6            7.32              3.06         58.35               143.21         0.610          pass              0.061              0.0                           0.170               -7.80              0.066                      ok           False                  False
  MELI           57.14               14            2.28             23.81       1481.29                60.76         0.598          pass              0.111              8.3                           0.226              -13.08             -1.515 downtrend_blocked_slope           False                  False
   ADI           70.00               10            2.79              7.78        394.63                66.18         0.586          pass              0.163             34.9                           0.429               -6.30             -0.171                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-16T12:00:06.189973-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:55:04.372932-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:50:05.541562-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:45:04.541902-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:40:05.500831-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:35:03.430976-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:30:04.371241-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:25:06.045979-05:00 early_entry_1125 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "entry_ask": 11.05, "entry_bid": 10.65, "entry_mode": "early", "entry_option_price": 10.85, "hypothetical_budget": 58512.4, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 3.69, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.58, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T11:20:06.269332-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:15:03.556110-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116132503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116132503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116132503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116132503)

</details>

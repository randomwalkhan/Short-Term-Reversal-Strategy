# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 11:55:01 EDT`
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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           84.62               13            2.94              6.42        308.71                64.14         0.584          pass              0.267             22.0                           0.250                5.89              0.516                                 ok            True                  False
  META           81.82               22            1.35              6.31        666.51                55.99         0.578          pass              0.306             40.0                           0.396               17.35              1.713                                 ok            True                  False
   ADI           80.00               15            2.57              7.11        392.60                55.18         0.574          pass              0.108              5.6                           0.110               -1.61             -0.045                                 ok            True                  False
  QCOM           81.48               27            1.62              2.15        188.24                63.33         0.568          pass              0.381             57.1                           0.349               -1.39              0.237                                 ok            True                  False
  UPRO           90.91               22            1.42              1.45        145.54                40.56         0.561          pass              0.524             32.4                           0.247                3.84              0.378                                 ok            True                  False
   LIN          100.00               14            1.14              4.24        527.97                20.88         0.548          pass              0.533             17.3                           0.357                2.48              0.045                                 ok            True                  False
  AMGN           90.00               10            1.62              4.13        361.62                21.45         0.544          pass              0.390             23.0                           0.452               -0.85             -0.073                                 ok            True                  False
  CSCO           94.44               18            1.35              1.14        120.82                35.64         0.539          pass              0.671             59.6                           0.538                2.06              0.331                                 ok            True                  False
  ABNB           93.33               15            2.20              2.29        147.64                37.12         0.520          pass              0.538             32.3                           0.388               -1.24             -0.025                                 ok            True                  False
  ROST           89.29               28            0.92              1.43        222.27                30.69         0.513          pass              0.473             18.2                           0.283                5.75              0.669                                 ok            True                  False
   MAR           90.91               11            1.86              4.89        374.02                19.73         0.513          pass              0.411             20.9                           0.292               -1.53              0.021                                 ok            True                  False
  KLAC           75.00               12            4.10              6.64        228.67               110.61         0.650          pass              0.137             19.6                           0.187              -20.24             -2.595 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-13T11:55:01.971433-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:50:06.106391-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:35:02.081051-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:30:05.079424-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:25:02.062910-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:20:02.121903-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:15:04.147580-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:10:02.119516-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "SNPS260814C00445000", "current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "entry_ask": 27.0, "entry_bid": 20.8, "entry_mode": "early", "entry_option_price": 23.9, "hypothetical_budget": 13497.63, "hypothetical_contracts": 5, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 25.94, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "matched_signals": 39, "recovery_stability_score": 0.603, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T11:05:06.382767-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:00:04.971643-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713115501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713115501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713115501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713115501)

</details>

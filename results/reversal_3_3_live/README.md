# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 14:05:01 EDT`
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
  META           81.82               22            1.35              6.31        666.51                55.99         0.578          pass              0.306             40.0                           0.358               17.35              1.713                                 ok            True                  False
  UPRO           93.75               16            1.99              2.04        145.29                40.56         0.565          pass              0.513             16.8                           0.291                3.24              0.352                                 ok            True                  False
  QCOM           80.00               25            1.89              2.51        188.09                63.33         0.562          pass              0.306             50.0                           0.436               -1.66              0.225                                 ok            True                  False
   LIN          100.00               12            1.25              4.63        527.81                20.88         0.555          pass              0.498              9.8                           0.231                2.37              0.040                                 ok            True                  False
  AMGN           93.75               16            1.18              3.00        362.10                21.45         0.535          pass              0.592             44.0                           0.639               -0.40             -0.052                                 ok            True                  False
  CSCO           95.65               23            1.00              0.85        120.95                35.64         0.529          pass              0.750             70.1                           0.720                2.42              0.347                                 ok            True                  False
  ROST           89.29               28            0.96              1.50        222.24                30.69         0.509          pass              0.490             23.7                           0.269                5.71              0.667                                 ok            True                  False
  KLAC           72.73               11            4.49              7.28        228.40               110.61         0.626          pass              0.122             17.6                           0.376              -20.57             -2.613 downtrend_blocked_slope_and_streak           False                  False
   KDP           84.62               13            0.90              0.20         31.58                34.17         0.607          pass              0.204              0.0                           0.192               -6.31             -0.695 downtrend_blocked_slope_and_streak           False                  False
    MU           80.00               15            4.84             33.15        965.09               112.95         0.595          pass              0.208             38.3                           0.535              -18.62             -1.884            downtrend_blocked_slope           False                  False
   ADI           78.57               14            2.61              7.24        392.55                55.18         0.570          pass              0.139             18.6                           0.420               -1.65             -0.047                                 ok           False                  False
   TXN           80.00                5            4.00              8.72        307.72                64.14         0.564          pass              0.063              2.2                           0.176                4.74              0.466                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-13T12:00:04.108537-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:55:01.971433-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:50:06.106391-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:35:02.081051-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:30:05.079424-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:25:02.062910-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:20:02.121903-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:15:04.147580-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:10:02.119516-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "SNPS260814C00445000", "current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "entry_ask": 27.0, "entry_bid": 20.8, "entry_mode": "early", "entry_option_price": 23.9, "hypothetical_budget": 13497.63, "hypothetical_contracts": 5, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 25.94, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "matched_signals": 39, "recovery_stability_score": 0.603, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T11:05:06.382767-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713140501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713140501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713140501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713140501)

</details>

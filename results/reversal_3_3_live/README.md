# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 14:45:05 EDT`
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

- Cash: `$122,431.80`
- Equity: `$122,431.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CEG     option         option CEG261120C00270000     33          2026-10-15         2026-10-16         19.1       17.19 -6303.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.96               23            1.41              2.71        273.84                60.14         0.568            pass              0.412             27.7                           0.284                5.30              0.142                                 ok            True                  False
  ABNB           90.00               30            0.95              1.15        173.79                41.32         0.527            pass              0.571             39.6                           0.549                6.28              0.664                                 ok            True                  False
  DXCM           80.00               10            1.96              1.20         87.19                29.21         0.507            pass              0.075              8.0                           0.241                0.74              0.102                                 ok            True                  False
  PAYX           79.41               34            0.54              0.42        110.60                41.26         0.549            pass              0.320             35.0                           0.386               11.37              1.145                                 ok           False                  False
  CSCO           75.00                8            2.02              1.55        109.18                35.07         0.532            pass              0.096             14.3                           0.367               -4.07             -0.420 downtrend_blocked_slope_and_streak           False                  False
  SNPS           60.00                5            3.60             11.79        463.06                53.97         0.522            pass              0.099             15.4                           0.297               -7.89             -0.689 downtrend_blocked_slope_and_streak           False                  False
  QCOM           70.00               10            3.09              3.86        176.74                54.84         0.520            pass              0.089             12.2                           0.260               -6.49             -0.494 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00                3            2.45              9.25        535.48                21.00         0.510            pass              0.487             12.0                           0.229                1.68              0.274                                 ok           False                  False
  MPWR           73.68               19            2.34             20.44       1240.44                56.34         0.507            pass              0.202             30.5                           0.337              -15.26             -2.008            downtrend_blocked_slope           False                  False
  META           75.00                4            4.20             21.67        727.43                55.08         0.501            pass              0.052              0.7                           0.121               -3.07             -0.044           downtrend_blocked_streak           False                  False
  CDNS           77.78               18            1.78              4.05        322.64                38.31         0.500            pass              0.176             24.1                           0.388               -9.32             -1.112 downtrend_blocked_slope_and_streak           False                  False
  VRTX           62.50                8            1.91              6.79        505.84                25.61         0.497 below_threshold              0.067              5.8                           0.265               -1.13             -0.103                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-10-16T12:00:06.321774-04:00 early_entry_1200 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:55:06.475716-04:00 early_entry_1155 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:50:05.492018-04:00 early_entry_1150 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:45:05.286618-04:00 early_entry_1145 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:40:05.599147-04:00 early_entry_1140 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:40:05.599147-04:00      manage_1130               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 17.19, "pnl": -6303.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CEG"}
2026-10-16T11:35:05.403603-04:00 early_entry_1135 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:30:05.425810-04:00 early_entry_1130 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:25:04.296462-04:00 early_entry_1125 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:20:05.272593-04:00 early_entry_1120 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016144505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016144505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016144505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016144505)

</details>

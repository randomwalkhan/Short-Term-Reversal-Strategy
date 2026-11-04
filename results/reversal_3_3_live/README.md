# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:25:01 EST`
Last processed slot: `manage_1130`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           60.00               10            5.22              2.21         59.60               129.60         0.670            pass              0.116             16.4                           0.351              -38.26             -5.056            downtrend_blocked_slope           False                  False
  FTNT           91.67               48            0.06              0.05        128.09                91.30         0.653            pass              0.869             97.6                           0.465              -26.44             -4.257 downtrend_blocked_slope_and_streak           False                  False
  REGN           70.59               17            1.66             11.31        968.51                48.26         0.527            pass              0.248             49.6                           0.529               18.81              2.150                                 ok           False                  False
    ZS           90.91               33            1.44              2.28        224.11                64.45         0.520            pass              0.602             35.1                           0.209               -4.10             -0.957 downtrend_blocked_slope_and_streak           False                  False
  AVGO           66.67               18            1.98              4.60        330.16                44.04         0.503            pass              0.214             36.7                           0.443               -3.62             -0.075                                 ok           False                  False
  TEAM           94.74               19            2.33              3.12        189.71                53.65         0.499 below_threshold              0.582             26.3                           0.158              -17.26             -2.305            downtrend_blocked_slope           False                  False
   TXN           86.96               23            1.11              2.43        311.45                35.19         0.496 below_threshold              0.501             59.7                           0.582                9.09              1.031                                 ok           False                  False
  SNPS           60.00               20            1.66              5.39        460.57                45.79         0.493 below_threshold              0.210             31.2                           0.303                0.89              0.673                                 ok           False                  False
  CSCO           82.76               29            0.56              0.41        102.80                32.31         0.491 below_threshold              0.401             50.4                           0.236               -4.54             -0.527 downtrend_blocked_slope_and_streak           False                  False
  PANW           80.95               42            0.44              1.07        349.74                58.95         0.484 below_threshold              0.521             82.5                           0.413                0.41             -0.412                                 ok           False                  False
  CDNS           80.56               36            0.59              1.34        323.18                42.30         0.480 below_threshold              0.387             50.3                           0.414               -1.30              0.244                                 ok           False                  False
   AEP           50.00                2            2.19              1.99        129.01                19.14         0.480 below_threshold              0.209             53.6                           0.612               -0.30             -0.015                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-04T11:25:01.112223-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:10:06.095882-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:05:05.102696-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:00:06.142826-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:55:05.872153-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:50:01.073717-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:06.756427-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104112501)

</details>

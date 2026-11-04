# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:45:06 EST`
Last processed slot: `early_entry_1045`

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
   TXN           82.35               17            1.48              3.25        311.10                35.19         0.516            pass              0.197             12.1                           0.206                8.68              1.013                                 ok            True                  False
  INTC           54.55               11            4.39              1.86         59.75               129.60         0.719            pass              0.083              1.5                           0.066              -37.73             -5.017            downtrend_blocked_slope           False                  False
  REGN           87.50                8            2.22             15.15        966.87                48.26         0.567            pass              0.354             32.5                           0.312               18.13              2.124                                 ok           False                  False
    ZS           91.89               37            0.88              1.39        224.49                64.45         0.531            pass              0.731             60.3                           0.338               -3.56             -0.931 downtrend_blocked_slope_and_streak           False                  False
  DRAM           61.54               13            3.83              1.28         47.09                69.30         0.517            pass              0.072              0.0                           0.163               -6.80             -0.201                                 ok           False                  False
  AVGO           69.57               23            1.60              3.72        330.53                44.04         0.509            pass              0.195             19.0                           0.150               -3.25             -0.057                                 ok           False                  False
  LRCX           64.86               37            0.92              1.48        230.08                62.98         0.501            pass              0.440             70.0                           0.369              -12.35             -0.558            downtrend_blocked_slope           False                  False
  SNPS           70.37               27            1.18              3.84        461.24                45.79         0.500            pass              0.216             17.5                           0.244                1.38              0.695                                 ok           False                  False
  ASML           71.43                7            3.22             34.96       1537.16                44.05         0.498 below_threshold              0.050              0.0                           0.177              -10.29             -0.590            downtrend_blocked_slope           False                  False
  NVDA           76.47               17            1.54              2.22        205.74                32.59         0.496 below_threshold              0.231             44.7                           0.284               -8.32             -0.724 downtrend_blocked_slope_and_streak           False                  False
  PANW           81.40               43            0.33              0.81        349.85                58.95         0.485 below_threshold              0.546             86.7                           0.467                0.52             -0.408                                 ok           False                  False
  INSM           84.00               50            0.09              0.06        104.41                60.46         0.483 below_threshold              0.638             94.5                           0.581               10.96              1.732                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:06.756427-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:35:02.831899-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:30:06.151589-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:25:06.359695-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:05.290161-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104104506)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:20:06 EST`
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
   TXN           82.35               17            1.34              2.93        311.24                35.19         0.514            pass              0.315             51.3                           0.505                8.84              1.020                                 ok            True                  False
  INTC           54.55               11            4.83              2.05         59.67               129.60         0.681            pass              0.143             22.6                           0.401              -38.01             -5.038            downtrend_blocked_slope           False                  False
  REGN           70.59               17            1.62             11.06        968.62                48.26         0.529            pass              0.252             50.7                           0.576               18.85              2.152                                 ok           False                  False
    ZS           89.66               29            1.73              2.73        223.92                64.45         0.526            pass              0.503             22.2                           0.162               -4.38             -0.970 downtrend_blocked_slope_and_streak           False                  False
  AVGO           66.67               21            1.77              4.12        330.36                44.04         0.497 below_threshold              0.253             43.3                           0.439               -3.42             -0.065                                 ok           False                  False
  SNPS           66.67               18            1.98              6.43        460.12                45.79         0.493 below_threshold              0.156             17.9                           0.317                0.56              0.658                                 ok           False                  False
  CSCO           84.38               32            0.28              0.20        102.88                32.31         0.492 below_threshold              0.538             75.2                           0.338               -4.27             -0.514 downtrend_blocked_slope_and_streak           False                  False
  TEAM           96.30               27            1.72              2.30        190.07                53.65         0.489 below_threshold              0.700             45.8                           0.234              -16.73             -2.276            downtrend_blocked_slope           False                  False
  NVDA           73.33               15            1.87              2.71        205.53                32.59         0.485 below_threshold              0.180             32.7                           0.360               -8.63             -0.740 downtrend_blocked_slope_and_streak           False                  False
  CDNS           80.56               36            0.57              1.30        323.19                42.30         0.481 below_threshold              0.391             51.7                           0.462               -1.28              0.244                                 ok           False                  False
  PANW           81.40               43            0.41              1.00        349.77                58.95         0.480 below_threshold              0.536             83.6                           0.437                0.44             -0.411                                 ok           False                  False
  ASML           66.67                6            3.35             36.43       1536.53                44.05         0.478 below_threshold              0.134             28.9                           0.422              -10.41             -0.596            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:10:06.095882-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:05:05.102696-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:00:06.142826-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:55:05.872153-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:50:01.073717-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:06.756427-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:35:02.831899-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104112006)

</details>

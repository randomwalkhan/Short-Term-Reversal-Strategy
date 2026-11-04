# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:05:05 EST`
Last processed slot: `manage_1100`

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
  REGN           80.00               15            1.70             11.59        968.39                48.26         0.547            pass              0.233             48.4                           0.628               18.76              2.148                                 ok            True                  False
  FTNT           91.49               47            0.10              0.09        128.07                91.30         0.656            pass              0.860             95.8                           0.425              -26.47             -4.259 downtrend_blocked_slope_and_streak           False                  False
  INTC           62.50                8            6.12              2.59         59.44               129.60         0.635            pass              0.063              0.0                           0.150              -38.85             -5.100            downtrend_blocked_slope           False                  False
   AEP           75.00                4            1.57              1.43        129.25                19.14         0.529            pass              0.253             66.7                           0.866                0.33              0.014                                 ok           False                  False
    ZS           91.18               34            1.29              2.04        224.22                64.45         0.523            pass              0.636             41.9                           0.222               -3.96             -0.950 downtrend_blocked_slope_and_streak           False                  False
  QCOM           93.33               30            0.91              1.04        163.98                52.10         0.515            pass              0.717             58.7                           0.261               -8.44             -0.956            downtrend_blocked_slope           False                  False
  SNPS           63.64               22            1.55              5.01        460.73                45.79         0.492 below_threshold              0.237             36.0                           0.264                1.00              0.678                                 ok           False                  False
  PANW           81.40               43            0.29              0.71        349.90                58.95         0.488 below_threshold              0.551             88.4                           0.373                0.56             -0.406                                 ok           False                  False
  NXPI           96.00               25            1.29              2.38        261.77                42.74         0.483 below_threshold              0.548              0.0                           0.183                7.03              1.063                                 ok           False                  False
  AVGO           54.55               11            2.85              6.63        329.29                44.04         0.483 below_threshold              0.055              0.0                           0.157               -4.48             -0.115                                 ok           False                  False
   TXN           57.14                7            2.52              5.52        310.12                35.19         0.481 below_threshold              0.056              2.8                           0.185                7.53              0.965                                 ok           False                  False
  NVDA           70.00               10            2.41              3.49        205.20                32.59         0.480 below_threshold              0.088             13.4                           0.130               -9.13             -0.765 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-04T11:05:05.102696-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:00:06.142826-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:55:05.872153-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:50:01.073717-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:06.756427-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:35:02.831899-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:30:06.151589-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:25:06.359695-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104110505)

</details>

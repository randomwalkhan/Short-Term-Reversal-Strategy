# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:15:06 EST`
Last processed slot: `early_entry_1115`

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
  INTC           54.55               11            4.41              1.87         59.75               129.60         0.703            pass              0.165             29.4                           0.348              -37.74             -5.018            downtrend_blocked_slope           False                  False
    ZS           90.91               33            1.49              2.36        224.08                64.45         0.517            pass              0.594             32.8                           0.202               -4.15             -0.959 downtrend_blocked_slope_and_streak           False                  False
  REGN           72.73               22            1.43              9.77        969.17                48.26         0.512            pass              0.301             56.5                           0.628               19.08              2.160                                 ok           False                  False
  AVGO           64.71               17            2.02              4.70        330.11                44.04         0.504            pass              0.203             35.3                           0.322               -3.67             -0.077                                 ok           False                  False
  CSCO           84.38               32            0.28              0.20        102.88                32.31         0.492 below_threshold              0.538             75.2                           0.337               -4.27             -0.514 downtrend_blocked_slope_and_streak           False                  False
  LRCX           66.67               30            1.76              2.84        229.50                62.98         0.489 below_threshold              0.333             50.1                           0.355              -13.09             -0.597            downtrend_blocked_slope           False                  False
  NVDA           73.33               15            1.80              2.61        205.57                32.59         0.489 below_threshold              0.188             35.1                           0.305               -8.56             -0.737 downtrend_blocked_slope_and_streak           False                  False
  SNPS           73.33               30            1.01              3.27        461.48                45.79         0.486 below_threshold              0.357             58.2                           0.538                1.55              0.703                                 ok           False                  False
  PANW           82.61               46            0.06              0.15        350.14                58.95         0.485 below_threshold              0.611             97.5                           0.482                0.79             -0.395                                 ok           False                  False
  TEAM           96.88               32            1.32              1.77        190.29                53.65         0.483 below_threshold              0.769             58.2                           0.282              -16.40             -2.258            downtrend_blocked_slope           False                  False
   TXN           88.89               27            0.97              2.12        311.58                35.19         0.481 below_threshold              0.593             64.7                           0.476                9.25              1.037                                 ok           False                  False
   AEP           50.00                2            2.20              2.00        129.00                19.14         0.480 below_threshold              0.208             53.4                           0.775               -0.31             -0.015                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:10:06.095882-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:05:05.102696-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:00:06.142826-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:55:05.872153-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:50:01.073717-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:06.756427-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:35:02.831899-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:30:06.151589-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104111506)

</details>

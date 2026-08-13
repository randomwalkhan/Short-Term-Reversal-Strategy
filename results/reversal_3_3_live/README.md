# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 11:10:09 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   ROP          100.00               29            0.92              2.53        394.14                44.32         0.601          pass              0.611              8.1                           0.156                0.61              0.164                       ok            True                  False
  MPWR           84.21               38            0.69              6.89       1422.06                55.33         0.547          pass              0.481             42.3                           0.468                7.52              0.604                       ok            True                  False
  PCAR           95.45               22            1.40              1.28        130.51                29.70         0.535          pass              0.573             13.3                           0.163               -3.39             -0.213                       ok            True                  False
   BKR           83.33               24            1.18              0.53         64.05                33.24         0.517          pass              0.406             57.3                           0.691                6.43              0.784                       ok            True                  False
  INSM           69.23               13            2.96              2.74        131.10               107.72         0.737          pass              0.139             15.0                           0.314               26.48              3.762                       ok           False                  False
  ISRG           86.49               37            0.35              0.99        400.84                69.94         0.673          pass              0.590             56.6                           0.437               13.28              1.337                       ok           False                  False
  FAST          100.00               24            0.47              0.17         52.15                25.01         0.571          pass              0.724             57.8                           0.401               11.39              1.197                       ok           False                  False
  BKNG           97.50               40            0.30              0.44        212.07                44.60         0.548          pass              0.904             83.0                           0.461                9.51              1.213                       ok           False                  False
   HON           90.32               31            0.70              1.15        234.85                35.57         0.529          pass              0.592             41.3                           0.424               -3.40             -0.604  downtrend_blocked_slope           False                  False
  ADSK           79.31               29            1.23              2.14        248.59                45.76         0.516          pass              0.356             59.3                           0.327                4.89              0.819                       ok           False                  False
  ROST           81.82               11            1.87              3.24        246.86                22.10         0.516          pass              0.165             19.4                           0.142               -3.55             -0.147 downtrend_blocked_streak           False                  False
  CTSH           88.37               43            0.30              0.12         58.15                52.45         0.510          pass              0.742             89.3                           0.416                7.65              0.767                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-13T11:10:09.886626-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:05:09.901418-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:00:08.468855-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:55:08.693001-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:50:06.656727-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:45:05.716693-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:40:10.431028-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:35:08.719100-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:30:06.616446-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:25:07.519899-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813111009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813111009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813111009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813111009)

</details>

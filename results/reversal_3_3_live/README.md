# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 11:55:05 EST`
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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           93.75               16            0.93              0.16         24.78                35.54         0.588          pass              0.528             20.7                           0.188                7.79              1.094                                 ok            True                  False
  GILD           91.67               12            1.71              2.09        173.59                33.00         0.542          pass              0.422             14.4                           0.177                9.10              1.137                                 ok            True                  False
  AAPL          100.00               14            1.26              3.08        348.19                25.40         0.535          pass              0.515             11.6                           0.183               -0.89             -0.164                                 ok            True                  False
   KHC           86.96               23            1.20              0.21         25.35                36.26         0.519          pass              0.404             26.5                           0.236                0.18              0.160                                 ok            True                  False
   CSX           80.95               21            0.84              0.31         51.96                28.96         0.515          pass              0.361             70.4                           0.383               -0.03              0.034                                 ok            True                  False
  SBUX           83.33               12            1.85              1.42        109.09                28.08         0.511          pass              0.159              1.9                           0.074                5.65              0.640                                 ok            True                  False
  ORLY           95.24               21            1.19              0.77         92.01                25.40         0.504          pass              0.588             21.4                           0.243               -0.83              0.021                                 ok            True                  False
  ALNY           87.23               47            0.39              0.44        160.89               108.65         0.682          pass              0.642             60.4                           0.349              -29.40             -4.715            downtrend_blocked_slope           False                  False
  INTC           54.55               11            4.99              2.04         57.40               128.90         0.643          pass              0.224             50.9                           0.630              -35.24             -5.678            downtrend_blocked_slope           False                  False
  FTNT           60.00                5            4.23              3.83        127.75                91.87         0.628          pass              0.096             11.1                           0.180              -28.36             -4.613 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           78.57               14            1.58              3.20        287.56                52.55         0.594          pass              0.270             61.5                           0.497              -12.29             -1.695            downtrend_blocked_slope           False                  False
  GOOG           80.00               15            1.49              2.99        286.02                51.02         0.587          pass              0.277             61.5                           0.465              -11.76             -1.631            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T11:55:05.652080-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:50:05.625919-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:45:05.647675-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:40:04.478665-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:35:06.672345-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:30:06.947630-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:25:06.091579-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:20:06.476287-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:15:05.542359-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:10:04.336352-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105115505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105115505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105115505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105115505)

</details>

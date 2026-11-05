# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 12:20:06 EST`
Last processed slot: `manage_1230`

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
 CMCSA           92.86               14            1.11              0.19         24.77                35.54         0.587          pass              0.478             16.7                           0.255                7.60              1.085                                 ok            True                  False
  REGN           80.00               10            2.02             13.16        925.03                52.52         0.583          pass              0.069              3.7                           0.086               11.33              1.942                                 ok            True                  False
   MAR           80.00               10            1.43              4.26        423.04                23.45         0.535          pass              0.106             17.4                           0.330                5.54              0.824                                 ok            True                  False
  AAPL          100.00               16            1.17              2.86        348.28                25.40         0.528          pass              0.546             17.9                           0.307               -0.80             -0.160                                 ok            True                  False
  ORLY          100.00               13            1.65              1.07         91.88                25.40         0.528          pass              0.485              4.1                           0.219               -1.29             -0.000                                 ok            True                  False
   KHC           85.71               21            1.36              0.24         25.34                36.26         0.520          pass              0.328             16.9                           0.305                0.02              0.153                                 ok            True                  False
  ALNY           83.33               36            0.98              1.11        160.60               108.65         0.700          pass              0.419             28.9                           0.249              -29.82             -4.742            downtrend_blocked_slope           False                  False
  FTNT           55.56                9            3.34              3.03        128.09                91.87         0.654          pass              0.154             29.7                           0.612              -27.70             -4.571 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.80               41            0.05              0.06        159.15                70.30         0.636          pass              0.734             87.4                           0.509                0.19              0.652                                 ok           False                  False
  INTC           62.50                8            6.04              2.46         57.21               128.90         0.605          pass              0.182             40.6                           0.415              -35.96             -5.728            downtrend_blocked_slope           False                  False
  MDLZ           95.45               22            0.47              0.22         67.28                30.79         0.572          pass              0.581             14.7                           0.234                2.87              0.577                                 ok           False                  False
 GOOGL           85.71               28            0.89              1.81        288.15                52.55         0.559          pass              0.563             78.2                           0.813              -11.68             -1.663            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T12:00:04.376215-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:55:05.652080-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:50:05.625919-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:45:05.647675-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:40:04.478665-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:35:06.672345-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:30:06.947630-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:25:06.091579-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:20:06.476287-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:15:05.542359-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105122006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105122006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105122006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105122006)

</details>

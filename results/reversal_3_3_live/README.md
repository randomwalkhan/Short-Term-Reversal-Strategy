# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 13:50:06 EST`
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
  ORLY           93.33               15            1.37              0.89         91.96                25.40         0.526          pass              0.506             21.4                           0.360               -1.01              0.013                                 ok            True                  False
  CTAS           95.65               23            0.95              1.53        228.38                27.17         0.515          pass              0.591             17.6                           0.249                1.25              0.221                                 ok            True                  False
  ALNY           83.33               36            0.96              1.08        160.62               108.65         0.702          pass              0.427             31.6                           0.378              -29.80             -4.740            downtrend_blocked_slope           False                  False
  GOOG           80.00               10            1.78              3.59        285.76                51.02         0.598          pass              0.221             53.8                           0.450              -12.03             -1.645            downtrend_blocked_slope           False                  False
 GOOGL           75.00                8            2.05              4.14        287.15                52.55         0.597          pass              0.210             50.1                           0.432              -12.71             -1.717            downtrend_blocked_slope           False                  False
  REGN           76.92               13            1.79             11.67        925.67                52.52         0.573          pass              0.152             25.0                           0.299               11.59              1.952                                 ok           False                  False
  FTNT           60.00                5            5.15              4.67        127.39                91.87         0.566          pass              0.080              7.9                           0.223              -29.06             -4.657 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           92.86               28            0.14              0.02         24.84                35.54         0.561          pass              0.787             89.4                           0.718                8.65              1.130                                 ok           False                  False
  MDLZ           96.30               27            0.31              0.15         67.32                30.79         0.552          pass              0.701             44.0                           0.335                3.04              0.584                                 ok           False                  False
  AAPL          100.00                8            1.65              4.04        347.78                25.40         0.541          pass              0.522             22.5                           0.395               -1.29             -0.182                                 ok           False                  False
   CSX           75.00                4            2.04              0.75         51.78                28.96         0.539          pass              0.139             28.3                           0.195               -1.24             -0.022                                 ok           False                  False
   MAR           77.78                9            1.50              4.45        422.96                23.45         0.533          pass              0.126             24.1                           0.382                5.47              0.821                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105135006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105135006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105135006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105135006)

</details>

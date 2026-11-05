# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 14:10:05 EST`
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
 CMCSA           90.91               22            0.50              0.09         24.81                35.54         0.574          pass              0.615             62.1                           0.416                8.25              1.113                                 ok            True                  False
  ORLY          100.00               14            1.43              0.93         91.94                25.40         0.534          pass              0.533             17.7                           0.218               -1.07              0.010                                 ok            True                  False
   MAR           81.82               11            1.35              4.01        423.15                23.45         0.533          pass              0.203             31.6                           0.466                5.63              0.828                                 ok            True                  False
   XEL           81.82               11            1.18              0.66         80.22                19.85         0.518          pass              0.244             45.7                           0.247                0.82              0.239                                 ok            True                  False
  CTAS           95.65               23            0.98              1.56        228.36                27.17         0.513          pass              0.607             22.9                           0.347                1.23              0.220                                 ok            True                  False
   KHC           90.62               32            0.55              0.10         25.40                36.26         0.507          pass              0.679             66.3                           0.449                0.84              0.190                                 ok            True                  False
  ALNY           82.86               35            1.04              1.18        160.58               108.65         0.702          pass              0.389             25.3                           0.350              -29.87             -4.744            downtrend_blocked_slope           False                  False
  GOOG           83.33               12            1.64              3.30        285.88                51.02         0.598          pass              0.334             57.5                           0.477              -11.90             -1.638            downtrend_blocked_slope           False                  False
 GOOGL           80.00               10            1.91              3.87        287.27                52.55         0.598          pass              0.220             53.4                           0.450              -12.59             -1.710            downtrend_blocked_slope           False                  False
  FTNT           60.00                5            4.87              4.41        127.50                91.87         0.583          pass              0.097             13.0                           0.459              -28.84             -4.644 downtrend_blocked_slope_and_streak           False                  False
  REGN           80.00                5            2.50             16.32        923.68                52.52         0.580          pass              0.059              0.4                           0.223               10.78              1.919                                 ok           False                  False
  MDLZ           95.45               22            0.46              0.22         67.29                30.79         0.572          pass              0.599             20.5                           0.261                2.88              0.577                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105141005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105141005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105141005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105141005)

</details>

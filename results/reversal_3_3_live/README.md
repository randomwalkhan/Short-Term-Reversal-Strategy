# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 10:35:05 EST`
Last processed slot: `manage_1030`

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
   MAR           86.67               15            0.98              2.91        423.62                23.45         0.542          pass              0.326             20.2                           0.183                6.03              0.845                                 ok            True                  False
  ISRG           92.31               26            1.12              3.77        480.48                40.52         0.538          pass              0.492              1.1                           0.084                7.40              0.428                                 ok            True                  False
  DXCM           82.61               23            1.57              0.97         88.06                45.01         0.523          pass              0.266             19.2                           0.198               11.20              1.272                                 ok            True                  False
   KHC           90.62               32            0.53              0.09         25.40                36.26         0.514          pass              0.616             44.9                           0.360                0.86              0.191                                 ok            True                  False
  IDXX           71.43                7            2.59             12.69        693.11                74.33         0.684          pass              0.079              3.4                           0.086               20.06              2.388                                 ok           False                  False
  FTNT           66.67               12            2.89              2.62        128.27                91.87         0.672          pass              0.196             38.6                           0.592              -27.36             -4.550 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           81.82               22            1.16              2.35        287.92                52.55         0.593          pass              0.330             47.3                           0.369              -11.92             -1.675            downtrend_blocked_slope           False                  False
  GOOG           82.61               23            1.14              2.29        286.32                51.02         0.579          pass              0.361             49.1                           0.376              -11.45             -1.615            downtrend_blocked_slope           False                  False
  MSFT          100.00                3            2.44              9.48        551.74                33.48         0.567          pass              0.503             15.6                           0.230                4.06              0.231                                 ok           False                  False
  GEHC           78.95               19            1.51              0.91         85.42                36.41         0.518          pass              0.124              4.1                           0.109               18.39              1.957                                 ok           False                  False
  INTC           50.00                4            7.76              3.16         56.91               128.90         0.514          pass              0.120             22.9                           0.405              -37.13             -5.812            downtrend_blocked_slope           False                  False
  ROST          100.00                2            3.08              5.30        243.47                31.27         0.509          pass              0.458              2.2                           0.085                0.63              0.256                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T10:35:05.725069-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:30:04.290480-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:25:05.601697-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:20:04.519114-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:15:04.415931-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:10:04.288762-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:05:06.545963-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:00:05.848004-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105103505)

</details>

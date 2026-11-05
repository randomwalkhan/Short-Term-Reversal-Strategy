# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 10:40:06 EST`
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
   MAR           86.67               15            1.06              3.16        423.52                23.45         0.537          pass              0.305             13.4                           0.117                5.94              0.841                                 ok            True                  False
  ISRG           90.91               22            1.62              5.45        479.76                40.52         0.527          pass              0.424              0.0                           0.177                6.86              0.405                                 ok            True                  False
  IDXX           71.43                7            2.63             12.87        693.04                74.33         0.681          pass              0.090              7.2                           0.144               20.01              2.386                                 ok           False                  False
  FTNT           60.00               10            3.17              2.87        128.16                91.87         0.662          pass              0.164             32.7                           0.624              -27.57             -4.563 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           78.57               14            1.68              3.39        287.48                52.55         0.605          pass              0.159             23.8                           0.264              -12.38             -1.699            downtrend_blocked_slope           False                  False
  GOOG           78.57               14            1.55              3.12        285.96                51.02         0.603          pass              0.178             30.4                           0.307              -11.82             -1.634            downtrend_blocked_slope           False                  False
  MSFT          100.00                3            2.66             10.35        551.36                33.48         0.554          pass              0.482              8.7                           0.186                3.83              0.221                                 ok           False                  False
  DXCM           66.67               12            1.98              1.22         87.96                45.01         0.550          pass              0.085              5.4                           0.125               10.74              1.253                                 ok           False                  False
  INTC           50.00                4            7.37              3.00         56.98               128.90         0.538          pass              0.134             26.8                           0.532              -36.86             -5.793            downtrend_blocked_slope           False                  False
  GEHC           71.43               14            1.67              1.00         85.38                36.41         0.531          pass              0.103              7.7                           0.093               18.21              1.950                                 ok           False                  False
  ROST          100.00                2            3.00              5.17        243.53                31.27         0.514          pass              0.465              4.7                           0.109                0.71              0.260                                 ok           False                  False
   KHC           91.18               34            0.42              0.07         25.41                36.26         0.510          pass              0.678             56.5                           0.450                0.97              0.196                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T10:40:06.595810-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:35:05.725069-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:30:04.290480-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:25:05.601697-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:20:04.519114-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:15:04.415931-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:10:04.288762-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:05:06.545963-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:00:05.848004-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105104006)

</details>

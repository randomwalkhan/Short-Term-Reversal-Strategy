# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 10:20:02 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               19            0.78              2.39        435.97                27.65         0.584          pass              0.610             30.5                           0.380                5.03              0.541                                 ok            True                  False
  CSCO           80.00               25            1.33              1.04        111.70                41.41         0.554          pass              0.188             10.8                           0.187               -0.91             -0.033                                 ok            True                  False
  FAST          100.00               16            1.10              0.40         50.97                21.07         0.543          pass              0.499              1.7                           0.039               -0.88             -0.082                                 ok            True                  False
  VRTX           97.14               35            0.57              2.17        546.62                32.96         0.513          pass              0.817             66.3                           0.543                7.65              0.666                                 ok            True                  False
  NVDA           88.89               27            1.61              2.57        226.88                42.92         0.509          pass              0.469             22.5                           0.229               -0.38             -0.171                                 ok            True                  False
  REGN          100.00               19            1.22              6.91        804.75                24.94         0.505          pass              0.699             62.9                           0.399               -0.59             -0.013                                 ok            True                  False
  MNST           94.12               34            0.41              0.13         46.64               551.83         1.000          pass              0.725             29.6                           0.258               -0.66              0.164                                 ok           False                  False
  INSM           80.00               20            2.18              1.85        120.60               110.68         0.779          pass              0.257             37.6                           0.428               -4.04             -0.582            downtrend_blocked_slope           False                  False
  MCHP           89.29               28            1.52              0.80         75.15                63.59         0.611          pass              0.504             25.2                           0.244               -5.53             -0.681            downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.49              0.20         56.75                68.22         0.603          pass              0.493             86.5                           0.677               -1.34             -0.237                                 ok           False                  False
  SOXL           78.12               32            3.71              3.19        121.68               111.92         0.576          pass              0.295             30.2                           0.286              -18.25             -2.115            downtrend_blocked_slope           False                  False
  INTC           82.05               39            0.40              0.26         91.98                58.21         0.537          pass              0.558             85.4                           0.461              -10.52             -1.336 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-28T10:20:02.098332-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:15:03.828658-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:10:03.076583-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:05:04.075473-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:00:04.882804-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T09:20:06.065187-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-27T12:00:04.808984-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:55:06.264052-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:50:05.715223-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:45:05.725743-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828102002)

</details>

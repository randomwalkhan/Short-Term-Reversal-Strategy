# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:00:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ADSK           84.85               33            0.89              1.36        216.37                55.58         0.532            pass              0.488             50.9                           0.360               -1.33              0.306                                 ok            True                  False
  PYPL           91.67               36            0.29              0.11         52.36                57.03         0.620            pass              0.546              0.0                           0.177               -4.91             -0.261            downtrend_blocked_slope           False                  False
   PEP          100.00                7            1.20              1.09        129.28                15.76         0.558            pass              0.491             11.9                           0.154               -6.86             -0.657 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.74               19            0.29              0.05         24.41                22.04         0.552            pass              0.685             58.8                           0.389               -1.97             -0.117                                 ok           False                  False
  CHTR           88.89               27            2.23              2.00        127.31                64.18         0.528            pass              0.443             13.2                           0.171              -17.55             -1.457 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.47              0.83        248.57                46.23         0.527            pass              0.864             74.8                           0.573               -7.04             -0.443            downtrend_blocked_slope           False                  False
   ADP           95.00               20            0.73              1.38        270.63                22.01         0.526            pass              0.671             50.7                           0.284               -2.39              0.124           downtrend_blocked_streak           False                  False
   BKR           96.15               26            0.87              0.35         57.10                30.72         0.525            pass              0.635             25.4                           0.259              -10.63             -1.366 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               23            0.22              0.11         72.25                19.27         0.515            pass              0.718             60.0                           0.465               -3.96             -0.531            downtrend_blocked_slope           False                  False
  VRSK           88.89               18            1.85              2.27        174.44                39.25         0.509            pass              0.375             11.2                           0.145               -7.08             -0.255            downtrend_blocked_slope           False                  False
  INTU          100.00               29            1.14              2.42        302.15                42.64         0.507            pass              0.749             57.3                           0.489               -9.91             -0.613 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.15               26            0.13              0.04         42.05                15.92         0.499 below_threshold              0.827             90.0                           0.636               -3.72             -0.459 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                       detail
2026-09-21T10:00:04.768791-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T09:20:04.809937-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                    {'saved': 92, 'empty': 1}
2026-09-18T15:10:04.788288-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                     {"early_entry_score": 0.508, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.515}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
2026-09-18T14:50:01.910301-04:00       entry_1500          timing_overlay                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-18", "training_samples": 5785, "window": 5}
2026-09-18T14:50:01.910301-04:00       entry_1500           entry_skipped                                                                                                                                                                                                       {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921100004)

</details>

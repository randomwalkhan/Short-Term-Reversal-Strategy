# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 09:45:06 EDT`
Last processed slot: `manual`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           94.12               34            0.72              0.98        193.45                50.60         0.542          pass              0.652             20.5                           0.336               -1.70              0.305                                 ok            True                  False
  ADSK           84.38               32            1.06              1.61        216.26                55.58         0.533          pass              0.324              2.4                           0.215               -1.49              0.298                                 ok            True                  False
   TRI           94.12               34            0.44              0.29         94.26                58.24         0.580          pass              0.743             49.4                           0.345              -11.08             -0.480 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                6            1.28              1.16        129.25                15.76         0.560          pass              0.461              1.6                           0.052               -6.93             -0.660 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.12               17            0.41              0.07         24.41                22.04         0.558          pass              0.566             29.1                           0.341               -2.05             -0.120                                 ok           False                  False
  ADBE           96.30               27            1.31              2.28        247.94                46.23         0.546          pass              0.581              4.4                           0.202               -7.82             -0.482            downtrend_blocked_slope           False                  False
  CHTR           88.89               27            2.15              1.93        127.34                64.18         0.535          pass              0.414              3.5                           0.215              -17.49             -1.454 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               18            0.41              0.21         72.21                19.27         0.533          pass              0.537             10.1                           0.190               -4.14             -0.539            downtrend_blocked_slope           False                  False
   BKR           96.00               25            0.93              0.37         57.09                30.72         0.527          pass              0.615             20.9                           0.185              -10.68             -1.369 downtrend_blocked_slope_and_streak           False                  False
   ADP           94.44               18            0.90              1.72        270.48                22.01         0.526          pass              0.607             38.7                           0.259               -2.57              0.116           downtrend_blocked_streak           False                  False
   CEG           83.33               24            1.04              1.86        253.91                41.10         0.517          pass              0.343             36.3                           0.277              -15.69             -1.924 downtrend_blocked_slope_and_streak           False                  False
  VRSK           88.24               17            1.86              2.29        174.43                39.25         0.514          pass              0.318              0.0                           0.204               -7.10             -0.256            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                       detail
2026-09-21T09:20:04.809937-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                    {'saved': 92, 'empty': 1}
2026-09-18T15:10:04.788288-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500          timing_overlay                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-18", "training_samples": 5785, "window": 5}
2026-09-18T14:50:01.910301-04:00       entry_1500           entry_skipped                                                                                                                                                                                                       {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                     {"early_entry_score": 0.508, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.515}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
2026-09-18T12:00:05.801546-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921094506)

</details>

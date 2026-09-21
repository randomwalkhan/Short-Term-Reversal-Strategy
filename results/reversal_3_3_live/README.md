# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 09:40:05 EDT`
Last processed slot: `manage_0930`

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
  PANW           82.22               45            0.30              0.76        363.25                79.43         0.585          pass              0.563             81.8                           0.572                8.77              1.270                                 ok           False                  False
   PEP          100.00               10            0.97              0.88        129.37                15.76         0.554          pass              0.531             25.3                           0.254               -6.64             -0.646 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.43              0.75        248.60                46.23         0.542          pass              0.698             18.9                           0.281               -7.00             -0.441            downtrend_blocked_slope           False                  False
  ADSK           88.10               42            0.11              0.17        216.88                55.58         0.541          pass              0.693             74.2                           0.390               -0.55              0.341                                 ok           False                  False
  CHTR           89.47               38            1.15              1.04        127.73                64.18         0.534          pass              0.567             24.9                           0.313              -16.65             -1.408 downtrend_blocked_slope_and_streak           False                  False
  WDAY           95.45               44            0.04              0.05        193.85                50.60         0.529          pass              0.928             91.9                           0.582               -1.02              0.336                                 ok           False                  False
   BKR           96.30               27            0.80              0.32         57.11                30.72         0.523          pass              0.660             31.3                           0.255              -10.57             -1.363 downtrend_blocked_slope_and_streak           False                  False
   CEG           84.00               25            0.94              1.67        253.99                41.10         0.521          pass              0.313             18.1                           0.226              -15.60             -1.919 downtrend_blocked_slope_and_streak           False                  False
  FTNT           90.48               42            0.49              0.58        169.59                57.71         0.517          pass              0.729             65.8                           0.461                8.14              1.117                                 ok           False                  False
   ADP           96.00               25            0.50              0.95        270.81                22.01         0.511          pass              0.750             66.2                           0.387               -2.17              0.135           downtrend_blocked_streak           False                  False
  SHOP           85.71               35            0.97              0.88        128.12                49.80         0.510          pass              0.483             37.5                           0.352              -12.30             -0.658            downtrend_blocked_slope           False                  False
  TMUS           87.50                8            2.29              2.69        167.03                33.56         0.508          pass              0.271              6.8                           0.141               -9.47             -0.925            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921094005)

</details>

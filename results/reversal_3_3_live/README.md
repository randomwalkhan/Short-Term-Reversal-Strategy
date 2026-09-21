# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 15:50:06 EDT`
Last processed slot: `manage_1600`

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
  WDAY           93.75               32            0.99              1.34        193.29                50.60         0.535            pass              0.608             13.6                           0.196               -1.96              0.293                                 ok            True                  False
   KHC           94.12               17            0.39              0.07         24.40                22.04         0.556            pass              0.633             51.3                           0.331               -2.07             -0.121                                 ok           False                  False
  ADBE           97.44               39            0.08              0.13        248.86                46.23         0.545            pass              0.936             95.9                           0.653               -6.67             -0.425            downtrend_blocked_slope           False                  False
   XEL          100.00               14            0.74              0.37         72.14                19.27         0.535            pass              0.508              9.3                           0.356               -4.46             -0.554            downtrend_blocked_slope           False                  False
   EXC           93.75               16            0.46              0.14         42.01                15.92         0.534            pass              0.654             64.5                           0.407               -4.04             -0.474 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.91               11            1.63              1.92        167.36                33.56         0.522            pass              0.520             56.7                           0.377               -8.86             -0.894            downtrend_blocked_slope           False                  False
  CHTR           83.33               18            3.29              2.95        126.90                64.18         0.506            pass              0.196              1.2                           0.162              -18.45             -1.507 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.30               27            0.41              0.77        270.89                22.01         0.505            pass              0.781             72.4                           0.395               -2.08              0.139           downtrend_blocked_streak           False                  False
  VRSK           89.47               19            1.84              2.25        174.44                39.25         0.501            pass              0.449             28.9                           0.308               -7.07             -0.254            downtrend_blocked_slope           False                  False
   ROP           91.67               12            2.14              5.59        370.34                24.70         0.498 below_threshold              0.376              0.5                           0.166              -10.44             -0.901 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00               31            1.04              0.43         59.68                41.33         0.497 below_threshold              0.594              1.4                           0.094               -4.91              0.091                                 ok           False                  False
   PEP           92.59               27            0.07              0.06        129.72                15.76         0.495 below_threshold              0.784             95.2                           0.620               -5.79             -0.605 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-09-21T15:10:05.959722-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                {"early_entry_score": 0.641, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.503}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
2026-09-21T14:50:06.827514-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-21", "training_samples": 5798, "window": 5}
2026-09-21T12:00:03.740450-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:55:03.827589-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921155006)

</details>

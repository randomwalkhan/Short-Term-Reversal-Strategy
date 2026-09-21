# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 15:05:05 EDT`
Last processed slot: `entry_1500`

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
  WDAY           94.29               35            0.61              0.83        193.52                50.60         0.540            pass              0.742             46.9                           0.320               -1.58              0.310                                 ok            True                  False
  CTSH          100.00               34            0.61              0.26         59.76                41.33         0.505            pass              0.698             29.1                           0.405               -4.50              0.110                                 ok            True                  False
  VRSK           90.48               21            1.64              2.02        174.55                39.25         0.501            pass              0.512             36.4                           0.592               -6.89             -0.245                                 ok            True                  False
   KHC           94.74               19            0.29              0.05         24.41                22.04         0.551            pass              0.700             64.1                           0.501               -1.97             -0.117                                 ok           False                  False
   XEL          100.00               15            0.64              0.32         72.16                19.27         0.536            pass              0.505              6.1                           0.166               -4.36             -0.549            downtrend_blocked_slope           False                  False
  CHTR           88.89               27            2.24              2.01        127.31                64.18         0.526            pass              0.462             19.6                           0.478              -17.56             -1.458 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.45               22            0.31              0.09         42.03                15.92         0.510            pass              0.760             76.4                           0.462               -3.90             -0.467 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.43               28            0.26              0.50        271.01                22.01         0.508            pass              0.818             82.3                           0.542               -1.94              0.146           downtrend_blocked_streak           False                  False
  TMUS           95.24               21            1.04              1.23        167.65                33.56         0.502            pass              0.741             72.4                           0.588               -8.31             -0.867            downtrend_blocked_slope           False                  False
   ROP           94.44               18            1.72              4.49        370.82                24.70         0.493 below_threshold              0.491              1.1                           0.064              -10.05             -0.881 downtrend_blocked_slope_and_streak           False                  False
  PAYX           88.00               25            0.82              0.66        115.86                23.92         0.483 below_threshold              0.516             51.5                           0.557               -5.36             -0.190           downtrend_blocked_streak           False                  False
  SBUX           87.50               24            0.82              0.55         95.59                22.99         0.465 below_threshold              0.533             64.4                           0.726               -9.02             -0.805 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-09-21T15:05:05.768467-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T15:00:04.975214-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:55:04.962001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-21T14:50:06.827514-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped                                                                                {"early_entry_score": 0.641, "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "CTSH", "timing_score": 0.503}
2026-09-21T14:50:06.827514-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.649, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 17.62, "option_volume": 12.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.544}
2026-09-21T14:50:06.827514-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-21", "training_samples": 5798, "window": 5}
2026-09-21T12:00:03.740450-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:55:03.827589-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:50:05.829625-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921150505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921150505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921150505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921150505)

</details>

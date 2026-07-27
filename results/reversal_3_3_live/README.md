# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 14:50:01 EDT`
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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               12            1.19              0.68         81.38                20.22         0.558            pass              0.544             24.8                           0.463                0.27              0.129                                 ok            True                  False
   AEP           82.35               17            1.21              1.15        135.05                20.37         0.504            pass              0.242             27.4                           0.475               -1.28             -0.019                                 ok            True                  False
  TMUS           91.89               37            0.16              0.20        180.01                59.26         0.577            pass              0.828             90.9                           0.462               -4.56             -0.616            downtrend_blocked_slope           False                  False
   EXC           95.83               24            0.43              0.14         47.47                24.01         0.548            pass              0.781             77.7                           0.607                0.50              0.130                                 ok           False                  False
  DRAM           77.27               22            3.48              1.30         52.64                97.77         0.546            pass              0.248             37.7                           0.373              -10.38             -0.589            downtrend_blocked_slope           False                  False
  CSCO           89.74               39            0.07              0.06        114.15                39.56         0.527            pass              0.789             94.4                           0.697               -4.33             -0.206                                 ok           False                  False
   WBD           60.00                5            1.69              0.30         25.64                22.96         0.524            pass              0.101             16.3                           0.176               -6.48             -0.866            downtrend_blocked_slope           False                  False
   CSX          100.00                2            2.94              1.10         52.76                24.65         0.513            pass              0.504             17.4                           0.460                4.08              0.517                                 ok           False                  False
  PANW           93.94               33            1.51              3.42        322.32                61.51         0.510            pass              0.654             25.9                           0.249               -3.45             -0.830 downtrend_blocked_slope_and_streak           False                  False
   TXN           87.10               31            1.17              2.30        278.59                50.69         0.505            pass              0.513             44.4                           0.346               -7.46             -0.742            downtrend_blocked_slope           False                  False
  KLAC           84.62               13            5.12              7.55        207.29                94.03         0.496 below_threshold              0.277             27.9                           0.363              -10.13             -0.890 downtrend_blocked_slope_and_streak           False                  False
  CRWD           89.47               38            1.11              1.42        182.67                61.00         0.492 below_threshold              0.597             36.2                           0.340               -3.54             -1.176 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-07-27T14:50:01.830454-04:00       entry_1500           entry_skipped                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.242, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 375.0, "option_spread_pct": 15.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.504}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.544, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 216.0, "option_spread_pct": 14.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.558}
2026-07-27T14:50:01.830454-04:00       entry_1500          timing_overlay                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-27", "training_samples": 5518, "window": 5}
2026-07-27T12:00:02.583905-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:50:05.732067-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:45:02.697826-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:40:04.711421-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:35:01.677814-04:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727145001)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:25:02 EDT`
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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           88.24               17            1.46              0.99         95.96                24.15         0.537          pass              0.344              7.8                           0.096               -0.50              0.216                                 ok            True                  False
  BKNG           90.00               30            0.87              1.17        192.40                45.18         0.529          pass              0.453              0.0                           0.150                6.56              1.162                                 ok            True                  False
  DRAM           76.67               30            1.49              0.53         50.14               111.30         0.611          pass              0.411             72.1                           0.860               -6.48             -1.714 downtrend_blocked_slope_and_streak           False                  False
  MRVL           81.08               37            0.31              0.41        187.38                91.71         0.605          pass              0.552             94.1                           0.976               -4.09             -1.497 downtrend_blocked_slope_and_streak           False                  False
  LRCX           86.21               29            1.17              2.39        291.99                90.68         0.588          pass              0.588             78.9                           0.916               -5.59             -1.339 downtrend_blocked_slope_and_streak           False                  False
  AAPL           95.83               24            0.95              2.06        308.03                37.33         0.578          pass              0.658             35.6                           0.359               -6.32             -0.339 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           93.75               32            0.08              0.04         62.29                33.81         0.565          pass              0.797             75.5                           0.318                3.30              0.564                                 ok           False                  False
    MU           78.79               33            1.46              8.42        819.42               109.24         0.542          pass              0.439             77.3                           0.918               -6.29             -1.785 downtrend_blocked_slope_and_streak           False                  False
  SOXL           78.12               32            3.17              2.55        113.63               178.56         0.542          pass              0.414             71.2                           0.907              -18.81             -4.227 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.77               31            0.32              0.11         50.35                27.78         0.541          pass              0.798             68.0                           0.742                0.26             -0.052                                 ok           False                  False
  GILD           87.10               31            0.42              0.38        130.05                32.59         0.539          pass              0.523             46.6                           0.353               -2.66             -0.045           downtrend_blocked_streak           False                  False
   KDP           88.57               35            0.11              0.02         31.11                33.11         0.517          pass              0.636             63.2                           0.278                2.12              0.472                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-03T10:25:02.838853-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:20:02.187581-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:15:04.011672-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:10:03.982772-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00      manage_1000               exit       {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.7325, "pnl": -1655.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-03T10:00:05.013413-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:00:05.013413-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.055, "pnl": 3663.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 22.2, "ticker": "PYPL"}
2026-08-03T03:00:01.318857-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-01T02:55:05.543757-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803102502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803102502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803102502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803102502)

</details>

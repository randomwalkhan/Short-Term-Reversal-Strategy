# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:10:03 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           88.89               18            1.31              0.88         96.00                24.15         0.546            pass              0.347              0.8                           0.034               -0.35              0.224                                 ok            True                  False
  AMAT           89.66               29            1.48              5.27        505.41                87.25         0.606            pass              0.617             57.4                           0.740               -4.86             -1.452 downtrend_blocked_slope_and_streak           False                  False
  AAPL           95.00               20            1.10              2.39        307.89                37.33         0.593            pass              0.602             25.4                           0.279               -6.46             -0.346 downtrend_blocked_slope_and_streak           False                  False
   CSX           96.15               26            0.44              0.15         50.33                27.78         0.566            pass              0.731             56.0                           0.583                0.14             -0.057                                 ok           False                  False
   KDP           88.57               35            0.08              0.02         31.11                33.11         0.521            pass              0.447              0.0                           0.157                2.15              0.474                                 ok           False                  False
  DRAM           76.00               25            3.28              1.15         49.88               111.30         0.517            pass              0.268             38.7                           0.619               -8.18             -1.798 downtrend_blocked_slope_and_streak           False                  False
  BKNG           90.91               44            0.01              0.01        192.90                45.18         0.502            pass              0.795             84.6                           0.412                7.49              1.201                                 ok           False                  False
  GILD           90.24               41            0.07              0.06        130.18                32.59         0.499 below_threshold              0.797             91.2                           0.438               -2.32             -0.029           downtrend_blocked_streak           False                  False
  CDNS           83.33               18            2.21              5.25        337.77                48.77         0.496 below_threshold              0.222             10.1                           0.110                0.78              0.015                                 ok           False                  False
  ASML           91.43               35            0.85              9.67       1624.85                49.80         0.486 below_threshold              0.732             70.6                           0.712               -7.00             -1.291 downtrend_blocked_slope_and_streak           False                  False
  LRCX           81.82               22            3.18              6.51        290.23                90.68         0.486 below_threshold              0.304             42.5                           0.670               -7.51             -1.432 downtrend_blocked_slope_and_streak           False                  False
  MRVL           78.79               33            2.37              3.12        186.22                91.71         0.481 below_threshold              0.368             55.4                           0.758               -6.07             -1.592 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-08-03T10:10:03.982772-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00      manage_1000               exit       {"asset_type": "option", "contract_symbol": "CSX260918C00050000", "fill_price": 1.7325, "pnl": -1655.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSX"}
2026-08-03T10:00:05.013413-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:00:05.013413-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.055, "pnl": 3663.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 22.2, "ticker": "PYPL"}
2026-08-03T03:00:01.318857-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-08-01T02:55:05.543757-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:50:03.559727-04:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:45:01.711119-04:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:40:01.558683-04:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803101003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803101003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803101003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803101003)

</details>

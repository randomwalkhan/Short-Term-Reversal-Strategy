# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 10:30:04 EDT`
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

- Cash: `$85,238.30`
- Equity: `$85,238.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261120C00155000     24          2026-09-29         2026-09-30         15.9        18.6 6480.0   16.981132 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           85.71               35            0.73              0.75        146.68               117.21         0.747            pass              0.614             73.3                           0.369               40.45              2.914                       ok            True                  False
  MSTR           94.29               35            0.72              0.78        154.33                99.32         0.682            pass              0.704             29.6                           0.260               21.69              1.377                       ok            True                  False
  DRAM           83.33               30            0.93              0.40         61.12                54.99         0.591            pass              0.403             40.6                           0.470                9.74              0.608                       ok            True                  False
  AMGN           84.38               32            0.50              1.48        423.00                46.59         0.590            pass              0.338              5.4                           0.109               12.00              1.220                       ok            True                  False
  MPWR           85.19               27            1.31             12.37       1348.69                52.13         0.543            pass              0.359             17.6                           0.122               16.44              1.606                       ok            True                  False
  PYPL           92.00               25            0.98              0.37         53.73                34.93         0.529            pass              0.489              5.4                           0.134                1.23              0.293                       ok            True                  False
  AMAT           84.62               39            0.92              3.30        510.60                51.71         0.524            pass              0.456             28.9                           0.171               22.13              1.982                       ok            True                  False
   ADI           87.50               24            1.18              3.29        396.81                32.38         0.509            pass              0.365              6.8                           0.117                8.70              0.890                       ok            True                  False
  MRVL           83.33               30            1.97              3.63        261.71                56.16         0.508            pass              0.320             15.6                           0.252               12.35              0.958                       ok            True                  False
  ALNY           80.56               36            1.02              1.81        253.29                45.82         0.500 below_threshold              0.269             10.2                           0.103                5.06              0.601                       ok            True                  False
   TRI           89.74               39            0.15              0.10         96.20                56.37         0.586            pass              0.765             84.4                           0.569               -5.14             -0.167 downtrend_blocked_streak           False                  False
  META           75.00               16            1.72              8.89        734.98                54.80         0.583            pass              0.181             27.4                           0.209                7.92              0.912                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-30T10:30:04.117201-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:25:03.100104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:20:05.117028-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:15:05.931688-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:10:05.044472-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:05:05.127688-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:00:05.050989-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "entry_ask": 8.7, "entry_bid": 6.75, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 42619.15, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 4833.0, "option_spread_pct": 25.24, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.628, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "matched_signals": 33, "recovery_stability_score": 0.628, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "trend_health_status": "ok"}, {"current_drop_pct": 0.61, "early_entry_score": 0.758, "early_reclaim_pct": 67.8, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 92.11, "ticker": "BKR", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T09:50:05.025462-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "MSTR261120C00155000", "fill_price": 18.6, "pnl": 6480.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.98, "ticker": "MSTR"}
2026-09-30T00:00:05.973499-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92, 'empty': 1}
2026-09-29T15:10:01.396429-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930103004)

</details>

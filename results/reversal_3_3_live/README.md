# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 10:00:40 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INSM           81.48               27            1.66              1.53        131.62               107.72         0.760            pass              0.288             19.8                           0.204               28.18              3.823                       ok            True                  False
  ISRG           87.18               39            0.26              0.72        400.96                69.94         0.668            pass              0.657             68.3                           0.573               13.39              1.341                       ok           False                  False
   ROP           97.37               38            0.08              0.21        395.14                44.32         0.591            pass              0.923             92.3                           0.533                1.46              0.202                       ok           False                  False
  FAST          100.00               26            0.33              0.12         52.17                25.01         0.567            pass              0.775             70.7                           0.559               11.55              1.204                       ok           False                  False
  BKNG           97.56               41            0.13              0.20        212.17                44.60         0.553            pass              0.932             92.4                           0.682                9.70              1.220                       ok           False                  False
   BKR           88.89                9            2.46              1.11         63.81                33.24         0.546            pass              0.325             11.2                           0.189                5.06              0.725                       ok           False                  False
  CDNS           93.62               47            0.18              0.42        322.95                47.89         0.529            pass              0.827             70.4                           0.392               -3.09             -0.339  downtrend_blocked_slope           False                  False
   HON           91.89               37            0.40              0.66        235.06                35.57         0.516            pass              0.723             58.2                           0.358               -3.11             -0.590  downtrend_blocked_slope           False                  False
  PCAR           97.30               37            0.40              0.36        130.90                29.70         0.500 below_threshold              0.855             75.0                           0.506               -2.41             -0.167                       ok           False                  False
  ROST           94.44               36            0.34              0.60        247.99                22.10         0.463 below_threshold              0.860             85.2                           0.797               -2.05             -0.077 downtrend_blocked_streak           False                  False
  IDXX           95.45               44            0.01              0.03        570.57                27.90         0.441 below_threshold              0.942             99.2                           0.578                2.10              0.327                       ok           False                  False
  TTWO           85.00               40            0.55              0.93        242.60                36.12         0.441 below_threshold              0.428             16.9                           0.120               -2.33              0.183                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-13T10:00:40.571954-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T16:10:05.737758-04:00      manage_1600                    exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-12T14:50:05.779182-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-12", "training_samples": 5645, "window": 5}
2026-08-12T14:50:05.779182-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.604, "option_liquidity_status": "low_volume", "option_open_interest": 178.0, "option_spread_pct": 8.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.806}
2026-08-12T14:50:05.779182-04:00       entry_1500                   entry {"allocated_cash": 17360.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 62, "early_entry_score": 0.819, "entry_mode": "regular", "entry_option_price": 2.8, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7246.0, "option_spread_pct": 5.71, "option_volume": 86.0, "success_rate": 93.94, "ticker": "PYPL", "timing_score": 0.657}
2026-08-12T12:00:04.666373-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813100040)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813100040)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813100040)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813100040)

</details>

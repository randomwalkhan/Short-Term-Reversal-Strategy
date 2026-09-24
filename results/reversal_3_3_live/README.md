# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 10:10:01 EDT`
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

- Cash: `$67,953.30`
- Equity: `$67,953.30`
- Realized PnL: `$57,953.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261023C00165000     30          2026-09-23         2026-09-24       11.725     10.5525 -3517.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CRWD           87.18               39            1.19              2.18        261.56                96.70         0.693          pass              0.518             21.3                           0.185               24.82              2.214                  ok            True                  False
  SOXL           80.00               30            3.95              4.05        144.52               119.42         0.632          pass              0.342             48.3                           0.548               11.67              2.306                  ok            True                  False
  PANW           80.95               42            0.62              1.70        392.57                79.07         0.628          pass              0.500             70.7                           0.410               16.64              1.360                  ok            True                  False
  NVDA           91.30               23            1.50              2.37        224.50                44.57         0.579          pass              0.517             23.5                           0.342               -0.58              0.380                  ok            True                  False
  TEAM          100.00               35            1.22              1.67        194.37                58.95         0.556          pass              0.780             52.5                           0.303                8.42              0.841                  ok            True                  False
  ADSK           81.48               27            1.57              2.39        216.13                55.47         0.551          pass              0.318             36.9                           0.437                3.45              0.233                  ok            True                  False
  WDAY           94.29               35            0.53              0.71        192.07                50.68         0.540          pass              0.852             83.4                           0.594                2.85              0.324                  ok            True                   True
  MPWR           85.19               27            1.92             18.25       1347.65                51.84         0.537          pass              0.421             38.5                           0.670               10.44              1.206                  ok            True                  False
   WMT           85.71               14            1.29              1.00        110.10                21.22         0.537          pass              0.243              3.4                           0.082                3.09              0.278                  ok            True                  False
    MU           90.00               30            1.90             14.23       1065.78                49.67         0.528          pass              0.561             36.1                           0.489                2.31              0.936                  ok            True                  False
  MSFT          100.00               14            1.56              5.48        498.24                22.42         0.527          pass              0.529             16.4                           0.247                0.23              0.071                  ok            True                  False
  DRAM           82.14               28            2.25              0.98         61.48                51.34         0.519          pass              0.278             16.5                           0.214               -1.75              0.491                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-24T10:10:01.731428-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261030C00192500", "current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "entry_ask": 12.7, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 11.0, "hypothetical_budget": 33976.65, "hypothetical_contracts": 30, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 30.91, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "matched_signals": 35, "recovery_stability_score": 0.594, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-24T10:05:06.327033-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:05:06.327033-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "MSTR261023C00165000", "fill_price": 10.5525, "pnl": -3517.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-24T10:00:05.543945-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T15:10:05.441341-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T15:05:06.124690-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T15:00:04.510549-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T14:55:06.453181-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T14:50:06.624928-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 35175.0, "asset_type": "option", "contract_symbol": "MSTR261023C00165000", "contracts": 30, "early_entry_score": 0.563, "entry_mode": "regular", "entry_option_price": 11.725, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 984.0, "option_spread_pct": 2.13, "option_volume": 82.0, "success_rate": 92.59, "ticker": "MSTR", "timing_score": 0.682}
2026-09-23T14:50:06.624928-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-23", "training_samples": 5799, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924101001)

</details>

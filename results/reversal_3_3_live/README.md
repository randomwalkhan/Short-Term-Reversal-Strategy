# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-24 10:15:06 EDT`
Last processed slot: `early_entry_1015`

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
  CRWD           87.18               39            1.18              2.17        261.56                96.70         0.693          pass              0.519             21.7                           0.219               24.83              2.214                  ok            True                  False
  PANW           80.49               41            0.74              2.05        392.42                79.07         0.625          pass              0.470             64.7                           0.403               16.50              1.354                  ok            True                  False
  SOXL           80.00               30            4.14              4.24        144.43               119.42         0.622          pass              0.333             45.9                           0.491               11.46              2.298                  ok            True                  False
  NVDA           91.30               23            1.50              2.38        224.49                44.57         0.579          pass              0.516             23.2                           0.297               -0.58              0.380                  ok            True                  False
  TEAM          100.00               38            0.65              0.89        194.70                58.95         0.574          pass              0.868             74.6                           0.461                9.04              0.867                  ok            True                  False
  ADSK           82.14               28            1.41              2.14        216.23                55.47         0.556          pass              0.363             43.4                           0.495                3.62              0.241                  ok            True                  False
  SHOP           85.71               42            0.50              0.50        142.13                61.97         0.547          pass              0.667             86.7                           0.775               11.70              1.163                  ok            True                  False
  MPWR           85.19               27            1.80             17.11       1348.14                51.84         0.544          pass              0.433             42.3                           0.640               10.57              1.211                  ok            True                  False
  WDAY           94.12               34            0.74              0.99        191.95                50.68         0.533          pass              0.821             76.9                           0.516                2.64              0.315                  ok            True                  False
   WMT           87.50               16            1.23              0.95        110.12                21.22         0.531          pass              0.317              8.1                           0.147                3.16              0.281                  ok            True                  False
    MU           89.66               29            1.97             14.80       1065.54                49.67         0.530          pass              0.538             33.5                           0.335                2.23              0.932                  ok            True                  False
  MSFT          100.00               14            1.67              5.84        498.09                22.42         0.521          pass              0.512             10.9                           0.223                0.12              0.066                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-24T10:15:06.803201-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:10:01.731428-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261030C00192500", "current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "entry_ask": 12.7, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 11.0, "hypothetical_budget": 33976.65, "hypothetical_contracts": 30, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 30.91, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.852, "early_reclaim_pct": 83.4, "matched_signals": 35, "recovery_stability_score": 0.594, "success_rate": 94.29, "ticker": "WDAY", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-24T10:05:06.327033-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-24T10:05:06.327033-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "MSTR261023C00165000", "fill_price": 10.5525, "pnl": -3517.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-24T10:00:05.543945-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T15:10:05.441341-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T15:05:06.124690-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T15:00:04.510549-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T14:55:06.453181-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-23T14:50:06.624928-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 35175.0, "asset_type": "option", "contract_symbol": "MSTR261023C00165000", "contracts": 30, "early_entry_score": 0.563, "entry_mode": "regular", "entry_option_price": 11.725, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 984.0, "option_spread_pct": 2.13, "option_volume": 82.0, "success_rate": 92.59, "ticker": "MSTR", "timing_score": 0.682}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260924101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260924101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260924101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260924101506)

</details>

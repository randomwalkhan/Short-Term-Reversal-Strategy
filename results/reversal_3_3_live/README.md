# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 09:55:03 EDT`
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

- Cash: `$47,718.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00150000     30          2026-08-31         2026-09-01          8.2        7.38 -2460.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.61               23            3.14              4.27        192.34               115.35         0.718          pass              0.244              5.4                           0.248               15.38              1.401                  ok            True                  False
   TRI           94.12               34            0.63              0.48        107.12                60.77         0.603          pass              0.681             28.0                           0.158                8.36              0.539                  ok            True                  False
  SHOP           91.67               12            3.67              3.79        145.75                69.51         0.582          pass              0.388              1.6                           0.182               -4.50              0.017                  ok            True                  False
  CPRT           88.89               18            1.82              0.42         32.81                40.13         0.556          pass              0.346              0.0                           0.008                2.18              0.073                  ok            True                  False
  DRAM           83.87               31            1.90              0.76         56.58                66.99         0.548          pass              0.403             34.9                           0.559                1.31              0.097                  ok            True                  False
  CSCO           85.29               34            0.81              0.63        110.22                40.87         0.543          pass              0.412             18.9                           0.200               -2.93             -0.087                  ok            True                  False
  PAYX          100.00               28            0.56              0.50        127.13                24.69         0.527          pass              0.734             53.9                           0.423                6.82              0.638                  ok            True                  False
   CSX           91.67               12            1.29              0.45         50.32                15.01         0.526          pass              0.450             24.3                           0.231               -1.42              0.027                  ok            True                  False
  NVDA           88.46               26            1.63              2.51        219.42                45.52         0.520          pass              0.485             33.6                           0.495               -1.29              0.117                  ok            True                  False
  UPRO           87.50               16            2.06              2.16        149.29                31.61         0.512          pass              0.314              7.5                           0.264               -4.71             -0.207                  ok            True                  False
  IDXX           87.50               16            1.83              7.15        553.63                29.41         0.511          pass              0.350             19.5                           0.263                0.07             -0.045                  ok            True                  False
  ALNY           83.87               31            1.05              1.77        239.93                49.87         0.510          pass              0.421             42.4                           0.345                6.04              0.475                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-01T09:50:02.006317-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "SHOP261016C00150000", "fill_price": 7.38, "pnl": -2460.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-09-01T00:00:06.642760-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 93}
2026-08-31T15:10:01.102922-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-08-31T15:05:01.519781-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-08-31T15:00:06.338616-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-08-31T14:55:01.449547-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-08-31T14:50:01.533389-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.713, "option_liquidity_status": "low_open_interest", "option_open_interest": 65.0, "option_spread_pct": 13.02, "option_volume": 30.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.579}
2026-08-31T14:50:01.533389-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-31", "training_samples": 5735, "window": 5}
2026-08-31T14:50:01.533389-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"allocated_cash": 24600.0, "asset_type": "option", "contract_symbol": "SHOP261016C00150000", "contracts": 30, "early_entry_score": 0.512, "entry_mode": "regular", "entry_option_price": 8.2, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 1113.0, "option_spread_pct": 3.66, "option_volume": 42.0, "success_rate": 92.31, "ticker": "SHOP", "timing_score": 0.575}
2026-08-31T12:00:06.280096-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "GEHC261002C00071000", "current_drop_pct": 0.59, "early_entry_score": 0.811, "early_reclaim_pct": 70.4, "entry_ask": 3.3, "entry_bid": 1.25, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 25089.05, "hypothetical_contracts": 110, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 90.11, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.649, "shadow_only": true, "success_rate": 96.97, "ticker": "GEHC", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.811, "early_reclaim_pct": 70.4, "matched_signals": 33, "recovery_stability_score": 0.649, "success_rate": 96.97, "ticker": "GEHC", "timing_score": 0.461, "trend_health_status": "ok"}, {"current_drop_pct": 0.75, "early_entry_score": 0.805, "early_reclaim_pct": 66.5, "matched_signals": 32, "recovery_stability_score": 0.712, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.584, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901095503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901095503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901095503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901095503)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 09:50:02 EDT`
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
  TEAM           86.67               30            2.47              3.35        192.73               115.35         0.724          pass              0.441             19.2                           0.251               16.18              1.433                  ok            True                  False
   TRI           94.12               34            0.63              0.48        107.12                60.77         0.603          pass              0.681             28.0                           0.151                8.36              0.539                  ok            True                  False
  SHOP           88.89               18            3.13              3.23        145.99                69.51         0.578          pass              0.361              4.3                           0.088               -3.97              0.042                  ok            True                  False
  DRAM           83.87               31            2.13              0.85         56.54                66.99         0.534          pass              0.378             27.1                           0.512                1.07              0.086                  ok            True                  False
  CSCO           86.84               38            0.63              0.49        110.28                40.87         0.532          pass              0.533             36.9                           0.333               -2.75             -0.078                  ok            True                  False
  CPRT           80.00               25            1.39              0.32         32.85                40.13         0.527          pass              0.187             11.5                           0.112                2.62              0.092                  ok            True                  False
  UPRO           87.50               16            1.84              1.93        149.44                31.61         0.525          pass              0.348             18.6                           0.471               -4.46             -0.195                  ok            True                  False
   CSX           90.91               11            1.49              0.53         50.28                15.01         0.519          pass              0.386             12.0                           0.150               -1.63              0.017                  ok            True                  False
  CHTR           92.31               26            2.10              2.24        151.48                52.85         0.515          pass              0.635             49.7                           0.562                3.57              0.287                  ok            True                  False
  NVDA           88.00               25            1.80              2.79        219.31                45.52         0.514          pass              0.444             26.3                           0.432               -1.47              0.109                  ok            True                  False
    ZS           92.31               13            3.48              4.60        186.42                58.29         0.501          pass              0.421              7.5                           0.130               -1.42             -0.091                  ok            True                  False
  MNST           92.50               40            0.04              0.01         45.91               551.67         1.000          pass              0.907             91.3                           0.554                0.83             -0.088                  ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901095002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901095002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901095002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901095002)

</details>

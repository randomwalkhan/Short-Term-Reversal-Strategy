# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 10:00:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           85.71               28            2.59              3.52        192.66               115.35         0.723          pass              0.418             24.5                           0.308               16.04              1.427                      ok            True                  False
   TRI           93.94               33            0.80              0.60        107.06                60.77         0.598          pass              0.612              9.0                           0.073                8.17              0.531                      ok            True                  False
  SHOP           90.91               11            3.80              3.92        145.69                69.51         0.577          pass              0.367              3.9                           0.182               -4.63              0.011                      ok            True                  False
  CPRT           88.24               17            1.97              0.45         32.80                40.13         0.550          pass              0.330              3.0                           0.060                2.02              0.066                      ok            True                  False
  CSCO           85.71               35            0.76              0.59        110.24                40.87         0.541          pass              0.446             24.3                           0.229               -2.88             -0.084                      ok            True                  False
  DRAM           83.87               31            2.25              0.90         56.52                66.99         0.526          pass              0.365             22.9                           0.459                0.94              0.080                      ok            True                  False
  UPRO           87.50               16            1.96              2.06        149.39                31.61         0.518          pass              0.332             13.3                           0.451               -4.58             -0.201                      ok            True                  False
  NVDA           88.46               26            1.69              2.61        219.38                45.52         0.516          pass              0.477             30.9                           0.545               -1.35              0.114                      ok            True                  False
  IDXX           89.47               19            1.68              6.53        553.89                29.41         0.505          pass              0.443             26.5                           0.280                0.23             -0.038                      ok            True                  False
  CHTR           86.67               15            3.29              3.51        150.94                52.85         0.502          pass              0.325             21.1                           0.240                2.31              0.231                      ok            True                  False
  MNST           92.50               40            0.04              0.01         45.91               551.67         1.000          pass              0.907             91.3                           0.623                0.83             -0.088                      ok           False                  False
  INSM           87.80               41            0.57              0.49        121.61               109.80         0.780          pass              0.672             61.8                           0.406               -5.61             -0.680 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-01T10:00:06.717269-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "entry_ask": 14.4, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 18, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 358.0, "option_spread_pct": 26.77, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "matched_signals": 36, "recovery_stability_score": 0.67, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T09:50:02.006317-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "SHOP261016C00150000", "fill_price": 7.38, "pnl": -2460.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-09-01T00:00:06.642760-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-31T15:10:01.102922-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-31T15:05:01.519781-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-31T15:00:06.338616-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-31T14:55:01.449547-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-31T14:50:01.533389-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-31", "training_samples": 5735, "window": 5}
2026-08-31T14:50:01.533389-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.713, "option_liquidity_status": "low_open_interest", "option_open_interest": 65.0, "option_spread_pct": 13.02, "option_volume": 30.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.579}
2026-08-31T14:50:01.533389-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 24600.0, "asset_type": "option", "contract_symbol": "SHOP261016C00150000", "contracts": 30, "early_entry_score": 0.512, "entry_mode": "regular", "entry_option_price": 8.2, "execution_mode": "option", "matched_signals": 13, "option_liquidity_status": "ok", "option_open_interest": 1113.0, "option_spread_pct": 3.66, "option_volume": 42.0, "success_rate": 92.31, "ticker": "SHOP", "timing_score": 0.575}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901100006)

</details>

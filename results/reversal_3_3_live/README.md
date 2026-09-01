# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-01 10:05:04 EDT`
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
  TEAM           87.10               31            2.02              2.75        192.99               115.35         0.739          pass              0.526             41.0                           0.366               16.71              1.453                  ok            True                  False
  ABNB           93.75               32            0.51              0.65        182.94                62.80         0.658          pass              0.792             71.0                           0.606                1.67              0.091                  ok            True                   True
   TRI           94.12               34            0.63              0.47        107.12                60.77         0.603          pass              0.683             28.6                           0.170                8.36              0.539                  ok            True                  False
  SHOP           90.91               11            3.80              3.92        145.69                69.51         0.577          pass              0.367              3.8                           0.099               -4.63              0.010                  ok            True                  False
  CSCO           85.29               34            0.89              0.69        110.20                40.87         0.539          pass              0.390             11.6                           0.158               -3.00             -0.090                  ok            True                  False
  UPRO           87.50               16            1.77              1.86        149.47                31.61         0.530          pass              0.358             21.7                           0.523               -4.39             -0.192                  ok            True                  False
  NVDA           88.46               26            1.49              2.31        219.51                45.52         0.528          pass              0.502             39.0                           0.638               -1.15              0.124                  ok            True                  False
  DRAM           83.87               31            2.29              0.91         56.51                66.99         0.524          pass              0.360             21.6                           0.459                0.91              0.079                  ok            True                  False
  CPRT           80.00               25            1.38              0.32         32.85                40.13         0.523          pass              0.254             34.1                           0.274                2.63              0.093                  ok            True                  False
  ALNY           86.49               37            0.52              0.87        240.32                49.87         0.510          pass              0.619             71.8                           0.449                6.61              0.499                  ok            True                  False
  CHTR           85.71               14            3.34              3.56        150.91                52.85         0.504          pass              0.289             19.8                           0.227                2.26              0.229                  ok            True                  False
  MNST           92.11               38            0.09              0.03         45.91               551.67         1.000          pass              0.857             82.6                           0.542                0.79             -0.090                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-01T10:05:04.005187-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "ABNB261002C00182500", "current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "entry_ask": 7.85, "entry_bid": 5.35, "entry_mode": "early", "entry_option_price": 6.6, "hypothetical_budget": 23859.05, "hypothetical_contracts": 36, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 37.88, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.606, "shadow_only": true, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 71.0, "matched_signals": 32, "recovery_stability_score": 0.606, "success_rate": 93.75, "ticker": "ABNB", "timing_score": 0.658, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T10:00:06.717269-04:00 early_entry_1000      early_entry_shadow                  {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "entry_ask": 14.4, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 23859.05, "hypothetical_contracts": 18, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 358.0, "option_spread_pct": 26.77, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.67, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.801, "early_reclaim_pct": 62.4, "matched_signals": 36, "recovery_stability_score": 0.67, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.401, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-01T09:50:02.006317-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "SHOP261016C00150000", "fill_price": 7.38, "pnl": -2460.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-09-01T00:00:06.642760-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-31T15:10:01.102922-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-31T15:05:01.519781-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-31T15:00:06.338616-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-31T14:55:01.449547-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-31T14:50:01.533389-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"early_entry_score": 0.713, "option_liquidity_status": "low_open_interest", "option_open_interest": 65.0, "option_spread_pct": 13.02, "option_volume": 30.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.579}
2026-08-31T14:50:01.533389-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-31", "training_samples": 5735, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260901100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260901100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260901100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260901100504)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:10:05 EDT`
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

- Cash: `$46,498.30`
- Equity: `$83,698.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$-1,540.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META261120C00735000       2026-09-30                   1      8     38740.0                 37200.0        48.42           46.5      733.79        725.46          bid_ask_mid                       46.5                bid_ask_mid                    True         -1540.0                  -3.98         84.38               32              0.68         44.85           47.45                   54.8                 798.0          103.0               0.02                      ok
```

## Today's Closed Trades (2026-10-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           86.11               36            0.50              0.52        147.64               113.77         0.718          pass              0.635             75.6                           0.425               28.21              1.792                       ok            True                  False
  INTC           88.89               36            0.92              0.77        119.90                73.63         0.589          pass              0.654             61.5                           0.554                9.49              0.532                       ok            True                  False
  AMGN           85.19               27            0.76              2.25        420.55                46.02         0.584          pass              0.507             65.8                           0.395               10.14              1.020                       ok            True                  False
  MPWR           90.91               33            0.67              6.32       1344.51                50.40         0.537          pass              0.631             44.4                           0.341               14.59              1.123                       ok            True                  False
   STX           87.88               33            1.12              7.23        919.24                53.17         0.506          pass              0.606             63.9                           0.434               13.65              0.955                       ok            True                  False
  MRVL           81.82               33            1.24              2.30        263.23                55.88         0.505          pass              0.404             50.5                           0.348                8.38              0.643                       ok            True                  False
  NXPI           87.10               31            0.77              1.27        236.98                38.88         0.502          pass              0.391              3.7                           0.059                3.40              0.349                       ok            True                  False
  DRAM           80.00               35            0.45              0.19         60.28                53.77         0.566          pass              0.385             53.8                           0.321                4.00              0.095                       ok           False                  False
  META           87.80               41            0.01              0.03        725.17                55.93         0.564          pass              0.761             98.8                           0.423                6.36              0.542                       ok           False                  False
   XEL           66.67                9            0.93              0.46         70.28                18.32         0.538          pass              0.153             33.2                           0.416               -5.17             -0.458  downtrend_blocked_slope           False                  False
  ASML           83.33               36            0.38              4.80       1809.61                42.37         0.536          pass              0.487             57.0                           0.352               10.75              0.952                       ok           False                  False
  QCOM           92.68               41            0.22              0.28        183.92                56.29         0.521          pass              0.753             54.3                           0.332               -2.69             -0.223 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-01T10:10:05.306830-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:05:05.587824-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "entry_ask": 17.55, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 16.425, "hypothetical_budget": 23249.15, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 78.0, "option_spread_pct": 13.7, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "matched_signals": 41, "recovery_stability_score": 0.567, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T10:00:05.588413-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T00:00:05.224460-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-09-30T15:10:04.050158-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:05:04.200259-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:00:05.217258-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T14:55:06.123157-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T14:50:06.616315-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-30", "training_samples": 5904, "window": 5}
2026-09-30T14:50:06.616315-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 38740.0, "asset_type": "option", "contract_symbol": "META261120C00735000", "contracts": 8, "early_entry_score": 0.534, "entry_mode": "regular", "entry_option_price": 48.425, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 798.0, "option_spread_pct": 1.55, "option_volume": 103.0, "success_rate": 84.38, "ticker": "META", "timing_score": 0.562}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001101005)

</details>

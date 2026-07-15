# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 15:15:04 EDT`
Last processed slot: `manual`

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

- Cash: `$16,570.25`
- Equity: `$30,410.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$-220.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   ADI     option         option ADI260821C00380000       2026-07-15                   0      4     14060.0                 13840.0        35.15           34.6      388.76        389.92          bid_ask_mid                       34.6                bid_ask_mid                    True          -220.0                  -1.56         86.21               29              1.02          62.6           59.54                  55.85                 129.0           42.0               0.05                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               12            0.85              0.35         58.65                30.54         0.630          pass              0.613             45.7                           0.272                0.80             -0.099                                 ok            True                  False
   TXN           90.91               22            1.87              4.00        303.83                65.52         0.577          pass              0.558             43.0                           0.437                0.59              0.263                                 ok            True                  False
   ADI           87.10               31            0.74              2.04        391.87                55.85         0.575          pass              0.594             69.2                           0.643               -1.85              0.100                                 ok            True                  False
   LIN          100.00               13            1.17              4.26        520.71                20.66         0.557          pass              0.576             33.4                           0.437               -0.48             -0.298                                 ok            True                  False
   XEL          100.00               11            1.14              0.64         79.90                21.57         0.542          pass              0.539             26.0                           0.290               -1.30             -0.112                                 ok            True                  False
  NXPI           84.62               26            1.46              2.91        282.62                58.07         0.539          pass              0.452             56.0                           0.442               -0.47              0.251                                 ok            True                  False
   WBD           83.33               12            1.11              0.21         27.39                20.00         0.531          pass              0.256             33.7                           0.338                1.93              0.268                                 ok            True                  False
  MSTR           77.27               44            0.48              0.33         97.44               100.18         0.628          pass              0.403             46.6                           0.306               11.71              0.418                                 ok           False                  False
  KLAC           78.95               19            3.31              5.34        228.08               109.33         0.601          pass              0.255             45.1                           0.448              -26.17             -2.062 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00                5            1.69              0.56         46.68                21.56         0.578          pass              0.490             10.7                           0.214               -1.06             -0.096                                 ok           False                  False
   CSX           88.89                9            1.37              0.48         49.71                19.08         0.571          pass              0.391             32.2                           0.335                3.59              0.332                                 ok           False                  False
  AMAT           80.00               15            3.35             13.99        589.71                98.89         0.560          pass              0.234             48.2                           0.471              -20.37             -1.406 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-15T15:10:01.366399-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:00:06.972520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T14:50:07.762689-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"allocated_cash": 14060.0, "asset_type": "option", "contract_symbol": "ADI260821C00380000", "contracts": 4, "early_entry_score": 0.523, "entry_mode": "regular", "entry_option_price": 35.15, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 129.0, "option_spread_pct": 5.41, "option_volume": 42.0, "success_rate": 86.21, "ticker": "ADI", "timing_score": 0.569}
2026-07-15T14:50:07.762689-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.633, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 14.0, "option_spread_pct": 5.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.636}
2026-07-15T14:50:07.762689-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-15", "training_samples": 5408, "window": 5}
2026-07-15T12:00:03.706415-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "CRWD260821C00210000", "current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "entry_ask": 14.6, "entry_bid": 14.25, "entry_mode": "early", "entry_option_price": 14.425, "hypothetical_budget": 15315.13, "hypothetical_contracts": 10, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1292.0, "option_spread_pct": 2.43, "option_volume": 518.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.726, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "matched_signals": 39, "recovery_stability_score": 0.726, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-15T11:55:06.679355-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:50:02.876804-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:45:04.888686-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715151504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715151504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715151504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715151504)

</details>

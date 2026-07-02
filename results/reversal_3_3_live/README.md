# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 16:00:05 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$13,976.50`
- Equity: `$28,376.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   0     96     13920.0                 14400.0         1.45            1.5       33.12          33.3          bid_ask_mid                        1.5                bid_ask_mid                    True           480.0                   3.45         100.0               15              0.76         30.37           29.25                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  UPRO           85.71               28            0.61              0.60        141.13                55.10         0.609          pass              0.557             74.5                           0.721                1.51              0.084                      ok            True                  False
  ASML           91.67               12            4.05             52.24       1820.65                76.04         0.514          pass              0.440             21.5                           0.462               -5.32             -0.212                      ok            True                  False
  AVGO           73.33               15            2.47              6.38        366.60                71.90         0.640          pass              0.185             29.4                           0.529               -8.17             -0.954 downtrend_blocked_slope           False                  False
   WBD           75.00                4            1.32              0.25         26.70                21.87         0.606          pass              0.175             38.3                           0.437                0.82              0.093                      ok           False                  False
   TXN           88.00               25            1.33              2.77        297.22                67.74         0.602          pass              0.552             59.5                           0.646               -2.46             -0.867 downtrend_blocked_slope           False                  False
    MU           91.67               12            5.43             39.25       1015.46               134.25         0.599          pass              0.479             31.6                           0.606               -6.42             -0.550 downtrend_blocked_slope           False                  False
   KDP          100.00               28            0.18              0.04         33.35                28.32         0.560          pass              0.837             87.1                           0.672                8.60              1.100                      ok           False                  False
  NXPI           89.47               19            2.05              4.00        277.47                63.41         0.555          pass              0.520             50.6                           0.704               -7.98             -1.341 downtrend_blocked_slope           False                  False
   ADI           77.78                9            3.01              8.20        385.46                61.24         0.554          pass              0.140             28.3                           0.514               -8.97             -1.273 downtrend_blocked_slope           False                  False
  MPWR           84.21               19            3.26             30.43       1318.69                89.16         0.536          pass              0.347             40.5                           0.645              -10.91             -1.618 downtrend_blocked_slope           False                  False
  PCAR           78.95               19            1.44              1.23        120.71                34.47         0.510          pass              0.208             32.2                           0.492                1.83              0.223                      ok           False                  False
    EA          100.00               26            0.16              0.22        205.35                 4.00         0.505          pass              0.644             28.9                           0.377                1.04              0.150                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-02T15:10:04.628574-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-02T15:05:06.760446-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-02T15:00:02.818576-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-02T14:55:03.805247-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-02T14:50:01.813724-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 13920.0, "asset_type": "option", "contract_symbol": "KDP260821C00033000", "contracts": 96, "early_entry_score": 0.63, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 2956.0, "option_spread_pct": 13.79, "option_volume": 194.0, "success_rate": 100.0, "ticker": "KDP", "timing_score": 0.609}
2026-07-02T14:50:01.813724-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.47, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 22.49, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.614}
2026-07-02T14:50:01.813724-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-02", "training_samples": 5311, "window": 5}
2026-07-02T12:00:01.950437-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:55:04.784699-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:50:04.781471-04:00 early_entry_1150      early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "entry_ask": 14.2, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 2.86, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702160005)

</details>

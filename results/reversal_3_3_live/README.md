# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-08 13:00:04 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$13,056.75`
- Equity: `$25,881.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260821C00047500       2026-07-07                   1     54     12690.0                 12825.0         2.35           2.38       48.48         48.27          bid_ask_mid                       2.38                bid_ask_mid                    True           135.0                   1.06          91.3               23              0.68         28.35           31.15                  21.52                2967.0           20.0               0.09                      ok
```

## Today's Closed Trades (2026-07-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.33               15            0.55              0.23         60.12                30.26         0.592            pass              0.655             68.9                           0.550               -1.09             -0.165                      ok            True                  False
  UPRO           90.00               20            1.33              1.32        141.64                46.91         0.581            pass              0.573             60.5                           0.746                3.88              0.693                      ok            True                  False
  PAYX          100.00               15            1.57              1.19        107.61                32.70         0.551            pass              0.625             45.5                           0.409                8.60              1.170                      ok            True                  False
  GILD           86.36               22            0.81              0.77        136.03                35.29         0.551            pass              0.427             40.9                           0.306                8.16              0.838                      ok            True                  False
   ADP           93.33               15            1.49              2.56        244.50                31.95         0.547            pass              0.544             33.6                           0.300                9.73              1.291                      ok            True                  False
  PCAR           80.95               21            1.34              1.17        123.96                37.78         0.529            pass              0.282             43.4                           0.705                5.15              0.540                      ok            True                  False
  TMUS           88.24               17            1.34              1.74        183.99                35.69         0.522            pass              0.493             58.3                           0.340               -1.26             -0.033                      ok            True                  False
  GOOG           85.00               20            1.60              4.08        361.87                34.43         0.509            pass              0.289             12.6                           0.281                3.38              0.647                      ok            True                  False
   LIN           91.67               12            1.52              5.72        535.78                22.37         0.501            pass              0.471             32.1                           0.564                3.47              0.535                      ok            True                  False
   XEL          100.00               21            0.52              0.29         80.54                21.69         0.500 below_threshold              0.592             22.9                           0.188               -0.10             -0.118                      ok            True                  False
  DRAM           90.00               30            0.14              0.06         60.56               122.15         0.794            pass              0.774             98.1                           0.898              -12.59             -1.991 downtrend_blocked_slope           False                  False
  CTSH           72.00               25            1.57              0.48         43.73                62.27         0.591            pass              0.254             31.7                           0.387                5.62              0.752                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-08T12:00:02.532330-04:00 early_entry_1200 early_entry_shadow                                  {"contract_symbol": "TMUS260821C00185000", "current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "entry_ask": 9.7, "entry_bid": 9.2, "entry_mode": "early", "entry_option_price": 9.45, "hypothetical_budget": 6528.38, "hypothetical_contracts": 6, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 378.0, "option_spread_pct": 5.29, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "matched_signals": 35, "recovery_stability_score": 0.622, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T11:57:36.728497-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "entry_ask": 24.7, "entry_bid": 21.4, "entry_mode": "early", "entry_option_price": 23.05, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 53.0, "option_spread_pct": 14.32, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.713, "early_reclaim_pct": 79.7, "matched_signals": 45, "recovery_stability_score": 0.636, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.374, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T11:17:31.826171-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-08T10:00:23.726420-04:00 early_entry_1000 early_entry_shadow              {"contract_symbol": "ALNY260821C00320000", "current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "entry_ask": 24.2, "entry_bid": 21.6, "entry_mode": "early", "entry_option_price": 22.9, "hypothetical_budget": 6528.38, "hypothetical_contracts": 2, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 53.0, "option_spread_pct": 11.35, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.694, "early_reclaim_pct": 77.5, "matched_signals": 43, "recovery_stability_score": 0.607, "success_rate": 88.37, "ticker": "ALNY", "timing_score": 0.382, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-08T00:00:05.492385-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-07T15:10:01.115389-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T15:05:02.177767-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T15:00:05.200618-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T14:55:05.093959-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-07T14:50:02.270348-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-07", "training_samples": 5385, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260708130004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260708130004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260708130004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260708130004)

</details>

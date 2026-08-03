# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 15:35:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$17,739.75`
- Equity: `$34,964.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$-265.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-08-03                   0    106     17490.0                 17225.0         1.65           1.62       49.76         49.63          bid_ask_mid                       1.62                bid_ask_mid                    True          -265.0                  -1.52         100.0               11              1.28         25.54           25.73                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               12            1.51              0.66         62.03                33.81         0.599          pass              0.482              3.1                           0.171                1.83              0.499                                 ok            True                  False
   EXC           93.75               16            1.07              0.34         45.67                22.49         0.554          pass              0.477              4.9                           0.228               -1.37             -0.148                                 ok            True                  False
  AMGN          100.00               11            1.67              4.50        383.23                25.80         0.532          pass              0.550             30.2                           0.338                4.00              0.635                                 ok            True                  False
   WDC           86.96               23            3.07             11.71        539.82               105.07         0.512          pass              0.508             61.6                           0.562                8.35             -0.226                                 ok            True                  False
   CSX          100.00                9            1.51              0.53         50.17                27.78         0.611          pass              0.465              1.3                           0.161               -0.94             -0.106                                 ok           False                  False
  AAPL           93.75               16            1.30              2.80        307.71                37.33         0.599          pass              0.577             36.9                           0.320               -6.64             -0.355 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00                8            1.40              0.77         77.87                17.46         0.565          pass              0.473              5.5                           0.154               -1.99             -0.244           downtrend_blocked_streak           False                  False
   KDP           77.78               18            0.96              0.21         31.03                33.11         0.555          pass              0.127              6.2                           0.188                1.25              0.433                                 ok           False                  False
   PEP           87.10               31            0.26              0.25        139.45                26.18         0.535          pass              0.556             57.6                           0.429                2.76              0.487                                 ok           False                  False
  CTAS           94.74               38            0.39              0.56        204.39                38.81         0.533          pass              0.683             16.7                           0.195                1.01              0.348                                 ok           False                  False
   ROP           92.11               38            0.13              0.36        391.81                47.47         0.528          pass              0.819             85.7                           0.621                7.89              1.454                                 ok           False                  False
  KLAC           89.19               37            0.62              0.79        182.48                69.24         0.527          pass              0.736             86.3                           0.801              -12.48             -2.260 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-03T15:10:06.837493-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-03T15:05:02.121763-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-03T15:00:06.049845-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-03T14:55:04.961002-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-03T14:50:05.995871-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 17490.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 106, "early_entry_score": 0.481, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 2866.0, "option_spread_pct": 6.06, "option_volume": 205.0, "success_rate": 100.0, "ticker": "CSX", "timing_score": 0.614}
2026-08-03T14:50:05.995871-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-03", "training_samples": 5546, "window": 5}
2026-08-03T12:00:03.854898-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CDNS260918C00335000", "current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "entry_ask": 25.3, "entry_bid": 22.6, "entry_mode": "early", "entry_option_price": 23.95, "hypothetical_budget": 17614.88, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.27, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "matched_signals": 45, "recovery_stability_score": 0.703, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-03T11:55:02.829313-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:50:02.007481-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:45:01.947551-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803153502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803153502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803153502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803153502)

</details>

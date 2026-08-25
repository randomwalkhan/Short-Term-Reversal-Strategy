# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 15:40:01 EDT`
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

- Cash: `$1,114.00`
- Equity: `$58,110.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$407.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 28440.0        30.35           31.6      310.66        313.46          bid_ask_mid                       31.6                bid_ask_mid                    True          1125.0                   4.12         87.50               32              1.06         63.04           62.96                  88.60                 214.0           30.0               0.05                      ok
   KHC     option         option  KHC261016C00025000       2026-08-25                   0    287     29274.0                 28556.5         1.02            1.0       25.19         25.24          bid_ask_mid                        1.0                bid_ask_mid                    True          -717.5                  -2.45         86.67               15              1.85         24.46           23.19                  37.91                4031.0          107.0               0.04                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           82.14               28            2.37              3.30        197.73                78.88         0.565          pass              0.303             23.3                           0.331                7.26              0.717                                 ok            True                  False
  PAYX          100.00               24            0.68              0.60        125.75                34.31         0.547          pass              0.718             56.6                           0.563                3.18              0.332                                 ok            True                  False
   MAR           96.55               29            0.68              1.71        359.47                33.78         0.546          pass              0.775             64.6                           0.363                2.57              0.227                                 ok            True                  False
   KHC           83.33               18            1.66              0.30         25.54                37.91         0.546          pass              0.237             13.3                           0.458                2.41              0.333                                 ok            True                  False
   KDP           84.62               13            2.05              0.47         32.31                31.66         0.522          pass              0.220              8.3                           0.325                9.13              0.858                                 ok            True                  False
  COST           94.74               19            1.05              7.13        968.34                19.15         0.517          pass              0.539             11.5                           0.150                1.79              0.073                                 ok            True                  False
  MNST           91.89               37            0.26              0.09         48.88               552.55         1.000          pass              0.832             78.4                           0.792                7.17              0.667                                 ok           False                  False
  INSM           86.67               45            0.54              0.47        123.78               110.65         0.764          pass              0.573             39.6                           0.237               -6.98             -0.541            downtrend_blocked_slope           False                  False
  TEAM           73.91               23            3.37              4.05        169.60               115.46         0.710          pass              0.178              6.9                           0.191                7.44              1.003                                 ok           False                  False
  AMAT           90.62               32            1.07              3.62        482.64                81.86         0.646          pass              0.608             37.7                           0.458               -8.77             -1.193            downtrend_blocked_slope           False                  False
  MCHP           87.88               33            1.09              0.57         73.97                69.73         0.617          pass              0.500             25.0                           0.189               -8.86             -0.820            downtrend_blocked_slope           False                  False
  AMZN           73.68               38            0.57              1.04        261.62                59.56         0.602          pass              0.347             33.5                           0.409               -4.29             -0.341 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et       slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-25T15:10:01.918364-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                          {"early_entry_score": 0.306, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.47, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-08-25T14:50:01.861538-04:00 entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                                                {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
2026-08-25T14:50:01.861538-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.471, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.32, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.558}
2026-08-25T14:50:01.861538-04:00 entry_1500                   entry {"allocated_cash": 29274.0, "asset_type": "option", "contract_symbol": "KHC261016C00025000", "contracts": 287, "early_entry_score": 0.276, "entry_mode": "regular", "entry_option_price": 1.02, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 4031.0, "option_spread_pct": 3.92, "option_volume": 107.0, "success_rate": 86.67, "ticker": "KHC", "timing_score": 0.558}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825154001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825154001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825154001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825154001)

</details>

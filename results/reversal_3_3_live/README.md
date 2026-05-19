# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:05:01 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$15,642.50`
- Equity: `$28,492.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12850.0        13.55          12.85      241.03        241.08          bid_ask_mid                      12.85                bid_ask_mid                    True          -700.0                  -5.17         97.62               42              0.58         61.06           59.41                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               29            1.29              0.98        107.75               114.00         0.739          pass              0.749             49.5                           0.341               -1.28             -0.441                  ok            True                  False
  NXPI           80.65               31            0.96              1.97        290.84                90.65         0.717          pass              0.393             54.5                           0.402               -1.19             -0.214                  ok            True                  False
   TXN           85.71               14            1.75              3.69        299.02                69.24         0.682          pass              0.397             50.0                           0.400                5.10              0.676                  ok            True                  False
  CSCO           90.91               11            1.74              1.45        118.26                49.96         0.643          pass              0.443             27.1                           0.265               23.87              2.953                  ok            True                  False
    MU           84.85               33            1.33              6.33        678.83                90.51         0.556          pass              0.506             56.0                           0.337                5.05              0.694                  ok            True                  False
  GOOG           86.36               22            1.28              3.51        391.61                40.55         0.540          pass              0.438             44.6                           0.383                1.00              0.042                  ok            True                  False
  ASML           83.87               31            0.94              9.66       1468.25                50.95         0.536          pass              0.446             49.6                           0.320                1.09             -0.152                  ok            True                  False
 GOOGL           86.96               23            1.34              3.72        395.35                40.53         0.534          pass              0.452             42.3                           0.371                0.82              0.052                  ok            True                  False
  NVDA           89.29               28            1.16              1.81        221.55                44.74         0.524          pass              0.510             30.1                           0.291               11.83              1.118                  ok            True                  False
   CSX           87.10               31            0.69              0.22         46.10                31.65         0.517          pass              0.485             34.7                           0.520                1.89              0.242                  ok            True                  False
  AVGO           88.89               18            2.30              6.77        417.81                42.85         0.513          pass              0.413             23.9                           0.252               -3.82             -0.120                  ok            True                  False
  FAST           91.30               23            1.00              0.31         43.87                22.17         0.507          pass              0.578             46.3                           0.562               -1.74             -0.204                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-19T10:05:01.031829-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-19T00:00:06.432342-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T14:50:01.599355-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-18", "training_samples": 5028, "window": 5}
2026-05-18T12:00:03.667934-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519100501)

</details>

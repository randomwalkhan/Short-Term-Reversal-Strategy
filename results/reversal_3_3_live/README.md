# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 09:55:02 EDT`
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

- Cash: `$27,460.60`
- Equity: `$55,788.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$1,012.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 28327.5        30.35          31.48      310.66        312.56          bid_ask_mid                      31.48                bid_ask_mid                    True          1012.5                   3.71          87.5               32              1.06         63.04           64.19                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           92.31               26            0.66              0.22         48.63               552.32         1.000          pass              0.657             40.6                           0.302                5.28              0.601                      ok            True                  False
  ALNY           83.33               30            1.22              2.05        239.20               130.65         0.845          pass              0.357             16.9                           0.139                5.90              0.643                      ok            True                  False
  SHOP           91.89               37            0.84              0.90        153.49                72.08         0.629          pass              0.743             61.0                           0.531                1.45             -0.113                      ok            True                  False
  REGN          100.00               17            1.31              7.65        830.28                29.20         0.580          pass              0.550             15.3                           0.139                3.21              0.440                      ok            True                  False
  DXCM           87.88               33            0.93              0.58         88.91                51.46         0.561          pass              0.569             49.7                           0.427               -2.72             -0.101                      ok            True                  False
  AMGN          100.00               24            0.58              1.81        441.47                27.99         0.556          pass              0.637             29.3                           0.231                6.26              0.814                      ok            True                  False
  VRSK           89.47               38            0.53              0.69        188.19                41.10         0.505          pass              0.697             69.2                           0.537                3.95              0.504                      ok            True                  False
  VRTX           97.22               36            0.63              2.43        551.81                33.40         0.503          pass              0.745             40.4                           0.428                4.50              0.796                      ok            True                  False
  INSM           87.50               40            0.81              0.70        123.59               110.58         0.694          pass              0.712             80.8                           0.450               -7.10             -0.461 downtrend_blocked_slope           False                  False
   APP           71.11               45            0.23              0.50        310.33                88.60         0.656          pass              0.519             84.3                           0.478                2.00             -0.117                      ok           False                  False
  ABNB           94.12               34            0.48              0.64        190.22                61.60         0.654          pass              0.750             49.3                           0.301                5.27              0.515                      ok           False                  False
  LRCX           85.29               34            0.67              1.47        314.03                81.56         0.653          pass              0.531             54.9                           0.410               -4.16             -0.845 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                  detail
2026-08-26T09:50:01.107222-04:00  manage_1000                    exit                                                                                         {"asset_type": "option", "contract_symbol": "KHC261016C00025000", "fill_price": 0.918, "pnl": -2927.4, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KHC"}
2026-08-26T00:00:04.646772-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 93}
2026-08-25T15:10:01.918364-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00   entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped                                  {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped            {"early_entry_score": 0.306, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.47, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826095502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826095502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826095502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826095502)

</details>

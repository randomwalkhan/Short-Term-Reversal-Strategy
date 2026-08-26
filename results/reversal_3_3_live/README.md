# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 10:00:05 EDT`
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
- Equity: `$56,193.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$1,417.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 28732.5        30.35          31.92      310.66        311.84          bid_ask_mid                      31.92                bid_ask_mid                    True          1417.5                   5.19          87.5               32              1.06         63.04           66.48                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.51              0.18         48.65               552.32         1.000          pass              0.737             53.6                           0.413                5.44              0.607                                 ok            True                  False
  ALNY           84.85               33            1.05              1.76        239.33               130.65         0.842          pass              0.453             28.7                           0.180                6.08              0.651                                 ok            True                  False
  SHOP           91.43               35            1.02              1.10        153.41                72.08         0.630          pass              0.692             52.6                           0.508                1.26             -0.121                                 ok            True                  False
  REGN          100.00               17            1.35              7.89        830.18                29.20         0.577          pass              0.543             12.8                           0.205                3.16              0.438                                 ok            True                  False
  AMGN          100.00               20            0.76              2.34        441.24                27.99         0.571          pass              0.573             16.5                           0.188                6.08              0.806                                 ok            True                  False
  DXCM           87.88               33            0.91              0.57         88.92                51.46         0.563          pass              0.572             50.9                           0.454               -2.70             -0.100                                 ok            True                  False
   KHC           86.36               22            1.11              0.20         25.24                34.81         0.536          pass              0.525             73.8                           0.868                2.08              0.189                                 ok            True                  False
  BKNG           96.15               26            1.40              2.10        212.88                35.36         0.518          pass              0.612             17.8                           0.168               -0.70              0.042                                 ok            True                  False
  INSM           86.84               38            0.98              0.85        123.53               110.58         0.694          pass              0.668             76.6                           0.315               -7.26             -0.469            downtrend_blocked_slope           False                  False
  ABNB           94.29               35            0.42              0.56        190.26                61.60         0.652          pass              0.781             55.9                           0.307                5.33              0.518                                 ok           False                  False
  AMAT           87.88               33            0.81              2.74        478.87                76.53         0.647          pass              0.574             48.6                           0.442              -13.05             -1.328 downtrend_blocked_slope_and_streak           False                  False
  MCHP           89.74               39            0.18              0.09         73.46                69.10         0.644          pass              0.763             81.9                           0.538               -7.09             -0.799            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-08-26T10:00:05.932819-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T09:50:01.107222-04:00      manage_1000                    exit                                                                                         {"asset_type": "option", "contract_symbol": "KHC261016C00025000", "fill_price": 0.918, "pnl": -2927.4, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KHC"}
2026-08-26T00:00:04.646772-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 93}
2026-08-25T15:10:01.918364-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00       entry_1500 entry_candidate_skipped                                  {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826100005)

</details>

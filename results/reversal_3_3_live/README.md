# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 09:35:05 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$1,421.80`
- Equity: `$134,630.80`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-3,061.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 64224.0         20.0          20.07      220.60        223.18     last_price_stale                        NaN                unavailable                   False           224.0                   0.35         100.0               12              3.08         70.90            1.56                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 68985.0          1.1           1.05       44.42         44.54     last_price_stale                        NaN                unavailable                   False         -3285.0                  -4.55          80.0               15              0.97         20.09            0.78                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            0.80              0.35         62.82                25.86         0.599          pass              0.495             28.8                           0.264                1.57              0.154                  ok            True                  False
  GILD           90.00               10            1.64              1.83        157.91                28.72         0.578          pass              0.357             10.9                           0.246                5.52              0.355                  ok            True                  False
   KDP           93.33               15            1.17              0.29         34.87                25.67         0.565          pass              0.513             22.6                           0.196                5.88              0.529                  ok            True                  False
  CTSH           88.89               18            1.91              0.93         68.94                46.75         0.562          pass              0.350              1.1                           0.109               10.90              1.278                  ok            True                  False
   KHC           89.66               29            0.63              0.11         24.68                34.80         0.547          pass              0.586             49.2                           0.428                9.54              1.016                  ok            True                  False
   ADP           90.91               22            0.69              1.45        300.50                25.17         0.545          pass              0.498             24.3                           0.542                8.39              0.937                  ok            True                  False
   MAR           80.00               10            1.48              4.10        392.99                21.92         0.529          pass              0.234             60.3                           0.739                4.68              0.532                  ok            True                  False
   ROP           89.29               28            1.02              3.16        440.30                39.00         0.526          pass              0.540             40.0                           0.732               18.65              2.036                  ok            True                  False
   PEP           80.00               25            0.66              0.63        135.19                25.06         0.518          pass              0.260             36.2                           0.389                5.70              0.681                  ok            True                  False
  VRTX           80.00               20            1.34              4.85        515.41                29.88         0.518          pass              0.140              7.0                           0.277                5.22              0.612                  ok            True                  False
  ALNY           86.11               36            0.92              1.46        227.03                40.93         0.503          pass              0.387              0.0                           0.297                0.78             -0.101                  ok            True                  False
  PAYX           76.92               13            0.92              0.75        115.38                26.74         0.576          pass              0.078              0.0                           0.317                8.99              0.967                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-27T00:00:06.979802-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-26T15:10:06.955297-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:05:03.905393-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:00:06.230753-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:55:05.952188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:50:06.038156-04:00       entry_1500                   entry {"allocated_cash": 64000.0, "asset_type": "option", "contract_symbol": "TEAM261218C00230000", "contracts": 32, "early_entry_score": 0.492, "entry_mode": "regular", "entry_option_price": 20.0, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 10.0, "option_volume": 39.0, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.514}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 22.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.533}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                {"early_entry_score": 0.52, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 722.0, "option_spread_pct": 14.29, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.538}
2026-10-26T14:50:06.038156-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-26", "training_samples": 6183, "window": 5}
2026-10-26T12:00:05.800227-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027093505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027093505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027093505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027093505)

</details>

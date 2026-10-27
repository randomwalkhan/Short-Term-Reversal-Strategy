# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 10:25:06 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$139,451.80`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$1,760.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 65760.0         20.0          20.55      220.60        219.38          bid_ask_mid                      20.55                bid_ask_mid                    True          1760.0                   2.75         100.0               12              3.08         70.90           74.66                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 72270.0          1.1           1.10       44.42         44.35          bid_ask_mid                       1.10                bid_ask_mid                    True             0.0                   0.00          80.0               15              0.97         20.09           24.37                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.91               11            0.89              0.39         62.80                25.86         0.604          pass              0.437             26.3                           0.343                1.48              0.150                      ok            True                  False
 CMCSA           88.89               18            0.59              0.09         22.01                26.02         0.560          pass              0.417             23.5                           0.324                4.98              0.586                      ok            True                  False
   KDP           93.75               16            1.09              0.27         34.88                25.67         0.559          pass              0.602             46.5                           0.652                5.97              0.533                      ok            True                  False
   KHC           85.71               21            1.29              0.22         24.63                34.80         0.551          pass              0.314             11.1                           0.223                8.83              0.986                      ok            True                  False
   WMT           82.35               17            0.91              0.77        119.96                23.89         0.546          pass              0.169              1.8                           0.208                6.15              0.473                      ok            True                  False
  TEAM          100.00               24            1.80              2.82        222.21                43.78         0.531          pass              0.604             19.2                           0.252                5.45              0.863                      ok            True                  False
  GILD           92.00               25            0.98              1.09        158.22                28.72         0.528          pass              0.613             46.8                           0.585                6.23              0.386                      ok            True                  False
    ZS           90.91               33            1.22              2.22        259.50                57.14         0.518          pass              0.578             27.3                           0.259               12.52              1.861                      ok            True                  False
  ORLY           93.75               16            1.32              0.84         90.69                20.34         0.512          pass              0.472              4.8                           0.212                4.44              0.475                      ok            True                  False
  TMUS           87.80               41            0.10              0.10        146.89                64.06         0.636          pass              0.745             91.0                           0.731               -4.51             -0.675 downtrend_blocked_slope           False                  False
  MSTR           90.70               43            0.03              0.03        139.81                70.18         0.599          pass              0.837             97.2                           0.531               -8.15             -0.346 downtrend_blocked_slope           False                  False
   ADP          100.00                3            2.29              4.82        299.05                25.17         0.567          pass              0.462              1.9                           0.067                6.64              0.863                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-27T10:25:06.119259-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:20:06.240513-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:15:05.594224-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:10:04.139511-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "entry_ask": 13.2, "entry_bid": 10.2, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 25.64, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "matched_signals": 37, "recovery_stability_score": 0.75, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:05:02.075117-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:00:04.985513-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T00:00:06.979802-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-10-26T15:10:06.955297-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T15:05:03.905393-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T15:00:06.230753-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027102506)

</details>

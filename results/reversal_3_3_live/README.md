# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 10:35:07 EDT`
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
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 65760.0         20.0          20.55      220.60        219.07          bid_ask_mid                      20.55                bid_ask_mid                    True          1760.0                   2.75         100.0               12              3.08         70.90           75.40                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 72270.0          1.1           1.10       44.42         44.35          bid_ask_mid                       1.10                bid_ask_mid                    True             0.0                   0.00          80.0               15              0.97         20.09           24.37                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ           91.67               12            0.84              0.37         62.81                25.86         0.601          pass              0.475             30.3                           0.478                1.53              0.153                  ok            True                  False
   KDP           94.44               18            0.94              0.23         34.89                25.67         0.555          pass              0.655             53.5                           0.673                6.12              0.539                  ok            True                  False
   KHC           85.71               21            1.31              0.23         24.63                34.80         0.550          pass              0.310              9.7                           0.207                8.81              0.986                  ok            True                  False
   WMT           82.35               17            0.91              0.76        119.96                23.89         0.546          pass              0.180              5.2                           0.103                6.16              0.473                  ok            True                  False
  TEAM          100.00               22            1.94              3.04        222.11                43.78         0.536          pass              0.572             12.8                           0.194                5.30              0.856                  ok            True                  False
  GILD           92.00               25            0.97              1.08        158.23                28.72         0.528          pass              0.615             47.4                           0.566                6.24              0.387                  ok            True                  False
    ZS           89.66               29            1.57              2.87        259.22                57.14         0.517          pass              0.497             20.2                           0.210               12.11              1.845                  ok            True                  False
  ORLY           94.12               17            1.29              0.82         90.70                20.34         0.508          pass              0.501              8.9                           0.174                4.48              0.477                  ok            True                  False
  ABNB           83.33               18            1.65              1.98        170.20                25.32         0.500          pass              0.268             25.1                           0.256                1.59              0.134                  ok            True                  False
   ROP           78.57               14            1.48              4.57        439.69                39.00         0.564          pass              0.211             42.7                           0.487               18.11              2.015                  ok           False                  False
 CMCSA           90.00               20            0.43              0.07         22.02                26.02         0.559          pass              0.522             44.1                           0.373                5.15              0.594                  ok           False                  False
   ADP          100.00                3            2.41              5.09        298.94                25.17         0.559          pass              0.461              1.6                           0.069                6.51              0.857                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-27T10:35:07.163044-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:30:04.056749-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:25:06.119259-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:20:06.240513-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:15:05.594224-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:10:04.139511-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "entry_ask": 13.2, "entry_bid": 10.2, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 25.64, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "matched_signals": 37, "recovery_stability_score": 0.75, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:05:02.075117-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:00:04.985513-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T00:00:06.979802-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-10-26T15:10:06.955297-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027103507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027103507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027103507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027103507)

</details>

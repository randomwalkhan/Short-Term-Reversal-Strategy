# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 10:15:05 EDT`
Last processed slot: `early_entry_1015`

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
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 65760.0         20.0          20.55      220.60        220.12          bid_ask_mid                      20.55                bid_ask_mid                    True          1760.0                   2.75         100.0               12              3.08         70.90           73.85                  47.89                 302.0           39.0               0.10                      ok
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 72270.0          1.1           1.10       44.42         44.43          bid_ask_mid                       1.10                bid_ask_mid                    True             0.0                   0.00          80.0               15              0.97         20.09           24.46                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.91               11            0.88              0.39         62.80                25.86         0.604          pass              0.439             27.0                           0.419                1.49              0.151                  ok            True                  False
   PEP           80.00               15            0.98              0.93        135.06                25.06         0.561          pass              0.108              6.0                           0.263                5.37              0.667                  ok            True                  False
   KDP           93.33               15            1.16              0.28         34.87                25.67         0.560          pass              0.574             43.1                           0.644                5.90              0.530                  ok            True                  False
   KHC           83.33               18            1.40              0.24         24.63                34.80         0.560          pass              0.211              4.2                           0.211                8.72              0.982                  ok            True                  False
   ROP           83.33               18            1.33              4.10        439.89                39.00         0.553          pass              0.343             48.6                           0.716               18.29              2.022                  ok            True                  False
    ZS           91.18               34            0.96              1.74        259.70                57.14         0.529          pass              0.621             36.8                           0.214               12.81              1.873                  ok            True                  False
  TEAM          100.00               30            1.47              2.31        222.43                43.78         0.513          pass              0.686             33.9                           0.325                5.81              0.878                  ok            True                  False
   WMT           84.00               25            0.67              0.57        120.05                23.89         0.513          pass              0.322             21.4                           0.264                6.41              0.484                  ok            True                  False
  GILD           90.00               30            0.74              0.82        158.34                28.72         0.509          pass              0.631             60.1                           0.681                6.49              0.397                  ok            True                  False
  MSFT           96.15               26            0.62              2.31        531.61                19.60         0.504          pass              0.651             31.4                           0.248               -2.60             -0.232                  ok            True                  False
  ABNB           83.33               18            1.60              1.91        170.23                25.32         0.503          pass              0.276             27.8                           0.271                1.65              0.137                  ok            True                  False
   ADP          100.00                3            2.11              4.45        299.21                25.17         0.578          pass              0.466              2.6                           0.091                6.84              0.872                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-27T10:15:05.594224-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:10:04.139511-04:00 early_entry_1010      early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "entry_ask": 13.2, "entry_bid": 10.2, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 25.64, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "matched_signals": 37, "recovery_stability_score": 0.75, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:05:02.075117-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:00:04.985513-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T00:00:06.979802-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-10-26T15:10:06.955297-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T15:05:03.905393-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T15:00:06.230753-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T14:55:05.952188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 22.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.533}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027101505)

</details>

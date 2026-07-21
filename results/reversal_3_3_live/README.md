# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-21 13:54:15 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$34,176.75`
- Equity: `$34,176.75`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-21)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  ASML     option         option ASML260821C01800000      1          2026-07-20         2026-07-21        94.95       122.6 2765.0    29.12059 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.00               10            1.98              0.79         56.48                61.63         0.666          pass              0.170             34.6                           0.380               22.00              2.902                      ok            True                  False
  MDLZ          100.00               14            0.75              0.32         60.13                32.62         0.626          pass              0.673             61.3                           0.763               -0.67              0.202                      ok            True                  False
  BKNG           89.66               29            0.96              1.20        178.93                41.79         0.544          pass              0.519             26.8                           0.392               -2.32              0.191                      ok            True                  False
  TMUS           83.33               12            2.00              2.74        194.46                36.36         0.539          pass              0.223             22.4                           0.434                3.78              0.675                      ok            True                  False
  PAYX          100.00               12            2.20              1.78        114.44                33.31         0.536          pass              0.489              7.3                           0.285                4.20              0.782                      ok            True                  False
   CSX           91.30               23            0.56              0.20         50.03                18.51         0.503          pass              0.627             62.9                           0.614                2.72              0.353                      ok            True                  False
  MNST          100.00               26            0.53              0.36         95.30                21.78         0.502          pass              0.765             69.5                           0.752               -2.04             -0.004                      ok            True                  False
 CMCSA           76.47               17            0.19              0.03         23.77                28.63         0.608          pass              0.340             77.5                           0.730                1.39              0.227                      ok           False                  False
   KHC           87.50               16            0.44              0.08         25.83                34.83         0.600          pass              0.459             53.1                           0.484                1.76              0.450                      ok           False                  False
   PEP           86.36               22            0.44              0.42        135.28                30.90         0.592          pass              0.458             49.6                           0.641               -6.98             -0.522 downtrend_blocked_slope           False                  False
   ADP          100.00                2            2.67              4.76        253.20                34.09         0.574          pass              0.464              2.3                           0.235                1.15              0.503                      ok           False                  False
   EXC           95.45               22            0.30              0.10         45.92                23.50         0.564          pass              0.777             80.3                           0.685               -3.68             -0.307 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-07-21T11:17:25.409204-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:59:34.342189-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:16:24.427902-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "CTAS260821C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "entry_ask": 8.0, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 17088.38, "hypothetical_contracts": 22, "matched_signals": 34, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 548.0, "option_spread_pct": 14.77, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.741, "early_reclaim_pct": 77.8, "matched_signals": 34, "recovery_stability_score": 0.727, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-21T09:33:02.218910-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "ASML260821C01800000", "fill_price": 122.6, "pnl": 2765.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 29.12, "ticker": "ASML"}
2026-07-21T00:00:02.341945-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-07-20T15:10:01.116454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-20T15:05:01.111853-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-20T15:00:01.116839-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-20T14:55:03.114879-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-07-20T14:50:01.117820-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 9495.0, "asset_type": "option", "contract_symbol": "ASML260821C01800000", "contracts": 1, "early_entry_score": 0.694, "entry_mode": "regular", "entry_option_price": 94.95, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 3.9, "option_volume": 26.0, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.585}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260721135415)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260721135415)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260721135415)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260721135415)

</details>

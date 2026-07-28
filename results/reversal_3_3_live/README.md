# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-28 15:45:01 EDT`
Last processed slot: `manual`

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

- Cash: `$18,410.50`
- Equity: `$36,470.50`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$-322.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   0    129     18382.5                 18060.0         1.42            1.4       51.22          51.1          bid_ask_mid                        1.4                bid_ask_mid                    True          -322.5                  -1.75         92.86               14              1.11         25.66           26.42                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           90.00               10            1.25              0.45         51.61                24.65         0.595            pass              0.333              2.3                           0.131                3.04              0.471                                 ok            True                  False
  KLAC           84.62               13            4.85              6.90        200.40                94.03         0.564            pass              0.321             40.6                           0.530              -12.94             -1.034 downtrend_blocked_slope_and_streak           False                  False
   TXN           89.47               38            0.21              0.41        279.24                50.69         0.498 below_threshold              0.771             93.8                           0.690               -6.61             -0.701            downtrend_blocked_slope           False                  False
  ASML           92.31               13            4.11             47.65       1634.84                55.90         0.498 below_threshold              0.497             33.1                           0.486               -8.04             -0.459            downtrend_blocked_slope           False                  False
  MCHP           89.66               29            1.98              1.08         77.44                53.73         0.492 below_threshold              0.579             48.7                           0.490               -9.35             -0.820 downtrend_blocked_slope_and_streak           False                  False
   BKR           75.00                4            3.61              1.53         59.93                42.85         0.479 below_threshold              0.106             19.5                           0.433                1.28              0.220                                 ok           False                  False
   ADI           84.38               32            0.84              2.19        370.95                41.03         0.471 below_threshold              0.529             72.7                           0.588               -4.47             -0.410 downtrend_blocked_slope_and_streak           False                  False
  SBUX           87.50               32            0.67              0.48        103.44                24.10         0.461 below_threshold              0.485             30.7                           0.403               -4.08             -0.373 downtrend_blocked_slope_and_streak           False                  False
  MSTR           67.74               31            3.10              2.14         97.73                77.85         0.457 below_threshold              0.320             44.7                           0.334                3.79              0.174                                 ok           False                  False
  SNPS           76.19               21            2.22              6.04        386.40                41.22         0.452 below_threshold              0.136              5.8                           0.169              -12.32             -1.476 downtrend_blocked_slope_and_streak           False                  False
  NXPI           82.61               23            2.39              4.48        265.75                43.93         0.442 below_threshold              0.291             30.3                           0.298               -6.15             -0.346            downtrend_blocked_slope           False                  False
  INSM           77.50               40            0.73              0.53        104.50                34.55         0.439 below_threshold              0.397             51.0                           0.335               -4.74             -0.408            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-28T15:10:01.368201-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T15:05:06.240924-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T15:00:04.083002-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T14:55:03.998605-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-28T14:50:06.162637-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 18382.5, "asset_type": "option", "contract_symbol": "CSX260918C00052500", "contracts": 129, "early_entry_score": 0.452, "entry_mode": "regular", "entry_option_price": 1.425, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 4433.0, "option_spread_pct": 3.51, "option_volume": 101.0, "success_rate": 92.86, "ticker": "CSX", "timing_score": 0.582}
2026-07-28T14:50:06.162637-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-28", "training_samples": 5521, "window": 5}
2026-07-28T11:54:53.220532-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T11:14:56.207799-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T10:51:29.274795-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-28T10:15:51.062656-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "MAR260918C00380000", "current_drop_pct": 0.78, "early_entry_score": 0.779, "early_reclaim_pct": 64.8, "entry_ask": 20.2, "entry_bid": 16.5, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 18396.5, "hypothetical_contracts": 10, "matched_signals": 30, "option_liquidity_status": "wide_spread", "option_open_interest": 1131.0, "option_spread_pct": 20.16, "option_volume": 41.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.515, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.779, "early_reclaim_pct": 64.8, "matched_signals": 30, "recovery_stability_score": 0.755, "success_rate": 100.0, "ticker": "MAR", "timing_score": 0.515, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260728154501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260728154501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260728154501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260728154501)

</details>

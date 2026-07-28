# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-28 15:40:02 EDT`
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

- Cash: `$18,410.50`
- Equity: `$37,115.50`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$322.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   0    129     18382.5                 18705.0         1.42           1.45       51.22          51.2          bid_ask_mid                       1.45                bid_ask_mid                    True           322.5                   1.75         92.86               14              1.11         25.66           26.51                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           93.33               15            1.07              0.39         51.63                24.65         0.579            pass              0.480             11.2                           0.227                3.23              0.480                                 ok            True                  False
  KLAC           84.62               13            4.70              6.69        200.49                94.03         0.574            pass              0.328             42.5                           0.644              -12.80             -1.027 downtrend_blocked_slope_and_streak           False                  False
  ASML           92.31               13            4.10             47.46       1634.92                55.90         0.499 below_threshold              0.498             33.3                           0.559               -8.03             -0.458            downtrend_blocked_slope           False                  False
   TXN           89.47               38            0.31              0.62        279.15                50.69         0.491 below_threshold              0.760             90.6                           0.731               -6.71             -0.706            downtrend_blocked_slope           False                  False
  MCHP           90.00               30            1.96              1.07         77.44                53.73         0.487 below_threshold              0.596             49.2                           0.538               -9.33             -0.819 downtrend_blocked_slope_and_streak           False                  False
   BKR           75.00                4            3.67              1.56         59.92                42.85         0.476 below_threshold              0.102             18.2                           0.428                1.22              0.217                                 ok           False                  False
   ADI           84.38               32            0.81              2.12        370.98                41.03         0.473 below_threshold              0.532             73.6                           0.661               -4.44             -0.409 downtrend_blocked_slope_and_streak           False                  False
  SBUX           87.88               33            0.57              0.41        103.47                24.10         0.461 below_threshold              0.532             40.7                           0.463               -3.99             -0.368 downtrend_blocked_slope_and_streak           False                  False
  MSTR           67.74               31            3.08              2.13         97.74                77.85         0.459 below_threshold              0.321             45.0                           0.355                3.81              0.175                                 ok           False                  False
  SNPS           77.27               22            2.16              5.89        386.46                41.22         0.451 below_threshold              0.146              7.1                           0.201              -12.27             -1.473 downtrend_blocked_slope_and_streak           False                  False
  NXPI           81.82               22            2.50              4.69        265.66                43.93         0.441 below_threshold              0.254             27.1                           0.316               -6.26             -0.351            downtrend_blocked_slope           False                  False
    EA          100.00               40            0.05              0.08        209.04                 3.91         0.436 below_threshold              0.879             78.6                           0.448                1.26              0.133                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260728154002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260728154002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260728154002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260728154002)

</details>

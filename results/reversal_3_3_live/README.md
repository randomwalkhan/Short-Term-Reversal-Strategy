# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 15:25:04 EST`
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

- Cash: `$48,929.80`
- Equity: `$97,969.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$1,840.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   0     32     47200.0                 49040.0        14.75          15.32       344.6        343.64          bid_ask_mid                      15.32                bid_ask_mid                    True          1840.0                    3.9         100.0               14              1.32         27.92           30.03                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           96.15               26            1.30              6.29        686.95                78.44         0.715          pass              0.610             10.6                           0.272                0.68             -0.079                                 ok            True                  False
  AAPL          100.00               13            1.47              3.59        347.67                27.12         0.555          pass              0.539             21.2                           0.291                0.58              0.023                                 ok            True                  False
   MAR           90.00               10            1.41              4.09        412.29                25.25         0.553          pass              0.391             22.9                           0.409               -1.82             -0.145                                 ok            True                  False
  SBUX           87.50               24            0.79              0.58        104.22                35.02         0.519          pass              0.446             33.6                           0.396               -1.10             -0.214                                 ok            True                  False
  ALNY           74.19               31            1.68              1.74        147.08               110.46         0.720          pass              0.233              7.1                           0.089               -6.80             -0.591 downtrend_blocked_slope_and_streak           False                  False
  INTC           63.64               11            5.83              2.27         54.75               141.91         0.675          pass              0.090              5.2                           0.175               -6.77             -1.033 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                1            7.51             19.92        370.48               122.37         0.614          pass              0.475              4.6                           0.198              -10.39             -0.794 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.47               17            1.51              2.88        271.43                55.59         0.561          pass              0.115              4.1                           0.116               -5.70             -0.646            downtrend_blocked_slope           False                  False
  GOOG           75.00               16            1.53              2.90        269.78                53.33         0.560          pass              0.108              3.9                           0.076               -6.01             -0.661            downtrend_blocked_slope           False                  False
  FTNT           50.00                8            5.09              4.69        129.45                96.17         0.537          pass              0.065              3.8                           0.191                4.99              0.558                                 ok           False                  False
  ABNB           89.74               39            0.56              0.67        172.50                57.19         0.536          pass              0.646             46.4                           0.293               -9.56             -0.884 downtrend_blocked_slope_and_streak           False                  False
  ISRG           84.62               26            1.07              3.04        405.94                45.14         0.536          pass              0.316             10.8                           0.167              -11.02             -1.243 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-20T15:10:05.376851-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T15:05:06.103074-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T15:00:05.079544-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T14:55:06.056762-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T14:50:04.211371-05:00       entry_1500                   entry {"allocated_cash": 47200.0, "asset_type": "option", "contract_symbol": "AAPL270115C00345000", "contracts": 32, "early_entry_score": 0.57, "entry_mode": "regular", "entry_option_price": 14.75, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 12741.0, "option_spread_pct": 3.39, "option_volume": 229.0, "success_rate": 100.0, "ticker": "AAPL", "timing_score": 0.558}
2026-11-20T14:50:04.211371-05:00       entry_1500 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.665, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 75.0, "option_spread_pct": 14.91, "option_volume": 62.0, "reason": "no_trade_low_option_liquidity", "ticker": "IDXX", "timing_score": 0.708}
2026-11-20T14:50:04.211371-05:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-20", "training_samples": 6240, "window": 5}
2026-11-20T12:00:03.900140-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120152504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120152504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120152504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120152504)

</details>

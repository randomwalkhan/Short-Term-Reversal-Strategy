# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 14:50:03 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$18,164.25`
- Equity: `$32,804.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$540.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14640.0        35.25           36.6      477.34        474.48          bid_ask_mid                       36.6                bid_ask_mid                    True           540.0                   3.83         97.22               36              0.69         45.69           51.61                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.59               27            1.28              2.02        223.77               139.09         0.747          pass              0.682             52.6                           0.476               19.10              3.730                                 ok            True                  False
  MELI           94.74               38            0.50              5.96       1692.98                61.27         0.615          pass              0.777             45.2                           0.311                4.96              0.804                                 ok            True                  False
  INTC           95.45               22            2.28              1.93        120.06                85.20         0.583          pass              0.634             32.0                           0.556                1.90              0.997                                 ok            True                  False
  INSM           67.86               28            1.91              1.45        107.75               111.11         0.758          pass              0.197              0.2                           0.028               -8.06             -0.417            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.74              0.66        127.48                25.60         0.594          pass              0.104             10.5                           0.229               -1.38              0.098                                 ok           False                  False
  AMAT           91.43               35            0.10              0.31        449.55                50.48         0.565          pass              0.795             88.9                           0.585                2.10              0.646                                 ok           False                  False
  REGN           80.95               21            1.65              7.16        618.45                44.05         0.546          pass              0.175              7.1                           0.186              -14.12             -1.114 downtrend_blocked_slope_and_streak           False                  False
  GOOG           87.50                8            1.94              5.24        383.87                41.01         0.544          pass              0.319             21.4                           0.284               -4.67             -0.356            downtrend_blocked_slope           False                  False
 GOOGL           87.50                8            2.09              5.70        387.69                41.30         0.540          pass              0.303             16.4                           0.260               -4.76             -0.348            downtrend_blocked_slope           False                  False
  SBUX          100.00                6            1.67              1.18        100.24                16.60         0.536          pass              0.593             46.5                           0.452               -6.35             -0.745            downtrend_blocked_slope           False                  False
  KLAC           91.67               36            0.34              4.53       1925.69                52.36         0.535          pass              0.718             60.0                           0.445                1.62              0.905                                 ok           False                  False
  AMGN           90.62               32            0.34              0.81        336.13                27.03         0.507          pass              0.680             66.4                           0.567                0.49              0.279                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-29T14:50:03.249987-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T14:50:03.249987-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-29", "training_samples": 5149, "window": 5}
2026-05-29T12:00:03.057178-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529145003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529145003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529145003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529145003)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 09:30:02 EST`
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

- Cash: `$64,944.05`
- Equity: `$129,459.05`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$-172.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ORLY     option         option ORLY261218C00095000       2026-11-05                   1    345     64687.5                 64515.0         1.88           1.87       90.92         89.38     last_price_stale                        NaN                unavailable                   False          -172.5                  -0.27         100.0               14              1.54         28.75            3.13                   25.4                2285.0          162.0               0.13                      ok
```

## Today's Closed Trades (2026-11-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   APP           91.67               48            0.59              1.46        355.47               119.33         0.750          pass              0.840             84.6                           0.629               36.03              2.421                      ok            True                   True
  MSFT          100.00               14            1.59              5.95        533.38                35.82         0.547          pass              0.621             46.6                           0.333                0.56              0.096                      ok            True                  False
   MAR           81.82               11            1.36              3.97        415.58                25.23         0.531          pass              0.270             53.9                           0.388                5.35              0.806                      ok            True                  False
  CTAS           94.74               19            1.18              1.88        225.61                27.57         0.516          pass              0.681             58.8                           0.530               -0.17              0.294                      ok            True                  False
  FAST           94.74               19            0.89              0.33         52.76                21.79         0.511          pass              0.573             23.0                           0.265                1.51              0.247                      ok            True                  False
  IDXX          100.00                2            3.09             14.50        664.50                77.01         0.702          pass              0.470              0.0                           0.250               15.99              2.323                      ok           False                  False
  ALNY           62.50               16            2.74              3.09        159.75               108.53         0.669          pass              0.125              6.2                           0.183              -30.07             -4.686 downtrend_blocked_slope           False                  False
  ISRG           85.71                7            2.35              7.71        465.21                42.48         0.562          pass              0.213              1.6                           0.108                1.15              0.360                      ok           False                  False
  TMUS           60.00               10            2.11              2.38        159.57                69.87         0.562          pass              0.172             38.5                           0.279                7.27              1.015                      ok           False                  False
  REGN           72.73               22            1.45              9.16        898.97                54.35         0.560          pass              0.172             12.1                           0.330               10.53              1.691                      ok           False                  False
  AAPL          100.00                8            1.64              3.94        342.48                25.86         0.553          pass              0.482              8.8                           0.276               -2.64             -0.192                      ok           False                  False
  GILD           80.00                5            2.13              2.50        166.50                37.28         0.553          pass              0.093             12.7                           0.223                5.10              0.794                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-06T00:00:05.873156-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-05T15:10:05.513182-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:05:05.534747-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T15:00:06.437749-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:55:05.870253-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-05T14:50:06.583825-05:00       entry_1500              entry {"allocated_cash": 64687.5, "asset_type": "option", "contract_symbol": "ORLY261218C00095000", "contracts": 345, "early_entry_score": 0.515, "entry_mode": "regular", "entry_option_price": 1.875, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 2285.0, "option_spread_pct": 13.33, "option_volume": 162.0, "success_rate": 100.0, "ticker": "ORLY", "timing_score": 0.528}
2026-11-05T14:50:06.583825-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-05", "training_samples": 6319, "window": 5}
2026-11-05T12:00:04.376215-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:55:05.652080-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:50:05.625919-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106093002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106093002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106093002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106093002)

</details>

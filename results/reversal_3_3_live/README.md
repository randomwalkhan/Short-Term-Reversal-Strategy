# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 09:40:04 EST`
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
  ORLY     option         option ORLY261218C00095000       2026-11-05                   1    345     64687.5                 64515.0         1.88           1.87       90.92         89.33     last_price_stale                        NaN                unavailable                   False          -172.5                  -0.27         100.0               14              1.54         28.75            3.13                   25.4                2285.0          162.0               0.13                      ok
```

## Today's Closed Trades (2026-11-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  IDXX           94.12               17            1.82              8.57        667.04                77.01         0.685          pass              0.614             40.9                           0.524               17.50              2.382                      ok            True                  False
  GILD           86.67               15            1.39              1.63        166.87                37.28         0.542          pass              0.394             43.0                           0.433                5.90              0.828                      ok            True                  False
   MAR           88.24               17            0.95              2.77        416.09                25.23         0.525          pass              0.522             67.8                           0.759                5.79              0.825                      ok            True                  False
  ISRG           90.91               22            1.56              5.12        466.32                42.48         0.519          pass              0.547             41.5                           0.564                1.97              0.397                      ok            True                  False
  REGN           84.62               39            0.61              3.85        901.25                54.35         0.516          pass              0.563             64.9                           0.763               11.48              1.730                      ok            True                  False
  VRTX           80.95               21            1.35              5.11        540.31                36.99         0.509          pass              0.281             43.6                           0.561                2.15              0.437                      ok            True                  False
  MSFT          100.00               29            0.79              2.98        534.65                35.82         0.504          pass              0.797             73.3                           0.631                1.37              0.132                      ok            True                  False
  ALNY           84.44               45            0.51              0.56        156.42               108.53         0.700          pass              0.587             66.1                           0.506              -30.43             -4.709 downtrend_blocked_slope           False                  False
   KDP          100.00                2            2.44              0.63         36.62                35.93         0.578          pass              0.529             23.7                           0.324                3.78              0.536                      ok           False                  False
  TMUS           69.23               13            1.73              1.95        159.76                69.87         0.575          pass              0.226             49.6                           0.538                7.69              1.032                      ok           False                  False
  MSTR           87.80               41            0.19              0.17        129.23                81.05         0.565          pass              0.744             93.3                           0.620              -11.62             -1.020 downtrend_blocked_slope           False                  False
  AAPL          100.00                9            1.42              3.43        342.70                25.86         0.560          pass              0.518             20.6                           0.245               -2.43             -0.183                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106094004)

</details>

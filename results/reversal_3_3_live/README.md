# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 10:00:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$4,018.50`
- Equity: `$34,003.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$400.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 13785.0        44.70          45.95      510.62        505.19     last_price_stale                        NaN                unavailable                   False           375.0                   2.80         97.14               35              0.50         52.16           61.38                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   1      5     16175.0                 16200.0        32.35          32.40      352.55        349.29     last_price_stale                        NaN                unavailable                   False            25.0                   0.15         97.30               37              0.56         47.46            0.00                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           91.67               12            2.17              4.67        306.17                67.99         0.701          pass              0.515             40.2                           0.427                7.83              1.008                                 ok            True                  False
 GOOGL           85.71               28            0.93              2.61        399.95                40.65         0.553          pass              0.497             56.5                           0.731                3.02              0.327                                 ok            True                  False
  GOOG           86.67               30            0.83              2.30        396.19                40.76         0.551          pass              0.543             59.1                           0.707                2.78              0.319                                 ok            True                  False
  SNPS           97.06               34            0.95              3.38        508.57                41.57         0.540          pass              0.769             51.8                           0.575                3.31              0.326                                 ok            True                  False
  CDNS           97.06               34            0.98              2.42        351.80                37.94         0.519          pass              0.767             51.7                           0.477                2.48              0.187                                 ok            True                  False
  MCHP           86.67               15            3.19              2.17         96.11                50.84         0.511          pass              0.299             12.2                           0.202               -0.01             -0.102                                 ok            True                  False
  NXPI           76.19               21            2.13              4.39        292.29                90.16         0.715          pass              0.244             33.2                           0.574               -2.49             -0.025                                 ok           False                  False
  CHTR           66.67                6            4.57              4.74        145.97               114.29         0.670          pass              0.067              0.0                           0.157              -17.77             -1.743            downtrend_blocked_slope           False                  False
  INSM           46.67               15            3.28              2.65        114.48               110.45         0.633          pass              0.143             15.6                           0.202              -16.08             -2.262 downtrend_blocked_slope_and_streak           False                  False
  SHOP           86.11               36            1.23              0.84         97.06                79.75         0.611          pass              0.444             15.5                           0.205              -24.63             -2.772 downtrend_blocked_slope_and_streak           False                  False
   AEP           80.00                5            1.41              1.27        128.06                23.26         0.589          pass              0.122             21.0                           0.231               -6.72             -0.621            downtrend_blocked_slope           False                  False
  GEHC           61.54               26            1.41              0.62         62.41                57.53         0.585          pass              0.299             44.6                           0.272                1.24              0.214                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T10:00:02.295451-04:00 early_entry_1000  entry_skipped                                                                             {"reason": "max_open_positions"}
2026-05-15T00:00:05.036344-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-14T15:10:04.841035-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T14:55:08.383255-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T14:50:07.158439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-14T14:50:07.158439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-14", "training_samples": 5049, "window": 5}
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-14T10:50:02.088724-04:00 early_entry_1050  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515100002)

</details>

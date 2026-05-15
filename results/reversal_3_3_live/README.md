# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 10:05:04 EDT`
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
- Equity: `$32,653.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-950.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 13785.0        44.70          45.95      510.62        506.41     last_price_stale                        NaN                unavailable                   False           375.0                   2.80         97.14               35              0.50         52.16           60.57                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   1      5     16175.0                 14850.0        32.35          29.70      352.55        350.52          bid_ask_mid                       29.7                bid_ask_mid                    True         -1325.0                  -8.19         97.30               37              0.56         47.46           47.24                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.31               13            1.95              4.21        306.36                67.99         0.706          pass              0.557             46.1                           0.503                8.07              1.018                                 ok            True                  False
  SNPS           97.14               35            0.71              2.53        508.94                41.57         0.548          pass              0.813             64.0                           0.670                3.56              0.337                                 ok            True                   True
 GOOGL           87.50               32            0.76              2.13        400.16                40.65         0.540          pass              0.594             64.5                           0.778                3.20              0.335                                 ok            True                  False
  GOOG           88.24               34            0.63              1.76        396.41                40.76         0.538          pass              0.639             68.6                           0.761                2.98              0.328                                 ok            True                  False
  MCHP           83.33               12            3.35              2.27         96.07                50.84         0.518          pass              0.178              7.9                           0.153               -0.17             -0.109                                 ok            True                  False
  CDNS           97.30               37            0.78              1.91        352.02                37.94         0.512          pass              0.817             61.8                           0.679                2.69              0.197                                 ok            True                   True
  NXPI           72.73               22            1.90              3.91        292.50                90.16         0.717          pass              0.273             40.6                           0.606               -2.25             -0.014                                 ok           False                  False
  CHTR           66.67                6            4.55              4.72        145.98               114.29         0.670          pass              0.076              3.2                           0.067              -17.75             -1.742            downtrend_blocked_slope           False                  False
  INSM           38.46               13            3.45              2.79        114.42               110.45         0.625          pass              0.116             11.1                           0.146              -16.23             -2.270 downtrend_blocked_slope_and_streak           False                  False
   AEP           80.00                5            1.47              1.32        128.03                23.26         0.586          pass              0.111             17.5                           0.198               -6.78             -0.624            downtrend_blocked_slope           False                  False
  GEHC           65.52               29            1.17              0.51         62.45                57.53         0.585          pass              0.346             53.8                           0.323                1.48              0.224                                 ok           False                  False
   XEL           93.33               15            1.12              0.63         79.76                24.20         0.577          pass              0.501             18.2                           0.208               -4.18             -0.310            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T10:05:04.229030-04:00 early_entry_1005  entry_skipped                                                                             {"reason": "max_open_positions"}
2026-05-15T10:00:02.295451-04:00 early_entry_1000  entry_skipped                                                                             {"reason": "max_open_positions"}
2026-05-15T00:00:05.036344-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-14T15:10:04.841035-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T14:55:08.383255-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-14T14:50:07.158439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-14T14:50:07.158439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-14", "training_samples": 5049, "window": 5}
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515100504)

</details>

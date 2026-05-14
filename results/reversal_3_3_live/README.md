# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-14 15:40:05 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$33,578.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-25.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   1      3     13410.0                 13635.0        44.70          45.45      510.62        508.81          bid_ask_mid                      45.45                bid_ask_mid                    True           225.0                   1.68         97.14               35              0.50         52.16           56.19                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   0      5     16175.0                 15925.0        32.35          31.85      352.55        352.05          bid_ask_mid                      31.85                bid_ask_mid                    True          -250.0                  -1.55         97.30               37              0.56         47.46           46.86                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               18            3.38              2.85        119.07               109.59         0.651          pass              0.647             42.9                           0.471               23.02              2.674                                 ok            True                  False
   KDP           88.00               25            0.84              0.17         29.24                33.33         0.548          pass              0.487             39.5                           0.518               -1.14             -0.001                                 ok            True                  False
    MU           83.87               31            1.85             10.41        799.17                77.31         0.543          pass              0.436             46.1                           0.310               52.52              4.625                                 ok            True                  False
  MPWR           88.89               27            1.55             17.85       1642.70                51.84         0.507          pass              0.546             48.3                           0.629                0.65              0.278                                 ok            True                  False
  MDLZ           83.33               24            0.77              0.33         61.38                21.21         0.505          pass              0.359             42.1                           0.411               -0.64             -0.009                                 ok            True                  False
   ADI           81.48               27            1.11              3.37        430.94                36.56         0.504          pass              0.329             41.9                           0.497                6.29              0.814                                 ok            True                  False
  CDNS           97.30               37            0.72              1.79        353.78                37.69         0.501          pass              0.804             58.0                           0.540                6.80              0.580                                 ok            True                  False
  NXPI           74.07               27            1.19              2.50        297.34                89.45         0.721          pass              0.336             50.1                           0.719                0.43              0.147                                 ok           False                  False
  INSM           74.29               35            1.12              0.92        117.59               110.56         0.585          pass              0.479             84.5                           0.630              -14.42             -2.473 downtrend_blocked_slope_and_streak           False                  False
  SNPS           97.56               41            0.09              0.33        509.14                41.52         0.547          pass              0.935             93.3                           0.595                5.43              0.543                                 ok           False                  False
  QCOM          100.00                1            5.42              8.09        209.70                94.09         0.543          pass              0.498             14.4                           0.277               12.27              2.365                                 ok           False                  False
   BKR           66.67               24            1.04              0.48         65.21                37.91         0.532          pass              0.285             46.0                           0.368               -6.78             -0.778 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-14T15:10:04.841035-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:55:08.383255-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:50:07.158439-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T14:50:07.158439-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-14", "training_samples": 5049, "window": 5}
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:50:02.088724-04:00 early_entry_1050  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:06:24.763261-04:00 early_entry_1005          entry {"allocated_cash": 16175.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.833, "entry_mode": "early", "entry_option_price": 32.35, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 10.2, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.51}
2026-05-14T00:00:04.843423-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260514154005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260514154005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260514154005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260514154005)

</details>

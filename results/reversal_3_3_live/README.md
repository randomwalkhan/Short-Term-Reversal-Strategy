# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-14 13:00:04 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$34,118.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$515.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   1      3     13410.0                 13950.0        44.70           46.5      510.62        509.28          bid_ask_mid                       46.5                bid_ask_mid                    True           540.0                   4.03         97.14               35              0.50         52.16           57.58                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   0      5     16175.0                 16150.0        32.35           32.3      352.55        352.27          bid_ask_mid                       32.3                bid_ask_mid                    True           -25.0                  -0.15         97.30               37              0.56         47.46           49.22                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               21            2.57              2.16        119.36               109.59         0.678          pass              0.711             56.6                           0.666               24.05              2.712                                 ok            True                  False
    MU           84.85               33            1.28              7.18        800.55                77.31         0.566          pass              0.528             62.8                           0.669               53.41              4.651                                 ok            True                  False
   KDP           89.29               28            0.67              0.14         29.25                33.33         0.545          pass              0.527             35.0                           0.308               -0.97              0.007                                 ok            True                  False
  MPWR           87.50               24            1.71             19.75       1641.88                51.84         0.525          pass              0.406             20.2                           0.284                0.48              0.270                                 ok            True                  False
  CDNS           97.30               37            0.67              1.67        353.83                37.69         0.504          pass              0.813             60.8                           0.484                6.85              0.583                                 ok            True                  False
  NXPI           70.83               24            1.58              3.30        297.00                89.45         0.721          pass              0.192              8.7                           0.178                0.04              0.129                                 ok           False                  False
  INSM           71.43               28            1.69              1.39        117.39               110.56         0.589          pass              0.409             76.7                           0.496              -14.91             -2.499 downtrend_blocked_slope_and_streak           False                  False
   AEP           91.30               23            0.16              0.15        127.89                23.15         0.578          pass              0.663             72.4                           0.402               -6.16             -0.628            downtrend_blocked_slope           False                  False
  QCOM          100.00                1            5.00              7.45        209.98                94.09         0.576          pass              0.495             12.5                           0.205               12.77              2.385                                 ok           False                  False
  SNPS           97.56               41            0.00              0.00        509.28                41.52         0.553          pass              0.955            100.0                           0.538                5.53              0.547                                 ok           False                  False
   BKR           58.82               17            1.28              0.59         65.16                37.91         0.551          pass              0.202             33.3                           0.396               -7.01             -0.789 downtrend_blocked_slope_and_streak           False                  False
  GOOG           88.89               36            0.46              1.28        398.49                40.78         0.528          pass              0.676             71.0                           0.622                4.00              0.371                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:50:02.088724-04:00 early_entry_1050  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:06:24.763261-04:00 early_entry_1005          entry {"allocated_cash": 16175.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.833, "entry_mode": "early", "entry_option_price": 32.35, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 10.2, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.51}
2026-05-14T00:00:04.843423-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
2026-05-13T15:10:06.837461-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-13T15:05:03.914074-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260514130004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260514130004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260514130004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260514130004)

</details>

# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-14 09:44:26 EDT`
Last processed slot: `manual`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$35,394.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$1,791.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   1      3     13410.0                 15201.0         44.7          50.67      510.62        506.87          1791.0                  13.36         97.14               35               0.5         52.16             0.0                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               21            2.56              2.15        119.37               109.59         0.679          pass              0.712             56.8                           0.747               24.06              2.712                  ok            True                  False
  TEAM           84.85               33            2.21              1.25         80.09               113.96         0.672          pass              0.428             26.1                           0.290               14.94             -0.045                  ok            True                  False
  QCOM           86.67               15            2.21              3.30        211.75                94.09         0.634          pass              0.458             61.2                           0.663               16.08              2.517                  ok            True                  False
  FTNT           96.67               30            1.26              1.04        117.25                71.27         0.629          pass              0.762             55.2                           0.326               37.84              3.922                  ok            True                  False
  MSTR           89.47               38            0.97              1.21        177.51                76.86         0.600          pass              0.615             38.6                           0.323                6.56              0.405                  ok            True                  False
 GOOGL           86.21               29            0.84              2.37        401.61                40.63         0.546          pass              0.488             46.9                           0.455                3.75              0.360                  ok            True                  False
  MCHP           83.87               31            0.92              0.62         96.44                51.21         0.543          pass              0.403             35.0                           0.385                3.13              0.289                  ok            True                  False
  GOOG           87.50               32            0.74              2.07        398.15                40.78         0.536          pass              0.551             50.1                           0.473                3.70              0.358                  ok            True                  False
  MPWR           88.89               27            1.44             16.66       1643.21                51.84         0.524          pass              0.501             32.7                           0.259                0.75              0.282                  ok            True                  False
   ADI           81.25               32            0.63              1.90        431.57                36.56         0.511          pass              0.356             41.6                           0.327                6.81              0.836                  ok            True                  False
  CDNS           96.67               30            1.41              3.49        353.05                37.69         0.505          pass              0.638             18.1                           0.246                6.06              0.549                  ok            True                  False
  MSFT           87.50               32            0.62              1.77        404.45                28.62         0.505          pass              0.522             41.6                           0.291               -1.25             -0.170                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-14T00:00:04.843423-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-13T15:10:06.837461-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:05:03.914074-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260514094426)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260514094426)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260514094426)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260514094426)

</details>

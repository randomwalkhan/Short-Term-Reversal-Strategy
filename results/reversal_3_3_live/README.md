# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 09:45:06 EDT`
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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$19,575.25`
- Equity: `$31,075.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-510.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   1      2     12010.0                 11500.0        60.05           57.5       531.8        498.33     last_price_stale                        NaN                unavailable                   False          -510.0                  -4.25         97.22               36              0.52         54.56             0.1                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           84.85               33            1.20              7.79        925.07               100.84         0.651          pass              0.579             77.0                           0.445               14.14              2.087                      ok            True                  False
  SOXL           88.46               26            2.36              3.60        216.41               139.87         0.634          pass              0.637             80.5                           0.462               15.50              2.658                      ok            True                  False
  INTC           96.15               26            1.88              1.60        121.08                92.16         0.607          pass              0.742             58.4                           0.467               -0.67              0.742                      ok            True                  False
   HON           82.35               17            1.01              1.64        230.85                25.08         0.541          pass              0.247             27.8                           0.224                5.74              0.839                      ok            True                  False
  AMAT           83.33               24            1.90              5.95        445.70                50.47         0.523          pass              0.235              0.0                           0.177                0.84              0.349                      ok            True                  False
  NXPI           91.43               35            0.55              1.26        328.70                91.24         0.503          pass              0.774             84.0                           0.690                9.73              1.356                      ok            True                   True
  MNST           91.89               37            0.50              0.31         89.11                49.17         0.502          pass              0.738             63.7                           0.472                3.33              0.265                      ok            True                  False
    ZS           84.00               25            1.99              1.76        125.65               152.21         0.824          pass              0.403             37.9                           0.301              -18.72             -1.225 downtrend_blocked_slope           False                  False
  MELI           94.87               39            0.45              5.29       1693.90                61.41         0.610          pass              0.801             50.2                           0.365                8.11              0.857                      ok           False                  False
  CSCO           94.87               39            0.01              0.01        119.67                51.65         0.598          pass              0.944             98.2                           0.630               17.46              0.907                      ok           False                  False
  ROST           83.33                6            2.39              3.91        231.79                38.54         0.583          pass              0.147              0.0                           0.163                7.61              1.143                      ok           False                  False
  ASML           94.29               35            0.49              5.51       1595.51                53.18         0.578          pass              0.773             56.0                           0.323                0.53              0.549                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-28T00:00:03.757313-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528094506)

</details>

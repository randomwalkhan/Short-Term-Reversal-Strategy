# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 09:55:06 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,075.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-510.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   1      2     12010.0                 11500.0        60.05           57.5       531.8        497.23     last_price_stale                        NaN                unavailable                   False          -510.0                  -4.25         97.22               36              0.52         54.56            0.39                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           84.38               32            1.49              9.66        924.27               100.84         0.639          pass              0.542             71.5                           0.395               13.81              2.074                      ok            True                  False
  CSCO           92.31               26            0.76              0.64        119.40                51.65         0.631          pass              0.506              2.7                           0.150               16.58              0.873                      ok            True                  False
  SOXL           90.91               22            3.45              5.26        215.72               139.87         0.593          pass              0.645             71.5                           0.383               14.23              2.607                      ok            True                  False
  ASML           93.94               33            0.87              9.72       1593.71                53.18         0.566          pass              0.649             22.3                           0.172                0.15              0.531                      ok            True                  False
  INTC           95.24               21            3.17              2.70        120.61                92.16         0.554          pass              0.618             29.9                           0.259               -1.97              0.682                      ok            True                  False
  MNST           90.00               30            0.74              0.46         89.04                49.17         0.533          pass              0.593             46.5                           0.368                3.08              0.254                      ok            True                  False
  AMAT           80.95               21            2.03              6.38        445.51                50.47         0.528          pass              0.178              8.8                           0.093                0.70              0.342                      ok            True                  False
   TXN           95.83               24            0.94              2.09        316.55                35.35         0.512          pass              0.684             46.6                           0.278                2.65              0.459                      ok            True                  False
    ZS           82.35               17            2.59              2.30        125.43               152.21         0.832          pass              0.250             19.2                           0.154              -19.22             -1.253 downtrend_blocked_slope           False                  False
  MELI           93.18               44            0.07              0.88       1695.79                61.41         0.600          pass              0.887             91.7                           0.619                8.51              0.874                      ok           False                  False
  FTNT          100.00               48            0.09              0.08        127.90                70.83         0.597          pass              0.879             73.3                           0.346                8.60              0.906                      ok           False                  False
  ROST           85.71                7            2.24              3.67        231.90                38.54         0.586          pass              0.257             15.2                           0.138                7.78              1.150                      ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528095506)

</details>

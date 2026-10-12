# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:25:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$58,874.30`
- Equity: `$122,874.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$5,600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 64000.0         3.65            4.0       59.31         59.63          bid_ask_mid                        4.0                bid_ask_mid                    True          5600.0                   9.59          93.1               29              1.17         50.42           52.93                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           83.33               30            0.88              3.14        508.64                55.08         0.593            pass              0.366             28.2                           0.313               21.05              2.057                                 ok            True                  False
    ZS           90.91               33            1.54              2.52        232.65                75.53         0.523            pass              0.604             35.8                           0.280               15.42              1.676                                 ok            True                  False
  ABNB           87.50               32            0.94              1.09        165.40                38.25         0.505            pass              0.535             45.8                           0.413                5.28              0.468                                 ok            True                  False
  QCOM           86.96               23            1.55              1.90        174.68                55.68         0.589            pass              0.387             18.6                           0.232               -7.84             -0.736 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               24            3.01             16.51        775.92                69.65         0.530            pass              0.255              6.5                           0.199              -17.59             -2.250            downtrend_blocked_slope           False                  False
 CMCSA           88.24               17            0.44              0.06         20.63                20.79         0.528            pass              0.450             43.7                           0.382               -4.13             -0.362            downtrend_blocked_slope           False                  False
   WDC           75.86               29            2.23              6.21        394.62                64.73         0.514            pass              0.233             18.2                           0.372              -14.30             -1.826            downtrend_blocked_slope           False                  False
   CEG           87.80               41            0.24              0.50        297.85                62.49         0.510            pass              0.697             79.4                           0.477               14.18              1.756                                 ok           False                  False
  PAYX           81.82               44            0.08              0.06        103.96                39.82         0.504            pass              0.499             66.7                           0.356                4.63              0.565                                 ok           False                  False
  INTC           77.78               18            3.51              2.57        103.60                69.66         0.503            pass              0.118              4.7                           0.199              -12.93             -1.477 downtrend_blocked_slope_and_streak           False                  False
  DASH           76.92               13            2.75              3.79        194.88                43.05         0.502            pass              0.145             24.9                           0.409                7.12              0.719                                 ok           False                  False
  CSCO           33.33                3            2.68              2.22        117.44                33.46         0.495 below_threshold              0.077              9.0                           0.159                8.36              1.129                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:25:04.307064-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:20:06.400928-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012102504)

</details>

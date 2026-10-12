# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:20:06 EDT`
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
- Equity: `$120,474.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$3,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 61600.0         3.65           3.85       59.31         59.81          bid_ask_mid                       3.85                bid_ask_mid                    True          3200.0                   5.48          93.1               29              1.17         50.42           52.54                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           83.33               36            0.61              2.19        509.05                55.08         0.573            pass              0.469             49.9                           0.519               21.37              2.069                                 ok            True                  False
    ZS           91.67               36            1.40              2.30        232.75                75.53         0.513            pass              0.660             41.5                           0.298               15.58              1.683                                 ok            True                  False
  ABNB           88.24               34            0.84              0.97        165.45                38.25         0.500 below_threshold              0.584             51.6                           0.503                5.38              0.473                                 ok            True                  False
  QCOM           86.96               23            1.42              1.74        174.75                55.68         0.596            pass              0.408             25.4                           0.274               -7.72             -0.730 downtrend_blocked_slope_and_streak           False                  False
   STX           85.19               27            2.46             13.50        777.21                69.65         0.545            pass              0.377             23.5                           0.426              -17.12             -2.224            downtrend_blocked_slope           False                  False
   WDC           76.67               30            1.72              4.78        395.23                64.73         0.538            pass              0.298             37.0                           0.619              -13.85             -1.802            downtrend_blocked_slope           False                  False
 CMCSA           88.24               17            0.36              0.05         20.64                20.79         0.533            pass              0.479             53.1                           0.434               -4.06             -0.359            downtrend_blocked_slope           False                  False
  INTC           81.82               22            2.90              2.13        103.79                69.66         0.519            pass              0.218             12.6                           0.203              -12.38             -1.448 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               40            0.29              0.59        297.82                62.49         0.513            pass              0.678             75.7                           0.490               14.13              1.754                                 ok           False                  False
  CSCO           50.00                4            2.61              2.16        117.46                33.46         0.510            pass              0.085             11.3                           0.185                8.44              1.132                                 ok           False                  False
  DASH           76.92               13            2.66              3.65        194.93                43.05         0.508            pass              0.153             27.5                           0.346                7.23              0.724                                 ok           False                  False
  PAYX           81.82               44            0.12              0.08        103.94                39.82         0.502            pass              0.449             50.0                           0.260                4.59              0.563                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:20:06.400928-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012102006)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:10:05 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$123,674.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$6,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 64800.0         3.65           4.05       59.31         60.17          bid_ask_mid                       4.05                bid_ask_mid                    True          6400.0                  10.96          93.1               29              1.17         50.42           50.81                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           82.14               28            1.01              3.62        508.44                55.08         0.596            pass              0.288             17.2                           0.225               20.88              2.051                                 ok            True                  False
    ZS           93.10               29            1.85              3.03        232.43                75.53         0.537            pass              0.536              1.9                           0.169               15.05              1.662                                 ok            True                  False
  ABNB           86.21               29            1.06              1.23        165.34                38.25         0.514            pass              0.460             38.7                           0.283                5.14              0.463                                 ok            True                  False
  QCOM           86.96               23            1.72              2.11        174.59                55.68         0.580            pass              0.342              3.8                           0.103               -8.00             -0.744 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               24            2.84             15.56        776.33                69.65         0.540            pass              0.272             11.9                           0.222              -17.44             -2.241            downtrend_blocked_slope           False                  False
   WDC           75.86               29            1.92              5.33        395.00                64.73         0.532            pass              0.269             29.8                           0.543              -14.02             -1.811            downtrend_blocked_slope           False                  False
 CMCSA           91.30               23            0.00              0.00         20.66                20.79         0.522            pass              0.740            100.0                           0.620               -3.71             -0.343            downtrend_blocked_slope           False                  False
   CEG           86.84               38            0.36              0.76        297.74                62.49         0.520            pass              0.628             69.0                           0.472               14.04              1.750                                 ok           False                  False
  INTC           80.00               20            3.18              2.33        103.70                69.66         0.514            pass              0.131              4.3                           0.171              -12.63             -1.461 downtrend_blocked_slope_and_streak           False                  False
  DASH           72.73               11            2.80              3.85        194.85                43.05         0.508            pass              0.128             23.6                           0.246                7.07              0.717                                 ok           False                  False
  PAYX           81.82               44            0.09              0.06        103.95                39.82         0.503            pass              0.486             62.5                           0.307                4.62              0.564                                 ok           False                  False
  UPRO           86.49               37            0.23              0.25        155.61                29.53         0.492 below_threshold              0.475             24.2                           0.272                4.45              0.617                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:35:05.586025-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:30:06.510407-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012101005)

</details>

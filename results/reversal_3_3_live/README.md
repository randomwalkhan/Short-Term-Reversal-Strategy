# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:00:05 EDT`
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
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 64800.0         3.65           4.05       59.31         59.97          bid_ask_mid                       4.05                bid_ask_mid                    True          6400.0                  10.96          93.1               29              1.17         50.42            51.2                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           84.21               38            0.56              1.99        509.14                55.08         0.566            pass              0.519             54.4                           0.505               21.44              2.072                                 ok            True                  False
    ZS           91.89               37            0.81              1.32        233.16                75.53         0.554            pass              0.640             29.1                           0.189               16.28              1.710                                 ok            True                  False
  ABNB           88.24               34            0.81              0.94        165.47                38.25         0.508            pass              0.505             24.7                           0.192                5.41              0.474                                 ok            True                  False
  MPWR           85.00               20            2.20             21.34       1377.14                56.07         0.502            pass              0.352             33.9                           0.515                0.49              0.259                                 ok            True                  False
  QCOM           86.96               23            1.41              1.73        174.76                55.68         0.600            pass              0.359              8.9                           0.178               -7.71             -0.730 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               24            2.65             14.53        776.77                69.65         0.551            pass              0.287             16.4                           0.258              -17.28             -2.233            downtrend_blocked_slope           False                  False
  CSCO           60.00                5            2.41              1.99        117.54                33.46         0.531            pass              0.057              1.4                           0.156                8.66              1.141                                 ok           False                  False
 CMCSA           88.24               17            0.41              0.06         20.63                20.79         0.529            pass              0.460             46.9                           0.342               -4.11             -0.361            downtrend_blocked_slope           False                  False
  INTC           81.82               22            2.81              2.06        103.82                69.66         0.527            pass              0.195              4.5                           0.104              -12.30             -1.444 downtrend_blocked_slope_and_streak           False                  False
   WDC           75.86               29            2.23              6.19        394.63                64.73         0.514            pass              0.233             18.4                           0.396              -14.30             -1.826            downtrend_blocked_slope           False                  False
  DASH           77.78                9            3.39              4.67        194.50                43.05         0.493 below_threshold              0.049              0.0                           0.150                6.41              0.689                                 ok           False                  False
  NVDA           90.48               21            0.94              1.50        228.64                25.28         0.489 below_threshold              0.429              9.1                           0.207               -0.75              0.095                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:35:05.586025-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:30:06.510407-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:25:06.103095-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:20:06.276038-04:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012100005)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:05:03 EDT`
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
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 64800.0         3.65           4.05       59.31         60.12          bid_ask_mid                       4.05                bid_ask_mid                    True          6400.0                  10.96          93.1               29              1.17         50.42            50.2                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           83.33               36            0.68              2.42        508.95                55.08         0.570            pass              0.453             44.7                           0.376               21.29              2.066                                 ok            True                  False
    ZS           91.67               36            1.15              1.88        232.93                75.53         0.538            pass              0.585             15.7                           0.150               15.88              1.695                                 ok            True                  False
  ABNB           80.00               20            1.65              1.92        165.05                38.25         0.527            pass              0.132              4.4                           0.084                4.51              0.435                                 ok            True                  False
  QCOM           86.96               23            1.51              1.86        174.70                55.68         0.594            pass              0.348              5.3                           0.070               -7.81             -0.734 downtrend_blocked_slope_and_streak           False                  False
  CSCO           60.00                5            2.27              1.88        117.58                33.46         0.538            pass              0.081              9.0                           0.137                8.82              1.148                                 ok           False                  False
   STX           86.96               23            3.10             16.99        775.72                69.65         0.535            pass              0.332              2.2                           0.125              -17.67             -2.254            downtrend_blocked_slope           False                  False
 CMCSA           89.47               19            0.29              0.04         20.64                20.79         0.526            pass              0.553             62.5                           0.400               -3.99             -0.356            downtrend_blocked_slope           False                  False
  INTC           81.82               22            2.91              2.13        103.79                69.66         0.521            pass              0.189              2.9                           0.081              -12.39             -1.449 downtrend_blocked_slope_and_streak           False                  False
   WDC           75.86               29            2.18              6.07        394.68                64.73         0.517            pass              0.239             20.1                           0.436              -14.26             -1.823            downtrend_blocked_slope           False                  False
   CEG           87.80               41            0.22              0.47        297.87                62.49         0.511            pass              0.702             80.8                           0.540               14.20              1.757                                 ok           False                  False
  PAYX           81.82               44            0.16              0.12        103.93                39.82         0.499 below_threshold              0.392             31.2                           0.246                4.55              0.561                                 ok           False                  False
  UPRO           84.21               38            0.03              0.04        155.70                29.53         0.498 below_threshold              0.512             54.5                           0.308                4.65              0.626                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:35:05.586025-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:30:06.510407-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:25:06.103095-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012100503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012100503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012100503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012100503)

</details>

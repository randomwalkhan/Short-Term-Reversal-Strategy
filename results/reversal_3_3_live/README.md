# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 09:35:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$17,610.75`
- Equity: `$33,290.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-80.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15680.0         9.85            9.8       98.17         98.05     last_price_stale                        NaN                unavailable                   False           -80.0                  -0.51         95.65               23              3.29          79.1            1.56                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           81.25               16            1.99              1.20         85.53                69.04         0.642            pass              0.202             21.6                           0.249               -1.78              0.146                                 ok            True                  False
  TEAM           94.12               34            1.43              0.99         99.04                86.36         0.637            pass              0.773             57.6                           0.465               14.79              1.817                                 ok            True                  False
  PANW           86.96               23            1.62              3.09        270.73                60.15         0.581            pass              0.434             34.7                           0.276                5.82              1.190                                 ok            True                  False
  MSFT           85.19               27            0.87              2.54        415.58                34.82         0.559            pass              0.405             32.4                           0.326               -1.32              0.129                                 ok            True                  False
  ADBE           81.48               27            1.83              3.23        250.06                48.16         0.507            pass              0.333             43.2                           0.240                0.85              0.643                                 ok            True                  False
  DASH           88.89               27            1.91              2.09        155.90                51.66         0.505            pass              0.536             45.1                           0.344               -3.43             -0.104                                 ok            True                  False
   ADP           96.77               31            0.75              1.23        231.42                32.55         0.503            pass              0.769             59.4                           0.373                2.17              0.606                                 ok            True                  False
   ROP           91.67               36            0.62              1.45        331.56                35.97         0.503            pass              0.691             52.1                           0.295                0.97              0.444                                 ok            True                  False
  WDAY           87.10               31            1.47              1.48        143.64                69.97         0.500 below_threshold              0.476             32.2                           0.295               10.94              1.837                                 ok            True                  False
    ZS           81.82               33            1.06              0.97        130.36               157.69         0.898            pass              0.426             44.6                           0.326              -29.05             -2.405            downtrend_blocked_slope           False                  False
  INTU           81.25               32            1.07              2.22        295.81                99.91         0.743            pass              0.382             42.7                           0.383               -8.23             -0.507 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00                9            1.46              1.03        100.09                33.39         0.620            pass              0.538             25.3                           0.327                2.13              0.535                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-06-06T02:55:05.037778-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:50:04.162002-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:45:02.082249-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:40:02.201062-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:35:06.145778-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:30:02.216838-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:25:03.009223-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:20:05.037850-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:15:06.052679-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:10:01.102354-04:00 share_ext_0210 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608093501)

</details>

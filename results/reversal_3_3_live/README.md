# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 10:05:01 EST`
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

- Cash: `$58,976.55`
- Equity: `$124,826.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$7,650.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 65850.0         19.4          21.95      259.39        266.32          bid_ask_mid                      21.95                bid_ask_mid                    True          7650.0                  13.14          84.0               25              1.96         51.59           52.32                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           83.33               18            0.84              0.76        129.88                19.46         0.532            pass              0.212              5.6                           0.095                3.53              0.253                                 ok            True                  False
  GILD           91.67               24            0.98              1.17        170.18                29.81         0.515            pass              0.516             20.0                           0.203               10.42              1.012                                 ok            True                  False
  INTC           74.19               31            1.99              0.92         65.37               126.81         0.764            pass              0.326             36.4                           0.348              -29.97             -2.584            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.42              4.21        134.27                91.18         0.612            pass              0.083              7.1                           0.173              -24.16             -2.661 downtrend_blocked_slope_and_streak           False                  False
  ALNY           57.14                7            4.35              5.02        162.85               108.44         0.602            pass              0.091             10.4                           0.110              -32.35             -3.646            downtrend_blocked_slope           False                  False
  CTSH           91.43               35            0.60              0.27         64.99                51.72         0.557            pass              0.688             53.5                           0.523               -3.10             -0.850            downtrend_blocked_slope           False                  False
  TEAM          100.00               19            2.25              3.01        190.43                55.13         0.539            pass              0.531              5.8                           0.176              -12.73             -1.468            downtrend_blocked_slope           False                  False
    MU           76.47               34            0.93              5.76        882.27                60.34         0.537            pass              0.337             41.1                           0.293               -3.14              0.172                                 ok           False                  False
  CSCO           77.27               22            1.01              0.74        104.19                35.63         0.525            pass              0.229             32.2                           0.252               -2.86             -0.042           downtrend_blocked_streak           False                  False
   XEL           76.92               13            1.12              0.62         79.55                18.77         0.517            pass              0.269             65.6                           0.718                5.04              0.410                                 ok           False                  False
   KDP           96.77               31            0.13              0.03         35.83                21.81         0.512            pass              0.858             89.0                           0.731                3.87              0.354                                 ok           False                  False
  INSM           80.00               40            1.03              0.81        112.23                62.44         0.497 below_threshold              0.339             29.7                           0.219               16.93              1.821                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-02T10:05:01.515738-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:00:05.841210-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T03:00:04.577568-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-31T02:55:06.398168-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:50:05.964599-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:45:05.451859-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:40:06.038699-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:35:06.236503-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:30:05.652864-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:25:01.174270-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102100501)

</details>

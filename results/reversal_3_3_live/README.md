# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 10:15:01 EST`
Last processed slot: `early_entry_1015`

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
- Equity: `$126,176.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$9,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 67200.0         19.4           22.4      259.39        266.64          bid_ask_mid                       22.4                bid_ask_mid                    True          9000.0                  15.46          84.0               25              1.96         51.59           51.02                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           80.00               15            0.98              0.89        129.83                19.46         0.537            pass              0.134             15.6                           0.198                3.38              0.247                                 ok            True                  False
   XEL           83.33               18            0.79              0.44         79.63                18.77         0.510            pass              0.420             75.7                           0.786                5.39              0.425                                 ok            True                  False
  INTC           71.43               28            2.35              1.08         65.30               126.81         0.759            pass              0.271             25.0                           0.250              -30.22             -2.601            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.30              4.10        134.32                91.18         0.619            pass              0.091              9.7                           0.126              -24.06             -2.655 downtrend_blocked_slope_and_streak           False                  False
  ALNY           57.14                7            4.34              5.02        162.85               108.44         0.602            pass              0.092             10.4                           0.104              -32.34             -3.646            downtrend_blocked_slope           False                  False
  GILD           87.50                8            1.92              2.29        169.70                29.81         0.551            pass              0.257              0.6                           0.059                9.37              0.969                                 ok           False                  False
    MU           76.47               34            0.93              5.75        882.28                60.34         0.538            pass              0.337             41.2                           0.345               -3.14              0.172                                 ok           False                  False
  TEAM          100.00               19            2.23              3.00        190.44                55.13         0.537            pass              0.563             16.6                           0.138              -12.72             -1.467            downtrend_blocked_slope           False                  False
  CSCO           82.76               29            0.60              0.44        104.32                35.63         0.511            pass              0.430             59.6                           0.514               -2.46             -0.023           downtrend_blocked_streak           False                  False
   KDP           96.97               33            0.04              0.01         35.84                21.81         0.504            pass              0.893             96.3                           0.737                3.96              0.358                                 ok           False                  False
  INSM           65.22               23            2.39              1.88        111.77                62.44         0.496 below_threshold              0.173             12.4                           0.229               15.32              1.758                                 ok           False                  False
  AAPL           94.12               17            1.22              2.95        343.37                14.54         0.487 below_threshold              0.520             16.1                           0.237               -0.73              0.035                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-02T10:15:01.964431-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:10:04.210177-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:05:01.515738-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T10:00:05.841210-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T03:00:04.577568-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-31T02:55:06.398168-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:50:05.964599-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:45:05.451859-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:40:06.038699-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:35:06.236503-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102101501)

</details>

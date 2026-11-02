# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 09:50:04 EST`
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
- Equity: `$123,626.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$6,450.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 64650.0         19.4          21.55      259.39        264.24          bid_ask_mid                      21.55                bid_ask_mid                    True          6450.0                  11.08          84.0               25              1.96         51.59           50.74                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   BKR           86.67               15            1.85              0.71         54.92                45.39         0.575          pass              0.355             28.7                           0.209               -2.87             -0.149                                 ok            True                  False
   XEL           80.00               10            1.30              0.73         79.51                18.77         0.528          pass              0.232             59.8                           0.749                4.84              0.401                                 ok            True                  False
  INTC           74.19               31            2.10              0.97         65.35               126.81         0.759          pass              0.315             33.0                           0.258              -30.04             -2.589            downtrend_blocked_slope           False                  False
  ALNY           66.67               12            2.87              3.31        163.58               108.44         0.666          pass              0.203             40.9                           0.277              -31.30             -3.576            downtrend_blocked_slope           False                  False
  FTNT           66.67                6            3.78              3.61        134.53                91.18         0.634          pass              0.096             10.9                           0.128              -23.66             -2.631 downtrend_blocked_slope_and_streak           False                  False
  TMUS           88.10               42            0.04              0.05        156.42                67.84         0.609          pass              0.773             98.7                           0.938                0.18             -0.264                                 ok           False                  False
  CTSH           91.43               35            0.66              0.30         64.98                51.72         0.554          pass              0.673             48.8                           0.463               -3.16             -0.853            downtrend_blocked_slope           False                  False
  LRCX           69.77               43            0.08              0.14        239.05                61.33         0.549          pass              0.461             68.8                           0.282              -12.23             -0.794 downtrend_blocked_slope_and_streak           False                  False
    MU           75.76               33            1.02              6.30        882.04                60.34         0.541          pass              0.254             15.4                           0.097               -3.22              0.168                                 ok           False                  False
  CSCO           72.22               18            1.21              0.88        104.13                35.63         0.536          pass              0.107              0.0                           0.210               -3.05             -0.051           downtrend_blocked_streak           False                  False
  TEAM          100.00               28            1.56              2.09        190.82                55.13         0.525          pass              0.663             30.3                           0.282              -12.11             -1.436            downtrend_blocked_slope           False                  False
   KDP           96.97               33            0.03              0.01         35.84                21.81         0.505          pass              0.897             97.6                           0.672                3.98              0.358                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-11-02T03:00:04.577568-05:00   data_refresh  data_refresh                   {'saved': 91, 'empty': 2}
2026-10-31T02:55:06.398168-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:50:05.964599-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:45:05.451859-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:40:06.038699-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:35:06.236503-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:30:05.652864-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:25:01.174270-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:20:06.862130-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:15:06.209587-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102095004)

</details>

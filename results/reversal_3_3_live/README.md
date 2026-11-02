# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 09:35:05 EST`
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

- Cash: `$58,976.55`
- Equity: `$117,776.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 58800.0         19.4           19.6      259.39        264.39     last_price_stale                        NaN                unavailable                   False           600.0                   1.03          84.0               25              1.96         51.59             0.0                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TMUS           84.85               33            0.53              0.58        156.19                67.84         0.632          pass              0.598             84.2                           0.747               -0.31             -0.287                                 ok            True                  False
   XEL           80.00               15            0.98              0.55         79.58                18.77         0.515          pass              0.294             69.7                           0.908                5.18              0.416                                 ok            True                  False
    ZS           90.48               21            2.43              4.05        236.09                62.20         0.510          pass              0.481             25.7                           0.351                9.18              1.113                                 ok            True                  False
  INTC           68.18               22            2.95              1.36         65.18               126.81         0.758          pass              0.163              2.5                           0.103              -30.65             -2.629            downtrend_blocked_slope           False                  False
  ALNY           72.73               11            2.96              3.42        163.54               108.44         0.672          pass              0.191             39.0                           0.312              -31.36             -3.580            downtrend_blocked_slope           False                  False
  FTNT           66.67                9            3.20              3.05        134.77                91.18         0.658          pass              0.066              0.0                           0.230              -23.20             -2.604 downtrend_blocked_slope_and_streak           False                  False
  CTSH           90.91               33            1.01              0.46         64.91                51.72         0.547          pass              0.563             21.4                           0.175               -3.50             -0.869            downtrend_blocked_slope           False                  False
    MU           81.40               43            0.23              1.45        884.12                60.34         0.537          pass              0.495             67.9                           0.317               -2.46              0.204                                 ok           False                  False
   KDP           96.15               26            0.42              0.11         35.79                21.81         0.531          pass              0.655             31.8                           0.364                3.57              0.340                                 ok           False                  False
  TEAM          100.00               39            0.55              0.74        191.40                55.13         0.530          pass              0.762             38.7                           0.325              -11.22             -1.390            downtrend_blocked_slope           False                  False
  AVGO           78.05               41            0.08              0.18        326.00                45.61         0.524          pass              0.499             82.1                           0.532               -2.62              0.056                                 ok           False                  False
   WDC           75.00               36            1.53              3.92        364.43                75.11         0.523          pass              0.269             14.6                           0.194                2.36              0.541                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102093505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102093505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102093505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102093505)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 09:45:06 EST`
Last processed slot: `manual`

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
- Equity: `$121,076.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$3,900.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 62100.0         19.4           20.7      259.39        265.17          bid_ask_mid                       20.7                bid_ask_mid                    True          3900.0                    6.7          84.0               25              1.96         51.59           52.75                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   BKR           92.31               26            1.30              0.50         55.01                45.39         0.544          pass              0.638             49.7                           0.421               -2.33             -0.124                                 ok            True                  False
    ZS           85.71               14            3.19              5.31        235.56                62.20         0.505          pass              0.238              2.7                           0.113                8.34              1.078                                 ok            True                  False
  AAPL           94.12               17            1.02              2.47        343.57                14.54         0.500          pass              0.527             17.8                           0.186               -0.54              0.044                                 ok            True                  False
  INTC           74.19               31            2.10              0.97         65.35               126.81         0.759          pass              0.315             33.0                           0.256              -30.04             -2.589            downtrend_blocked_slope           False                  False
  ALNY           80.77               26            1.72              1.99        164.15               108.44         0.664          pass              0.387             64.5                           0.511              -30.49             -3.523            downtrend_blocked_slope           False                  False
  FTNT           66.67                9            3.20              3.05        134.77                91.18         0.656          pass              0.090              8.2                           0.089              -23.20             -2.604 downtrend_blocked_slope_and_streak           False                  False
  TMUS           87.18               39            0.27              0.29        156.31                67.84         0.614          pass              0.722             92.0                           0.884               -0.04             -0.275                                 ok           False                  False
  CTSH           91.18               34            0.78              0.35         64.96                51.72         0.553          pass              0.633             39.9                           0.383               -3.27             -0.858            downtrend_blocked_slope           False                  False
  TEAM          100.00               28            1.52              2.04        190.84                55.13         0.534          pass              0.573              0.0                           0.197              -12.08             -1.434            downtrend_blocked_slope           False                  False
    MU           78.95               38            0.73              4.52        882.80                60.34         0.531          pass              0.358             39.4                           0.208               -2.94              0.181                                 ok           False                  False
   XEL           75.00                8            1.42              0.79         79.48                18.77         0.530          pass              0.222             56.4                           0.674                4.72              0.396                                 ok           False                  False
  CSCO           83.33               30            0.52              0.38        104.35                35.63         0.514          pass              0.440             55.3                           0.372               -2.38             -0.019           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102094506)

</details>

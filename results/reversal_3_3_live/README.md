# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 09:40:02 EST`
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
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 58800.0         19.4           19.6      259.39        264.49     last_price_stale                        NaN                unavailable                   False           600.0                   1.03          84.0               25              1.96         51.59             0.0                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   BKR           86.67               15            1.83              0.71         54.93                45.39         0.576          pass              0.357             29.4                           0.218               -2.85             -0.148                                 ok            True                  False
   KDP           93.75               16            1.03              0.26         35.73                21.81         0.552          pass              0.462              0.0                           0.250                2.93              0.312                                 ok            True                  False
   XEL           81.82               11            1.20              0.67         79.53                18.77         0.529          pass              0.297             62.9                           0.867                4.95              0.406                                 ok            True                  False
    MU           80.00               40            0.65              4.02        883.02                60.34         0.525          pass              0.391             46.1                           0.240               -2.86              0.185                                 ok            True                  False
    ZS           88.24               17            2.67              4.44        235.93                62.20         0.519          pass              0.374             18.6                           0.241                8.92              1.102                                 ok            True                  False
  INTC           75.76               33            1.77              0.82         65.41               126.81         0.766          pass              0.360             43.4                           0.349              -29.81             -2.574            downtrend_blocked_slope           False                  False
  FTNT           81.25               16            2.45              2.34        135.08                91.18         0.671          pass              0.229             29.7                           0.294              -22.60             -2.568 downtrend_blocked_slope_and_streak           False                  False
  ALNY           80.77               26            1.81              2.09        164.10               108.44         0.660          pass              0.381             62.7                           0.486              -30.55             -3.527            downtrend_blocked_slope           False                  False
  TMUS           87.80               41            0.09              0.10        156.40                67.84         0.613          pass              0.761             97.2                           0.888                0.13             -0.267                                 ok           False                  False
  CTSH           92.86               42            0.08              0.04         65.09                51.72         0.546          pass              0.880             94.0                           0.835               -2.59             -0.826            downtrend_blocked_slope           False                  False
  TEAM          100.00               37            0.71              0.95        191.31                55.13         0.530          pass              0.756             41.1                           0.343              -11.36             -1.397            downtrend_blocked_slope           False                  False
  AVGO           77.50               40            0.20              0.45        325.89                45.61         0.521          pass              0.442             63.3                           0.431               -2.74              0.051                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102094002)

</details>

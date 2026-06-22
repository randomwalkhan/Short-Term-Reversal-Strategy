# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-22 13:05:02 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$13,462.50`
- Equity: `$27,684.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$1,170.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   1     52     13052.0                 14222.0         2.51           2.74      117.33        117.47          bid_ask_mid                       2.74                bid_ask_mid                    True          1170.0                   8.96         86.21               29              0.68         25.57            28.8                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               22            2.28              4.96        308.45               150.94         0.822          pass              0.691             42.8                           0.575               15.19              1.394                      ok            True                  False
  UPRO           92.31               26            0.89              0.89        142.43                49.73         0.609          pass              0.605             36.3                           0.357                2.92              0.509                      ok            True                  False
  CDNS           89.47               19            2.04              5.53        385.02                57.09         0.594          pass              0.414             14.0                           0.360                0.88              0.005                      ok            True                  False
  MPWR           90.91               22            2.39             26.12       1552.51                82.20         0.589          pass              0.535             34.9                           0.434                3.06              0.061                      ok            True                  False
  PAYX          100.00               22            0.78              0.54         98.01                31.80         0.571          pass              0.730             64.4                           0.589               -3.04             -0.240                      ok            True                  False
  ASML           93.10               29            1.55             20.90       1920.72                57.74         0.565          pass              0.622             29.7                           0.466               15.72              1.224                      ok            True                  False
   WDC           91.30               23            2.38             12.42        740.91                88.76         0.548          pass              0.449              2.1                           0.156               42.36              4.530                      ok            True                  False
  NVDA           81.82               33            0.68              1.00        210.26                45.37         0.548          pass              0.381             41.3                           0.325                2.03              0.176                      ok            True                  False
  PANW           92.31               39            0.87              1.75        287.03                57.46         0.519          pass              0.713             46.5                           0.404                4.86              0.843                      ok            True                  False
    ZS           75.00               28            2.01              1.76        124.10               152.43         0.856          pass              0.265             19.8                           0.442               -6.45             -0.394 downtrend_blocked_slope           False                  False
   PEP          100.00               20            0.22              0.22        141.93                22.29         0.621          pass              0.708             59.7                           0.362               -0.15              0.043                      ok           False                  False
   KHC          100.00                1            2.26              0.36         22.67                27.88         0.619          pass              0.468              1.9                           0.143               -1.22             -0.194                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-06-22T03:00:02.560041-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-06-20T02:55:02.206016-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:50:04.120512-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:45:02.079519-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:40:02.993800-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:35:04.122508-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:30:05.305021-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T01:05:03.587151-04:00 share_ext_0105 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T01:00:02.570714-04:00 share_ext_0100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T00:55:02.530724-04:00 share_ext_0055 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260622130502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260622130502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260622130502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260622130502)

</details>

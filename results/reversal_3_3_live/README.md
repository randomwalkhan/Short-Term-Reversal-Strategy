# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 09:31:23 EDT`
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
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 15680.0         9.85            9.8       98.17         98.86     last_price_stale                        NaN                unavailable                   False           -80.0                  -0.51         95.65               23              3.29          79.1            1.56                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           80.00               20            0.91              0.55         85.80                69.04         0.694          pass              0.245             36.2                           0.405               -0.70              0.196                                 ok            True                  False
  TEAM           95.24               42            0.61              0.43         99.29                86.36         0.648          pass              0.895             76.7                           0.517               15.73              1.854                                 ok            True                  False
  PAYX          100.00               18            0.77              0.54        100.30                33.39         0.613          pass              0.651             45.4                           0.518                2.85              0.567                                 ok            True                  False
  PANW           86.36               22            1.77              3.38        270.60                60.15         0.586          pass              0.309              0.4                           0.191                5.66              1.183                                 ok            True                  False
  INTU           80.95               42            0.21              0.43        296.58                99.91         0.746          pass              0.533             77.6                           0.487               -7.44             -0.467 downtrend_blocked_slope_and_streak           False                  False
   CEG           82.86               35            0.53              0.94        254.43                55.63         0.587          pass              0.302              0.0                           0.257              -11.31             -1.484            downtrend_blocked_slope           False                  False
  INSM           72.97               37            1.08              0.71         93.91                54.02         0.568          pass              0.335             32.7                           0.431              -12.27             -0.916            downtrend_blocked_slope           False                  False
   EXC           75.00               12            0.66              0.21         45.66                19.68         0.565          pass              0.227             52.4                           0.449               -0.76             -0.183                                 ok           False                  False
  META           77.78               18            1.60              6.66        590.15                30.98         0.549          pass              0.120              3.9                           0.242               -3.93             -0.195                                 ok           False                  False
  MSFT           88.57               35            0.37              1.08        416.21                34.82         0.545          pass              0.636             62.2                           0.418               -0.82              0.152                                 ok           False                  False
  COST           72.00               25            0.70              4.73        969.84                28.11         0.532          pass              0.282             43.0                           0.450               -6.14             -0.491            downtrend_blocked_slope           False                  False
   AEP           78.57               28            0.19              0.17        129.07                24.28         0.525          pass              0.440             89.3                           0.641               -2.04             -0.210           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608093123)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608093123)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608093123)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608093123)

</details>

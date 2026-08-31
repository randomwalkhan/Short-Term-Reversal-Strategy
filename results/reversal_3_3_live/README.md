# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 09:35:06 EDT`
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

- Cash: `$26,688.10`
- Equity: `$52,585.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$-203.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SHOP     option         option SHOP261016C00155000       2026-08-28                   1     29     26100.0                 25897.0          9.0           8.93      153.02         148.5     last_price_stale                        NaN                unavailable                   False          -203.0                  -0.78         94.59               37              0.85         45.17            3.13                  69.26                 763.0          153.0               0.07                      ok
```

## Today's Closed Trades (2026-08-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           81.82               11            1.56              0.51         46.64               551.82         1.000          pass              0.183              9.3                           0.266                1.34              0.008                  ok            True                  False
  ABNB           93.55               31            0.63              0.83        189.07                62.79         0.664          pass              0.643             25.2                           0.196                4.99              0.358                  ok            True                  False
  AMGN          100.00               11            1.31              3.96        430.72                27.94         0.602          pass              0.503             12.0                           0.169                2.36              0.214                  ok            True                  False
   TRI           94.12               34            0.63              0.47        106.03                60.45         0.594          pass              0.857             86.9                           0.941                7.26              0.455                  ok            True                   True
  SHOP           88.89               18            2.88              3.08        151.58                66.63         0.589          pass              0.407             19.3                           0.169               -0.10              0.355                  ok            True                  False
  MSTR           84.62               39            0.61              0.55        127.08                81.68         0.589          pass              0.375              0.0                           0.237               29.54              3.313                  ok            True                  False
  MELI          100.00               30            1.17             16.16       1959.33                48.83         0.575          pass              0.683             30.5                           0.278                8.70              0.836                  ok            True                  False
  VRTX           94.74               19            1.53              5.80        539.21                33.03         0.566          pass              0.510              0.0                           0.202                3.46              0.256                  ok            True                  False
  WDAY           80.56               36            0.99              1.42        204.11                72.83         0.563          pass              0.445             66.9                           0.608                6.02              0.370                  ok            True                  False
  PAYX          100.00               28            0.52              0.46        126.84                24.67         0.541          pass              0.683             36.4                           0.340                6.62              0.621                  ok            True                  False
   MAR           93.33               15            1.44              3.54        349.56                33.77         0.535          pass              0.475             10.9                           0.194               -2.76             -0.211                  ok            True                  False
 CMCSA           90.00               20            1.07              0.20         26.97                25.33         0.530          pass              0.423             12.1                           0.154                4.69              0.369                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-31T03:00:02.021557-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-29T02:55:05.202083-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:30:05.313779-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:25:01.129841-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:20:04.124730-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:15:04.187905-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831093506)

</details>

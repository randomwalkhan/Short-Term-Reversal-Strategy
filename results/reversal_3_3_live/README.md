# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 09:30:05 EDT`
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
  SHOP     option         option SHOP261016C00155000       2026-08-28                   1     29     26100.0                 25897.0          9.0           8.93      153.02        150.66     last_price_stale                        NaN                unavailable                   False          -203.0                  -0.78         94.59               37              0.85         45.17            3.13                  69.26                 763.0          153.0               0.07                      ok
```

## Today's Closed Trades (2026-08-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   TRI           93.33               30            0.98              0.73        105.91                60.45         0.595          pass              0.787             79.5                           0.808                6.87              0.439                  ok            True                   True
  SHOP           93.75               32            1.47              1.57        152.23                66.63         0.594          pass              0.749             58.9                           0.353                1.35              0.421                  ok            True                  False
  AMGN          100.00               15            1.05              3.20        435.62                27.94         0.587          pass              0.573             27.1                           0.435                3.71              0.274                  ok            True                  False
  WDAY           80.56               36            0.65              0.94        204.32                72.83         0.584          pass              0.481             78.1                           0.651                6.38              0.385                  ok            True                  False
  PAYX          100.00               22            0.72              0.64        126.76                24.67         0.566          pass              0.569             10.7                           0.130                6.39              0.611                  ok            True                  False
  VRTX           96.55               29            1.07              4.05        539.95                33.03         0.537          pass              0.621             13.5                           0.257                3.95              0.277                  ok            True                  False
  TMUS           96.15               26            0.61              0.77        181.04                26.61         0.530          pass              0.758             66.1                           0.565                0.66             -0.070                  ok            True                  False
   MAR           95.00               20            1.16              2.86        349.86                33.77         0.528          pass              0.520              0.0                           0.167               -2.49             -0.198                  ok            True                  False
 CMCSA           92.00               25            0.81              0.15         26.99                25.33         0.520          pass              0.485              4.3                           0.238                4.97              0.381                  ok            True                  False
  SNPS           83.87               31            1.19              3.70        441.03                54.17         0.517          pass              0.359             21.3                           0.332                5.83              1.067                  ok            True                  False
  BKNG           96.97               33            0.89              1.28        205.08                35.32         0.513          pass              0.739             44.9                           0.383               -0.47             -0.195                  ok            True                  False
  INTU           91.43               35            0.58              1.44        357.44                43.37         0.509          pass              0.705             60.9                           0.606                6.08              0.130                  ok            True                   True
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831093005)

</details>

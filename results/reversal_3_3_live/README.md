# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 09:35:06 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$2,402.75`
- Equity: `$28,552.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$235.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14250.0         3.62           3.75      103.16        103.61     last_price_stale                        NaN                unavailable                   False           475.0                   3.45         94.74               19              0.93         28.13            0.78                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   2      4     12140.0                 11900.0        30.35          29.75      415.18        425.49     last_price_stale                        NaN                unavailable                   False          -240.0                  -1.98         91.67               36              0.62         50.17            0.00                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               25            1.52              1.42        133.32                66.43         0.638          pass              0.740             58.8                           0.413               14.26              1.609                       ok            True                  False
  TEAM           90.91               33            2.42              1.45         84.80               109.49         0.631          pass              0.626             39.5                           0.367               -4.54             -0.033                       ok            True                  False
  SHOP           83.33               42            0.52              0.37        102.84                78.13         0.601          pass              0.413             21.3                           0.366               -0.07              0.511                       ok            True                  False
  MELI           92.00               25            1.94             22.57       1654.75                60.80         0.577          pass              0.478              0.0                           0.197                4.81              0.677                       ok            True                  False
  ASML           87.88               33            0.81              9.31       1628.91                54.77         0.575          pass              0.482             20.4                           0.189                3.44              0.364                       ok            True                  False
  ROST           93.75               16            1.53              2.52        233.73                38.50         0.567          pass              0.463              0.0                           0.177                7.77              0.722                       ok            True                  False
   ADP           90.00               20            1.63              2.57        224.21                37.70         0.530          pass              0.461             24.8                           0.280                4.71              0.675                       ok            True                  False
   ROP           88.24               17            1.69              3.86        325.28                26.18         0.513          pass              0.356             12.7                           0.198               -2.24              0.049                       ok            True                  False
  INSM           75.61               41            0.63              0.47        106.04               110.00         0.748          pass              0.414             46.4                           0.412                1.62             -0.589                       ok           False                  False
  INTC           96.77               31            1.04              0.87        119.47                91.79         0.683          pass              0.758             50.0                           0.435               -8.38             -0.398 downtrend_blocked_streak           False                  False
  INTU           82.35               17            2.87              6.42        317.19                90.56         0.669          pass              0.213             12.2                           0.140              -20.98             -2.248  downtrend_blocked_slope           False                  False
  CSCO           83.33                6            1.97              1.66        119.70                52.25         0.659          pass              0.201             15.3                           0.231               19.57              1.879                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                     detail
2026-05-26T00:00:03.086607-04:00   data_refresh  data_refresh                                              {'saved': 92}
2026-05-25T23:55:01.101287-04:00 share_ext_2355 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:50:02.099383-04:00 share_ext_2350 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:45:01.097228-04:00 share_ext_2345 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:40:05.102217-04:00 share_ext_2340 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:35:01.093781-04:00 share_ext_2335 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:30:01.103317-04:00 share_ext_2330 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:25:02.099760-04:00 share_ext_2325 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:20:01.104241-04:00 share_ext_2320 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:15:05.147623-04:00 share_ext_2315 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526093506)

</details>

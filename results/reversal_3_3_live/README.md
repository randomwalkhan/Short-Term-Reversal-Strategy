# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 09:35:03 EDT`
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

- Cash: `$21,608.00`
- Equity: `$42,731.00`
- Realized PnL: `$31,228.00`
- Unrealized PnL: `$1,503.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260918C00140000       2026-08-14                   1      9     19620.0                 21123.0         21.8          23.47      141.95        151.41     last_price_stale                        NaN                unavailable                   False          1503.0                   7.66         82.86               35              2.35        114.04             0.0                 164.53                 831.0          148.0               0.04                      ok
```

## Today's Closed Trades (2026-08-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           84.85               33            1.07              1.71        227.92               127.87         0.833          pass              0.489             41.1                           0.423                2.67              0.330                  ok            True                  False
  TEAM           81.82               33            1.17              1.33        161.65               128.53         0.812          pass              0.446             54.4                           0.503               54.58              5.077                  ok            True                  False
  SHOP           97.06               34            0.95              1.03        153.88                83.98         0.692          pass              0.827             65.9                           0.730               30.63              2.331                  ok            True                   True
  ABNB           94.12               34            0.79              1.02        183.62                64.74         0.636          pass              0.686             28.8                           0.287               21.22              2.497                  ok            True                  False
 CMCSA           90.91               22            0.76              0.14         26.12                41.99         0.624          pass              0.540             35.5                           0.370                5.78              0.618                  ok            True                  False
  PAYX          100.00               15            1.29              1.11        121.55                35.05         0.590          pass              0.618             41.9                           0.305                2.35              0.380                  ok            True                  False
  GEHC           94.29               35            0.72              0.37         73.53                52.52         0.586          pass              0.766             53.1                           0.475                7.56              0.751                  ok            True                  False
   TRI           91.89               37            0.94              0.68        103.32                75.08         0.554          pass              0.764             70.6                           0.456                1.01              0.126                  ok            True                  False
  MDLZ           92.31               26            0.62              0.28         63.49                26.02         0.545          pass              0.639             50.0                           0.454                2.41              0.208                  ok            True                  False
   ROP          100.00               24            1.22              3.41        397.88                41.77         0.529          pass              0.660             37.9                           0.383                0.49              0.088                  ok            True                  False
  WDAY           85.19               27            2.45              3.41        197.22                90.03         0.527          pass              0.385             26.9                           0.385               17.42              1.851                  ok            True                  False
   XEL          100.00               25            0.73              0.41         79.00                16.04         0.519          pass              0.634             27.5                           0.212                1.16              0.214                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-17T03:00:01.859006-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-15T02:55:03.720107-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:40:01.513034-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:35:02.859847-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:30:02.424773-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:25:41.575248-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:15:46.829792-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:05:48.567191-04:00 share_ext_0205 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817093503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817093503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817093503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817093503)

</details>

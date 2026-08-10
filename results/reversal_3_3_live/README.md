# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 09:50:02 EDT`
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

- Cash: `$16,479.50`
- Equity: `$33,117.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$423.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 16638.0         1.72           1.77       58.88         58.81          bid_ask_mid                       1.77                bid_ask_mid                    True           423.0                   2.61         94.12               17              1.51         27.86           31.47                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.08               37            0.92              0.90        139.86               179.06         0.827          pass              0.504             70.8                           0.471                8.44              2.695                       ok            True                  False
  TMUS           89.47               19            1.60              1.98        176.34                55.81         0.649          pass              0.399              7.0                           0.099               -1.61             -0.178                       ok            True                  False
 CMCSA           92.31               13            1.64              0.29         25.24                44.15         0.633          pass              0.422              3.5                           0.097                9.41              0.759                       ok            True                  False
  FAST          100.00               20            0.67              0.24         51.74                28.62         0.592          pass              0.641             38.4                           0.388                8.69              0.981                       ok            True                  False
  BKNG           95.24               21            1.62              2.43        213.38                46.72         0.570          pass              0.534              1.3                           0.137               12.93              1.031                       ok            True                  False
  MCHP           84.85               33            1.42              0.84         84.33                76.06         0.563          pass              0.429             30.1                           0.275                7.17              0.975                       ok            True                  False
  ORLY           88.00               25            1.26              0.83         93.18                35.75         0.538          pass              0.367              0.0                           0.203                1.94              0.409                       ok            True                  False
  PCAR           96.88               32            0.52              0.48        132.90                29.28         0.522          pass              0.660             20.2                           0.211               -0.76             -0.192                       ok            True                  False
  CTSH           86.84               38            0.66              0.27         57.56                54.30         0.513          pass              0.623             67.5                           0.553               21.76              1.511                       ok            True                  False
   HON           86.96               23            1.05              1.81        245.43                29.28         0.504          pass              0.480             52.3                           0.341               -0.86              0.011                       ok            True                  False
  ALNY           88.37               43            0.43              0.66        218.91               128.37         0.802          pass              0.566             20.8                           0.248              -21.61             -2.622  downtrend_blocked_slope           False                  False
  DRAM           77.14               35            0.91              0.32         50.46               108.94         0.698          pass              0.440             67.8                           0.763               -4.37              0.506 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-10T03:00:02.466412-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-08T02:55:02.757209-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:50:05.752555-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:45:01.896094-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:40:05.765932-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:35:06.001208-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:30:03.730064-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:25:01.945300-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:20:01.711308-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T02:15:01.723035-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810095002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810095002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810095002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810095002)

</details>

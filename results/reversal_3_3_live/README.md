# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 09:35:03 EDT`
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

- Cash: `$16,479.50`
- Equity: `$33,587.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$893.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 17108.0         1.72           1.82       58.88         58.93     last_price_stale                        NaN                unavailable                   False           893.0                   5.51         94.12               17              1.51         27.86            1.56                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.33               36            1.11              1.16        148.57               133.30         0.797          pass              0.520             59.2                           0.361               53.76              3.900                  ok            True                  False
    MU           80.00               35            0.79              4.84        875.49               110.35         0.706          pass              0.447             70.0                           0.674               -3.28              0.685                  ok            True                  False
 CMCSA           87.50               16            1.18              0.21         25.27                44.15         0.637          pass              0.361             18.9                           0.198                9.91              0.780                  ok            True                  False
  TMUS           90.32               31            0.85              1.06        176.74                55.81         0.629          pass              0.509             10.1                           0.227               -0.86             -0.143                  ok            True                  False
  WDAY           83.33               36            0.62              0.78        179.31                69.52         0.610          pass              0.508             61.6                           0.514               21.00              1.529                  ok            True                  False
  SHOP           97.73               44            0.54              0.57        151.32                81.28         0.603          pass              0.925             88.4                           0.654               18.81              2.040                  ok            True                   True
   ROP          100.00               29            0.72              2.03        401.38                46.43         0.597          pass              0.721             44.8                           0.340                6.49              0.342                  ok            True                  False
  FAST          100.00               20            0.69              0.25         51.73                28.62         0.590          pass              0.626             33.3                           0.253                8.65              0.979                  ok            True                  False
   STX           90.32               31            0.98              5.55        810.38                91.44         0.583          pass              0.685             70.4                           0.620               -1.49              0.494                  ok            True                   True
  MDLZ           88.24               17            1.01              0.44         62.42                30.17         0.570          pass              0.398             25.0                           0.188                2.16             -0.008                  ok            True                  False
  BKNG           95.83               24            1.37              2.06        213.54                46.72         0.568          pass              0.592             14.0                           0.241               13.22              1.043                  ok            True                  False
  MCHP           84.85               33            1.59              0.95         84.28                76.06         0.552          pass              0.391             17.7                           0.271                6.98              0.967                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810093503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810093503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810093503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810093503)

</details>

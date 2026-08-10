# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 09:40:01 EDT`
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
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 17108.0         1.72           1.82       58.88          58.9     last_price_stale                        NaN                unavailable                   False           893.0                   5.51         94.12               17              1.51         27.86            1.56                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           84.62               39            0.85              0.88        148.69               133.30         0.797          pass              0.603             69.0                           0.406               54.18              3.912                  ok            True                  False
  SOXL           80.00               35            2.30              2.26        139.31               179.06         0.773          pass              0.268              8.1                           0.294                6.94              2.632                  ok            True                  False
    MU           81.25               32            1.85             11.35        872.71               110.35         0.659          pass              0.335             29.7                           0.378               -4.31              0.637                  ok            True                  False
 CMCSA           89.47               19            0.83              0.15         25.30                44.15         0.644          pass              0.507             43.2                           0.420               10.31              0.796                  ok            True                  False
  TMUS           90.62               32            0.83              1.03        176.75                55.81         0.623          pass              0.574             27.1                           0.253               -0.84             -0.142                  ok            True                  False
  FAST          100.00               22            0.64              0.23         51.74                28.62         0.580          pass              0.661             41.1                           0.427                8.72              0.982                  ok            True                  False
   STX           90.00               30            1.22              6.95        809.78                91.44         0.572          pass              0.646             62.9                           0.578               -1.73              0.483                  ok            True                  False
  MDLZ           88.24               17            1.13              0.50         62.40                30.17         0.558          pass              0.414             30.7                           0.257                2.03             -0.014                  ok            True                  False
  BKNG           97.06               34            0.73              1.09        213.95                46.72         0.546          pass              0.778             54.4                           0.396               13.96              1.073                  ok            True                  False
  MCHP           84.85               33            1.77              1.05         84.24                76.06         0.539          pass              0.370             11.2                           0.131                6.79              0.959                  ok            True                  False
   PEP           80.00               25            0.63              0.62        138.76                22.07         0.514          pass              0.266             38.2                           0.381               -1.18             -0.272                  ok            True                  False
  CTSH           86.84               38            0.76              0.31         57.54                54.30         0.506          pass              0.607             62.4                           0.529               21.64              1.506                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810094001)

</details>

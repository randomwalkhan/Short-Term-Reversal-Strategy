# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 09:55:01 EDT`
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
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 16638.0         1.72           1.77       58.88         58.83          bid_ask_mid                       1.77                bid_ask_mid                    True           423.0                   2.61         94.12               17              1.51         27.86           31.06                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  LRCX           87.50               32            0.91              1.98        310.50                90.05         0.671            pass              0.414              0.0                           0.177                5.80              1.435                      ok            True                  False
 CMCSA           92.31               13            1.46              0.26         25.25                44.15         0.643            pass              0.471             19.6                           0.184                9.61              0.767                      ok            True                  False
  TMUS           93.10               29            0.93              1.15        176.70                55.81         0.634            pass              0.678             46.2                           0.420               -0.94             -0.147                      ok            True                  False
  KLAC           83.78               37            0.56              0.78        197.78                68.97         0.575            pass              0.338              0.0                           0.177               -3.13              0.521                      ok            True                  False
  MDLZ           92.86               14            1.47              0.64         62.33                30.17         0.560            pass              0.504             26.0                           0.240                1.68             -0.030                      ok            True                  False
  BKNG           95.00               20            1.94              2.90        213.18                46.72         0.552            pass              0.522              0.0                           0.190               12.57              1.017                      ok            True                  False
  MCHP           86.21               29            2.09              1.24         84.16                76.06         0.545            pass              0.352              1.9                           0.108                6.44              0.944                      ok            True                  False
   PEP           80.00               25            0.74              0.72        138.71                22.07         0.506            pass              0.243             30.9                           0.373               -1.29             -0.277                      ok            True                  False
  ORLY           88.24               34            0.84              0.55         93.29                35.75         0.504            pass              0.535             35.0                           0.317                2.37              0.428                      ok            True                  False
   HON           87.50               24            0.98              1.69        245.48                29.28         0.503            pass              0.510             55.3                           0.341               -0.80              0.014                      ok            True                  False
  NVDA           83.78               37            0.73              1.14        223.47                42.49         0.500 below_threshold              0.350              6.3                           0.265               13.14              1.676                      ok            True                  False
  ALNY           88.64               44            0.20              0.31        219.07               128.37         0.808            pass              0.701             63.3                           0.335              -21.42             -2.611 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810095501)

</details>

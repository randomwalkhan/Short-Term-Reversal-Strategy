# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 09:45:01 EDT`
Last processed slot: `manual`

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
- Equity: `$31,707.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$-987.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   1     94     16215.0                 15228.0         1.72           1.62       58.88         58.75          bid_ask_mid                       1.62                bid_ask_mid                    True          -987.0                  -6.09         94.12               17              1.51         27.86           29.37                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               35            2.28              2.24        139.31               179.06         0.769          pass              0.328             28.0                           0.306                6.96              2.633                  ok            True                  False
    MU           80.00               35            0.82              5.04        875.41               110.35         0.704          pass              0.443             68.8                           0.689               -3.31              0.684                  ok            True                  False
  TMUS           90.00               20            1.43              1.77        176.43                55.81         0.657          pass              0.399              0.0                           0.150               -1.44             -0.170                  ok            True                  False
  PYPL           94.29               35            0.54              0.22         58.97                60.12         0.651          pass              0.800             62.4                           0.560                4.78              0.354                  ok            True                   True
 CMCSA           87.50               16            1.30              0.23         25.26                44.15         0.630          pass              0.335             10.8                           0.127                9.78              0.774                  ok            True                  False
   STX           90.32               31            0.77              4.37        810.89                91.44         0.598          pass              0.705             76.6                           0.639               -1.28              0.504                  ok            True                   True
  FAST          100.00               20            0.72              0.26         51.73                28.62         0.588          pass              0.625             33.0                           0.262                8.62              0.978                  ok            True                  False
  MDLZ           91.67               12            1.61              0.71         62.31                30.17         0.566          pass              0.385              1.5                           0.034                1.53             -0.036                  ok            True                  False
  BKNG           96.15               26            1.29              1.94        213.59                46.72         0.561          pass              0.620             19.2                           0.193               13.31              1.047                  ok            True                  False
  MCHP           83.87               31            1.95              1.16         84.19                76.06         0.538          pass              0.307              3.2                           0.080                6.59              0.951                  ok            True                  False
  MPWR           81.08               37            0.68              6.68       1398.68                61.17         0.509          pass              0.301             13.8                           0.164                3.95              0.711                  ok            True                  False
   PEP           80.00               25            0.76              0.74        138.70                22.07         0.506          pass              0.230             26.3                           0.189               -1.30             -0.278                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810094501)

</details>

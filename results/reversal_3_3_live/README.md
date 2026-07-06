# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 09:50:01 EDT`
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

- Cash: `$13,976.50`
- Equity: `$28,280.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$384.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   1     96     13920.0                 14304.0         1.45           1.49       33.12         32.69     last_price_stale                        NaN                unavailable                   False           384.0                   2.76         100.0               15              0.76         30.37            0.78                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   WBD           91.67               12            0.70              0.13         26.42                22.17         0.611          pass              0.401              5.1                           0.191                0.36             -0.086                  ok            True                  False
   EXC           81.25               16            0.61              0.20         47.79                22.14         0.583          pass              0.238             35.6                           0.261                3.89              0.299                  ok            True                  False
   XEL          100.00               20            0.58              0.33         81.82                20.81         0.569          pass              0.643             39.9                           0.303                5.26              0.330                  ok            True                  False
  GILD           92.86               14            1.34              1.23        130.74                30.05         0.558          pass              0.493             22.7                           0.234                4.65              0.444                  ok            True                  False
  CTAS           88.89               27            0.84              1.07        180.91                35.27         0.534          pass              0.529             41.6                           0.342                5.26              0.558                  ok            True                  False
  PYPL           81.25               16            1.52              0.48         45.26                34.53         0.525          pass              0.303             59.2                           0.639                5.34              0.718                  ok            True                  False
  MNST          100.00               22            0.77              0.53         97.37                16.38         0.523          pass              0.582             16.6                           0.228                6.03              0.590                  ok            True                  False
  FAST           94.44               18            1.23              0.42         48.42                20.75         0.518          pass              0.533             14.3                           0.222                4.60              0.598                  ok            True                  False
   ADP           92.31               26            0.86              1.46        241.65                30.79         0.516          pass              0.605             39.4                           0.306                9.97              1.124                  ok            True                  False
  BKNG           88.89               36            0.58              0.75        184.24                41.33         0.507          pass              0.621             53.3                           0.341                6.81              0.856                  ok            True                  False
  MDLZ          100.00                4            1.49              0.64         60.64                28.43         0.633          pass              0.490              9.0                           0.136                0.64             -0.030                  ok           False                  False
   KHC           85.71                7            1.63              0.29         25.25                36.79         0.616          pass              0.318             34.8                           0.297                9.36              1.293                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-07-06T03:00:03.074522-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-07-04T02:55:10.939731-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:50:08.940118-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:45:08.118438-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:40:02.422082-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:35:05.961779-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:30:09.469505-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:25:09.745804-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:20:09.451939-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:15:07.359670-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706095001)

</details>

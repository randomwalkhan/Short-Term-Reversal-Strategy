# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 09:45:05 EDT`
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

- Cash: `$41,269.30`
- Equity: `$79,609.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$-1,755.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   1     27     40095.0                 38340.0        14.85           14.2      196.86        202.04     last_price_stale                        NaN                unavailable                   False         -1755.0                  -4.38         94.59               37              0.97         55.98             0.0                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.87               31            2.34              2.68        162.52               114.85         0.703          pass              0.355             13.9                           0.377               12.69              0.941                      ok            True                  False
  AMGN           85.19               27            0.70              1.97        402.20                47.11         0.576          pass              0.469             53.2                           0.346                1.80              0.112                      ok            True                  False
  ASML           80.65               31            0.69              8.97       1863.46                42.39         0.551          pass              0.389             59.0                           0.650                8.37              0.841                      ok            True                  False
  AMAT           84.62               39            0.62              2.34        539.04                49.71         0.537          pass              0.471             33.7                           0.422               15.61              1.630                      ok            True                  False
  CSCO           86.67               30            0.51              0.40        112.03                31.23         0.533          pass              0.475             36.8                           0.401                0.54              0.302                      ok            True                  False
   ADI           88.00               25            1.07              3.11        415.82                32.86         0.524          pass              0.378              4.1                           0.200                7.75              0.791                      ok            True                  False
   XEL           85.00               20            0.64              0.32         71.26                18.48         0.512          pass              0.336             28.1                           0.229               -1.27             -0.060                      ok            True                  False
  MRVL           82.35               34            1.04              1.97        271.44                54.74         0.510          pass              0.346             24.1                           0.324                4.70              0.459                      ok            True                  False
    MU           89.66               29            1.37             10.33       1070.46                50.82         0.509          pass              0.456              7.1                           0.233                1.55              0.022                      ok            True                  False
  DRAM           80.56               36            0.19              0.08         61.70                54.09         0.581          pass              0.443             65.7                           0.541                0.06             -0.118                      ok           False                  False
  MPWR           92.50               40            0.13              1.32       1439.16                53.21         0.566          pass              0.861             90.4                           0.723               12.70              0.727                      ok           False                  False
  INTC           85.71               35            1.46              1.22        118.81                74.20         0.559          pass              0.583             69.5                           0.858               -3.44             -0.512 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-05T03:00:05.114767-04:00   data_refresh  data_refresh                   {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:25:01.959731-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:20:06.968956-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:15:04.972202-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005094505)

</details>

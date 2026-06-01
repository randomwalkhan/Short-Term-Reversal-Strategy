# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 09:45:06 EDT`
Last processed slot: `manual`

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

- Cash: `$18,164.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14100.0        35.25          35.25      477.34        476.56     last_price_stale                        NaN                unavailable                   False             0.0                    0.0         97.22               36              0.69         45.69             0.0                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.59               27            1.57              2.46        223.00               138.67         0.744          pass              0.713             63.2                           0.710               34.33              4.462                                 ok            True                  False
  CSCO           92.31               26            0.88              0.74        120.10                51.99         0.615          pass              0.646             50.0                           0.443                0.97              0.250                                 ok            True                  False
  LRCX           89.66               29            1.01              2.25        317.22                55.15         0.557          pass              0.654             71.3                           0.745               10.62              1.582                                 ok            True                  False
  CTSH           89.66               29            0.96              0.37         55.59                47.94         0.534          pass              0.522             28.2                           0.266               17.99              1.259                                 ok            True                  False
  INSM           71.43               35            1.10              0.83        106.56               110.85         0.752          pass              0.388             48.7                           0.424               -3.12             -0.159                                 ok           False                  False
  ROST           88.89                9            1.79              2.90        230.49                40.27         0.612          pass              0.363             21.6                           0.167                6.97              1.023                                 ok           False                  False
  ASML           94.87               39            0.11              1.23       1612.23                52.38         0.575          pass              0.929             93.9                           0.856                7.27              0.988                                 ok           False                  False
   AEP           72.73               11            1.07              0.95        126.26                24.34         0.570          pass              0.121             19.0                           0.180                0.13             -0.029                                 ok           False                  False
  AMGN           83.33                6            1.73              4.07        335.04                25.52         0.556          pass              0.232             29.3                           0.266                1.43              0.268                                 ok           False                  False
  AMAT           92.11               38            0.02              0.05        450.04                49.82         0.546          pass              0.862             99.4                           0.889                3.19              0.879                                 ok           False                  False
   HON           75.00                8            1.71              2.84        236.64                24.41         0.539          pass              0.110             18.8                           0.230                9.64              1.087                                 ok           False                  False
  COST           76.47               17            0.94              6.32        953.61                27.93         0.536          pass              0.175             24.9                           0.281               -9.69             -1.318 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-06-01T03:00:05.806892-04:00   data_refresh  data_refresh                               {'saved': 92}
2026-05-30T02:55:03.369308-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:50:06.334333-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:45:02.331534-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:40:01.232868-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:35:01.344797-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:30:06.367900-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:25:04.377495-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:20:05.639064-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-30T02:15:01.287104-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601094506)

</details>

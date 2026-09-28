# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 09:45:06 EDT`
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

- Cash: `$38,003.30`
- Equity: `$71,453.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$-2,100.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00160000       2026-09-25                   1     20     35550.0                 33450.0        17.77          16.73      158.68        159.29          bid_ask_mid                      16.73                bid_ask_mid                    True         -2100.0                  -5.91          93.1               29              1.81         73.26           70.51                 109.71                2435.0         2824.0               0.01                      ok
```

## Today's Closed Trades (2026-09-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               21            1.20              2.21        262.32                41.90         0.556          pass              0.408             42.1                           0.433               -1.68              0.030                                 ok            True                  False
  MPWR           85.71               28            1.17             11.18       1362.64                54.48         0.545          pass              0.536             69.5                           0.616               18.21              2.210                                 ok            True                  False
  SOXL           80.00               25            5.24              5.56        149.09               120.87         0.533          pass              0.259             35.3                           0.291               42.02              4.586                                 ok            True                  False
  PYPL           86.67               15            1.65              0.64         54.77                60.08         0.516          pass              0.433             56.7                           0.488                0.19              0.078                                 ok            True                  False
  UPRO           85.00               20            1.48              1.58        151.55                32.02         0.512          pass              0.304             17.6                           0.161                2.91              0.577                                 ok            True                  False
    MU           92.59               27            2.05             15.57       1075.61                50.18         0.502          pass              0.571             24.0                           0.223               14.72              1.841                                 ok            True                  False
  NXPI           87.10               31            0.91              1.52        237.43                39.27         0.500          pass              0.594             71.5                           0.526                5.68              0.683                                 ok            True                  False
   TRI           84.21               19            2.30              1.60         98.31                56.74         0.573          pass              0.245              5.0                           0.177               -8.61             -0.573 downtrend_blocked_slope_and_streak           False                  False
  LRCX           79.55               44            0.24              0.53        314.98                61.39         0.547          pass              0.537             94.0                           0.879               15.10              1.868                                 ok           False                  False
  AMAT           85.00               40            0.46              1.57        484.33                51.73         0.532          pass              0.646             86.6                           0.823               13.80              1.750                                 ok           False                  False
  MSFT          100.00                7            2.24              8.08        512.71                25.07         0.507          pass              0.503             17.3                           0.279               -0.15              0.190                                 ok           False                  False
  KLAC           76.32               38            0.69              0.91        187.53                50.67         0.506          pass              0.476             79.4                           0.690               10.37              1.409                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-09-28T03:00:06.642645-04:00   data_refresh  data_refresh                   {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:40:05.820539-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:35:05.219756-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:30:04.108962-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:25:06.088084-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:20:05.261496-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:15:05.559549-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928094506)

</details>

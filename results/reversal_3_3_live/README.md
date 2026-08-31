# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 09:45:05 EDT`
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

- Cash: `$26,688.10`
- Equity: `$49,960.60`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$-2,827.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SHOP     option         option SHOP261016C00155000       2026-08-28                   1     29     26100.0                 23272.5          9.0           8.02      153.02        146.43          bid_ask_mid                       8.02                bid_ask_mid                    True         -2827.5                 -10.83         94.59               37              0.85         45.17           55.48                  69.26                 763.0          153.0               0.07                      ok
```

## Today's Closed Trades (2026-08-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           86.67               15            1.26              0.41         46.68               551.82         1.000          pass              0.412             33.5                           0.287                1.65              0.022                  ok            True                  False
  ABNB           94.12               17            1.60              2.12        188.52                62.79         0.683          pass              0.498              2.3                           0.192                3.97              0.313                  ok            True                  False
  MELI          100.00               17            1.82             25.02       1955.53                48.83         0.614          pass              0.528              6.5                           0.147                8.00              0.806                  ok            True                  False
   TRI           92.86               28            1.21              0.90        105.84                60.45         0.593          pass              0.746             74.8                           0.626                6.63              0.429                  ok            True                  False
  MSTR           84.62               39            0.68              0.60        127.05                81.68         0.584          pass              0.375              0.0                           0.203               29.45              3.310                  ok            True                  False
  AMGN          100.00               21            0.66              1.99        431.57                27.94         0.579          pass              0.698             55.8                           0.508                3.03              0.244                  ok            True                  False
  PAYX          100.00               27            0.57              0.51        126.82                24.67         0.544          pass              0.657             29.6                           0.328                6.56              0.618                  ok            True                  False
  WDAY           80.77               26            2.28              3.27        203.32                72.83         0.544          pass              0.253             23.8                           0.256                4.64              0.310                  ok            True                  False
  SBUX           95.24               21            0.64              0.49        107.64                22.68         0.543          pass              0.635             35.6                           0.252               -0.71              0.155                  ok            True                  False
  VRTX           96.88               32            0.65              2.47        540.63                33.03         0.537          pass              0.788             62.7                           0.520                4.39              0.296                  ok            True                  False
 CMCSA           90.48               21            1.02              0.19         26.98                25.33         0.527          pass              0.455             16.7                           0.141                4.75              0.371                  ok            True                  False
   KDP           84.00               25            1.03              0.23         32.08                30.92         0.527          pass              0.324             21.4                           0.177                5.18              0.487                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-31T03:00:02.021557-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-29T02:55:05.202083-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:30:05.313779-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:25:01.129841-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:20:04.124730-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:15:04.187905-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831094505)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 09:35:10 EDT`
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

- Cash: `$62,756.80`
- Equity: `$121,206.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$-1,225.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-16                   1     35     59675.0                 58450.0        17.05           16.7      270.43        271.01     last_price_stale                        NaN                unavailable                   False         -1225.0                  -2.05         85.71               21              1.66         51.07             0.2                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   KDP           94.74               19            0.81              0.20         34.54                30.61         0.582          pass              0.684             57.6                           0.459               11.17              1.305                       ok            True                  False
  CTSH           94.44               36            0.76              0.35         65.88                41.45         0.510          pass              0.715             35.3                           0.507               12.64              1.554                       ok            True                  False
   KHC           86.36               22            1.06              0.17         23.61                22.28         0.507          pass              0.386             28.6                           0.351                7.28              0.763                       ok            True                  False
  INTU           87.88               33            0.52              1.18        324.65                39.88         0.501          pass              0.632             72.7                           0.518               14.16              1.371                       ok            True                  False
  TMUS           85.71               35            0.44              0.49        158.89                56.39         0.610          pass              0.549             56.2                           0.407               -3.79             -0.625  downtrend_blocked_slope           False                  False
 CMCSA           88.89                9            1.14              0.18         21.82                21.89         0.562          pass              0.373             26.5                           0.329                1.93              0.302                       ok           False                  False
  PAYX           78.12               32            0.75              0.58        111.38                41.41         0.558          pass              0.327             41.6                           0.428               11.04              1.163                       ok           False                  False
  MDLZ           95.00               20            0.48              0.21         63.82                19.69         0.550          pass              0.658             45.5                           0.415                8.75              0.869                       ok           False                  False
  ABNB           92.68               41            0.07              0.09        173.66                41.37         0.534          pass              0.860             89.4                           0.546                5.79              0.809                       ok           False                  False
   EXC           78.57               14            0.94              0.29         43.38                17.09         0.533          pass              0.080              0.0                           0.200                5.56              0.516                       ok           False                  False
  META           92.00               25            0.88              4.36        707.45                56.19         0.511          pass              0.569             32.6                           0.270               -5.23             -0.240 downtrend_blocked_streak           False                  False
   ADP           93.55               31            0.38              0.78        288.57                21.32         0.505          pass              0.784             77.3                           0.624               10.58              1.102                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-19T03:00:04.169170-04:00   data_refresh  data_refresh                   {'saved': 91, 'empty': 2}
2026-10-17T02:55:05.454730-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:50:06.805476-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:45:05.931268-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:40:05.272709-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:35:06.507747-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:30:06.058985-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:25:05.586713-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:20:06.484266-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-17T02:15:02.115456-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019093510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019093510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019093510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019093510)

</details>

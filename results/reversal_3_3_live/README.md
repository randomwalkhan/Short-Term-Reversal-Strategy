# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 09:45:04 EDT`
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

- Cash: `$62,756.80`
- Equity: `$131,181.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$8,750.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-16                   1     35     59675.0                 68425.0        17.05          19.55      270.43        268.31          bid_ask_mid                      19.55                bid_ask_mid                    True          8750.0                  14.66         85.71               21              1.66         51.07            62.7                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.89               27            0.97              1.85        270.58                59.14         0.578          pass              0.458             16.7                           0.295                0.41             -0.627                                 ok            True                  False
   KDP           96.00               25            0.51              0.12         34.57                30.61         0.566          pass              0.777             73.5                           0.611               11.51              1.319                                 ok            True                  False
 CMCSA           90.91               11            0.96              0.15         21.84                21.89         0.562          pass              0.469             38.2                           0.384                2.12              0.310                                 ok            True                  False
  ABNB           91.67               36            0.54              0.65        173.42                41.37         0.535          pass              0.609             23.9                           0.185                5.30              0.788                                 ok            True                  False
   ADP           91.30               23            0.75              1.52        288.25                21.32         0.528          pass              0.608             55.6                           0.358               10.17              1.086                                 ok            True                  False
  CTAS           91.67               24            0.87              1.31        213.13                23.07         0.516          pass              0.549             31.1                           0.295                8.41              0.977                                 ok            True                  False
  CTSH           94.59               37            0.59              0.27         65.91                41.45         0.513          pass              0.770             50.0                           0.470               12.84              1.562                                 ok            True                  False
   KHC           87.50               24            0.97              0.16         23.61                22.28         0.501          pass              0.446             34.3                           0.424                7.37              0.767                                 ok            True                  False
  TMUS           82.14               28            0.75              0.83        158.74                56.39         0.628          pass              0.317             25.6                           0.230               -4.09             -0.640            downtrend_blocked_slope           False                  False
  PAYX           74.07               27            1.21              0.95        111.22                41.41         0.555          pass              0.186              5.6                           0.098               10.52              1.142                                 ok           False                  False
  META           86.67               15            1.50              7.46        706.13                56.19         0.527          pass              0.264              0.0                           0.197               -5.83             -0.268 downtrend_blocked_slope_and_streak           False                  False
   EXC           75.00               12            1.16              0.35         43.35                17.09         0.526          pass              0.066              0.0                           0.172                5.33              0.506                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019094504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019094504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019094504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019094504)

</details>

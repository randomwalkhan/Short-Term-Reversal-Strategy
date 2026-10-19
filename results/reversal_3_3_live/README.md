# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 09:30:05 EDT`
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
   CEG     option         option CEG261120C00270000       2026-10-16                   1     35     59675.0                 58450.0        17.05           16.7      270.43        276.98     last_price_stale                        NaN                unavailable                   False         -1225.0                  -2.05         85.71               21              1.66         51.07             0.0                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   KDP           92.31               13            1.30              0.32         34.48                30.61         0.586            pass              0.502             31.8                           0.250               10.62              1.283                       ok            True                  False
  MDLZ           92.86               14            0.66              0.29         63.78                19.69         0.572            pass              0.502             25.0                           0.225                8.55              0.861                       ok            True                  False
  CTSH           93.33               30            1.27              0.59         65.78                41.45         0.515            pass              0.540              0.0                           0.283               12.07              1.531                       ok            True                  False
   KHC           83.33               18            1.39              0.23         23.58                22.28         0.509            pass              0.193              0.0                           0.163                6.91              0.747                       ok            True                  False
  TMUS           86.84               38            0.31              0.35        158.95                56.39         0.607            pass              0.592             54.1                           0.405               -3.67             -0.620  downtrend_blocked_slope           False                  False
 CMCSA           88.89                9            1.14              0.18         21.82                21.89         0.562            pass              0.366             24.2                           0.278                1.93              0.302                       ok           False                  False
   ADP           85.71                7            1.69              3.42        287.43                21.32         0.562            pass              0.209              0.0                           0.250                9.13              1.042                       ok           False                  False
  PAYX           75.00               28            1.07              0.83        111.27                41.41         0.561            pass              0.176              0.0                           0.250               10.68              1.148                       ok           False                  False
   PEP           77.27               22            0.73              0.68        131.20                21.98         0.505            pass              0.204             24.6                           0.229                3.88              0.460                       ok           False                  False
  AMGN           84.85               33            0.58              1.77        431.73                28.96         0.497 below_threshold              0.433             33.4                           0.251                6.70              0.767                       ok           False                  False
  INTU           85.19               27            1.28              2.90        323.90                39.88         0.490 below_threshold              0.398             32.5                           0.213               13.28              1.336                       ok           False                  False
  META           90.91               33            0.48              2.36        708.31                56.19         0.486 below_threshold              0.683             63.5                           0.412               -4.85             -0.221 downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019093005)

</details>

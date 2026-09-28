# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 09:30:06 EDT`
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

- Cash: `$38,003.30`
- Equity: `$71,803.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$-1,750.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00160000       2026-09-25                   1     20     35550.0                 33800.0        17.77           16.9      158.68        158.88     last_price_stale                        NaN                unavailable                   False         -1750.0                  -4.92          93.1               29              1.81         73.26            0.39                 109.71                2435.0         2824.0               0.01                      ok
```

## Today's Closed Trades (2026-09-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.76               29            2.89              3.06        150.16               120.87         0.653          pass              0.459             64.3                           0.524               45.55              4.697                  ok            True                  False
  AMGN           84.62               26            0.75              2.16        413.68                46.27         0.600          pass              0.290              0.0                           0.177                7.87              1.088                  ok            True                  False
    ZS           96.97               33            1.69              2.28        192.07                81.17         0.582          pass              0.750             46.1                           0.526               -1.01              0.455                  ok            True                  False
  META           82.61               23            1.26              6.64        748.82                50.12         0.545          pass              0.411             66.6                           0.609               11.59              1.565                  ok            True                  False
  CRWD           86.84               38            1.63              2.88        250.90                73.82         0.543          pass              0.561             45.9                           0.558                5.37              0.745                  ok            True                  False
   STX           87.88               33            1.02              6.56        914.02                54.25         0.542          pass              0.615             65.8                           0.515               12.74              1.890                  ok            True                  False
   CEG           84.85               33            0.53              0.97        262.85                41.90         0.542          pass              0.509             57.5                           0.423               -1.02              0.061                  ok            True                  False
    MU           91.89               37            0.61              4.62       1080.30                50.18         0.538          pass              0.783             77.4                           0.575               16.41              1.908                  ok            True                   True
  PANW           81.40               43            1.00              2.63        373.61                68.79         0.530          pass              0.475             61.5                           0.664               -0.79              0.176                  ok            True                  False
  MPWR           84.00               25            1.72             16.45       1360.38                54.48         0.526          pass              0.425             55.2                           0.479               17.55              2.185                  ok            True                  False
  MRVL           80.00               35            0.83              1.52        261.28                67.81         0.522          pass              0.450             76.9                           0.549               18.71              1.924                  ok            True                  False
  PYPL           85.71               14            1.93              0.75         54.72                60.08         0.520          pass              0.231              0.0                           0.206               -0.10              0.065                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928093006)

</details>

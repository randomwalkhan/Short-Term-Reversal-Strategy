# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 09:40:03 EDT`
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

- Cash: `$1,161.80`
- Equity: `$143,751.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-1,080.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 72270.0         1.10           1.10       44.42         44.62     last_price_stale                        NaN                unavailable                   False             0.0                   0.00          80.0               15              0.97         20.09            0.78                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   2     40     71400.0                 70320.0        17.85          17.58      223.97        221.64     last_price_stale                        NaN                unavailable                   False         -1080.0                  -1.51         100.0               38              0.68         80.16            3.13                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.86               14            0.56              0.25         63.69                25.23         0.596            pass              0.517             29.4                           0.238                2.67              0.358                                 ok            True                  False
    ZS           92.11               38            0.53              0.95        254.74                57.49         0.544            pass              0.651             29.2                           0.264               12.41              1.251                                 ok            True                  False
  TEAM          100.00               17            2.62              4.18        225.82                47.89         0.510            pass              0.562             21.6                           0.180                6.69              0.982                                 ok            True                  False
  AAPL           86.67               15            1.33              3.24        346.34                16.45         0.501            pass              0.342             26.9                           0.418                0.62              0.138                                 ok            True                  False
  TMUS           85.29               34            0.44              0.45        146.35                64.13         0.631            pass              0.565             67.0                           0.425               -3.93             -0.385            downtrend_blocked_slope           False                  False
   CEG           85.37               41            0.21              0.37        253.29                65.46         0.608            pass              0.597             64.2                           0.419              -13.94             -1.564 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.88               32            0.20              0.05         34.66                26.07         0.526            pass              0.731             44.0                           0.316                5.68              0.650                                 ok           False                  False
 CMCSA          100.00                2            2.40              0.38         22.53                23.68         0.520            pass              0.493             13.5                           0.154                7.09              0.881                                 ok           False                  False
  CRWD           86.36               44            0.30              0.54        257.34                57.83         0.505            pass              0.641             73.4                           0.393               -2.36             -0.326           downtrend_blocked_streak           False                  False
  INTU           89.47               38            0.24              0.58        343.14                39.39         0.499 below_threshold              0.690             66.8                           0.539               11.95              1.410                                 ok           False                  False
  NFLX           72.73               22            1.38              0.64         65.58                35.37         0.499 below_threshold              0.130              0.0                           0.150               -8.03             -0.990 downtrend_blocked_slope_and_streak           False                  False
  TTWO           88.46               26            1.20              1.71        202.96                30.02         0.498 below_threshold              0.382              0.0                           0.164               -3.63             -0.042                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-26T03:00:06.095406-04:00   data_refresh  data_refresh                   {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:45:06.637393-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:40:05.798457-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:35:04.182353-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:30:05.264704-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:25:04.373629-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:20:05.341779-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:15:04.235685-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026094003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026094003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026094003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026094003)

</details>

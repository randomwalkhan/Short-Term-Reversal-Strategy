# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 09:55:06 EDT`
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

- Cash: `$17,668.00`
- Equity: `$34,418.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   1     25     16375.0                 16750.0         6.55            6.7       129.9        131.03          bid_ask_mid                        6.7                bid_ask_mid                    True           375.0                   2.29         91.67               24              0.73         32.92           34.46                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           90.00               30            0.90              5.37        849.39               103.51         0.724          pass              0.589             38.8                           0.230               -1.93              0.582                                 ok            True                  False
   WDC           82.14               28            1.58              5.75        517.33               113.75         0.712          pass              0.281             10.9                           0.093               -7.91              0.042                                 ok            True                  False
  PYPL           86.67               30            0.77              0.30         56.02                61.92         0.651          pass              0.484             35.8                           0.289               16.94              1.278                                 ok            True                  False
  SOXL           85.29               34            1.20              1.15        136.30               179.12         0.820          pass              0.538             51.7                           0.248              -18.27             -1.534            downtrend_blocked_slope           False                  False
  KLAC           90.91               33            0.97              1.43        209.91                94.03         0.694          pass              0.686             57.5                           0.348               -6.20             -0.695 downtrend_blocked_slope_and_streak           False                  False
  AMAT           93.55               31            0.88              3.29        534.84                84.50         0.647          pass              0.759             64.2                           0.363               -7.62             -0.764 downtrend_blocked_slope_and_streak           False                  False
  INTC           87.18               39            0.56              0.36         92.17                79.50         0.610          pass              0.497             16.9                           0.123              -10.97             -0.908 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.48               21            0.41              0.17         60.45                31.78         0.604          pass              0.550             45.7                           0.269                0.68              0.160                                 ok           False                  False
  LRCX           84.62               26            2.04              4.36        303.34                85.02         0.588          pass              0.416             42.5                           0.269               -9.38             -1.028 downtrend_blocked_slope_and_streak           False                  False
   CSX          100.00                7            1.62              0.60         52.97                24.65         0.585          pass              0.483              8.0                           0.087                5.50              0.578                                 ok           False                  False
   EXC           95.83               24            0.40              0.13         47.47                24.01         0.557          pass              0.787             79.3                           0.638                0.53              0.131                                 ok           False                  False
   WBD           90.00               20            0.64              0.12         25.72                22.96         0.535          pass              0.592             68.3                           0.736               -5.48             -0.818            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-27T09:35:01.555025-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:30:04.489033-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:25:02.551278-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:20:01.575598-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:15:05.384671-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:10:05.509301-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:05:02.526128-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T09:00:04.546327-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:55:01.530928-04:00 data_refresh data_refresh {'saved': 93}
2026-07-27T08:50:01.513320-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727095506)

</details>

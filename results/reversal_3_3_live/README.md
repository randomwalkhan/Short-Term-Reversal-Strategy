# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 09:35:01 EDT`
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

- Cash: `$15,257.25`
- Equity: `$31,682.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$1,460.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 16425.0         2.05           2.25       52.68         52.02     last_price_stale                        NaN                unavailable                   False          1460.0                   9.76         93.55               31              0.59         45.34            3.13                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           96.15               26            1.18              0.99        119.93                60.79         0.620          pass              0.624             18.4                           0.185               -0.61              0.126                                 ok            True                  False
  PAYX          100.00               20            0.72              0.50        100.06                34.26         0.594          pass              0.749             74.5                           0.509                5.43              0.426                                 ok            True                  False
  WDAY           85.19               27            2.14              2.10        139.33                67.85         0.554          pass              0.463             51.8                           0.446               10.22              0.510                                 ok            True                  False
  CDNS           92.31               26            1.26              3.46        389.42                58.96         0.553          pass              0.691             66.9                           0.549                3.18              0.256                                 ok            True                  False
  CRWD           87.10               31            1.07              4.85        642.85                62.27         0.549          pass              0.580             65.2                           0.553               -1.14             -0.820                                 ok            True                  False
   ADP           96.15               26            1.04              1.68        230.45                32.72         0.542          pass              0.719             52.7                           0.342                5.11              0.483                                 ok            True                  False
   ROP           91.30               23            1.17              2.75        334.19                30.83         0.536          pass              0.528             28.8                           0.344                4.68              0.372                                 ok            True                  False
  TEAM           91.30               23            3.69              2.47         94.55                85.52         0.529          pass              0.494             17.7                           0.212                3.38             -0.362                                 ok            True                  False
  ASML           92.86               28            1.49             18.54       1769.82                54.01         0.505          pass              0.684             57.0                           0.538                9.60              1.050                                 ok            True                  False
    ZS           76.92               26            1.81              1.59        125.16               158.01         0.887          pass              0.318             40.8                           0.361               -2.25             -0.811 downtrend_blocked_slope_and_streak           False                  False
  MRVL          100.00               30            0.44              0.83        266.53               141.19         0.748          pass              0.883             91.5                           0.732               33.72              3.628                                 ok           False                  False
  INTU           71.43               21            2.40              4.93        291.67               101.32         0.706          pass              0.213             23.0                           0.247               -6.82             -1.153 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-06-10T09:20:01.107182-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:15:04.252289-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:10:02.279935-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:05:01.300064-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T09:00:02.291233-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:55:03.361552-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:50:01.278104-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:45:01.119334-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:40:02.326474-04:00 data_refresh data_refresh {'saved': 93}
2026-06-10T08:35:05.344979-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610093501)

</details>

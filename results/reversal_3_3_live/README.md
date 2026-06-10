# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 09:40:04 EDT`
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
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 16425.0         2.05           2.25       52.68         52.63     last_price_stale                        NaN                unavailable                   False          1460.0                   9.76         93.55               31              0.59         45.34            3.13                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               30            0.81              1.52        266.23               141.19         0.728          pass              0.859             84.3                           0.733               33.22              3.611                                 ok            True                   True
  CSCO           95.65               23            1.26              1.06        119.90                60.79         0.635          pass              0.588             12.6                           0.144               -0.69              0.123                                 ok            True                  False
  TEAM           91.18               34            1.51              1.01         95.18                85.52         0.597          pass              0.717             66.3                           0.594                5.72             -0.260                                 ok            True                   True
  WDAY           88.89               36            0.93              0.91        139.84                67.85         0.576          pass              0.705             79.1                           0.731               11.59              0.566                                 ok            True                   True
  CTSH           90.32               31            0.81              0.30         52.81                47.83         0.558          pass              0.670             66.4                           0.514               -1.22             -0.416                                 ok            True                  False
  ADBE           81.82               33            1.12              1.87        237.08                49.90         0.509          pass              0.424             57.2                           0.534               -1.27             -0.435                                 ok            True                  False
  PCAR           83.33               12            1.90              1.59        119.01                26.54         0.504          pass              0.173              7.0                           0.190                4.60              0.788                                 ok            True                  False
  DRAM          100.00               14            1.56              0.65         59.49               102.89         0.735          pass              0.710             69.9                           0.611               -3.11             -0.835            downtrend_blocked_slope           False                  False
  INTU           80.00               30            1.34              2.75        292.60               101.32         0.724          pass              0.377             57.2                           0.485               -5.81             -1.104 downtrend_blocked_slope_and_streak           False                  False
   TRI           78.95               19            1.12              0.65         82.04                68.38         0.677          pass              0.324             65.4                           0.518               -0.94             -0.411                                 ok           False                  False
  QCOM           93.75               16            1.98              2.85        204.20                99.46         0.661          pass              0.621             49.3                           0.540              -13.41             -1.724            downtrend_blocked_slope           False                  False
  SOXL           90.91               22            3.03              4.28        199.94               192.17         0.613          pass              0.648             72.0                           0.799              -10.24             -1.453            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610094004)

</details>

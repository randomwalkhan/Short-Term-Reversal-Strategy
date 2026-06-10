# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 09:30:06 EDT`
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
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 16425.0         2.05           2.25       52.68         52.46     last_price_stale                        NaN                unavailable                   False          1460.0                   9.76         93.55               31              0.59         45.34            3.13                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           80.00               25            2.25             14.75        929.57               110.66         0.632          pass              0.326             54.3                           0.480               -1.46             -0.470                                 ok            True                  False
  PAYX          100.00               21            0.59              0.41        100.10                34.26         0.595          pass              0.770             79.1                           0.590                5.57              0.432                                 ok            True                  False
  PANW           84.62               26            1.48              2.70        259.36                59.69         0.570          pass              0.451             54.7                           0.473                3.30             -0.204                                 ok            True                  False
  TEAM           92.86               28            2.67              1.79         94.84                85.52         0.564          pass              0.641             40.5                           0.369                4.48             -0.314                                 ok            True                  False
  WDAY           85.71               28            2.02              1.99        139.38                67.85         0.556          pass              0.491             54.5                           0.510               10.36              0.515                                 ok            True                  False
  CRWD           88.57               35            0.89              4.04        643.20                62.27         0.538          pass              0.662             71.0                           0.504               -0.96             -0.811                                 ok            True                  False
  LRCX           88.89               27            1.23              2.81        325.96                65.36         0.525          pass              0.604             67.0                           0.506                1.32              0.141                                 ok            True                  False
  ASML           92.00               25            1.81             22.51       1768.12                54.01         0.504          pass              0.614             47.8                           0.455                9.25              1.035                                 ok            True                  False
    ZS           78.79               33            1.27              1.12        125.36               158.01         0.882          pass              0.417             58.5                           0.442               -1.71             -0.786 downtrend_blocked_slope_and_streak           False                  False
  MRVL          100.00               30            0.43              0.80        266.54               141.19         0.749          pass              0.884             91.8                           0.699               33.74              3.628                                 ok           False                  False
  INTU           76.00               25            1.75              3.60        292.24               101.32         0.732          pass              0.264             30.1                           0.270               -6.21             -1.123 downtrend_blocked_slope_and_streak           False                  False
  DRAM          100.00               14            2.05              0.86         59.40               102.89         0.708          pass              0.679             60.4                           0.472               -3.60             -0.858            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610093006)

</details>

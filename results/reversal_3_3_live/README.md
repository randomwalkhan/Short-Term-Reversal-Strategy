# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 10:05:01 EDT`
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

- Cash: `$15,257.25`
- Equity: `$31,134.75`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$912.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 15877.5         2.05           2.17       52.68         52.91          bid_ask_mid                       2.17                bid_ask_mid                    True           912.5                    6.1         93.55               31              0.59         45.34           64.45                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               26            1.42              2.65        265.74               141.19         0.714          pass              0.796             72.7                           0.455               32.41              3.583                                 ok            True                  False
   TRI           83.33               24            0.63              0.36         82.16                68.38         0.680          pass              0.492             80.5                           0.779               -0.45             -0.389                                 ok            True                  False
    MU           80.00               25            2.10             13.78        929.98               110.66         0.642          pass              0.336             57.3                           0.486               -1.32             -0.463                                 ok            True                  False
  REGN           84.85               33            0.83              3.57        614.65                44.80         0.539          pass              0.468             43.8                           0.303               -2.65             -0.028                                 ok            True                  False
   CSX           92.59               27            0.57              0.19         47.20                21.23         0.511          pass              0.672             57.1                           0.506                0.03              0.283                                 ok            True                  False
  DRAM          100.00               18            0.89              0.37         59.70               102.89         0.745          pass              0.778             83.3                           0.736               -2.31             -0.797            downtrend_blocked_slope           False                  False
  INTU           76.00               25            1.81              3.72        292.18               101.32         0.722          pass              0.298             41.9                           0.453               -6.26             -1.125 downtrend_blocked_slope_and_streak           False                  False
  SOXL           92.86               28            0.93              1.32        201.12               192.17         0.696          pass              0.806             91.3                           0.737               -8.34             -1.358            downtrend_blocked_slope           False                  False
  TEAM           93.18               44            0.03              0.02         95.60                85.52         0.617          pass              0.911             99.3                           0.958                7.31             -0.193                                 ok           False                  False
  QCOM           88.89                9            3.28              4.71        203.40                99.46         0.617          pass              0.347             16.2                           0.219              -14.56             -1.785            downtrend_blocked_slope           False                  False
  CSCO           97.30               37            0.31              0.26        120.25                60.79         0.600          pass              0.884             81.5                           0.732                0.27              0.166                                 ok           False                  False
  WDAY           90.24               41            0.36              0.36        140.08                67.85         0.573          pass              0.806             91.8                           0.883               12.22              0.591                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-10T10:05:01.308545-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:00:06.287527-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T09:20:01.107182-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T09:15:04.252289-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T09:10:02.279935-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T09:05:01.300064-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T09:00:02.291233-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T08:55:03.361552-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T08:50:01.278104-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-10T08:45:01.119334-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610100501)

</details>

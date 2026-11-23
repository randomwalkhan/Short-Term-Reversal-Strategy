# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 11:30:26 EST`
Last processed slot: `manage_1130`

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

- Cash: `$48,929.80`
- Equity: `$100,769.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$4,640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   1     32     47200.0                 51840.0        14.75           16.2       344.6        348.32          bid_ask_mid                       16.2                bid_ask_mid                    True          4640.0                   9.83         100.0               14              1.32         27.92           28.07                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           95.65               23            0.84              0.15         24.84                33.22         0.536            pass              0.738             65.9                           0.776                0.73              0.075                                 ok            True                  False
  COST           85.71               21            0.57              4.43       1100.25                21.93         0.535            pass              0.468             63.0                           0.725                2.78              0.271                                 ok            True                  False
  VRSK           80.95               21            1.69              2.39        201.06                40.90         0.505            pass              0.327             59.4                           0.576               -0.96             -0.199                                 ok            True                  False
  PAYX           73.91               23            0.58              0.45        112.44                33.87         0.549            pass              0.297             51.7                           0.660               -2.42             -0.357            downtrend_blocked_slope           False                  False
  MDLZ          100.00               30            0.29              0.14         66.22                24.95         0.525            pass              0.831             81.6                           0.798               -0.53             -0.091                                 ok           False                  False
  CTSH           86.49               37            0.07              0.03         58.05                42.36         0.505            pass              0.678             91.7                           0.542               -8.30             -1.347 downtrend_blocked_slope_and_streak           False                  False
  TMUS           82.14               28            0.98              1.14        165.11                34.83         0.505            pass              0.308             26.9                           0.318               -2.81             -0.449            downtrend_blocked_slope           False                  False
  CHTR           77.27               44            0.30              0.27        128.62                65.33         0.486 below_threshold              0.519             90.2                           0.893                5.90              0.138                                 ok           False                  False
   PEP           89.19               37            0.16              0.16        140.47                27.59         0.483 below_threshold              0.744             90.4                           0.724               -1.11             -0.251                                 ok           False                  False
   ADP           90.62               32            0.39              0.82        301.36                24.32         0.480 below_threshold              0.703             75.2                           0.706               -0.50             -0.133                                 ok           False                  False
   ROP           87.88               33            0.54              1.75        459.08                29.79         0.475 below_threshold              0.588             59.1                           0.575               -3.03             -0.382 downtrend_blocked_slope_and_streak           False                  False
  MNST           64.71               17            1.51              0.46         43.49                30.90         0.473 below_threshold              0.258             54.6                           0.608               -5.72             -0.559            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-21T02:55:05.433853-05:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:50:06.291709-05:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:45:05.697713-05:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:40:04.140323-05:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:35:05.478218-05:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:30:05.376683-05:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:25:04.330669-05:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:20:06.220258-05:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123113026)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123113026)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123113026)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123113026)

</details>

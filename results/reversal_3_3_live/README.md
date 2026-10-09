# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-09 15:55:05 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$58,874.30`
- Equity: `$114,874.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$-2,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   0    160     58400.0                 56000.0         3.65            3.5       59.31         59.23          bid_ask_mid                        3.5                bid_ask_mid                    True         -2400.0                  -4.11          93.1               29              1.17         50.42           48.85                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261120C00115000     74          2026-10-08         2026-10-09         7.25       8.425 8695.0   16.206897 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           94.44               18            0.53              0.22         60.57                17.90         0.554            pass              0.637             47.5                           0.285                1.05              0.203                                 ok            True                  False
  CTSH           92.31               26            1.37              0.57         59.76                46.57         0.519            pass              0.569             27.4                           0.247                3.24              0.311                                 ok            True                  False
  SOXL           87.10               31            1.93              1.93        141.69               115.52         0.642            pass              0.522             42.7                           0.341               -7.72              0.105           downtrend_blocked_streak           False                  False
  META           83.78               37            0.32              1.63        720.19                52.31         0.577            pass              0.489             50.2                           0.393               -4.40             -0.190           downtrend_blocked_streak           False                  False
  QCOM           92.68               41            0.30              0.37        175.85                56.70         0.548            pass              0.855             87.3                           0.736              -13.12             -1.011 downtrend_blocked_slope_and_streak           False                  False
  NFLX           66.67               15            1.84              0.92         71.18                35.32         0.530            pass              0.086              0.0                           0.147               -1.26              0.012                                 ok           False                  False
  PAYX           78.38               37            0.36              0.26        104.35                40.01         0.527            pass              0.335             34.2                           0.282                2.68              0.402                                 ok           False                  False
  INTC           85.71               28            2.25              1.68        106.36                69.62         0.518            pass              0.390             21.9                           0.277              -14.90             -1.242 downtrend_blocked_slope_and_streak           False                  False
  INTU           88.89               36            0.49              1.04        303.43                43.01         0.510            pass              0.643             60.6                           0.448               10.16              1.273                                 ok           False                  False
  AMAT           84.21               38            0.73              2.61        508.45                47.71         0.487 below_threshold              0.413             21.8                           0.161                4.30              0.491                                 ok           False                  False
 CMCSA          100.00                3            2.69              0.40         21.04                20.06         0.483 below_threshold              0.514             21.9                           0.402               -4.33             -0.308            downtrend_blocked_slope           False                  False
  LRCX           82.93               41            0.54              1.21        320.07                52.42         0.480 below_threshold              0.513             62.2                           0.357                1.16              0.214                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-09T15:10:06.439526-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T15:05:05.713362-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T15:00:05.326710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T14:55:05.363044-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T14:50:06.079199-04:00       entry_1500              entry {"allocated_cash": 58400.0, "asset_type": "option", "contract_symbol": "CTSH261120C00060000", "contracts": 160, "early_entry_score": 0.592, "entry_mode": "regular", "entry_option_price": 3.65, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 209.0, "option_spread_pct": 8.22, "option_volume": 38.0, "success_rate": 93.1, "ticker": "CTSH", "timing_score": 0.518}
2026-10-09T14:50:06.079199-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-09", "training_samples": 5994, "window": 5}
2026-10-09T13:50:04.651779-04:00      manage_1400               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 8.425, "pnl": 8695.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.21, "ticker": "CSCO"}
2026-10-09T11:44:59.466753-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-09T00:00:06.171329-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-08T15:10:05.020875-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261009155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261009155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261009155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261009155505)

</details>

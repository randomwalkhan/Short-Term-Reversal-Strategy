# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-09 15:30:01 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$115,674.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$-1,600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   0    160     58400.0                 56800.0         3.65           3.55       59.31         59.22          bid_ask_mid                       3.55                bid_ask_mid                    True         -1600.0                  -2.74          93.1               29              1.17         50.42           50.39                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261120C00115000     74          2026-10-08         2026-10-09         7.25       8.425 8695.0   16.206897 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           92.31               26            1.37              0.57         59.76                46.57         0.523            pass              0.511              7.9                           0.140                3.24              0.311                                 ok            True                  False
  INTU           87.88               33            0.79              1.69        303.16                43.01         0.509            pass              0.523             36.2                           0.305                9.82              1.260                                 ok            True                  False
  SOXL           87.50               32            1.69              1.69        141.80               115.52         0.649            pass              0.561             49.8                           0.566               -7.49              0.116           downtrend_blocked_streak           False                  False
  META           84.21               38            0.21              1.04        720.44                52.31         0.579            pass              0.562             68.3                           0.592               -4.29             -0.184           downtrend_blocked_streak           False                  False
  QCOM           92.68               41            0.35              0.43        175.83                56.70         0.546            pass              0.849             85.5                           0.852              -13.16             -1.013 downtrend_blocked_slope_and_streak           False                  False
  INTC           87.10               31            1.78              1.34        106.51                69.62         0.534            pass              0.420             12.4                           0.295              -14.50             -1.221 downtrend_blocked_slope_and_streak           False                  False
  NFLX           70.59               17            1.63              0.82         71.22                35.32         0.534            pass              0.125              8.3                           0.149               -1.05              0.022                                 ok           False                  False
  PAYX           79.49               39            0.29              0.21        104.37                40.01         0.521            pass              0.340             31.6                           0.383                2.75              0.405                                 ok           False                  False
   PEP           50.00                2            1.74              1.56        127.67                20.67         0.514            pass              0.132             26.9                           0.538               -1.96             -0.216                                 ok           False                  False
  AMAT           84.62               39            0.30              1.08        509.11                47.71         0.507            pass              0.570             67.7                           0.505                4.75              0.511                                 ok           False                  False
  MDLZ           93.55               31            0.02              0.01         60.67                17.90         0.506            pass              0.847             98.4                           0.707                1.57              0.226                                 ok           False                  False
 CMCSA          100.00                3            2.57              0.38         21.05                20.06         0.489 below_threshold              0.525             25.3                           0.511               -4.22             -0.303            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261009153001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261009153001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261009153001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261009153001)

</details>

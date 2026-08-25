# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 10:00:02 EDT`
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

- Cash: `$30,388.00`
- Equity: `$59,458.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$1,755.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 29070.0        30.35           32.3      310.66         313.8          bid_ask_mid                       32.3                bid_ask_mid                    True          1755.0                   6.43          87.5               32              1.06         63.04           64.55                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.40              1.68        170.61               115.46         0.764          pass              0.455             51.8                           0.368                9.64              1.095                  ok            True                  False
  GEHC           95.65               23            1.20              0.62         73.92                49.18         0.623          pass              0.590             13.6                           0.206                0.76              0.204                  ok            True                  False
  DXCM           87.88               33            0.81              0.52         90.84                50.36         0.579          pass              0.536             38.3                           0.218                0.88              0.097                  ok            True                  False
  WDAY           80.65               31            1.91              2.67        198.01                78.88         0.572          pass              0.329             38.0                           0.294                7.76              0.739                  ok            True                  False
   TRI           88.46               26            1.80              1.37        108.03                67.11         0.568          pass              0.528             46.1                           0.545                2.41              0.452                  ok            True                  False
  FAST          100.00               16            1.15              0.41         51.10                22.00         0.558          pass              0.510              4.8                           0.075               -3.23             -0.229                  ok            True                  False
   KHC           85.00               20            1.40              0.25         25.56                37.91         0.553          pass              0.310             18.2                           0.219                2.68              0.345                  ok            True                  False
  PAYX          100.00               23            0.71              0.62        125.74                34.31         0.551          pass              0.706             54.8                           0.533                3.15              0.330                  ok            True                  False
  MDLZ           93.33               15            1.68              0.76         64.37                26.88         0.535          pass              0.450              2.7                           0.054                2.96              0.360                  ok            True                  False
 CMCSA           92.00               25            0.76              0.14         26.96                32.81         0.532          pass              0.587             37.9                           0.331                4.54              0.538                  ok            True                  False
  CTSH           88.57               35            0.79              0.34         62.05                52.34         0.530          pass              0.619             57.0                           0.531                5.92              0.804                  ok            True                  False
  SBUX           90.00               20            0.63              0.47        107.29                20.57         0.518          pass              0.588             67.7                           0.716                0.72             -0.090                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-25T10:00:02.656689-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T00:00:04.661538-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-24T15:10:01.417381-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:05:03.439109-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T15:00:02.474855-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:55:01.386568-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-24T14:50:01.463647-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-24", "training_samples": 5698, "window": 5}
2026-08-24T14:50:01.463647-04:00       entry_1500              entry {"allocated_cash": 27315.0, "asset_type": "option", "contract_symbol": "LRCX261016C00310000", "contracts": 9, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 5.27, "option_volume": 30.0, "success_rate": 87.5, "ticker": "LRCX", "timing_score": 0.666}
2026-08-24T12:00:04.404720-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:55:01.402592-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825100002)

</details>

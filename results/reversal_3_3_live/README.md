# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 10:15:01 EDT`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$1,895.00`
- Equity: `$27,600.00`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-1,592.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13005.0        15.28          14.45      245.93        246.24          bid_ask_mid                      14.45                bid_ask_mid                    True          -742.5                  -5.40         91.67               36              0.66         58.04           55.55                  42.55                2852.0           34.0               0.10                      ok
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 12700.0        13.55          12.70      241.03        240.35          bid_ask_mid                      12.70                bid_ask_mid                    True          -850.0                  -6.27         97.62               42              0.58         61.06           60.12                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               11            2.23              4.68        298.59                69.24         0.679          pass              0.475             36.6                           0.315                4.59              0.654                                 ok            True                  False
  FTNT          100.00               42            0.53              0.47        126.30                70.72         0.606          pass              0.887             75.5                           0.673               39.94              3.256                                 ok            True                   True
  GOOG           83.33               18            1.50              4.13        391.34                40.55         0.548          pass              0.302             34.8                           0.464                0.76              0.031                                 ok            True                  False
 GOOGL           84.21               19            1.53              4.24        395.12                40.53         0.545          pass              0.329             34.2                           0.467                0.63              0.044                                 ok            True                  False
  SNPS           97.14               35            0.82              2.85        497.21                41.65         0.530          pass              0.733             37.8                           0.277               -1.62             -0.168                                 ok            True                  False
  NVDA           85.71               21            1.72              2.68        221.17                44.74         0.529          pass              0.279              0.0                           0.203               11.19              1.092                                 ok            True                  False
  ASML           82.14               28            1.59             16.43       1465.35                50.95         0.510          pass              0.271             14.3                           0.115                0.42             -0.182                                 ok            True                  False
  AVGO           90.91               11            3.20              9.43        416.67                42.85         0.504          pass              0.348              0.0                           0.150               -4.71             -0.162                                 ok            True                  False
  NXPI           75.00               24            1.33              2.71        290.52                90.65         0.729          pass              0.278             37.4                           0.273               -1.55             -0.231                                 ok           False                  False
  INSM           78.72               47            0.04              0.03        107.14               111.34         0.722          pass              0.566             98.0                           0.735              -23.19             -1.634 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00               10            4.35              3.29        106.76               114.00         0.660          pass              0.473              2.3                           0.139               -4.33             -0.584 downtrend_blocked_slope_and_streak           False                  False
  MNST           69.23               13            1.82              1.13         88.06                49.83         0.612          pass              0.119             12.5                           0.221               14.68              1.479                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-19T10:15:01.057449-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-19T10:10:01.046495-04:00 early_entry_1010         entry {"allocated_cash": 13747.5, "asset_type": "option", "contract_symbol": "PANW260618C00250000", "contracts": 9, "early_entry_score": 0.729, "entry_mode": "early", "entry_option_price": 15.275, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2852.0, "option_spread_pct": 10.15, "option_volume": 34.0, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.462}
2026-05-19T10:05:01.031829-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T10:00:03.926915-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-19T00:00:06.432342-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519101501)

</details>

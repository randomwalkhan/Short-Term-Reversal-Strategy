# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 14:00:03 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$15,642.50`
- Equity: `$29,492.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$300.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13850.0        13.55          13.85      241.03        242.21          bid_ask_mid                      13.85                bid_ask_mid                    True           300.0                   2.21         97.62               42              0.58         61.06           60.17                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.48               21            1.32              2.79        301.53                68.84         0.690            pass              0.423              0.5                           0.036                6.90              0.898                                 ok            True                  False
  INTC          100.00               27            1.67              1.27        108.22               115.99         0.681            pass              0.770             63.0                           0.562               11.66              0.729                                 ok            True                  False
  SNPS           96.00               25            1.63              5.74        499.96                42.05         0.524            pass              0.668             38.5                           0.536               -0.66              0.008                                 ok            True                  False
  AAPL           88.24               17            1.31              2.74        299.05                22.88         0.524            pass              0.398             26.3                           0.509                7.14              0.697                                 ok            True                  False
  AMGN           86.36               22            0.75              1.71        325.58                26.25         0.500 below_threshold              0.456             52.2                           0.502                0.76              0.120                                 ok            True                  False
  NXPI           84.62               39            0.11              0.22        291.41                90.58         0.723            pass              0.649             86.8                           0.571                0.15             -0.040                                 ok           False                  False
  INSM           52.94               17            3.01              2.30        108.16               111.34         0.622            pass              0.197             29.3                           0.334              -24.39             -2.292 downtrend_blocked_slope_and_streak           False                  False
  CSCO           94.12               34            0.27              0.22        118.11                49.84         0.590            pass              0.851             85.3                           0.783               27.27              2.757                                 ok           False                  False
  SBUX           96.43               28            0.40              0.30        106.69                32.79         0.544            pass              0.807             77.6                           0.444                1.95              0.216                                 ok           False                  False
  MCHP           79.17               24            1.80              1.18         93.34                53.01         0.510            pass              0.175             10.1                           0.255               -3.29             -0.590 downtrend_blocked_slope_and_streak           False                  False
  AVGO           92.59               27            1.33              3.94        423.50                43.18         0.497 below_threshold              0.633             44.7                           0.559                0.73              0.101                                 ok           False                  False
  ASML           80.95               21            2.32             24.37       1491.36                50.55         0.485 below_threshold              0.208             20.3                           0.350                5.83              0.507                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-18T12:00:03.667934-04:00 early_entry_1200 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:55:01.697815-04:00 early_entry_1155 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:45:01.537610-04:00 early_entry_1145 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:40:04.531844-04:00 early_entry_1140 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:35:01.580218-04:00 early_entry_1135 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518140003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518140003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518140003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518140003)

</details>

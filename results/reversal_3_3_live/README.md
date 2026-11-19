# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 09:35:04 EST`
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

- Cash: `$56,193.80`
- Equity: `$106,563.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$645.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00400000       2026-11-18                   1     15     49725.0                 50370.0        33.15          33.58      389.81         401.0     last_price_stale                        NaN                unavailable                   False           645.0                    1.3         90.91               22              2.29         60.57             0.0                 121.47                4183.0           24.0               0.06                      ok
```

## Today's Closed Trades (2026-11-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.30               37            0.59              2.88        697.23                78.12         0.707          pass              0.651              0.0                           0.190                3.52              0.225                      ok            True                  False
   AEP          100.00               11            0.67              0.59        126.25                18.65         0.582          pass              0.465              0.0                           0.223               -0.13              0.012                      ok            True                  False
  SBUX           81.82               11            1.45              1.11        108.63                31.90         0.571          pass              0.112              0.0                           0.179                1.88              0.165                      ok            True                  False
 CMCSA           91.67               24            0.79              0.14         25.18                34.19         0.555          pass              0.560             33.3                           0.405                0.36              0.295                      ok            True                  False
  REGN           85.00               40            0.58              3.81        943.90                54.27         0.553          pass              0.429             13.3                           0.118                4.12              0.522                      ok            True                  False
  TMUS           83.33               30            0.83              0.95        163.61                47.11         0.553          pass              0.277              0.0                           0.171                1.29              0.088                      ok            True                  False
  VRSK           81.82               22            1.59              2.25        201.34                47.31         0.542          pass              0.222             13.2                           0.290               -5.85             -0.167                      ok            True                  False
   MAR           88.24               17            1.09              3.23        423.78                24.12         0.541          pass              0.331              3.5                           0.112                0.78              0.129                      ok            True                  False
   EXC           83.33               18            1.06              0.34         45.87                22.38         0.507          pass              0.205              3.9                           0.092               -2.15             -0.005                      ok            True                  False
   KDP           81.82               11            1.40              0.34         34.86                47.14         0.629          pass              0.193             25.0                           0.189               -6.42             -0.776 downtrend_blocked_slope           False                  False
   TRI           85.71               28            0.86              0.62        103.63                60.81         0.613          pass              0.363              9.6                           0.231              -12.23             -0.966 downtrend_blocked_slope           False                  False
  MDLZ          100.00                4            2.02              0.94         66.16                28.83         0.583          pass              0.461              0.7                           0.037               -2.39             -0.029                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-11-18T14:55:05.603926-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-11-18T14:50:05.341851-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"allocated_cash": 49725.0, "asset_type": "option", "contract_symbol": "APP270115C00400000", "contracts": 15, "early_entry_score": 0.497, "entry_mode": "regular", "entry_option_price": 33.15, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 4183.0, "option_spread_pct": 5.73, "option_volume": 24.0, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.787}
2026-11-18T14:50:05.341851-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-18", "training_samples": 6259, "window": 5}
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:55:05.147885-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:50:04.203803-05:00 early_entry_1150 early_entry_shadow {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "entry_ask": 6.3, "entry_bid": 5.7, "entry_mode": "early", "entry_option_price": 6.0, "hypothetical_budget": 52959.4, "hypothetical_contracts": 88, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 10.0, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "matched_signals": 39, "recovery_stability_score": 0.7, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119093504)

</details>

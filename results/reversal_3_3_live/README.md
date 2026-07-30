# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 09:30:01 EDT`
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

- Cash: `$17,629.75`
- Equity: `$34,324.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$-630.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FAST     option         option FAST260918C00045000       2026-07-29                   1     45     17325.0                 16695.0         3.85           3.71       47.84         47.62     last_price_stale                        NaN                unavailable                   False          -630.0                  -3.64         100.0               21              0.54         33.33             0.0                  27.18                 324.0           33.0               0.08                      ok
```

## Today's Closed Trades (2026-07-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           83.33               18            1.50              0.61         58.09                61.52         0.681          pass              0.241             10.3                           0.283                3.52              0.214                  ok            True                  False
  GEHC           91.67               24            1.24              0.62         71.63                59.17         0.647          pass              0.469              0.0                           0.230               12.42              0.607                  ok            True                  False
   KDP           85.00               20            0.89              0.20         31.37                34.46         0.593          pass              0.398             46.2                           0.313                3.01              0.043                  ok            True                  False
  AAPL           91.67               12            1.52              3.59        336.65                28.00         0.585          pass              0.412              9.8                           0.278                1.70              0.194                  ok            True                  False
  GILD           90.91               11            1.75              1.62        132.03                34.28         0.584          pass              0.401             15.0                           0.147                0.28             -0.127                  ok            True                  False
   PEP           80.00               15            1.25              1.26        142.96                31.31         0.576          pass              0.175             28.0                           0.324                4.65              0.366                  ok            True                  False
  BKNG           90.48               21            1.80              2.54        200.21                45.62         0.568          pass              0.457             15.7                           0.269               13.05              0.752                  ok            True                  False
  MNST           94.12               17            0.91              0.62         96.97                25.74         0.566          pass              0.696             72.0                           0.426               -1.69             -0.255                  ok            True                  False
  VRTX           84.62               13            1.78              6.02        480.75                33.19         0.562          pass              0.301             33.8                           0.327               -0.33             -0.026                  ok            True                  False
   EXC           94.12               17            1.01              0.33         46.89                23.57         0.552          pass              0.693             71.7                           0.487               -0.78              0.165                  ok            True                  False
  AMGN           90.00               10            2.00              5.43        385.31                27.22         0.544          pass              0.321              0.0                           0.163                6.93              0.701                  ok            True                  False
  DASH           96.67               30            1.48              2.01        192.67                53.51         0.531          pass              0.632             15.1                           0.257                1.53             -0.044                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-29T15:10:04.505433-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T15:05:04.399519-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T15:00:04.380256-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T14:55:04.522646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-29T14:50:04.497983-04:00       entry_1500              entry {"allocated_cash": 17325.0, "asset_type": "option", "contract_symbol": "FAST260918C00045000", "contracts": 45, "early_entry_score": 0.745, "entry_mode": "regular", "entry_option_price": 3.85, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 324.0, "option_spread_pct": 7.79, "option_volume": 33.0, "success_rate": 100.0, "ticker": "FAST", "timing_score": 0.573}
2026-07-29T14:50:04.497983-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-29", "training_samples": 5497, "window": 5}
2026-07-29T12:00:04.480323-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:55:04.538258-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:50:05.595902-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:45:05.536367-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730093001)

</details>

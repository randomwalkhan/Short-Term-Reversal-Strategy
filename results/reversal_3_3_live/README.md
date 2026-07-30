# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 09:50:01 EDT`
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

- Cash: `$17,629.75`
- Equity: `$33,604.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$-1,350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FAST     option         option FAST260918C00045000       2026-07-29                   1     45     17325.0                 15975.0         3.85           3.55       47.84         47.03          bid_ask_mid                       3.55                bid_ask_mid                    True         -1350.0                  -7.79         100.0               21              0.54         33.33           38.55                  27.18                 324.0           33.0               0.08                      ok
```

## Today's Closed Trades (2026-07-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           81.82               22            1.22              0.50         58.14                61.52         0.671          pass              0.293             32.4                           0.471                3.82              0.227                      ok            True                  False
   KDP           85.71               14            1.48              0.33         31.31                34.46         0.594          pass              0.270             10.6                           0.127                2.40              0.016                      ok            True                  False
   CSX           95.45               22            0.70              0.25         50.63                28.82         0.571          pass              0.577             13.4                           0.182                1.93              0.286                      ok            True                  False
  VRTX           84.62               13            1.65              5.57        480.94                33.19         0.570          pass              0.316             38.7                           0.275               -0.20             -0.020                      ok            True                  False
  MNST           94.12               17            1.06              0.72         96.92                25.74         0.556          pass              0.680             67.2                           0.469               -1.85             -0.262                      ok            True                  False
  BKNG           85.71               14            2.47              3.48        199.81                45.62         0.556          pass              0.252              5.9                           0.192               12.28              0.721                      ok            True                  False
  AMGN           91.67               12            1.65              4.48        385.72                27.22         0.555          pass              0.437             18.9                           0.196                7.32              0.718                      ok            True                  False
  ABNB           95.24               21            1.61              1.73        152.27                40.20         0.549          pass              0.644             38.5                           0.200                2.73              0.082                      ok            True                  False
  DASH           96.43               28            1.56              2.11        192.62                53.51         0.532          pass              0.677             34.6                           0.241                1.45             -0.048                      ok            True                  False
  IDXX           85.00               20            1.66              6.63        566.93                36.22         0.522          pass              0.282             10.0                           0.230                3.63             -0.011                      ok            True                  False
  GEHC           80.00                5            3.10              1.56         71.23                59.17         0.602          pass              0.110             16.5                           0.223               10.30              0.521                      ok           False                  False
  TMUS           77.78                9            2.24              2.85        180.30                56.22         0.591          pass              0.138             26.3                           0.322               -5.42             -0.971 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730095001)

</details>

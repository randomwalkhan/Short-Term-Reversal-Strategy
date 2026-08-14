# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-14 09:30:33 EDT`
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

- Cash: `$19,178.00`
- Equity: `$37,112.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$-931.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   BKR     option         option BKR260918C00065000       2026-08-13                   1     98     18865.0                 17934.0         1.92           1.83       63.47         63.57     last_price_stale                        NaN                unavailable                   False          -931.0                  -4.94         84.21               19              1.26         33.72            1.56                  33.24                2279.0           49.0               0.13                      ok
```

## Today's Closed Trades (2026-08-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.78               37            0.79              0.80        144.92               164.53         0.874          pass              0.547             59.5                           0.426               25.63              1.876                      ok            True                  False
  ALNY           83.87               31            1.10              1.75        226.37               128.90         0.835          pass              0.522             65.0                           0.387                9.30              0.518                      ok            True                  False
  SHOP           97.56               41            0.57              0.63        158.26                83.25         0.663          pass              0.917             83.7                           0.587               34.55              3.144                      ok            True                   True
  KLAC           83.33               36            0.75              1.10        208.90                69.66         0.614          pass              0.484             53.4                           0.377               13.66              1.318                      ok            True                  False
  PCAR          100.00               28            0.60              0.55        130.48                28.57         0.540          pass              0.740             55.4                           0.456               -1.81             -0.220                      ok            True                  False
  DASH          100.00               37            0.71              1.08        215.80                47.43         0.535          pass              0.634              0.0                           0.250                9.46              0.845                      ok            True                  False
  CSCO           89.47               38            0.59              0.47        113.27                42.49         0.520          pass              0.571             26.4                           0.268               -2.75             -0.158                      ok            True                  False
  AMGN          100.00               23            1.14              3.35        416.41                27.74         0.515          pass              0.549              3.6                           0.054                7.24              0.907                      ok            True                  False
  REGN           97.06               34            0.67              3.77        804.35                32.86         0.507          pass              0.639              9.4                           0.221                4.98              0.676                      ok            True                  False
  MNST           85.00               20            0.88              0.29         46.56               244.10         0.987          pass              0.367             22.6                           0.239              -52.62             -9.330 downtrend_blocked_slope           False                  False
  LRCX           88.89               36            0.49              1.16        336.51                86.66         0.706          pass              0.709             75.9                           0.471               14.45              1.199                      ok           False                  False
  ABNB           94.74               38            0.31              0.40        184.96                65.02         0.629          pass              0.871             76.1                           0.462               21.81              2.677                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-14T00:00:04.633795-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-13T15:10:04.909039-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:05:06.030850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T15:00:02.921317-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-08-13T14:55:04.897309-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-13", "training_samples": 5661, "window": 5}
2026-08-13T14:55:04.897309-04:00       entry_1500                   entry {"allocated_cash": 18865.0, "asset_type": "option", "contract_symbol": "BKR260918C00065000", "contracts": 98, "early_entry_score": 0.39, "entry_mode": "regular", "entry_option_price": 1.925, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2279.0, "option_spread_pct": 12.99, "option_volume": 49.0, "success_rate": 84.21, "ticker": "BKR", "timing_score": 0.546}
2026-08-13T14:55:04.897309-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                              {"early_entry_score": 0.522, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 5317.0, "option_spread_pct": 28.57, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.586}
2026-08-13T11:55:02.213370-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:53:25.963945-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:45:10.117918-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260814093033)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260814093033)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260814093033)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260814093033)

</details>

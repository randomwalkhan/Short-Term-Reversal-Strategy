# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 15:45:01 EDT`
Last processed slot: `manual`

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

- Cash: `$14,083.25`
- Equity: `$26,733.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$-575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ROST     option         option ROST260717C00240000       2026-06-15                   0     23     13225.0                 12650.0         5.75            5.5      236.66        236.45          bid_ask_mid                        5.5                bid_ask_mid                    True          -575.0                  -4.35         91.67               12              1.45         26.78           26.08                  38.75                 169.0           31.0               0.12                      ok
```

## Today's Closed Trades (2026-06-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           90.00               10            1.53              2.58        239.03                38.75         0.627          pass              0.372             14.2                           0.191                5.73              0.606                                 ok            True                  False
  AMGN           94.44               18            0.95              2.36        354.19                28.14         0.550          pass              0.568             24.9                           0.220                6.90              0.654                                 ok            True                  False
 CMCSA           80.00               15            1.41              0.24         24.40                24.55         0.525          pass              0.151             21.6                           0.440               -3.57             -0.131                                 ok            True                  False
  CPRT           84.62               13            2.13              0.46         30.55                31.00         0.522          pass              0.200              1.5                           0.273               -6.88             -0.229                                 ok            True                  False
  CTAS           95.45               22            1.30              1.61        175.59                29.28         0.511          pass              0.592             20.1                           0.204                0.62              0.225                                 ok            True                  False
   BKR           83.78               37            0.63              0.28         63.02                39.91         0.501          pass              0.560             76.4                           0.693               -0.37             -0.193                                 ok            True                  False
   KHC          100.00                3            1.29              0.22         24.30                26.17         0.655          pass              0.479              4.5                           0.210                3.73              0.772                                 ok           False                  False
   TRI           80.77               26            0.66              0.38         81.25                63.37         0.639          pass              0.283             30.8                           0.387              -13.93             -1.155 downtrend_blocked_slope_and_streak           False                  False
  WDAY           86.84               38            0.74              0.68        130.51                70.45         0.556          pass              0.591             55.6                           0.595              -17.43             -1.876 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.24               21            1.50              2.37        225.19                32.50         0.548          pass              0.565             12.4                           0.327               -4.67             -0.316            downtrend_blocked_slope           False                  False
   EXC           87.50               24            0.03              0.01         46.21                21.24         0.546          pass              0.642             98.1                           0.452                4.29              0.392                                 ok           False                  False
  MDLZ           66.67                3            2.21              0.97         62.57                19.17         0.528          pass              0.091             12.9                           0.360                0.90              0.341                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et       slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-15T15:10:06.131512-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:05:05.449965-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:00:05.161177-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:55:01.106139-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:50:01.113692-04:00 entry_1500          entry {"allocated_cash": 13225.0, "asset_type": "option", "contract_symbol": "ROST260717C00240000", "contracts": 23, "early_entry_score": 0.444, "entry_mode": "regular", "entry_option_price": 5.75, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.17, "option_volume": 31.0, "success_rate": 91.67, "ticker": "ROST", "timing_score": 0.621}
2026-06-15T14:50:01.113692-04:00 entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-15", "training_samples": 5261, "window": 5}
2026-06-12T15:10:11.830500-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:05:11.809096-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615154501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615154501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615154501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615154501)

</details>

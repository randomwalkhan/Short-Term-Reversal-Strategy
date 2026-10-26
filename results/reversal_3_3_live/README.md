# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 13:25:05 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$65,421.80`
- Equity: `$140,976.80`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$3,285.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 75555.0          1.1           1.15       44.42         44.38          bid_ask_mid                       1.15                bid_ask_mid                    True          3285.0                   4.55          80.0               15              0.97         20.09           22.44                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           89.29               28            0.58              0.10         24.76                34.81         0.543            pass              0.510             29.3                           0.355                9.82              1.087                      ok            True                  False
  CTSH          100.00               11            2.86              1.41         69.93                46.28         0.527            pass              0.500             13.7                           0.393               14.81              1.719                      ok            True                  False
  TEAM          100.00               17            2.69              4.29        225.77                47.89         0.505            pass              0.559             20.4                           0.332                6.61              0.979                      ok            True                  False
  TMUS           82.76               29            0.60              0.61        146.28                64.13         0.643            pass              0.464             66.6                           0.440               -4.09             -0.393 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.35              0.60         63.54                25.23         0.573            pass              0.312             18.2                           0.247                1.86              0.322                      ok           False                  False
   ADP           77.78                9            1.43              3.04        302.86                24.93         0.548            pass              0.069              4.8                           0.190                9.50              1.091                      ok           False                  False
   PEP           80.77               26            0.39              0.37        135.61                25.03         0.513            pass              0.232             17.7                           0.263                6.75              0.831                      ok           False                  False
  MSTR           88.89               27            2.40              2.46        144.96                68.80         0.502            pass              0.580             59.9                           0.683               -6.67             -0.351 downtrend_blocked_slope           False                  False
  VRTX           62.50                8            2.20              8.08        520.47                29.59         0.498 below_threshold              0.112             20.9                           0.255                1.06              0.603                      ok           False                  False
  AAPL           88.89               18            1.14              2.78        346.53                16.45         0.495 below_threshold              0.462             40.6                           0.414                0.82              0.147                      ok           False                  False
   XEL           88.89               27            0.43              0.23         77.95                17.66         0.492 below_threshold              0.494             31.6                           0.287                4.78              0.544                      ok           False                  False
 CMCSA          100.00                2            2.91              0.46         22.49                23.68         0.490 below_threshold              0.458              2.9                           0.198                6.53              0.857                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-26T12:00:05.800227-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:55:06.449404-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:50:05.011949-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:45:06.813895-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:40:04.884003-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:35:03.795292-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:30:06.493290-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:25:06.575832-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:20:06.988273-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:15:05.995279-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026132505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026132505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026132505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026132505)

</details>

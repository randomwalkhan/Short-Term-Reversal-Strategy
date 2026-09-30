# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 09:55:06 EDT`
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

- Cash: `$85,238.30`
- Equity: `$85,238.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261120C00155000     24          2026-09-29         2026-09-30         15.9        18.6 6480.0   16.981132 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  DRAM           83.33               30            1.06              0.46         61.09                54.99         0.583            pass              0.377             32.3                           0.270                9.60              0.602                  ok            True                  False
  META           83.87               31            0.81              4.19        736.99                54.80         0.559            pass              0.496             65.8                           0.688                8.92              0.954                  ok            True                  False
  ASML           81.82               33            0.55              7.05       1831.37                42.72         0.558            pass              0.373             38.6                           0.352               13.86              1.186                  ok            True                  False
  MRVL           80.65               31            1.65              3.04        261.97                56.16         0.521            pass              0.283             24.6                           0.232               12.72              0.973                  ok            True                  False
  PYPL           94.44               36            0.50              0.19         53.81                34.93         0.500            pass              0.685             25.4                           0.194                1.73              0.315                  ok            True                  False
  AMAT           82.93               41            0.03              0.11        511.96                51.71         0.566            pass              0.627             97.6                           0.646               23.22              2.022                  ok           False                  False
   WBD           95.24               42            0.06              0.01         30.84                37.86         0.557            pass              0.756             33.3                           0.207                9.83              1.040                  ok           False                  False
  MPWR           89.74               39            0.30              2.88       1352.75                52.13         0.543            pass              0.750             80.8                           0.448               17.62              1.652                  ok           False                  False
  ALNY           84.44               45            0.25              0.44        253.88                45.82         0.502            pass              0.603             78.1                           0.547                5.88              0.636                  ok           False                  False
  NXPI           85.71               35            0.49              0.81        236.12                39.17         0.499 below_threshold              0.624             84.9                           0.481                7.46              0.573                  ok           False                  False
  AVGO           87.50               40            0.02              0.05        355.08                31.31         0.494 below_threshold              0.730             93.5                           0.360                4.76              0.156                  ok           False                  False
   BKR           93.10               29            0.77              0.30         55.79                31.55         0.492 below_threshold              0.703             59.2                           0.496               -1.47             -0.115                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-30T09:50:05.025462-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "MSTR261120C00155000", "fill_price": 18.6, "pnl": 6480.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.98, "ticker": "MSTR"}
2026-09-30T00:00:05.973499-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {'saved': 92, 'empty': 1}
2026-09-29T15:10:01.396429-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-29T15:05:05.953732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-29T15:00:06.204288-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-29T14:55:06.447137-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-29T14:50:06.330440-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 38160.0, "asset_type": "option", "contract_symbol": "MSTR261120C00155000", "contracts": 24, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 15.9, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 1758.0, "option_spread_pct": 1.89, "option_volume": 230.0, "success_rate": 93.1, "ticker": "MSTR", "timing_score": 0.682}
2026-09-29T14:50:06.330440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-29", "training_samples": 5875, "window": 5}
2026-09-29T12:00:02.521898-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "entry_ask": 2.4, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 39379.15, "hypothetical_contracts": 173, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 10.99, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "matched_signals": 33, "recovery_stability_score": 0.603, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:55:06.341077-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "entry_ask": 2.35, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.25, "hypothetical_budget": 39379.15, "hypothetical_contracts": 175, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 8.89, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "matched_signals": 33, "recovery_stability_score": 0.577, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930095506)

</details>

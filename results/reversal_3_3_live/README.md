# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 10:10:04 EDT`
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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.29               35            0.73              0.80        156.80                99.69         0.716          pass              0.736             39.0                           0.191               20.37              2.190                       ok            True                  False
    ZS           97.37               38            0.97              1.35        198.81                81.58         0.593          pass              0.811             54.9                           0.481                1.84              0.351                       ok            True                  False
  CRWD           88.37               43            0.80              1.45        258.63                71.98         0.572          pass              0.603             40.8                           0.363                6.06              0.806                       ok            True                  False
   KDP           93.75               16            1.13              0.25         31.35                25.35         0.511          pass              0.646             62.6                           0.465               -0.51              0.037                       ok            True                  False
   WBD           95.00               40            0.13              0.03         30.89                38.06         0.576          pass              0.855             65.8                           0.425               10.10              1.216                       ok           False                  False
   TRI           88.24               34            0.82              0.56         97.09                56.59         0.575          pass              0.615             59.2                           0.697               -5.92             -0.298  downtrend_blocked_slope           False                  False
  AMGN           87.18               39            0.14              0.42        417.95                46.33         0.571          pass              0.703             87.1                           0.565               11.15              1.226                       ok           False                  False
   STX           88.57               35            0.33              2.16        920.58                53.46         0.543          pass              0.689             79.7                           0.581               19.09              1.897                       ok           False                  False
  PANW           63.16               19            3.08              8.46        388.46                69.78         0.524          pass              0.156             14.4                           0.215                1.31              0.391                       ok           False                  False
  TMUS           85.19               27            0.90              1.05        166.00                33.31         0.521          pass              0.444             46.8                           0.598               -8.60             -0.662  downtrend_blocked_slope           False                  False
  CDNS           61.54               13            2.53              5.78        324.22                46.51         0.513          pass              0.176             35.0                           0.466               16.24              1.933                       ok           False                  False
  WDAY           91.67               36            0.71              0.93        188.20                45.46         0.500          pass              0.709             58.3                           0.486               -1.78             -0.229 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-29T10:10:04.385907-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:05:05.319599-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00      manage_1000               exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 18.05, "pnl": 8760.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.35, "ticker": "CEG"}
2026-09-29T00:00:05.209830-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-28T15:10:04.000540-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-28T15:05:05.114052-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-28T15:00:06.099119-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-28T14:55:04.074412-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-28T14:50:04.136803-04:00       entry_1500              entry {"allocated_cash": 34560.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 24, "early_entry_score": 0.63, "entry_mode": "regular", "entry_option_price": 14.4, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 366.0, "option_spread_pct": 4.17, "option_volume": 20.0, "success_rate": 89.66, "ticker": "CEG", "timing_score": 0.542}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929101004)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 10:15:06 EDT`
Last processed slot: `early_entry_1015`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.29               35            0.83              0.91        156.75                99.69         0.710            pass              0.709             30.3                           0.160               20.24              2.186                      ok            True                  False
    ZS           97.50               40            0.81              1.13        198.91                81.58         0.591            pass              0.846             62.3                           0.534                2.00              0.358                      ok            True                  False
   STX           88.24               34            0.53              3.44        920.03                53.46         0.536            pass              0.636             67.6                           0.505               18.85              1.888                      ok            True                  False
  CRWD           89.13               46            0.08              0.14        259.19                71.98         0.602            pass              0.787             94.3                           0.745                6.83              0.839                      ok           False                  False
   TRI           88.24               34            0.80              0.55         97.10                56.59         0.576            pass              0.617             60.0                           0.702               -5.91             -0.297 downtrend_blocked_slope           False                  False
   WBD           95.00               40            0.15              0.03         30.89                38.06         0.574            pass              0.842             61.5                           0.414               10.08              1.215                      ok           False                  False
  TMUS           85.71               28            0.62              0.72        166.14                33.31         0.536            pass              0.517             63.5                           0.717               -8.34             -0.649 downtrend_blocked_slope           False                  False
  PANW           68.18               22            2.96              8.11        388.61                69.78         0.519            pass              0.186             17.9                           0.258                1.44              0.397                      ok           False                  False
  CDNS           70.59               17            2.34              5.35        324.41                46.51         0.509            pass              0.217             39.8                           0.565               16.46              1.942                      ok           False                  False
  ALNY           82.50               40            0.78              1.39        254.76                45.92         0.497 below_threshold              0.398             27.3                           0.288                6.34              0.711                      ok           False                  False
  PYPL           91.89               37            0.35              0.13         54.22                35.54         0.496 below_threshold              0.725             59.6                           0.570                0.52              0.241                      ok           False                  False
   KDP           95.45               22            0.86              0.19         31.38                25.35         0.495 below_threshold              0.744             71.6                           0.494               -0.23              0.050                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-09-29T10:15:06.005082-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:10:04.385907-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:05:05.319599-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:00:05.690737-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 18.05, "pnl": 8760.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.35, "ticker": "CEG"}
2026-09-29T00:00:05.209830-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-28T15:10:04.000540-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-09-28T15:05:05.114052-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-09-28T15:00:06.099119-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-09-28T14:55:04.074412-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929101506)

</details>

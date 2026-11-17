# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:35:06 EST`
Last processed slot: `manage_1030`

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

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           80.00               15            1.43              4.83        481.65                41.88         0.613          pass              0.186             30.5                           0.568                0.69             -0.078                                 ok            True                  False
 GOOGL           82.14               28            0.69              1.37        283.13                55.10         0.612          pass              0.338             33.2                           0.301                0.62              0.190                                 ok            True                  False
  GOOG           82.76               29            0.75              1.48        280.63                53.19         0.596          pass              0.358             32.6                           0.289                0.32              0.126                                 ok            True                  False
  QCOM           84.00               25            1.80              2.12        167.61                68.75         0.585          pass              0.306             13.7                           0.220                0.64              0.342                                 ok            True                  False
   CSX           83.33               18            1.17              0.43         51.85                34.26         0.585          pass              0.225              8.3                           0.158                1.38              0.268                                 ok            True                  False
   KDP           96.55               29            0.51              0.13         35.53                46.38         0.580          pass              0.743             52.6                           0.275                1.90             -0.106                                 ok            True                  False
   CEG           90.62               32            1.21              2.34        276.82                60.48         0.575          pass              0.602             38.1                           0.337                4.36              1.290                                 ok            True                  False
  VRSK           80.00               20            1.60              2.39        211.74                44.55         0.572          pass              0.230             35.4                           0.592                6.27              0.532                                 ok            True                  False
   ADP           86.36               22            0.92              2.03        312.56                28.40         0.552          pass              0.426             40.3                           0.586                4.91              0.399                                 ok            True                  False
  META           83.87               31            0.70              3.07        625.09                41.97         0.539          pass              0.441             47.9                           0.419                0.16              0.168                                 ok            True                  False
  SOXL           61.54               26            3.22              1.10         48.29               265.45         0.927          pass              0.272             24.2                           0.177              -35.46             -1.368 downtrend_blocked_slope_and_streak           False                  False
  INTC           66.67               27            2.35              0.91         55.05               143.34         0.809          pass              0.319             41.7                           0.370              -10.59             -0.127           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-11-17T10:35:06.835467-05:00 early_entry_1035 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:30:03.912380-05:00 early_entry_1030 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:25:05.911595-05:00 early_entry_1025 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:20:06.716157-05:00 early_entry_1020 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:15:04.834585-05:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:05:06.251834-05:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:00:06.465677-05:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T09:50:06.673535-05:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "QCOM261218C00170000", "fill_price": 10.0125, "pnl": -5785.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "QCOM"}
2026-11-17T00:00:04.730535-05:00     data_refresh       data_refresh                                                                                                                                                           {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117103506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117103506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117103506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117103506)

</details>

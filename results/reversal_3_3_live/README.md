# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:20:06 EST`
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
  FTNT           82.93               41            0.82              0.70        122.97                92.89         0.669          pass              0.481             45.4                           0.315               -4.56             -0.088                                 ok            True                  False
   ROP           81.25               16            1.35              4.56        481.77                41.88         0.613          pass              0.238             34.4                           0.542                0.77             -0.074                                 ok            True                  False
  QCOM           86.67               30            1.22              1.43        167.91                68.75         0.593          pass              0.495             41.6                           0.304                1.24              0.369                                 ok            True                  False
   KDP           96.15               26            0.66              0.16         35.51                46.38         0.588          pass              0.680             38.2                           0.248                1.74             -0.113                                 ok            True                  False
   CSX           83.33               18            1.24              0.45         51.84                34.26         0.580          pass              0.209              3.0                           0.161                1.31              0.265                                 ok            True                  False
   CEG           90.62               32            1.42              2.76        276.64                60.48         0.561          pass              0.567             27.0                           0.234                4.13              1.280                                 ok            True                  False
   ADP           86.96               23            0.83              1.82        312.65                28.40         0.552          pass              0.467             46.4                           0.639                5.01              0.403                                 ok            True                  False
  SOXL           70.59               34            0.64              0.22         48.67               265.45         0.956          pass              0.510             84.8                           0.376              -33.74             -1.249 downtrend_blocked_slope_and_streak           False                  False
  INTC           70.59               34            1.17              0.45         55.25               143.34         0.831          pass              0.456             71.0                           0.656               -9.50             -0.072           downtrend_blocked_streak           False                  False
   APP           87.50                8            3.94             11.45        410.31               119.50         0.787          pass              0.283              1.4                           0.048               62.47              4.126                                 ok           False                  False
  ALNY           73.33               30            1.68              1.88        158.92               110.59         0.741          pass              0.264             18.9                           0.269               -1.78              0.057                                 ok           False                  False
  DRAM           58.33               24            2.10              0.58         39.02               109.09         0.711          pass              0.224             19.9                           0.240              -19.30             -0.852 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-11-17T10:20:06.716157-05:00 early_entry_1020 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:15:04.834585-05:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:05:06.251834-05:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:00:06.465677-05:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T09:50:06.673535-05:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "QCOM261218C00170000", "fill_price": 10.0125, "pnl": -5785.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "QCOM"}
2026-11-17T00:00:04.730535-05:00     data_refresh       data_refresh                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117102006)

</details>

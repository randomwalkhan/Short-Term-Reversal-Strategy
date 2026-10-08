# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 10:50:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            4.07              4.53        156.97               112.38         0.591          pass              0.357             48.3                           0.504                4.18              1.047                                 ok            True                  False
  MPWR           88.00               25            1.56             15.58       1419.30                55.22         0.573          pass              0.524             51.0                           0.547                5.26              0.854                                 ok            True                  False
  MSTR           92.11               38            0.22              0.23        153.27                80.80         0.651          pass              0.857             94.1                           0.917               -5.30             -0.093           downtrend_blocked_streak           False                  False
  QCOM           87.50               24            1.69              2.09        176.22                56.66         0.585          pass              0.457             35.0                           0.443              -10.36             -1.099 downtrend_blocked_slope_and_streak           False                  False
  CSCO           88.89               27            0.46              0.38        117.23                34.80         0.566          pass              0.590             60.9                           0.588                9.66              1.209                                 ok           False                  False
   WDC           82.22               45            0.07              0.19        405.34                65.89         0.545          pass              0.604             96.9                           0.674              -10.03             -1.311            downtrend_blocked_slope           False                  False
   STX           88.00               25            2.49             14.09        801.53                69.74         0.543          pass              0.421             17.6                           0.197              -13.08             -1.594            downtrend_blocked_slope           False                  False
 CMCSA           87.50               16            0.50              0.07         20.91                21.76         0.531          pass              0.432             46.2                           0.289               -4.39             -0.352            downtrend_blocked_slope           False                  False
  REGN           83.33                6            2.17             11.27        737.29                27.38         0.519          pass              0.179             12.9                           0.268               -8.79             -0.773            downtrend_blocked_slope           False                  False
   CEG           88.89               45            0.09              0.19        299.51                58.54         0.516          pass              0.774             95.1                           0.457               14.41              1.504                                 ok           False                  False
  INTC           82.61               23            3.02              2.39        112.09                69.90         0.513          pass              0.283             25.2                           0.278              -13.89             -1.071 downtrend_blocked_slope_and_streak           False                  False
  AMAT           82.93               41            0.23              0.85        520.29                48.66         0.510          pass              0.606             92.5                           0.768                9.53              1.059                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-10-08T10:50:05.913383-04:00 early_entry_1050 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:45:06.914386-04:00 early_entry_1045 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:40:05.011138-04:00 early_entry_1040 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "ABNB261120C00160000", "fill_price": 11.05, "pnl": 8662.5, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.62, "ticker": "ABNB"}
2026-10-08T10:30:06.096812-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:25:06.880454-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:20:05.114713-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:15:04.991008-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:10:05.110275-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008105005)

</details>

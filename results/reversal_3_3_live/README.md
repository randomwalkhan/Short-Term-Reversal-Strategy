# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:50:06 EST`
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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           90.00               20            1.94              3.43        250.29                49.35         0.514          pass              0.488             34.6                           0.269               -0.57             -0.353                                 ok            True                  False
  INTC           60.00               25            2.58              1.01         55.29               141.91         0.771          pass              0.346             56.4                           0.320               -3.55             -0.879 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.60             14.87        372.65               122.37         0.717          pass              0.519             15.7                           0.216               -8.55             -0.702 downtrend_blocked_slope_and_streak           False                  False
  FTNT           68.42               19            2.56              2.35        130.45                96.17         0.667          pass              0.198             23.6                           0.267                7.79              0.678                                 ok           False                  False
  UPRO           80.00                5            3.14              2.59        116.78                72.20         0.586          pass              0.124             21.9                           0.178              -11.44             -1.621 downtrend_blocked_slope_and_streak           False                  False
   BKR           69.23               13            2.11              0.69         46.37                56.86         0.584          pass              0.143             21.4                           0.161               -4.11             -0.427 downtrend_blocked_slope_and_streak           False                  False
  QCOM           83.33               24            1.91              2.16        161.08                69.46         0.571          pass              0.339             33.1                           0.217               -3.92             -0.763 downtrend_blocked_slope_and_streak           False                  False
  MCHP           75.00               16            3.01              1.23         57.94                78.21         0.566          pass              0.182             28.5                           0.249               -2.81             -0.476            downtrend_blocked_slope           False                  False
   TXN          100.00                2            4.08              8.16        282.25                59.73         0.550          pass              0.514             19.8                           0.215               -1.18             -0.392                                 ok           False                  False
  CSCO           72.73               22            1.28              0.85         94.34                50.60         0.550          pass              0.237             33.9                           0.209               -0.38             -0.367                                 ok           False                  False
   ADI          100.00                5            4.23             11.17        372.65                64.58         0.544          pass              0.515             20.2                           0.219               -0.57             -0.444                                 ok           False                  False
  ISRG           89.47               38            0.44              1.25        406.70                45.14         0.509          pass              0.595             35.0                           0.265              -10.46             -1.215 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                           detail
2026-11-20T10:50:06.269299-05:00 early_entry_1050 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:45:05.890117-05:00 early_entry_1045 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:40:06.786688-05:00 early_entry_1040 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:35:04.912768-05:00 early_entry_1035 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:30:06.085636-05:00 early_entry_1030 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:25:04.965468-05:00 early_entry_1025 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:10:04.986532-05:00 early_entry_1010 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120105006)

</details>

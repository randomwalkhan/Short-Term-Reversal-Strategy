# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 12:25:05 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$122,431.80`
- Equity: `$122,431.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CEG     option         option CEG261120C00270000     33          2026-10-15         2026-10-16         19.1       17.19 -6303.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.11               36            0.65              1.25        274.47                60.14         0.539            pass              0.562             57.4                           0.345                6.11              0.177                                 ok            True                  False
  UPRO           93.33               15            1.70              1.80        150.75                28.58         0.507            pass              0.495             18.4                           0.300               -1.28             -0.206                                 ok            True                  False
  MSFT          100.00               10            1.90              7.18        536.36                21.00         0.501            pass              0.491             13.7                           0.323                2.25              0.299                                 ok            True                  False
  META           72.73               11            2.28             11.77        731.67                55.08         0.578            pass              0.089              8.2                           0.303               -1.12              0.047                                 ok           False                  False
  PAYX           79.41               34            0.52              0.41        110.61                41.26         0.552            pass              0.256             13.4                           0.147               11.38              1.146                                 ok           False                  False
  QCOM           85.71               28            1.17              1.46        177.78                54.84         0.549            pass              0.509             60.5                           0.566               -4.62             -0.404 downtrend_blocked_slope_and_streak           False                  False
  CSCO           81.82               11            1.75              1.34        109.27                35.07         0.538            pass              0.160             16.9                           0.266               -3.81             -0.407 downtrend_blocked_slope_and_streak           False                  False
  SNPS           66.67                6            3.41             11.16        463.33                53.97         0.533            pass              0.113             20.0                           0.497               -7.70             -0.680 downtrend_blocked_slope_and_streak           False                  False
  MPWR           79.31               29            0.99              8.64       1245.50                56.34         0.531            pass              0.392             70.6                           0.547              -14.09             -1.946            downtrend_blocked_slope           False                  False
  SHOP           85.19               27            1.43              1.79        177.37                48.01         0.495 below_threshold              0.416             38.4                           0.472               15.99              1.382                                 ok           False                  False
  DASH           87.18               39            0.77              1.04        192.61                48.67         0.493 below_threshold              0.498             21.3                           0.241                1.28             -0.027                                 ok           False                  False
  CTSH           94.44               36            0.71              0.33         65.63                43.59         0.490 below_threshold              0.736             42.9                           0.460               11.61              1.311                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-10-16T12:00:06.321774-04:00 early_entry_1200 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:55:06.475716-04:00 early_entry_1155 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:50:05.492018-04:00 early_entry_1150 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:45:05.286618-04:00 early_entry_1145 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:40:05.599147-04:00 early_entry_1140 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:40:05.599147-04:00      manage_1130               exit {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 17.19, "pnl": -6303.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CEG"}
2026-10-16T11:35:05.403603-04:00 early_entry_1135 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:30:05.425810-04:00 early_entry_1130 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:25:04.296462-04:00 early_entry_1125 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:20:05.272593-04:00 early_entry_1120 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016122505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016122505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016122505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016122505)

</details>

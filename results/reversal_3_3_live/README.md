# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 13:10:05 EDT`
Last processed slot: `manage_1300`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               21            1.73              3.34        273.57                60.14         0.561          pass              0.296              4.8                           0.138                4.95              0.127                                 ok            True                  False
  ABNB           90.62               32            0.90              1.10        173.81                41.32         0.525          pass              0.509              8.7                           0.191                6.33              0.666                                 ok            True                  False
  CTSH           92.31               26            1.44              0.66         65.49                43.59         0.500          pass              0.530             14.9                           0.215               10.79              1.278                                 ok            True                  False
  QCOM           84.62               26            1.28              1.60        177.71                54.84         0.553          pass              0.455             56.5                           0.503               -4.74             -0.410 downtrend_blocked_slope_and_streak           False                  False
  PAYX           78.12               32            0.67              0.52        110.56                41.26         0.552          pass              0.240             12.9                           0.275               11.21              1.139                                 ok           False                  False
  CSCO           75.00                8            1.93              1.48        109.21                35.07         0.539          pass              0.079              8.2                           0.159               -3.98             -0.416 downtrend_blocked_slope_and_streak           False                  False
  MPWR           78.26               23            1.62             14.13       1243.14                56.34         0.529          pass              0.295             51.9                           0.319              -14.64             -1.975            downtrend_blocked_slope           False                  False
  SNPS           60.00                5            3.55             11.63        463.13                53.97         0.525          pass              0.102             16.6                           0.315               -7.84             -0.687 downtrend_blocked_slope_and_streak           False                  False
  META           57.14                7            3.24             16.70        729.56                55.08         0.525          pass              0.055              0.8                           0.092               -2.09              0.002           downtrend_blocked_streak           False                  False
  CDNS           78.95               19            1.65              3.75        322.77                38.31         0.503          pass              0.200             29.8                           0.300               -9.20             -1.106 downtrend_blocked_slope_and_streak           False                  False
  MELI           72.22               18            1.90             24.76       1846.37                40.67         0.503          pass              0.112              2.7                           0.168                7.37              0.309                                 ok           False                  False
  UPRO          100.00                2            3.10              3.28        150.11                28.58         0.501          pass              0.462              4.0                           0.165               -2.68             -0.271            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016131005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016131005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016131005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016131005)

</details>

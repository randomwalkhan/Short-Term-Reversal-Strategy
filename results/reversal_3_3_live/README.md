# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:30:04 EDT`
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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               21            1.25              1.00        113.96                33.31         0.548          pass              0.591             21.0                           0.368                7.18              0.800                  ok            True                  False
   ROP           89.47               19            1.43              3.64        361.58                31.85         0.534          pass              0.474             35.9                           0.534               -1.48             -0.057                  ok            True                  False
   WBD           92.00               25            0.52              0.10         26.83                20.40         0.531          pass              0.633             53.3                           0.660                2.34              0.397                  ok            True                  False
  GILD           92.86               28            0.55              0.52        134.06                34.72         0.517          pass              0.613             32.7                           0.304                3.03              0.048                  ok            True                  False
   ADP           95.00               20            1.31              2.35        254.26                34.14         0.517          pass              0.582             21.2                           0.326                5.19              0.600                  ok            True                  False
  MNST          100.00               25            0.57              0.39         97.33                20.09         0.514          pass              0.763             70.5                           0.364               -0.44              0.160                  ok            True                  False
   CSX           91.67               24            0.54              0.19         50.67                17.40         0.510          pass              0.575             39.7                           0.257                3.41              0.449                  ok            True                  False
  ORLY           83.87               31            1.08              0.65         85.77                41.23         0.507          pass              0.407             37.6                           0.495                1.04              0.005                  ok            True                  False
  BKNG           85.00               20            1.98              2.52        180.60                41.44         0.503          pass              0.300             16.7                           0.242               -1.63              0.132                  ok            True                  False
  ABNB           97.06               34            0.66              0.67        145.69                32.96         0.500          pass              0.727             38.9                           0.353               -1.78             -0.055                  ok            True                  False
  PYPL           77.78               18            1.42              0.56         56.32                61.55         0.653          pass              0.230             37.1                           0.415               23.65              2.794                  ok           False                  False
  AAPL          100.00                4            2.06              4.80        331.68                36.42         0.630          pass              0.493             10.1                           0.161                4.55              0.693                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-20T10:30:04.102843-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:25:04.012806-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:20:01.111901-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "TXN260821C00290000", "fill_price": 23.275, "pnl": 2187.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.51, "ticker": "TXN"}
2026-07-20T10:05:02.132166-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:00:05.019489-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T03:00:02.156318-04:00     data_refresh       data_refresh                                                                                                                                                                          {'saved': 93}
2026-07-18T02:55:03.939140-04:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720103004)

</details>

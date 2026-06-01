# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 15:10:04 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01        28.30       25.47 -1415.0       -10.0        stop_loss_hit_at_scan
  SNPS     option         option SNPS260717C00470000      4          2026-05-29         2026-06-01        35.25       42.30  2820.0        20.0 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   HON           84.21               19            0.91              1.51        237.21                24.41         0.524            pass              0.399             58.1                           0.573               10.53              1.124                                 ok            True                  False
  AAPL           93.33               15            1.33              2.90        310.82                17.18         0.518            pass              0.564             41.1                           0.544                2.56              0.466                                 ok            True                  False
  INSM           67.74               31            1.57              1.18        106.41               110.85         0.731            pass              0.390             59.1                           0.688               -3.58             -0.181                                 ok           False                  False
   WMT           75.00               12            1.43              1.16        115.25                32.67         0.560            pass              0.142             24.2                           0.264              -13.21             -1.689 downtrend_blocked_slope_and_streak           False                  False
  REGN           72.73               11            2.21              9.53        610.70                42.14         0.548            pass              0.075              4.4                           0.196              -13.77             -0.864 downtrend_blocked_slope_and_streak           False                  False
  LRCX           92.31               39            0.20              0.46        317.98                55.15         0.545            pass              0.859             94.2                           0.571               11.52              1.619                                 ok           False                  False
   AEP           60.00                5            1.93              1.71        125.94                24.34         0.531            pass              0.082              9.6                           0.286               -0.74             -0.068                                 ok           False                  False
  COST           55.56                9            1.39              9.30        952.33                27.93         0.529            pass              0.152             32.9                           0.305              -10.10             -1.338 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               11            1.77              1.78        143.43                22.18         0.526            pass              0.365              5.0                           0.218               -5.01             -0.468            downtrend_blocked_slope           False                  False
  AMGN           66.67                3            2.21              5.20        334.56                25.52         0.520            pass              0.138             28.8                           0.455                0.93              0.246                                 ok           False                  False
  ISRG           81.82               11            2.68              7.98        421.22                37.20         0.503            pass              0.139             11.2                           0.153               -1.87             -0.462 downtrend_blocked_slope_and_streak           False                  False
  ROST           50.00                2            3.41              5.53        229.36                40.27         0.495 below_threshold              0.058              2.7                           0.218                5.21              0.947                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:50:02.013615-04:00 early_entry_1150  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601151004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601151004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601151004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601151004)

</details>

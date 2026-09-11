# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:20:04 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           87.80               41            0.86              1.26        208.32                89.85         0.652          pass              0.565             30.4                           0.266               -9.17             -0.889            downtrend_blocked_slope           False                  False
  AMGN          100.00               24            0.69              1.84        381.68                44.93         0.618          pass              0.667             37.3                           0.297              -13.08             -1.549 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               19            0.16              0.03         24.38                28.75         0.599          pass              0.770             83.3                           0.600               -1.55             -0.352            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.33              0.33        140.42                68.52         0.542          pass              0.779             81.6                           0.452               -5.55             -0.983            downtrend_blocked_slope           False                  False
  PANW           75.76               33            1.62              3.84        336.84                67.54         0.539          pass              0.272             21.5                           0.309              -13.02             -1.449            downtrend_blocked_slope           False                  False
  TEAM           93.94               33            1.43              1.80        178.80                63.98         0.533          pass              0.600              7.2                           0.143               -4.64             -0.762            downtrend_blocked_slope           False                  False
   EXC           95.65               23            0.08              0.02         43.38                15.10         0.531          pass              0.812             90.8                           0.383               -0.44              0.018                                 ok           False                  False
 CMCSA           93.94               33            0.16              0.03         25.16                36.51         0.525          pass              0.807             76.5                           0.429               -4.85             -0.714 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.97               33            0.96              1.68        248.11                48.95         0.513          pass              0.841             78.8                           0.605              -14.77             -1.918 downtrend_blocked_slope_and_streak           False                  False
  WDAY           95.24               42            0.32              0.41        184.91                76.08         0.507          pass              0.769             39.4                           0.241               -4.69             -0.885 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               22            1.11              6.17        790.61                28.70         0.504          pass              0.582             17.2                           0.169               -2.88             -0.164           downtrend_blocked_streak           False                  False
   WDC           82.35               34            1.43              4.61        458.95                66.80         0.504          pass              0.412             46.2                           0.361               -1.63              0.268           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
2026-09-11T10:00:03.674225-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-09-10T15:10:03.185946-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T15:05:01.362764-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-09-10T15:00:04.389376-04:00       entry_1500       slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911102004)

</details>

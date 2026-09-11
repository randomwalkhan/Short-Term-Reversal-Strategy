# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 10:35:04 EDT`
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
  CRWD           87.50               40            0.90              1.32        208.30                89.85         0.655          pass              0.547             27.1                           0.154               -9.20             -0.891            downtrend_blocked_slope           False                  False
  AMGN          100.00               16            1.07              2.87        381.24                44.93         0.642          pass              0.511              2.4                           0.102              -13.41             -1.566 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               18            0.27              0.05         24.37                28.75         0.599          pass              0.732             72.9                           0.692               -1.66             -0.357            downtrend_blocked_slope           False                  False
   PEP           90.00               20            0.17              0.16        136.58                17.04         0.565          pass              0.452             20.7                           0.252               -1.32             -0.188                                 ok           False                  False
  CHTR           90.48               42            0.14              0.14        140.50                68.52         0.555          pass              0.811             92.2                           0.654               -5.37             -0.974            downtrend_blocked_slope           False                  False
   EXC           94.44               18            0.25              0.08         43.36                15.10         0.550          pass              0.707             71.1                           0.329               -0.61              0.010                                 ok           False                  False
  REGN          100.00               12            1.54              8.55        789.60                28.70         0.539          pass              0.467              0.0                           0.197               -3.30             -0.184           downtrend_blocked_streak           False                  False
  TEAM           94.74               38            0.89              1.11        179.09                63.98         0.536          pass              0.763             43.2                           0.303               -4.12             -0.736            downtrend_blocked_slope           False                  False
  PANW           75.76               33            1.66              3.93        336.80                67.54         0.536          pass              0.266             19.6                           0.162              -13.05             -1.451            downtrend_blocked_slope           False                  False
  LRCX           83.33               42            0.04              0.09        297.97                53.83         0.527          pass              0.630             96.2                           0.688               -6.50              0.013           downtrend_blocked_streak           False                  False
  ADSK           90.00               40            0.33              0.48        211.40                52.16         0.519          pass              0.738             73.2                           0.402              -22.05             -2.877 downtrend_blocked_slope_and_streak           False                  False
   WDC           80.65               31            1.58              5.10        458.74                66.80         0.511          pass              0.330             40.4                           0.491               -1.78              0.261           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-09-11T10:35:04.843069-04:00 early_entry_1035 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:30:01.845613-04:00 early_entry_1030 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:25:04.822765-04:00 early_entry_1025 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:20:04.731608-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:15:01.602754-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:10:01.770369-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T10:05:03.681403-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261016C00130000", "fill_price": 13.65, "pnl": 6375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.44, "ticker": "MSTR"}
2026-09-11T10:00:03.674225-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T00:00:04.449434-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911103504)

</details>

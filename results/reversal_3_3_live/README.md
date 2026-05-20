# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 12:15:04 EDT`
Last processed slot: `manual`

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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  FTNT     option         option FTNT260717C00125000     14          2026-05-20         2026-05-20        8.825       10.15 1855.0   15.014164 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.75               32            0.55              1.17        301.81                69.06         0.621            pass              0.833             86.0                           0.622                3.87              0.572                                 ok            True                   True
  ADSK           90.91               22            1.35              2.30        243.17                38.52         0.511            pass              0.632             70.0                           0.533               -0.91             -0.154                                 ok            True                  False
  CTSH           88.89               27            1.04              0.37         50.72                50.98         0.511            pass              0.620             72.9                           0.705               -1.22             -0.213                                 ok            True                  False
  TEAM           88.24               34            1.78              1.08         86.16               114.61         0.619            pass              0.637             65.2                           0.633               -4.19             -0.536 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.45               22            0.13              0.08         94.44                29.36         0.566            pass              0.825             96.0                           0.780                4.59              0.250                                 ok           False                  False
   KDP           88.89               36            0.29              0.06         28.82                34.80         0.502            pass              0.712             83.8                           0.454                0.72              0.142                                 ok           False                  False
 GOOGL           88.89               36            0.52              1.42        387.05                41.27         0.499 below_threshold              0.632             57.4                           0.452               -3.12             -0.197                                 ok           False                  False
   WMT           90.48               21            0.89              0.84        133.84                20.68         0.497 below_threshold              0.623             73.5                           0.649                2.44              0.356                                 ok           False                  False
  TMUS           82.61               23            1.53              2.07        192.53                36.70         0.489 below_threshold              0.315             36.5                           0.509               -1.40             -0.200                                 ok           False                  False
  SNPS           97.14               35            0.70              2.43        492.83                41.71         0.488 below_threshold              0.864             82.7                           0.541               -2.78             -0.362 downtrend_blocked_slope_and_streak           False                  False
   TRI           75.00               12            2.62              1.60         86.66                57.28         0.485 below_threshold              0.195             44.5                           0.376               -7.29             -0.902 downtrend_blocked_slope_and_streak           False                  False
  GOOG           89.19               37            0.56              1.50        384.25                41.08         0.478 below_threshold              0.641             56.0                           0.464               -3.14             -0.207           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-20T12:00:03.589849-04:00 early_entry_1200 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:55:04.978899-04:00 early_entry_1155 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:50:01.042142-04:00 early_entry_1150 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00 early_entry_1140 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "FTNT260717C00125000", "fill_price": 10.15, "pnl": 1855.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.01, "ticker": "FTNT"}
2026-05-20T11:35:01.033169-04:00 early_entry_1135 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:30:01.977277-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:25:06.020090-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520121504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520121504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520121504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520121504)

</details>

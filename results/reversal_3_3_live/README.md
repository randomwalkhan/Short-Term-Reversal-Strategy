# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:50:01 EDT`
Last processed slot: `manage_1200`

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
  CTSH           88.00               25            1.20              0.43         50.70                50.98         0.513            pass              0.571             68.8                           0.632               -1.37             -0.221                                 ok            True                  False
   WMT           90.00               20            0.90              0.85        133.84                20.68         0.503            pass              0.603             73.3                           0.735                2.43              0.355                                 ok            True                  False
   TXN           93.75               32            0.45              0.96        301.90                69.06         0.627            pass              0.842             88.5                           0.491                3.97              0.576                                 ok           False                  False
  TEAM           87.88               33            1.98              1.20         86.11               114.61         0.612            pass              0.608             61.2                           0.492               -4.39             -0.545 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.24               21            0.35              0.23         94.38                29.36         0.558            pass              0.796             89.0                           0.686                4.35              0.240                                 ok           False                  False
  TMUS           76.92               13            2.18              2.95        192.15                36.70         0.507            pass              0.099              9.4                           0.269               -2.05             -0.230                                 ok           False                  False
  SNPS           97.14               35            0.55              1.90        493.05                41.71         0.498 below_threshold              0.876             86.4                           0.628               -2.63             -0.355 downtrend_blocked_slope_and_streak           False                  False
  ADSK           88.46               26            1.16              1.98        243.31                38.52         0.493 below_threshold              0.604             74.2                           0.655               -0.72             -0.145                                 ok           False                  False
   ADP           93.75               32            0.60              0.92        220.04                38.42         0.480 below_threshold              0.832             90.1                           0.653                5.75              0.485                                 ok           False                   True
   TRI           75.00               12            2.70              1.65         86.64                57.28         0.480 below_threshold              0.190             42.9                           0.396               -7.36             -0.905 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.70               43            0.18              0.50        387.45                41.27         0.476 below_threshold              0.788             85.1                           0.732               -2.79             -0.181                                 ok           False                  False
  CTAS           89.66               29            0.79              0.95        171.79                24.66         0.474 below_threshold              0.599             55.8                           0.560                1.15              0.283                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-20T11:50:01.042142-04:00 early_entry_1150 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00 early_entry_1140 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "FTNT260717C00125000", "fill_price": 10.15, "pnl": 1855.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.01, "ticker": "FTNT"}
2026-05-20T11:35:01.033169-04:00 early_entry_1135 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:30:01.977277-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:25:06.020090-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:15:01.033814-04:00 early_entry_1115 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520115001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520115001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520115001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520115001)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 13:40:04 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           80.00               30            0.68              8.86       1856.06                40.48         0.547            pass              0.318             43.3                           0.395                5.68              0.790                                 ok            True                  False
  DRAM           84.00               25            2.23              0.96         61.26                49.40         0.524            pass              0.293             11.3                           0.356               -5.23             -0.197                                 ok            True                  False
  ABNB           81.82               11            2.68              3.08        162.75                40.56         0.517            pass              0.143             12.0                           0.361               -1.32              0.528                                 ok            True                  False
  MSTR           92.31               39            0.07              0.08        164.39                79.08         0.639            pass              0.857             90.6                           0.493               -1.80             -0.062           downtrend_blocked_streak           False                  False
  MPWR           90.24               41            0.07              0.72       1479.58                53.63         0.560            pass              0.819             96.6                           0.715                7.27              0.845                                 ok           False                  False
  INTC           88.57               35            1.63              1.32        115.62                74.54         0.544            pass              0.572             40.9                           0.445               -7.72             -0.751 downtrend_blocked_slope_and_streak           False                  False
    MU           92.68               41            0.02              0.12       1063.91                46.96         0.530            pass              0.888             99.0                           0.587               -2.95             -0.143                                 ok           False                  False
  TMUS           87.88               33            0.49              0.57        164.40                30.04         0.509            pass              0.564             49.8                           0.590                0.87             -0.071                                 ok           False                  False
   PEP           82.61               23            0.33              0.29        125.53                14.62         0.486 below_threshold              0.306             33.9                           0.200               -4.54             -0.444            downtrend_blocked_slope           False                  False
  MCHP           93.02               43            0.13              0.08         81.46                36.65         0.481 below_threshold              0.782             62.1                           0.328                7.33              0.823                                 ok           False                  False
  CTSH           92.86               28            1.24              0.50         57.95                45.68         0.480 below_threshold              0.711             66.8                           0.350               -2.10              0.027                                 ok           False                  False
  TEAM          100.00               33            1.48              2.04        195.77                55.00         0.480 below_threshold              0.683             27.2                           0.361                2.69              0.107                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-06T12:00:05.410645-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:55:05.274079-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:50:04.350583-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:45:06.217443-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:40:04.013409-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006134004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006134004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006134004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006134004)

</details>

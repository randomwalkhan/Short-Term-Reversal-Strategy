# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 14:50:04 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$53,034.30`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   0     55     52112.5                 52112.5         9.48           9.48      160.14        160.29          bid_ask_mid                       9.48                bid_ask_mid                    True             0.0                    0.0         83.33               12               2.4         42.26           42.26                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ABNB           83.33               12            2.40              2.75        162.89                40.56         0.529            pass              0.219             21.4                           0.493               -1.03              0.542                                 ok            True                  False
  MSTR           91.89               37            0.48              0.55        164.19                79.08         0.628            pass              0.674             38.2                           0.184               -2.20             -0.081           downtrend_blocked_streak           False                  False
  MPWR           91.89               37            0.38              3.96       1478.19                53.63         0.568            pass              0.797             81.1                           0.621                6.94              0.831                                 ok           False                  False
  INTC           88.57               35            1.44              1.17        115.69                74.54         0.555            pass              0.594             47.7                           0.325               -7.54             -0.743 downtrend_blocked_slope_and_streak           False                  False
  ASML           72.73               22            1.71             22.20       1850.35                40.48         0.519            pass              0.198             22.2                           0.345                4.59              0.743                                 ok           False                  False
    MU           92.31               39            0.44              3.30       1062.55                46.96         0.517            pass              0.793             73.2                           0.386               -3.37             -0.162                                 ok           False                  False
   TRI           90.24               41            0.01              0.01         97.08                50.10         0.507            pass              0.821             99.2                           0.507                1.47             -0.052                                 ok           False                  False
  DRAM           84.00               25            2.65              1.14         61.18                49.40         0.498 below_threshold              0.273              5.5                           0.164               -5.64             -0.216                                 ok           False                  False
  AMAT           82.76               29            2.08              7.89        538.90                48.32         0.492 below_threshold              0.294             14.9                           0.255               12.39              1.576                                 ok           False                  False
  CTSH           89.47               19            1.99              0.81         57.82                45.68         0.489 below_threshold              0.501             46.5                           0.276               -2.85             -0.008                                 ok           False                  False
  TEAM          100.00               19            2.81              3.86        194.99                55.00         0.485 below_threshold              0.512              1.1                           0.088                1.31              0.046                                 ok           False                  False
  MELI           77.78               36            0.82             10.65       1856.05                43.88         0.481 below_threshold              0.372             50.1                           0.471                1.03              0.015                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-06T14:50:04.366747-04:00       entry_1500              entry {"allocated_cash": 52112.5, "asset_type": "option", "contract_symbol": "ABNB261120C00160000", "contracts": 55, "early_entry_score": 0.219, "entry_mode": "regular", "entry_option_price": 9.475, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 310.0, "option_spread_pct": 5.8, "option_volume": 20.0, "success_rate": 83.33, "ticker": "ABNB", "timing_score": 0.529}
2026-10-06T14:50:04.366747-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-06", "training_samples": 5941, "window": 5}
2026-10-06T12:00:05.410645-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:55:05.274079-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:50:04.350583-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:45:06.217443-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:40:04.013409-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006145004)

</details>

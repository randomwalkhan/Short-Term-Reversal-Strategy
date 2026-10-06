# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 15:45:04 EDT`
Last processed slot: `manual`

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
- Equity: `$106,521.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$1,375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   0     55     52112.5                 53487.5         9.48           9.72      160.14         160.7          bid_ask_mid                       9.72                bid_ask_mid                    True          1375.0                   2.64         83.33               12               2.4         42.26           42.65                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           91.18               34            0.60              6.22       1477.23                53.63         0.573            pass              0.726             70.3                           0.364                6.70              0.821                                 ok            True                  False
    MU           89.66               29            1.41             10.48       1059.47                46.96         0.519            pass              0.493             18.9                           0.218               -4.30             -0.206                                 ok            True                  False
  ABNB           83.33               18            2.09              2.40        163.04                40.56         0.510            pass              0.287             31.4                           0.464               -0.72              0.556                                 ok            True                  False
  SOXL           86.84               38            0.06              0.07        164.24               111.70         0.783            pass              0.717             89.9                           0.348                8.04              1.142                                 ok           False                  False
  MSTR           92.11               38            0.13              0.15        164.36                79.08         0.641            pass              0.822             82.7                           0.577               -1.86             -0.065           downtrend_blocked_streak           False                  False
  META           85.71               42            0.01              0.06        741.88                55.50         0.586            pass              0.706             98.5                           0.554                0.71             -0.209                                 ok           False                  False
  INTC           86.21               29            2.32              1.89        115.38                74.54         0.539            pass              0.393             15.6                           0.144               -8.37             -0.784 downtrend_blocked_slope_and_streak           False                  False
  ASML           71.43               21            1.79             23.29       1849.88                40.48         0.519            pass              0.180             18.4                           0.252                4.50              0.739                                 ok           False                  False
  MCHP           91.67               36            0.63              0.36         81.34                36.65         0.489 below_threshold              0.624             30.1                           0.260                6.81              0.801                                 ok           False                  False
  CTSH           89.47               19            2.05              0.84         57.81                45.68         0.485 below_threshold              0.496             44.9                           0.321               -2.91             -0.011                                 ok           False                  False
  TEAM          100.00               26            2.11              2.90        195.41                55.00         0.480 below_threshold              0.636             27.2                           0.453                2.05              0.078                                 ok           False                  False
  DRAM           85.71               21            3.41              1.47         61.04                49.40         0.474 below_threshold              0.286              4.3                           0.168               -6.37             -0.252            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-06T15:10:04.494335-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:05:04.280902-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:00:04.457281-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:55:01.305987-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:50:04.366747-04:00       entry_1500              entry {"allocated_cash": 52112.5, "asset_type": "option", "contract_symbol": "ABNB261120C00160000", "contracts": 55, "early_entry_score": 0.219, "entry_mode": "regular", "entry_option_price": 9.475, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 310.0, "option_spread_pct": 5.8, "option_volume": 20.0, "success_rate": 83.33, "ticker": "ABNB", "timing_score": 0.529}
2026-10-06T14:50:04.366747-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-06", "training_samples": 5941, "window": 5}
2026-10-06T12:00:05.410645-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:55:05.274079-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:50:04.350583-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:45:06.217443-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006154504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006154504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006154504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006154504)

</details>

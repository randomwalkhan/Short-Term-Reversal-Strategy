# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 11:55:01 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$23,958.10`
- Equity: `$48,078.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 24120.0         1.65           1.68       32.33         32.28          bid_ask_mid                       1.68                bid_ask_mid                    True           360.0                   1.52          87.5               16              1.99         38.72           40.97                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS          100.00               20            2.76              3.45        176.89                60.79         0.534          pass              0.542              7.3                           0.088               -6.05              0.064                                 ok            True                  False
  CSCO           88.24               34            0.76              0.58        109.49                36.37         0.520          pass              0.519             29.1                           0.326               -1.48             -0.073                                 ok            True                  False
  PAYX          100.00               12            1.59              1.40        125.04                25.34         0.518          pass              0.554             29.6                           0.283                0.93              0.210                                 ok            True                  False
  COST           90.91               22            0.96              6.31        937.25                19.36         0.508          pass              0.490             22.8                           0.180               -2.72             -0.185                                 ok            True                  False
  MNST           88.89               18            1.06              0.33         44.85               424.41         1.000          pass              0.505             38.3                           0.363               -6.15             -0.711            downtrend_blocked_slope           False                  False
  TEAM           92.50               40            0.22              0.29        186.90               117.24         0.779          pass              0.885             91.2                           0.423                7.11              1.180                                 ok           False                  False
  ABNB           95.00               40            0.08              0.10        182.50                64.48         0.647          pass              0.947             94.1                           0.795               -2.14             -0.244                                 ok           False                  False
   WDC           80.65               31            1.30              4.11        448.68                82.26         0.624          pass              0.385             55.0                           0.638               -3.79             -0.256 downtrend_blocked_slope_and_streak           False                  False
  MSTR           78.57               28            2.40              2.10        123.98                86.77         0.570          pass              0.240             21.1                           0.199               16.91              1.531                                 ok           False                  False
  MRVL           79.41               34            2.25              3.32        208.97                79.24         0.536          pass              0.307             31.2                           0.360              -13.33             -1.700 downtrend_blocked_slope_and_streak           False                  False
   HON           81.82               22            0.97              1.42        209.37                29.51         0.527          pass              0.199              5.8                           0.199               -6.21             -0.421 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               13            1.57              0.54         48.52                20.15         0.523          pass              0.508             12.1                           0.136               -6.72             -0.601 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:50:01.337983-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:45:01.308184-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:40:01.399320-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:35:06.484785-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:30:01.496570-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:25:02.340599-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:20:05.322061-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:15:02.323157-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:10:02.511069-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902115501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902115501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902115501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902115501)

</details>

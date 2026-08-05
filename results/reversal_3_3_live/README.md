# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 11:10:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$17,080.75`
- Equity: `$32,880.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 15800.0          4.1           3.95      138.68        138.31          bid_ask_mid                       3.95                bid_ask_mid                    True          -600.0                  -3.66         83.33               24              0.68          24.5           24.89                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            1.44              2.20        217.65               100.52         0.605          pass              0.409             60.6                           0.517                2.11              0.276                  ok            True                  False
  TEAM           84.62               39            0.78              0.61        110.05                86.98         0.602          pass              0.466             29.7                           0.174               28.16              2.850                  ok            True                  False
  CTAS           89.47               19            1.46              2.08        202.76                37.77         0.588          pass              0.371              0.0                           0.035               -0.34             -0.124                  ok            True                  False
  PAYX          100.00               11            1.38              1.14        118.17                35.13         0.581          pass              0.631             55.4                           0.267                6.78              0.735                  ok            True                  False
   CSX           91.67               24            0.56              0.20         50.94                29.11         0.563          pass              0.506             14.9                           0.190                1.63             -0.293                  ok            True                  False
   KDP           80.00               20            0.71              0.15         31.03                28.75         0.556          pass              0.269             48.8                           0.375                2.25              0.457                  ok            True                  False
  WDAY           83.33               36            0.69              0.83        170.92                70.04         0.555          pass              0.432             38.0                           0.208               28.45              2.884                  ok            True                  False
  MSFT           81.58               38            0.61              2.11        491.91                57.86         0.549          pass              0.422             46.1                           0.441               25.48              3.077                  ok            True                  False
   PEP           84.00               25            0.56              0.55        138.87                25.68         0.548          pass              0.363             33.9                           0.231                1.97              0.238                  ok            True                  False
  VRSK           93.55               31            1.21              1.64        192.10                43.54         0.521          pass              0.561              2.5                           0.061               -0.95             -0.324                  ok            True                  False
  CPRT           85.71               21            1.79              0.37         29.24                38.86         0.513          pass              0.350             24.5                           0.402                6.28              0.619                  ok            True                  False
   ADP           96.30               27            0.79              1.49        269.98                35.53         0.512          pass              0.719             51.6                           0.270               10.44              1.130                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T11:10:04.712256-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:05:03.723265-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:00:04.535517-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:55:04.718712-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:50:01.771343-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:45:01.734892-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:40:05.699069-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:35:01.163054-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:30:06.205244-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:25:05.700806-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805111004)

</details>

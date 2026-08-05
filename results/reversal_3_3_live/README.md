# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 11:45:04 EDT`
Last processed slot: `early_entry_1145`

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
- Equity: `$31,880.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-1,600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 14800.0          4.1            3.7      138.68        138.41          bid_ask_mid                        3.7                bid_ask_mid                    True         -1600.0                  -9.76         83.33               24              0.68          24.5           23.49                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            1.29              1.97        217.75               100.52         0.615          pass              0.423             64.8                           0.582                2.27              0.283                       ok            True                  False
 CMCSA           81.82               11            1.72              0.30         24.80                44.00         0.598          pass              0.198             27.7                           0.479                4.17              0.987                       ok            True                  False
  CTAS           83.33               12            1.76              2.50        202.58                37.77         0.598          pass              0.191              9.5                           0.235               -0.64             -0.138                       ok            True                  False
  WDAY           83.78               37            0.52              0.63        171.01                70.04         0.561          pass              0.497             53.4                           0.299               28.67              2.892                       ok            True                  False
   KDP           80.00               20            0.68              0.15         31.04                28.75         0.558          pass              0.276             51.2                           0.363                2.28              0.458                       ok            True                  False
  MSFT           81.08               37            0.71              2.45        491.76                57.86         0.548          pass              0.376             37.5                           0.332               25.35              3.073                       ok            True                  False
  CPRT           85.71               14            2.33              0.48         29.19                38.86         0.524          pass              0.246              4.9                           0.194                5.69              0.593                       ok            True                  False
   ADP           95.83               24            1.02              1.93        269.79                35.53         0.516          pass              0.657             37.4                           0.239               10.18              1.120                       ok            True                  False
  DRAM           77.14               35            0.38              0.15         54.83               109.93         0.731          pass              0.511             90.4                           0.772               -5.35             -0.567 downtrend_blocked_streak           False                  False
  SOXL           80.65               31            3.75              3.68        138.32               182.46         0.700          pass              0.368             47.0                           0.647              -16.36             -1.836 downtrend_blocked_streak           False                  False
  AMAT           90.00               30            1.30              4.98        544.49                87.24         0.657          pass              0.633             55.7                           0.621               -2.60             -0.305 downtrend_blocked_streak           False                  False
  TMUS           77.78                9            2.42              3.00        175.93                55.59         0.626          pass              0.150             29.0                           0.573               -9.43             -0.447  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:15:01.663027-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:10:04.712256-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:05:03.723265-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:00:04.535517-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805114504)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 11:35:01 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$32,480.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-1,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 15400.0          4.1           3.85      138.68        138.14          bid_ask_mid                       3.85                bid_ask_mid                    True         -1000.0                   -6.1         83.33               24              0.68          24.5           24.76                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.00               35            0.98              1.50        217.95               100.52         0.637          pass              0.450             73.2                           0.595                2.59              0.297                       ok            True                  False
  CTAS           83.33               12            1.83              2.61        202.53                37.77         0.594          pass              0.173              3.6                           0.129               -0.72             -0.141                       ok            True                  False
   CSX           92.00               25            0.52              0.19         50.95                29.11         0.558          pass              0.553             25.6                           0.314                1.67             -0.291                       ok            True                  False
  MSFT           81.58               38            0.57              1.98        491.96                57.86         0.552          pass              0.433             49.5                           0.471               25.53              3.079                       ok            True                  False
  WDAY           83.33               36            0.74              0.89        170.90                70.04         0.552          pass              0.419             33.9                           0.242               28.39              2.882                       ok            True                  False
   PEP           83.33               24            0.69              0.67        138.81                25.68         0.546          pass              0.293             18.6                           0.161                1.84              0.232                       ok            True                  False
  CPRT           85.71               14            2.33              0.48         29.19                38.86         0.526          pass              0.236              1.4                           0.087                5.69              0.593                       ok            True                  False
   ADP           95.45               22            1.27              2.40        269.59                35.53         0.512          pass              0.597             22.0                           0.127                9.90              1.108                       ok            True                  False
  DRAM           75.68               37            0.04              0.01         54.88               109.93         0.739          pass              0.551             99.1                           0.844               -5.02             -0.551 downtrend_blocked_streak           False                  False
  SOXL           80.65               31            3.48              3.41        138.44               182.46         0.717          pass              0.381             50.8                           0.580              -16.12             -1.823 downtrend_blocked_streak           False                  False
  AMAT           90.00               30            1.38              5.29        544.35                87.24         0.651          pass              0.624             52.9                           0.591               -2.68             -0.309 downtrend_blocked_streak           False                  False
  TEAM           85.00               40            0.11              0.08        110.27                86.98         0.641          pass              0.668             90.2                           0.616               29.03              2.881                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:15:01.663027-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:10:04.712256-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:05:03.723265-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:00:04.535517-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:55:04.718712-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:50:01.771343-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805113501)

</details>

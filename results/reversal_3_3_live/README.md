# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 13:20:02 EDT`
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

- Cash: `$23,958.10`
- Equity: `$47,358.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23400.0         1.65           1.62       32.33         32.17          bid_ask_mid                       1.62                bid_ask_mid                    True          -360.0                  -1.52          87.5               16              1.99         38.72           42.14                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  COST           87.50               16            1.10              7.24        936.86                19.36         0.532          pass              0.328             11.5                           0.240               -2.86             -0.191                                 ok            True                  False
  CSCO           87.88               33            0.80              0.62        109.48                36.37         0.521          pass              0.519             34.4                           0.504               -1.53             -0.075                                 ok            True                  False
    ZS          100.00               15            3.36              4.20        176.57                60.79         0.519          pass              0.530             15.0                           0.404               -6.62              0.036                                 ok            True                  False
  PAYX          100.00               15            1.40              1.23        125.11                25.34         0.511          pass              0.599             38.2                           0.436                1.13              0.219                                 ok            True                  False
  SNPS           90.48               42            0.66              1.92        414.00                58.04         0.508          pass              0.734             67.9                           0.398                2.70              0.870                                 ok            True                  False
  MNST           80.00               10            1.63              0.51         44.77               424.41         1.000          pass              0.114              4.5                           0.119               -6.69             -0.737            downtrend_blocked_slope           False                  False
  TEAM           92.86               42            0.10              0.13        186.97               117.24         0.776          pass              0.909             96.0                           0.626                7.24              1.186                                 ok           False                  False
   WDC           80.65               31            1.35              4.26        448.62                82.26         0.621          pass              0.379             53.4                           0.604               -3.84             -0.258 downtrend_blocked_slope_and_streak           False                  False
  MSTR           79.31               29            2.31              2.02        124.02                86.77         0.571          pass              0.256             24.2                           0.193               17.03              1.535                                 ok           False                  False
   STX           86.21               29            1.79             10.23        812.25                70.47         0.560          pass              0.507             52.8                           0.724               -3.67             -0.280 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            2.18              3.21        209.02                79.24         0.541          pass              0.315             33.5                           0.356              -13.26             -1.697 downtrend_blocked_slope_and_streak           False                  False
  INTU           91.18               34            0.75              1.82        344.15                46.23         0.513          pass              0.670             53.7                           0.490               -5.56             -0.576            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-02T12:00:02.480923-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:50:01.337983-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:45:01.308184-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:40:01.399320-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:35:06.484785-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:30:01.496570-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:25:02.340599-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:20:05.322061-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:15:02.323157-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902132002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902132002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902132002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902132002)

</details>

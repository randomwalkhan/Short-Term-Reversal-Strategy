# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 12:25:01 EDT`
Last processed slot: `manage_1230`

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
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23760.0         1.65           1.65       32.33         32.28          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0          87.5               16              1.99         38.72           41.16                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           92.31               39            0.80              1.04        186.58               117.24         0.758          pass              0.804             68.8                           0.310                6.49              1.154                                 ok            True                  False
  MSTR           82.86               35            1.40              1.23        124.35                86.77         0.593          pass              0.464             53.9                           0.716               18.11              1.577                                 ok            True                  False
    ZS          100.00               15            3.22              4.01        176.65                60.79         0.532          pass              0.512              8.5                           0.177               -6.48              0.043                                 ok            True                  False
  CSCO           87.10               31            0.93              0.71        109.43                36.37         0.526          pass              0.420             12.8                           0.166               -1.66             -0.081                                 ok            True                  False
  PAYX          100.00               16            1.35              1.19        125.13                25.34         0.507          pass              0.612             40.3                           0.443                1.18              0.221                                 ok            True                  False
  MNST           89.47               19            1.03              0.33         44.85               424.41         1.000          pass              0.531             39.6                           0.478               -6.12             -0.710            downtrend_blocked_slope           False                  False
   WDC           81.82               33            0.95              2.99        449.16                82.26         0.635          pass              0.467             67.2                           0.651               -3.45             -0.240           downtrend_blocked_streak           False                  False
   STX           84.62               26            2.01             11.48        811.72                70.47         0.563          pass              0.427             47.1                           0.677               -3.88             -0.290 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            1.95              2.88        209.16                79.24         0.555          pass              0.337             40.3                           0.525              -13.06             -1.686 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               13            1.60              0.55         48.52                20.15         0.521          pass              0.503             10.3                           0.188               -6.75             -0.602 downtrend_blocked_slope_and_streak           False                  False
   HON           81.82               22            1.13              1.66        209.27                29.51         0.516          pass              0.189              2.8                           0.161               -6.37             -0.429 downtrend_blocked_slope_and_streak           False                  False
  LRCX           82.86               35            0.78              1.59        289.52                48.78         0.515          pass              0.477             60.8                           0.454               -6.27             -0.689 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902122501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902122501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902122501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902122501)

</details>

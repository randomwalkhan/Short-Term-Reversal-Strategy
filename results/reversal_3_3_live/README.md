# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 13:15:01 EDT`
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

- Cash: `$23,958.10`
- Equity: `$47,358.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23400.0         1.65           1.62       32.33         32.24          bid_ask_mid                       1.62                bid_ask_mid                    True          -360.0                  -1.52          87.5               16              1.99         38.72            41.5                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.02              1.76        124.12                86.77         0.583          pass              0.293             33.7                           0.230               17.37              1.549                                 ok            True                  False
    ZS          100.00               13            3.50              4.37        176.50                60.79         0.523          pass              0.507             11.5                           0.319               -6.76              0.029                                 ok            True                  False
  CSCO           87.88               33            0.83              0.64        109.47                36.37         0.519          pass              0.512             32.1                           0.449               -1.56             -0.076                                 ok            True                  False
  COST           89.47               19            1.05              6.91        937.00                19.36         0.519          pass              0.411             15.5                           0.262               -2.81             -0.189                                 ok            True                  False
  SNPS           90.00               40            0.72              2.09        413.93                58.04         0.516          pass              0.714             65.2                           0.380                2.64              0.868                                 ok            True                  False
  PAYX          100.00               15            1.43              1.26        125.10                25.34         0.509          pass              0.595             36.8                           0.423                1.10              0.217                                 ok            True                  False
  MNST           80.00               10            1.62              0.51         44.77               424.41         1.000          pass              0.116              5.2                           0.151               -6.68             -0.737            downtrend_blocked_slope           False                  False
   WDC           80.65               31            1.44              4.53        448.50                82.26         0.616          pass              0.370             50.4                           0.548               -3.92             -0.262 downtrend_blocked_slope_and_streak           False                  False
   STX           85.19               27            1.96             11.18        811.85                70.47         0.560          pass              0.453             48.4                           0.673               -3.83             -0.288 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            2.14              3.15        209.04                79.24         0.543          pass              0.318             34.6                           0.469              -13.23             -1.695 downtrend_blocked_slope_and_streak           False                  False
  INTU           91.18               34            0.69              1.66        344.22                46.23         0.518          pass              0.683             57.8                           0.566               -5.49             -0.573            downtrend_blocked_slope           False                  False
   HON           75.00               16            1.53              2.25        209.02                29.51         0.516          pass              0.092              0.0                           0.214               -6.75             -0.447 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902131501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902131501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902131501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902131501)

</details>

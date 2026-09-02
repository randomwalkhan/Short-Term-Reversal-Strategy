# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 13:30:05 EDT`
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
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23400.0         1.65           1.62       32.33         32.19          bid_ask_mid                       1.62                bid_ask_mid                    True          -360.0                  -1.52          87.5               16              1.99         38.72           42.14                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS          100.00               18            2.95              3.69        176.79                60.79         0.525          pass              0.582             25.2                           0.551               -6.23              0.055                                 ok            True                  False
  COST           89.47               19            1.01              6.64        937.11                19.36         0.521          pass              0.421             18.8                           0.308               -2.77             -0.187                                 ok            True                  False
  CSCO           87.88               33            0.83              0.64        109.47                36.37         0.519          pass              0.511             31.8                           0.512               -1.56             -0.077                                 ok            True                  False
  PAYX          100.00               16            1.33              1.17        125.14                25.34         0.509          pass              0.614             41.2                           0.469                1.20              0.222                                 ok            True                  False
  MNST           80.00               10            1.57              0.49         44.78               424.41         1.000          pass              0.125              8.4                           0.117               -6.63             -0.734            downtrend_blocked_slope           False                  False
   WDC           80.65               31            1.35              4.27        448.61                82.26         0.621          pass              0.379             53.2                           0.667               -3.84             -0.258 downtrend_blocked_slope_and_streak           False                  False
  MSTR           79.31               29            2.27              1.98        124.03                86.77         0.573          pass              0.261             25.5                           0.202               17.07              1.537                                 ok           False                  False
   STX           86.67               30            1.60              9.13        812.73                70.47         0.566          pass              0.541             57.9                           0.758               -3.48             -0.271 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            2.18              3.21        209.02                79.24         0.541          pass              0.315             33.5                           0.341              -13.26             -1.697 downtrend_blocked_slope_and_streak           False                  False
  LRCX           83.33               36            0.71              1.45        289.58                48.78         0.514          pass              0.507             64.4                           0.549               -6.20             -0.686 downtrend_blocked_slope_and_streak           False                  False
  INTU           92.11               38            0.38              0.92        344.53                46.23         0.513          pass              0.790             76.5                           0.621               -5.20             -0.559            downtrend_blocked_slope           False                  False
  AMAT           86.11               36            0.68              2.09        440.95                44.19         0.513          pass              0.579             63.9                           0.681              -11.46             -1.252 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902133005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902133005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902133005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902133005)

</details>

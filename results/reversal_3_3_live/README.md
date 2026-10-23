# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:50:06 EDT`
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

- Cash: `$73,431.80`
- Equity: `$140,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-4,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 67400.0        17.85          16.85      223.97        223.74          bid_ask_mid                      16.85                bid_ask_mid                    True         -4000.0                   -5.6         100.0               38              0.68         80.16           77.94                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.17              0.29         35.07                27.06         0.555          pass              0.571             42.3                           0.520                9.51              0.910                                 ok            True                  False
 CMCSA           92.31               13            0.88              0.14         22.78                23.88         0.532          pass              0.565             54.5                           0.302                9.58              1.045                                 ok            True                  False
   KHC           82.35               17            1.51              0.27         24.98                34.71         0.528          pass              0.249             29.0                           0.305               10.96              1.088                                 ok            True                  False
   AEP           83.33               18            0.87              0.80        130.30                17.81         0.519          pass              0.239             14.9                           0.253                5.45              0.480                                 ok            True                  False
  ORLY          100.00               13            1.64              1.05         91.55                17.78         0.513          pass              0.480              2.9                           0.093                4.68              0.599                                 ok            True                  False
   ADP           91.67               24            0.68              1.46        307.32                23.94         0.509          pass              0.667             70.5                           0.406               12.91              1.240                                 ok            True                  False
   CEG           85.29               34            0.74              1.33        254.64                65.49         0.590          pass              0.589             76.1                           0.719              -15.02             -1.674 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.03              0.93         64.79                24.03         0.585          pass              0.515             18.7                           0.401                5.72              0.547                                 ok           False                  False
   XEL           75.00                8            1.21              0.67         78.68                16.59         0.541          pass              0.076              7.3                           0.202                5.73              0.587                                 ok           False                  False
   WMT           78.57               14            1.12              0.95        120.71                23.20         0.535          pass              0.131             17.1                           0.238                7.55              0.744                                 ok           False                  False
  REGN           78.57               14            1.72              9.87        814.86                31.70         0.534          pass              0.143             21.1                           0.303                7.83              0.836                                 ok           False                  False
   EXC           70.00               10            1.27              0.40         44.68                20.91         0.534          pass              0.092             13.0                           0.238                6.03              0.557                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-23T10:50:06.270815-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:45:06.482363-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:40:06.544410-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:35:06.665286-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023105006)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:55:02 EDT`
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
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 67400.0        17.85          16.85      223.97        223.56          bid_ask_mid                      16.85                bid_ask_mid                    True         -4000.0                   -5.6         100.0               38              0.68         80.16           78.05                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.74               19            0.84              0.21         35.10                27.06         0.551          pass              0.683             58.5                           0.737                9.87              0.925                                 ok            True                  False
 CMCSA           90.00               10            1.07              0.17         22.77                23.88         0.536          pass              0.453             44.3                           0.252                9.37              1.036                                 ok            True                  False
   KHC           85.71               21            1.14              0.20         25.00                34.71         0.530          pass              0.419             46.7                           0.554               11.38              1.105                                 ok            True                  False
   WMT           83.33               18            0.89              0.76        120.80                23.20         0.529          pass              0.298             34.1                           0.363                7.80              0.755                                 ok            True                  False
  AMGN           81.82               22            1.03              3.22        445.90                28.21         0.518          pass              0.287             35.7                           0.601                6.70              0.743                                 ok            True                  False
   AEP           85.00               20            0.80              0.73        130.33                17.81         0.513          pass              0.318             22.4                           0.310                5.53              0.484                                 ok            True                  False
   ADP           91.30               23            0.71              1.54        307.28                23.94         0.512          pass              0.646             68.8                           0.450               12.87              1.239                                 ok            True                  False
  ORLY           93.75               16            1.37              0.88         91.62                17.78         0.503          pass              0.513             18.7                           0.314                4.96              0.611                                 ok            True                  False
   CEG           83.33               36            0.51              0.92        254.82                65.49         0.590          pass              0.572             83.5                           0.775              -14.82             -1.663 downtrend_blocked_slope_and_streak           False                  False
   EXC           75.00               12            1.14              0.36         44.70                20.91         0.535          pass              0.133             22.2                           0.322                6.18              0.563                                 ok           False                  False
   CSX           66.67                3            2.00              0.72         51.36                26.41         0.533          pass              0.140             28.9                           0.435                7.14              0.614                                 ok           False                  False
  MDLZ           50.00                2            1.84              0.84         64.83                24.03         0.532          pass              0.132             26.4                           0.491                5.93              0.556                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-23T10:55:02.008027-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "entry_ask": 1.8, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.75, "hypothetical_budget": 36715.9, "hypothetical_contracts": 209, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1606.0, "option_spread_pct": 5.71, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.699, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "matched_signals": 36, "recovery_stability_score": 0.699, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.758, "early_reclaim_pct": 60.2, "matched_signals": 40, "recovery_stability_score": 0.584, "success_rate": 92.5, "ticker": "WDAY", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-23T10:50:06.270815-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:45:06.482363-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:40:06.544410-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:35:06.665286-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023105502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023105502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023105502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023105502)

</details>

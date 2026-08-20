# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-20 09:42:18 EDT`
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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           82.14               28            1.38              2.34        241.61               130.07         0.834          pass              0.340             26.6                           0.387               10.71              1.021                  ok            True                  False
  SHOP           97.30               37            0.75              0.77        146.25                84.09         0.680          pass              0.814             55.3                           0.433               -1.33             -0.363                  ok            True                  False
  ABNB           93.75               32            0.83              1.09        185.92                63.87         0.621          pass              0.796             73.7                           0.661               21.89              1.007                  ok            True                   True
  FAST          100.00               22            0.64              0.23         51.34                21.74         0.540          pass              0.669             45.0                           0.300                0.61             -0.108                  ok            True                  False
   MAR           92.00               25            1.10              2.76        358.76                36.48         0.538          pass              0.554             26.6                           0.213               -1.02              0.126                  ok            True                  False
  UPRO           80.65               31            0.68              0.72        151.77                40.33         0.535          pass              0.401             63.6                           0.739               -0.91             -0.153                  ok            True                  False
  BKNG           97.14               35            0.78              1.16        212.50                45.88         0.534          pass              0.712             30.5                           0.318                1.90             -0.070                  ok            True                  False
  REGN          100.00               28            0.86              5.05        838.68                29.05         0.520          pass              0.671             33.1                           0.278                8.09              0.648                  ok            True                  False
  ISRG           87.50               32            0.79              2.20        396.78                37.69         0.519          pass              0.435             12.3                           0.156                5.58              0.343                  ok            True                  False
  VRTX           93.33               15            1.86              7.18        548.98                32.17         0.513          pass              0.565             41.7                           0.288               11.94              0.839                  ok            True                  False
  AMGN          100.00               13            1.80              5.58        439.97                28.93         0.505          pass              0.675             68.2                           0.401                7.29              0.660                  ok            True                  False
  GILD           94.12               17            1.80              1.86        146.80                26.30         0.502          pass              0.536             20.9                           0.222               10.76              1.101                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-20T09:18:16.446091-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-19T11:30:46.509801-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-19T10:58:16.376316-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "ZS260918C00185000", "current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "entry_ask": 15.8, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 26569.0, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1626.0, "option_spread_pct": 4.53, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "matched_signals": 41, "recovery_stability_score": 0.774, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-19T10:25:26.675121-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T12:30:08.738941-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260820094218)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260820094218)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260820094218)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260820094218)

</details>

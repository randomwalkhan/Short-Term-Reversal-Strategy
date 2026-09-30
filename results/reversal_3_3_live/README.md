# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 10:45:06 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$85,238.30`
- Equity: `$85,238.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261120C00155000     24          2026-09-29         2026-09-30         15.9        18.6 6480.0   16.981132 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           85.29               34            0.93              0.95        146.59               117.21         0.742          pass              0.574             66.3                           0.329               40.17              2.905                  ok            True                  False
  MSTR           94.12               34            1.08              1.17        154.17                99.32         0.662          pass              0.714             37.0                           0.241               21.26              1.360                  ok            True                  False
  DRAM           83.87               31            0.87              0.37         61.13                54.99         0.590          pass              0.435             44.3                           0.489                9.80              0.611                  ok            True                  False
  ASML           80.65               31            0.72              9.24       1830.43                42.72         0.557          pass              0.295             27.3                           0.342               13.67              1.178                  ok            True                  False
   ADI           88.00               25            0.98              2.72        397.05                32.38         0.516          pass              0.439             24.6                           0.274                8.92              0.899                  ok            True                  False
  MPWR           83.33               24            1.92             18.19       1346.19                52.13         0.514          pass              0.265             10.3                           0.132               15.72              1.578                  ok            True                  False
   BKR           90.48               21            1.22              0.48         55.71                31.55         0.507          pass              0.509             35.1                           0.270               -1.93             -0.136                  ok            True                  False
  PYPL           93.55               31            0.82              0.31         53.76                34.93         0.505          pass              0.624             24.1                           0.285                1.40              0.300                  ok            True                  False
    ZS           97.87               47            0.05              0.07        198.32                81.34         0.617          pass              0.943             93.7                           0.586                3.48              0.092                  ok           False                  False
  META           76.47               17            1.54              7.98        735.37                54.80         0.589          pass              0.210             34.8                           0.313                8.12              0.921                  ok           False                  False
  AMGN           86.11               36            0.27              0.81        423.29                46.59         0.583          pass              0.554             53.0                           0.396               12.26              1.231                  ok           False                  False
  LRCX           81.40               43            0.11              0.26        323.75                58.87         0.571          pass              0.570             91.8                           0.436               20.28              1.824                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-30T10:45:06.139283-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                            {"contract_symbol": "DXCM261030C00086000", "current_drop_pct": 0.62, "early_entry_score": 0.67, "early_reclaim_pct": 63.0, "entry_ask": 5.3, "entry_bid": 3.2, "entry_mode": "early", "entry_option_price": 4.25, "hypothetical_budget": 42619.15, "hypothetical_contracts": 100, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 49.41, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.614, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.67, "early_reclaim_pct": 63.0, "matched_signals": 38, "recovery_stability_score": 0.614, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T10:40:05.432480-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:35:02.181722-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:30:04.117201-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:25:03.100104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:20:05.117028-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:15:05.931688-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:10:05.044472-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:05:05.127688-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:00:05.050989-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "entry_ask": 8.7, "entry_bid": 6.75, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 42619.15, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 4833.0, "option_spread_pct": 25.24, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.628, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "matched_signals": 33, "recovery_stability_score": 0.628, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "trend_health_status": "ok"}, {"current_drop_pct": 0.61, "early_entry_score": 0.758, "early_reclaim_pct": 67.8, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 92.11, "ticker": "BKR", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930104506)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 10:20:05 EDT`
Last processed slot: `manage_1030`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.35               34            0.62              0.27         61.18                54.99         0.587          pass              0.463             60.4                           0.707               10.08              0.623                       ok            True                  False
  ASML           80.65               31            0.72              9.26       1830.42                42.72         0.557          pass              0.285             23.9                           0.287               13.66              1.178                       ok            True                  False
  MPWR           87.88               33            0.78              7.41       1350.82                52.13         0.545          pass              0.570             50.7                           0.252               17.06              1.631                       ok            True                  False
  MRVL           80.65               31            1.64              3.03        261.97                56.16         0.520          pass              0.298             29.7                           0.290               12.73              0.974                       ok            True                  False
   ADI           88.89               27            0.87              2.41        397.19                32.38         0.513          pass              0.497             31.7                           0.236                9.04              0.905                       ok            True                  False
  PYPL           93.94               33            0.65              0.24         53.79                34.93         0.506          pass              0.657             27.1                           0.268                1.57              0.308                       ok            True                  False
  NXPI           86.21               29            0.97              1.60        235.78                39.17         0.504          pass              0.553             70.3                           0.347                6.94              0.551                       ok            True                  False
  MSTR           94.87               39            0.07              0.08        154.64                99.32         0.700          pass              0.932             90.8                           0.360               22.49              1.406                       ok           False                  False
    ZS           97.87               47            0.03              0.05        198.34                81.34         0.618          pass              0.950             96.1                           0.468                3.50              0.092                       ok           False                  False
   TRI           89.19               37            0.33              0.22         96.14                56.37         0.585          pass              0.677             64.4                           0.382               -5.32             -0.175 downtrend_blocked_streak           False                  False
  META           76.47               17            1.62              8.37        735.20                54.80         0.585          pass              0.200             31.6                           0.298                8.03              0.917                       ok           False                  False
  AMGN           87.80               41            0.05              0.15        423.57                46.59         0.570          pass              0.736             90.2                           0.447               12.51              1.241                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-30T10:20:05.117028-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:15:05.931688-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:10:05.044472-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:05:05.127688-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:00:05.050989-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "entry_ask": 8.7, "entry_bid": 6.75, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 42619.15, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 4833.0, "option_spread_pct": 25.24, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.628, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.76, "early_reclaim_pct": 63.8, "matched_signals": 33, "recovery_stability_score": 0.628, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "trend_health_status": "ok"}, {"current_drop_pct": 0.61, "early_entry_score": 0.758, "early_reclaim_pct": 67.8, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 92.11, "ticker": "BKR", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T09:50:05.025462-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "MSTR261120C00155000", "fill_price": 18.6, "pnl": 6480.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.98, "ticker": "MSTR"}
2026-09-30T00:00:05.973499-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92, 'empty': 1}
2026-09-29T15:10:01.396429-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-29T15:05:05.953732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-29T15:00:06.204288-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930102005)

</details>

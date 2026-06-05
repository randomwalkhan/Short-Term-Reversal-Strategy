# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 10:15:05 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$33,370.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  WDAY           87.88               33            1.30              1.35        147.33                69.97         0.576          pass              0.477             18.7                           0.142               13.93              1.958                       ok            True                  False
  TEAM           93.55               31            2.15              1.53        100.85                86.36         0.570          pass              0.620             20.7                           0.199               16.27              1.875                       ok            True                  False
  FTNT          100.00               15            1.91              2.00        148.81                44.88         0.555          pass              0.575             28.7                           0.475                9.62              1.458                       ok            True                  False
  PANW           89.66               29            1.31              2.56        278.15                60.15         0.553          pass              0.588             49.5                           0.412                8.96              1.323                       ok            True                  False
  CTSH           93.55               31            0.67              0.25         53.29                51.38         0.544          pass              0.768             70.7                           0.369                0.55              0.167                       ok            True                  False
  CRWD           80.00               10            3.48             17.50        711.59                64.90         0.514          pass              0.143             30.5                           0.415                7.07              1.192                       ok            True                  False
    MU           80.00               10            5.81             40.54        978.63               105.49         0.513          pass              0.139             29.1                           0.497               24.91              1.784                       ok            True                  False
    ZS           81.82               33            1.17              1.11        134.79               157.69         0.880          pass              0.381             30.4                           0.189              -26.70             -2.257  downtrend_blocked_slope           False                  False
  CSCO          100.00                1            3.60              3.28        128.60                55.20         0.582          pass              0.495             12.2                           0.246                4.08              0.801                       ok           False                  False
   ADI          100.00                6            2.81              8.42        425.15                45.54         0.555          pass              0.539             27.8                           0.613                5.24              0.394                       ok           False                  False
  QCOM           80.00                5            5.25              8.91        238.75                97.97         0.538          pass              0.122             22.7                           0.319               -3.13             -0.262  downtrend_blocked_slope           False                  False
  AVGO          100.00                1            4.68             13.74        413.02                65.35         0.524          pass              0.484             10.4                           0.238               -3.59             -0.063 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-05T10:15:05.401344-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "entry_ask": 13.3, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 16685.38, "hypothetical_contracts": 13, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 21.21, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.825, "early_reclaim_pct": 79.4, "matched_signals": 41, "recovery_stability_score": 0.587, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:10:05.013482-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "entry_ask": 13.3, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 157.0, "option_spread_pct": 27.35, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.839, "early_reclaim_pct": 83.7, "matched_signals": 41, "recovery_stability_score": 0.574, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-05T10:05:02.004075-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:05:02.004075-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "SOXL260717C00270000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SOXL"}
2026-06-05T10:00:04.998731-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T09:35:04.249601-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-05T09:30:04.938889-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-05T09:25:01.283083-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-05T09:20:04.897767-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-05T09:15:01.957387-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605101505)

</details>

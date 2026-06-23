# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-23 12:20:03 EDT`
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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   WMT     option         option  WMT260724C00120000     52          2026-06-18         2026-06-23         2.51         3.5  5148.0   39.442231 take_profit_day2_hit_at_scan
  MRVL     option         option MRVL260724C00310000      3          2026-06-22         2026-06-23        35.00        31.5 -1050.0  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AVGO           80.00               15            2.61              7.17        389.06                76.66         0.629            pass              0.257             53.5                           0.555               -3.56              0.136                                 ok            True                  False
  INTC           89.47               19            4.25              4.19        139.14                94.51         0.506            pass              0.525             53.9                           0.654               22.38              2.508                                 ok            True                  False
   WBD           88.89                9            0.76              0.14         26.89                19.64         0.584            pass              0.520             75.0                           0.646                1.04              0.042                                 ok           False                  False
   HON           60.00               10            1.65              2.63        226.98                40.60         0.568            pass              0.159             34.0                           0.379                5.93              0.870                                 ok           False                  False
  MRVL          100.00                2            8.72             18.79        299.81               151.43         0.556            pass              0.502             15.6                           0.444               -2.71              1.011                                 ok           False                  False
  UPRO           88.89                9            3.08              3.05        140.11                49.83         0.549            pass              0.401             36.3                           0.662               -1.09              0.351                                 ok           False                  False
  CSCO           95.24               42            0.11              0.09        121.49                40.78         0.498 below_threshold              0.940             96.6                           0.907               -2.22             -0.130           downtrend_blocked_streak           False                  False
  ROST           87.50                8            1.95              3.23        235.59                39.21         0.493 below_threshold              0.463             71.2                           0.562                2.37              0.167                                 ok           False                  False
  FAST           93.55               31            0.37              0.12         46.07                23.77         0.492 below_threshold              0.779             76.1                           0.764               -0.11             -0.120                                 ok           False                  False
  CTSH           87.50               32            0.86              0.25         41.72                52.33         0.487 below_threshold              0.562             55.6                           0.497              -21.74             -2.541 downtrend_blocked_slope_and_streak           False                  False
  ODFL           91.43               35            0.61              0.93        219.12                45.20         0.486 below_threshold              0.786             88.8                           0.647              -11.67             -1.480 downtrend_blocked_slope_and_streak           False                  False
  PCAR           84.62               26            0.85              0.71        119.81                32.72         0.477 below_threshold              0.435             52.6                           0.651                0.56              0.170                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T11:20:02.932662-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "GOOG260731C00345000", "current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "entry_ask": 18.9, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 142.0, "option_spread_pct": 5.99, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T10:51:17.657217-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T00:00:04.979813-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-22T15:10:01.120080-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:00:02.230019-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260623122003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260623122003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260623122003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260623122003)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 10:05:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           81.48               27            1.36              6.49        680.18                64.33         0.562          pass              0.383             57.9                           0.465               -6.31              0.030                                 ok            True                  False
    ZS           72.00               25            2.28              1.98        123.53               152.31         0.861          pass              0.296             36.7                           0.421              -10.14             -0.612 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.71              0.12         23.15                27.50         0.705          pass              0.586             38.4                           0.321                4.37              0.401                                 ok           False                  False
  INTU           75.00               36            1.09              2.05        268.20                98.62         0.683          pass              0.452             70.3                           0.806              -11.87             -1.258 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               23            0.06              0.06        141.57                22.29         0.602          pass              0.806             86.4                           0.467                0.60              0.165                                 ok           False                  False
   TRI           79.17               24            0.86              0.48         79.05                52.51         0.594          pass              0.359             68.7                           0.659               -8.36             -0.811 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.37               43            0.26              0.15         84.32                82.55         0.579          pass              0.756             91.6                           0.896              -17.07             -1.850 downtrend_blocked_slope_and_streak           False                  False
   EXC           88.00               25            0.05              0.02         45.55                20.58         0.565          pass              0.646             91.9                           0.599                2.03              0.229                                 ok           False                  False
  GILD           92.31               13            1.39              1.22        124.93                29.17         0.562          pass              0.413              2.8                           0.139               -3.61             -0.225           downtrend_blocked_streak           False                  False
  PAYX          100.00               28            0.24              0.16         97.51                31.76         0.560          pass              0.833             85.8                           0.794               -2.14             -0.162                                 ok           False                  False
  WDAY           82.05               39            0.63              0.54        121.60                69.08         0.558          pass              0.551             82.3                           0.884              -18.15             -2.057 downtrend_blocked_slope_and_streak           False                  False
   WMT           87.10               31            0.47              0.39        117.96                34.58         0.555          pass              0.508             41.0                           0.346               -0.14              0.031                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-18T10:05:02.276759-04:00 early_entry_1005      early_entry_shadow                {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "entry_ask": 9.5, "entry_bid": 5.95, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 13257.25, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 45.95, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.741, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T10:00:05.319103-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 9.9, "hypothetical_budget": 13257.25, "hypothetical_contracts": 13, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 34.0, "option_spread_pct": null, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T09:20:05.276411-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-17T16:10:06.900615-04:00      manage_1600                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "GOOG260724C00380000", "fill_price": 8.3025, "pnl": -1383.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GOOG"}
2026-06-17T15:10:05.396926-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:05:04.450318-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:00:06.393380-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
2026-06-17T14:50:06.575124-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618100502)

</details>

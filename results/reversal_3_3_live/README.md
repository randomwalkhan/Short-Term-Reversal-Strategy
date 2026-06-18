# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 10:00:05 EDT`
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
    ZS           68.18               22            2.71              2.36        123.37               152.31         0.854          pass              0.240             24.9                           0.295              -10.53             -0.632 downtrend_blocked_slope_and_streak           False                  False
  INTU           70.37               27            1.86              3.51        267.58                98.62         0.686          pass              0.329             49.1                           0.637              -12.55             -1.294 downtrend_blocked_slope_and_streak           False                  False
   KHC           85.71                7            0.54              0.09         23.16                27.50         0.674          pass              0.380             53.4                           0.521                4.55              0.409                                 ok           False                  False
   TRI           77.27               22            1.32              0.74         78.93                52.51         0.573          pass              0.292             51.6                           0.482               -8.79             -0.832 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               26            0.39              0.27         97.47                31.76         0.563          pass              0.793             76.5                           0.698               -2.29             -0.169                                 ok           False                  False
   WMT           87.10               31            0.48              0.40        117.96                34.58         0.554          pass              0.503             39.4                           0.338               -0.15              0.030                                 ok           False                  False
  GILD           83.33               18            0.87              0.76        125.12                29.17         0.553          pass              0.253             18.7                           0.143               -3.10             -0.201           downtrend_blocked_streak           False                  False
  TEAM           87.80               41            0.89              0.53         84.16                82.55         0.546          pass              0.676             71.2                           0.770              -17.60             -1.879 downtrend_blocked_slope_and_streak           False                  False
  PANW           90.48               42            0.23              0.45        281.94                57.71         0.544          pass              0.800             88.7                           0.570                0.80              0.519                                 ok           False                  False
  WDAY           82.05               39            0.84              0.71        121.52                69.08         0.543          pass              0.532             76.4                           0.826              -18.32             -2.067 downtrend_blocked_slope_and_streak           False                  False
  CRWD           76.19               21            2.17             10.35        678.52                64.33         0.543          pass              0.226             32.9                           0.254               -7.08             -0.007                                 ok           False                  False
  COST           50.00               10            1.51             10.22        961.21                23.27         0.524          pass              0.099             15.5                           0.206               -2.20             -0.072                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-18T10:00:05.319103-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 9.9, "hypothetical_budget": 13257.25, "hypothetical_contracts": 13, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 34.0, "option_spread_pct": null, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.755, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.886, "early_reclaim_pct": 79.3, "matched_signals": 42, "recovery_stability_score": 0.755, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T09:20:05.276411-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-17T16:10:06.900615-04:00      manage_1600                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "GOOG260724C00380000", "fill_price": 8.3025, "pnl": -1383.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GOOG"}
2026-06-17T15:10:05.396926-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:05:04.450318-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:00:06.393380-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
2026-06-17T14:50:06.575124-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
2026-06-17T14:50:06.575124-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.468, "error": "XEL: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "XEL", "timing_score": 0.64}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618100005)

</details>

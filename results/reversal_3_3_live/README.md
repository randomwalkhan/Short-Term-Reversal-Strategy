# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 10:00:06 EDT`
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

- Cash: `$128,734.80`
- Equity: `$128,734.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           84.38               32            0.55              2.82        736.33                55.15         0.582            pass              0.567             81.6                           0.820                1.04              0.176                                 ok            True                  False
    ZS           91.43               35            1.02              1.58        220.11                59.94         0.526            pass              0.746             74.0                           0.617                9.94              1.388                                 ok            True                   True
  UPRO           94.12               17            1.55              1.63        149.66                30.64         0.517            pass              0.546             23.8                           0.278                0.19              0.015                                 ok            True                  False
  MPWR           81.82               22            1.85             16.07       1236.22                56.61         0.540            pass              0.339             52.3                           0.625              -10.35             -1.570            downtrend_blocked_slope           False                  False
   CEG           83.33                6            3.59              7.03        276.53                59.82         0.532            pass              0.190             15.8                           0.201                4.09              0.709                                 ok           False                  False
  MSTR           84.62               13            4.60              4.61        141.26                78.69         0.507            pass              0.257             21.1                           0.282              -14.86             -1.475 downtrend_blocked_slope_and_streak           False                  False
  CDNS           75.00                8            2.87              6.62        326.62                37.41         0.498 below_threshold              0.140             30.2                           0.289               -8.76             -0.869 downtrend_blocked_slope_and_streak           False                  False
  SNPS           60.00                5            4.15             13.94        473.95                52.37         0.491 below_threshold              0.114             21.7                           0.233               -6.22             -0.330 downtrend_blocked_slope_and_streak           False                  False
  AVGO           80.00               10            2.72              6.60        343.42                35.83         0.487 below_threshold              0.106             19.0                           0.262               -1.98             -0.364            downtrend_blocked_slope           False                  False
  SHOP           84.38               32            1.11              1.34        171.92                48.53         0.482 below_threshold              0.549             79.2                           0.880               14.41              1.535                                 ok           False                  False
  CRWD           85.00               20            2.51              4.38        247.41                48.36         0.479 below_threshold              0.340             30.7                           0.329               -8.67             -0.894 downtrend_blocked_slope_and_streak           False                  False
  MELI           82.22               45            0.16              2.08       1838.22                40.65         0.478 below_threshold              0.575             89.4                           0.743                8.96              0.748                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-15T10:00:06.074428-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00217500", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "entry_ask": 17.75, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 16.325, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 17.46, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.617, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T09:50:06.230467-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 5.265, "pnl": -6727.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSCO"}
2026-10-15T00:00:06.592550-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-10-14T15:10:06.171047-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T15:05:05.885010-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T15:00:05.913118-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T14:55:05.778063-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T14:50:04.996677-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"allocated_cash": 67275.0, "asset_type": "option", "contract_symbol": "CSCO261120C00115000", "contracts": 115, "early_entry_score": 0.292, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 4547.0, "option_spread_pct": 1.71, "option_volume": 159.0, "success_rate": 86.67, "ticker": "CSCO", "timing_score": 0.547}
2026-10-14T14:50:04.996677-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-14", "training_samples": 6059, "window": 5}
2026-10-14T12:00:05.972511-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015100006)

</details>

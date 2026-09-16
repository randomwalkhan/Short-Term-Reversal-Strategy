# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 10:05:01 EDT`
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

- Cash: `$68,746.10`
- Equity: `$68,746.10`
- Realized PnL: `$58,746.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TMUS     option         option TMUS261016C00185000     70          2026-09-15         2026-09-16          5.1        4.59 -3570.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           85.29               34            1.26              1.14        129.11               105.80         0.681          pass              0.460             30.3                           0.183                2.47             -0.069                                 ok            True                  False
  CTSH          100.00               32            1.01              0.45         63.09                43.25         0.527          pass              0.760             53.6                           0.521               -1.18             -0.177                                 ok            True                  False
  CRWD           88.89               45            0.39              0.66        242.21               100.47         0.687          pass              0.768             87.4                           0.795               12.31              1.354                                 ok           False                  False
    ZS           97.62               42            0.27              0.37        193.73                82.15         0.630          pass              0.938             91.8                           0.833                8.40              0.944                                 ok           False                  False
  PYPL           91.43               35            0.34              0.13         53.75                57.87         0.625          pass              0.763             76.3                           0.758                2.59             -0.102                                 ok           False                  False
   TRI           94.29               35            0.35              0.25        102.50                58.06         0.607          pass              0.842             78.0                           0.779               -3.86             -0.620           downtrend_blocked_streak           False                  False
  TEAM          100.00               38            0.37              0.49        189.60                62.94         0.594          pass              0.902             85.4                           0.749                1.11              0.007                                 ok           False                  False
  AMGN           90.62               32            0.27              0.72        375.34                45.15         0.578          pass              0.488              0.0                           0.242              -14.49             -2.017 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.44               18            0.26              0.05         24.71                25.05         0.572          pass              0.634             46.2                           0.396               -3.13             -0.426            downtrend_blocked_slope           False                  False
   WMT           85.29               34            0.43              0.32        107.95                40.04         0.556          pass              0.391             11.5                           0.169                1.61              0.155                                 ok           False                  False
  ADSK           85.19               27            1.69              2.68        225.35                56.46         0.537          pass              0.357             17.1                           0.222              -10.10             -0.870 downtrend_blocked_slope_and_streak           False                  False
  WDAY           93.75               32            0.95              1.27        190.13                46.67         0.531          pass              0.742             58.4                           0.653               -4.80             -0.688 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-16T10:05:01.503854-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T10:00:05.613145-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "entry_ask": 3.5, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 3.125, "hypothetical_budget": 34373.05, "hypothetical_contracts": 109, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 24.0, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "matched_signals": 35, "recovery_stability_score": 0.729, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-16T09:50:01.541163-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "TMUS261016C00185000", "fill_price": 4.59, "pnl": -3570.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TMUS"}
2026-09-16T00:00:06.550315-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-15T15:10:04.348747-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:05:02.260320-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:00:05.246314-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T14:55:04.231884-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T14:50:04.834862-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-15", "training_samples": 5782, "window": 5}
2026-09-15T14:50:04.834862-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.751, "option_liquidity_status": "wide_spread", "option_open_interest": 7403.0, "option_spread_pct": 15.92, "option_volume": 40.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.562}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916100501)

</details>

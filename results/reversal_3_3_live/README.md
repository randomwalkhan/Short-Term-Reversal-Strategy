# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 10:10:06 EDT`
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

- Cash: `$135,462.30`
- Equity: `$135,462.30`
- Realized PnL: `$125,462.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-14)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS261120C00500000     28          2026-10-13         2026-10-14         25.4       22.86 -7112.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           80.00               15            1.93              6.70        491.64                50.26         0.588          pass              0.150             19.3                           0.238               11.50              0.658                                 ok            True                  False
  UPRO          100.00               10            1.90              2.07        154.51                28.27         0.556          pass              0.472              5.4                           0.183                3.72              0.433                                 ok            True                  False
    ZS           92.59               27            1.98              3.16        227.30                58.33         0.515          pass              0.611             36.9                           0.376               12.40              1.704                                 ok            True                  False
  PYPL           91.67               24            1.09              0.43         55.99                25.14         0.513          pass              0.463              2.4                           0.139                5.77              0.669                                 ok            True                  False
  MSFT           96.30               27            0.59              2.25        542.49                20.68         0.502          pass              0.625             20.6                           0.250                5.33              0.591                                 ok            True                  False
  META           63.64               11            2.09             11.15        757.72                53.30         0.605          pass              0.083              5.3                           0.195                2.95              0.286                                 ok           False                  False
   STX           82.50               40            0.02              0.08        747.17                68.64         0.595          pass              0.625             99.4                           0.804              -19.00             -2.403            downtrend_blocked_slope           False                  False
  TMUS           90.00               40            0.23              0.25        153.62                58.63         0.594          pass              0.763             78.9                           0.608               -5.95             -0.825            downtrend_blocked_slope           False                  False
  QCOM           82.61               23            1.94              2.40        175.83                53.60         0.554          pass              0.245             11.1                           0.193               -5.77             -0.614 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           90.91               11            0.86              0.13         20.83                21.61         0.553          pass              0.453             33.3                           0.316               -3.39             -0.365            downtrend_blocked_slope           False                  False
  MSTR           92.86               14            4.00              4.26        150.35                75.74         0.552          pass              0.438              4.5                           0.141               -4.57             -0.725            downtrend_blocked_slope           False                  False
  INTC           82.61               23            2.59              1.86        102.01                67.54         0.539          pass              0.290             26.5                           0.286              -16.70             -2.072 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-10-14T10:10:06.594596-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:05:04.809604-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:00:05.984655-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00225000", "current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "entry_ask": 15.55, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 14.025, "hypothetical_budget": 67731.15, "hypothetical_contracts": 48, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 21.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.846, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "matched_signals": 36, "recovery_stability_score": 0.846, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.22, "early_entry_score": 0.682, "early_reclaim_pct": 65.5, "matched_signals": 33, "recovery_stability_score": 0.807, "success_rate": 90.91, "ticker": "FTNT", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-14T09:50:06.904742-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "SNPS261120C00500000", "fill_price": 22.86, "pnl": -7112.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-10-14T00:00:06.708726-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-10-13T15:10:06.535380-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-10-13T15:05:06.894886-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-10-13T15:00:04.732732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-10-13T14:55:06.347378-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-10-13T14:50:04.759460-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-13", "training_samples": 6038, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014101006)

</details>

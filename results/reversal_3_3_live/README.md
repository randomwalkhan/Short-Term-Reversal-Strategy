# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:05:04 EDT`
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

- Cash: `$72,316.10`
- Equity: `$72,316.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.37               38            0.72              0.97        191.32                82.09         0.622          pass              0.859             70.2                           0.593                1.04              0.005                                 ok            True                   True
  TEAM          100.00               28            1.73              2.34        191.77                63.46         0.570          pass              0.703             42.0                           0.342               -2.44             -0.308                                 ok            True                  False
   AEP           87.50               16            0.73              0.62        121.96                16.70         0.519          pass              0.351             19.8                           0.248               -0.89             -0.085                                 ok            True                  False
  AAPL           87.50               24            0.89              2.07        332.19                23.75         0.507          pass              0.456             37.4                           0.343                4.19              0.313                                 ok            True                  False
  AMGN           90.91               11            1.45              3.88        379.84                45.29         0.626          pass              0.373              4.1                           0.083              -12.55             -1.922 downtrend_blocked_slope_and_streak           False                  False
  PYPL           91.67               36            0.25              0.09         53.99                58.07         0.621          pass              0.769             74.0                           0.428                2.59              0.037                                 ok           False                  False
  PANW           81.82               44            0.35              0.92        373.54                81.04         0.603          pass              0.554             81.6                           0.611               -2.49              0.061                                 ok           False                  False
  MSTR           80.00               15            5.12              4.91        134.84               103.17         0.573          pass              0.104              4.5                           0.138               -2.26              0.115           downtrend_blocked_streak           False                  False
   WMT           85.71               35            0.35              0.27        108.97                40.03         0.564          pass              0.546             56.8                           0.553                3.65              0.240                                 ok           False                  False
  REGN          100.00                2            2.37             13.19        788.09                29.50         0.562          pass              0.466              3.3                           0.162               -3.03             -0.645 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                8            1.09              1.04        135.90                16.22         0.561          pass              0.477              6.9                           0.134               -2.88             -0.270            downtrend_blocked_slope           False                  False
   EXC          100.00               11            0.68              0.20         42.63                14.63         0.553          pass              0.577             38.3                           0.437               -2.03             -0.205           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-09-15T10:05:04.072258-04:00 early_entry_1005 early_entry_shadow                        {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "entry_ask": 14.15, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 11.19, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "matched_signals": 38, "recovery_stability_score": 0.593, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:00:04.052597-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "entry_ask": 10.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.525, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 602.0, "option_spread_pct": 21.52, "option_volume": 98.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "matched_signals": 42, "recovery_stability_score": 0.701, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:00:04.052597-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "EXC261016C00043000", "fill_price": 0.855, "pnl": -3800.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "EXC"}
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-14T15:00:05.039225-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-14T14:55:02.132179-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-14T14:50:04.030674-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 38000.0, "asset_type": "option", "contract_symbol": "EXC261016C00043000", "contracts": 400, "early_entry_score": 0.606, "entry_mode": "regular", "entry_option_price": 0.95, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 123.0, "option_spread_pct": 10.53, "option_volume": 93.0, "success_rate": 100.0, "ticker": "EXC", "timing_score": 0.551}
2026-09-14T14:50:04.030674-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-14", "training_samples": 5764, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915100504)

</details>

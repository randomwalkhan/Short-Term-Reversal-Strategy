# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:15:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           93.55               31            0.73              0.28         53.91                58.07         0.623            pass              0.635             23.7                           0.208                2.09              0.015                                 ok            True                  False
    ZS           97.37               38            0.73              0.98        191.31                82.09         0.622            pass              0.858             69.9                           0.618                1.04              0.004                                 ok            True                   True
  TEAM          100.00               27            2.03              2.74        191.60                63.46         0.559            pass              0.666             32.1                           0.242               -2.73             -0.322                                 ok            True                  False
  CTSH           97.06               34            0.83              0.37         63.94                45.53         0.510            pass              0.838             75.8                           0.513               -1.56             -0.431                                 ok            True                  False
  AAPL           86.96               23            1.00              2.33        332.08                23.75         0.506            pass              0.412             29.7                           0.268                4.07              0.308                                 ok            True                  False
   AEP           90.48               21            0.61              0.52        122.01                16.70         0.500 below_threshold              0.501             32.9                           0.366               -0.77             -0.079                                 ok            True                  False
  AMGN           90.91               11            1.48              3.94        379.81                45.29         0.624            pass              0.379              6.3                           0.151              -12.56             -1.923 downtrend_blocked_slope_and_streak           False                  False
  MSTR           81.25               16            4.79              4.59        134.97               103.17         0.587            pass              0.164             10.6                           0.185               -1.93              0.131           downtrend_blocked_streak           False                  False
   WMT           85.29               34            0.38              0.29        108.96                40.03         0.567            pass              0.516             52.8                           0.577                3.62              0.239                                 ok           False                  False
   PEP          100.00               10            0.90              0.86        135.97                16.22         0.561            pass              0.524             22.6                           0.414               -2.70             -0.262            downtrend_blocked_slope           False                  False
  REGN          100.00                3            2.34             13.01        788.16                29.50         0.558            pass              0.470              4.9                           0.098               -2.99             -0.643 downtrend_blocked_slope_and_streak           False                  False
  SNPS           71.43               14            2.61              6.96        378.45                61.31         0.557            pass              0.095              4.1                           0.180              -15.49             -1.282            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-15T10:15:01.098518-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "entry_ask": 13.8, "entry_bid": 12.0, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 13.95, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "matched_signals": 38, "recovery_stability_score": 0.618, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 67.1, "matched_signals": 34, "recovery_stability_score": 0.698, "success_rate": 91.18, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:10:06.048953-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "entry_ask": 4.4, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 93, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 28.57, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:05:04.072258-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "entry_ask": 14.15, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 11.19, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "matched_signals": 38, "recovery_stability_score": 0.593, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:00:04.052597-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                  {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "entry_ask": 10.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.525, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 602.0, "option_spread_pct": 21.52, "option_volume": 98.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "matched_signals": 42, "recovery_stability_score": 0.701, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:00:04.052597-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "EXC261016C00043000", "fill_price": 0.855, "pnl": -3800.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "EXC"}
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 93}
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-14T15:00:05.039225-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-14T14:55:02.132179-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915101501)

</details>

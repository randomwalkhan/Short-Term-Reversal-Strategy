# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 11:30:04 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           92.31               26            2.84              3.13        155.80                99.69         0.634          pass              0.519              6.9                           0.174               17.80              2.092                      ok            True                  False
    ZS           97.44               39            0.93              1.30        198.83                81.58         0.589          pass              0.822             56.7                           0.554                1.88              0.353                      ok            True                  False
   BKR           85.71               14            1.49              0.59         56.87                32.18         0.516          pass              0.409             59.5                           0.422               -0.79              0.080                      ok            True                  False
  PYPL           92.59               27            0.96              0.36         54.12                35.54         0.513          pass              0.549             16.1                           0.250               -0.09              0.213                      ok            True                  False
   WBD           95.00               40            0.15              0.03         30.89                38.06         0.574          pass              0.842             61.5                           0.521               10.08              1.215                      ok           False                  False
   TRI           87.50               32            1.09              0.74         97.01                56.59         0.568          pass              0.540             45.6                           0.316               -6.18             -0.310 downtrend_blocked_slope           False                  False
  AMGN           87.50               40            0.12              0.35        417.98                46.33         0.567          pass              0.724             89.2                           0.644               11.18              1.227                      ok           False                  False
   KDP           80.00                5            1.56              0.34         31.31                25.35         0.537          pass              0.199             48.4                           0.420               -0.94              0.018                      ok           False                  False
  CDNS           68.18               22            1.54              3.53        325.19                46.51         0.529          pass              0.314             60.3                           0.651               17.41              1.978                      ok           False                  False
  CTAS           83.33                6            1.86              2.62        199.46                21.05         0.527          pass              0.168              8.8                           0.264               -1.06             -0.024                      ok           False                  False
  PANW           71.43               28            2.36              6.49        389.31                69.78         0.524          pass              0.276             34.4                           0.610                2.06              0.425                      ok           False                  False
  TMUS           70.00               10            2.08              2.42        165.41                33.31         0.522          pass              0.071              6.4                           0.219               -9.68             -0.717 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-29T11:30:04.434130-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                       {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "entry_ask": 15.8, "entry_bid": 15.25, "entry_mode": "early", "entry_option_price": 15.525, "hypothetical_budget": 39379.15, "hypothetical_contracts": 25, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 3.54, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "matched_signals": 42, "recovery_stability_score": 0.731, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:25:05.375211-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:20:05.555943-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:15:04.210610-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:10:05.512150-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:05:04.326934-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:00:04.441545-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "entry_ask": 2.4, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.325, "hypothetical_budget": 39379.15, "hypothetical_contracts": 169, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 6.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "matched_signals": 34, "recovery_stability_score": 0.563, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.801, "early_reclaim_pct": 62.3, "matched_signals": 37, "recovery_stability_score": 0.581, "success_rate": 94.59, "ticker": "ORLY", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T10:55:05.493456-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:50:04.346665-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:45:06.219567-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929113004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929113004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929113004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929113004)

</details>

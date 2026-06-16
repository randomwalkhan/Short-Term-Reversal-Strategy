# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-16 14:00:02 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$25,985.75`
- Equity: `$25,985.75`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  ROST     option         option ROST260717C00240000     23          2026-06-15         2026-06-16         5.75       5.175 -1322.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  DRAM           88.24               17            2.36              1.18         70.57               109.99         0.699          pass              0.485             49.7                           0.573               -0.26              0.315                  ok            True                  False
  MRVL          100.00               12            4.69             10.14        304.53               145.02         0.684          pass              0.560             26.3                           0.473                1.24             -0.226                  ok            True                  False
  AMAT           89.29               28            1.02              4.19        583.99                72.99         0.598          pass              0.594             55.7                           0.476               18.31              2.061                  ok            True                  False
   TXN           91.30               23            1.24              2.71        312.18                52.85         0.581          pass              0.521             24.9                           0.362                0.44              0.110                  ok            True                  False
  PAYX          100.00               11            1.67              1.18        100.40                31.37         0.580          pass              0.465              0.0                           0.036               -1.56              0.070                  ok            True                  False
  ROST           96.77               31            0.62              1.03        236.33                39.26         0.564          pass              0.725             42.8                           0.366                5.34              0.488                  ok            True                  False
   ADI           93.33               30            0.66              1.99        426.73                53.45         0.564          pass              0.685             46.5                           0.373                0.36             -0.068                  ok            True                  False
  UPRO           91.67               24            1.01              1.04        146.29                48.01         0.562          pass              0.525             21.4                           0.349               -3.72             -0.435                  ok            True                  False
  NXPI           93.75               16            2.44              5.40        313.56                59.92         0.555          pass              0.522             19.8                           0.327               -4.78             -0.431                  ok            True                  False
   CSX           95.45               22            0.75              0.25         47.28                20.12         0.537          pass              0.647             37.7                           0.232                1.94              0.261                  ok            True                  False
   LIN           95.00               20            0.96              3.51        519.98                19.32         0.526          pass              0.629             36.6                           0.356                4.48              0.434                  ok            True                  False
  MCHP          100.00               12            2.89              2.03         99.45                60.62         0.522          pass              0.561             31.9                           0.387                0.47              0.236                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-06-16T11:52:05.052043-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T11:10:06.057140-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T10:36:17.030970-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "MAR260717C00400000", "current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "entry_ask": 13.9, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 12992.88, "hypothetical_contracts": 10, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 400.0, "option_spread_pct": 18.9, "option_volume": 13.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "matched_signals": 32, "recovery_stability_score": 0.854, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-16T10:36:17.030970-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "ROST260717C00240000", "fill_price": 5.175, "pnl": -1322.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ROST"}
2026-06-16T10:14:03.006542-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T09:17:33.022205-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-06-16T09:07:53.036386-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-06-16T08:52:12.067336-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-06-16T08:35:06.869974-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-06-16T08:34:05.066207-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260616140002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260616140002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260616140002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260616140002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:30:06 EST`
Last processed slot: `manage_1030`

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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           86.67               30            1.17              1.41        171.87                68.34         0.589          pass              0.535             55.0                           0.508                5.17              0.724                      ok            True                  False
   CEG           87.50               32            1.24              2.42        278.73                61.55         0.564          pass              0.544             46.8                           0.275                7.41              1.240                      ok            True                  False
  ISRG           90.62               32            0.79              2.45        442.54                45.74         0.560          pass              0.607             40.3                           0.398                0.74             -0.274                      ok            True                  False
  AAPL           95.83               24            0.72              1.81        355.50                27.52         0.552          pass              0.610             20.6                           0.225                4.62              0.585                      ok            True                  False
  MSFT           96.30               27            0.93              3.40        522.42                36.51         0.541          pass              0.658             30.2                           0.262                2.35             -0.087                      ok            True                  False
  DXCM           83.33               36            0.85              0.50         83.12                50.11         0.533          pass              0.396             26.8                           0.276               -2.52             -0.413                      ok            True                  False
  NXPI           92.86               14            2.44              4.54        263.15                48.08         0.526          pass              0.542             40.0                           0.673                0.53              0.304                      ok            True                  False
  ALNY           65.22               23            2.35              2.72        163.88               110.81         0.715          pass              0.227             23.0                           0.310                2.00              0.140                      ok           False                  False
  INTC           63.64               11            6.07              2.54         58.57               143.21         0.673          pass              0.108             11.4                           0.208               -6.56              0.127                      ok           False                  False
  FTNT           64.71               17            2.75              2.45        126.17                93.31         0.671          pass              0.156             14.0                           0.207               -1.97              0.004                      ok           False                  False
  UPRO           80.00                5            3.77              3.65        136.93                68.17         0.587          pass              0.101             14.0                           0.207               -4.21             -0.141                      ok           False                  False
   BKR           60.00               10            2.67              0.92         49.04                57.94         0.574          pass              0.104             15.4                           0.271               -8.86             -0.552 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T10:30:06.080468-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:25:05.577386-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:20:06.177663-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:15:06.368361-05:00 early_entry_1015 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "entry_ask": 11.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.225, "hypothetical_budget": 58512.4, "hypothetical_contracts": 52, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "matched_signals": 36, "recovery_stability_score": 0.574, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:05:06.161722-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:00:04.523594-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116103006)

</details>

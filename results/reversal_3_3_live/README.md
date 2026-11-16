# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:20:06 EST`
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
  QCOM           87.10               31            1.04              1.26        171.93                68.34         0.591          pass              0.568             59.9                           0.521                5.30              0.730                      ok            True                  False
  AAPL           96.00               25            0.61              1.53        355.62                27.52         0.553          pass              0.654             32.9                           0.262                4.74              0.590                      ok            True                  False
   CEG           87.50               32            1.46              2.87        278.55                61.55         0.550          pass              0.513             37.2                           0.251                7.16              1.230                      ok            True                  False
  ISRG           91.43               35            0.68              2.11        442.68                45.74         0.549          pass              0.672             48.4                           0.382                0.85             -0.269                      ok            True                  False
  MSFT           96.00               25            1.05              3.84        522.23                36.51         0.546          pass              0.600             15.1                           0.151                2.22             -0.092                      ok            True                  False
  DXCM           83.33               36            0.94              0.55         83.10                50.11         0.528          pass              0.367             17.5                           0.169               -2.61             -0.417                      ok            True                  False
  NXPI           91.67               12            2.68              4.98        262.96                48.08         0.523          pass              0.479             34.1                           0.504                0.29              0.293                      ok            True                  False
  ALNY           58.82               17            2.69              3.11        163.71               110.81         0.722          pass              0.155             11.9                           0.125                1.65              0.125                      ok           False                  False
  INTC           63.64               11            6.02              2.51         58.58               143.21         0.676          pass              0.111             12.2                           0.190               -6.50              0.129                      ok           False                  False
  FTNT           57.14               14            3.02              2.69        126.07                93.31         0.666          pass              0.097              1.4                           0.046               -2.24             -0.009                      ok           False                  False
  TEAM           77.78               27            1.82              1.91        149.17                76.26         0.577          pass              0.337             55.3                           0.473              -21.29             -2.935 downtrend_blocked_slope           False                  False
  UPRO           80.00                5            3.99              3.87        136.84                68.17         0.576          pass              0.068              3.3                           0.088               -4.43             -0.152                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T10:20:06.177663-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:15:06.368361-05:00 early_entry_1015 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "entry_ask": 11.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.225, "hypothetical_budget": 58512.4, "hypothetical_contracts": 52, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "matched_signals": 36, "recovery_stability_score": 0.574, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:05:06.161722-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:00:04.523594-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-06T15:05:05.959531-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-06T15:00:05.889317-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116102006)

</details>

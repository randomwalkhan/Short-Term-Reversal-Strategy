# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 10:35:02 EDT`
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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           88.89               18            2.36              5.15        309.25                64.14         0.591          pass              0.462             37.4                           0.666                6.52              0.543                                 ok            True                  False
  QCOM           83.33               30            1.01              1.34        188.59                63.33         0.588          pass              0.501             73.3                           0.800               -0.78              0.265                                 ok            True                  False
   ADI           83.33               24            1.62              4.47        393.73                55.18         0.577          pass              0.362             40.6                           0.647               -0.64             -0.001                                 ok            True                  False
  UPRO           88.00               25            1.02              1.04        145.71                40.56         0.562          pass              0.523             51.3                           0.450                4.26              0.397                                 ok            True                  False
  NXPI           85.00               20            2.30              4.70        290.25                55.03         0.544          pass              0.358             34.6                           0.616                2.58              0.427                                 ok            True                  False
   LIN          100.00               17            1.06              3.92        528.11                20.88         0.534          pass              0.556             18.6                           0.267                2.57              0.049                                 ok            True                  False
  AVGO           81.48               27            1.37              3.82        398.33                49.47         0.533          pass              0.382             58.5                           0.775                5.92              0.825                                 ok            True                  False
  CSCO           95.65               23            0.98              0.83        120.95                35.64         0.530          pass              0.752             70.6                           0.888                2.44              0.348                                 ok            True                  False
   MAR           92.31               13            1.52              4.01        374.39                19.73         0.526          pass              0.459             19.4                           0.215               -1.20              0.036                                 ok            True                  False
  KLAC           81.82               22            2.52              4.08        229.77               110.61         0.687          pass              0.349             50.6                           0.826              -18.93             -2.520 downtrend_blocked_slope_and_streak           False                  False
  AMAT           83.33               18            2.48             10.45        598.02                98.14         0.652          pass              0.377             56.5                           0.811              -15.41             -1.852 downtrend_blocked_slope_and_streak           False                  False
    MU           83.33               18            4.18             28.65        967.02               112.95         0.619          pass              0.344             46.6                           0.792              -18.05             -1.853            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-13T10:35:02.047813-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:30:06.369215-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:25:04.964455-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:20:02.018219-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:15:05.926049-04:00 early_entry_1015 early_entry_shadow                   {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "entry_ask": 14.0, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 13.3, "hypothetical_budget": 13497.63, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 840.0, "option_spread_pct": 10.53, "option_volume": 123.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "matched_signals": 38, "recovery_stability_score": 0.761, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:10:04.827690-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "entry_ask": 15.1, "entry_bid": 12.2, "entry_mode": "early", "entry_option_price": 13.65, "hypothetical_budget": 13497.63, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 840.0, "option_spread_pct": 21.25, "option_volume": 123.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "matched_signals": 40, "recovery_stability_score": 0.769, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:00:02.015857-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:00:02.015857-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-13T09:55:05.995868-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-07-13T09:20:04.012010-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'empty': 63, 'saved': 30}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713103502)

</details>

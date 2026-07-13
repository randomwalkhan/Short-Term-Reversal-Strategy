# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 10:20:02 EDT`
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
   TXN           84.62               13            3.02              6.59        308.64                64.14         0.579          pass              0.261             19.9                           0.403                5.80              0.512                                 ok            True                  False
   ADI           85.71               21            2.03              5.63        393.24                55.18         0.574          pass              0.359             25.3                           0.551               -1.07             -0.020                                 ok            True                  False
  UPRO           90.91               22            1.22              1.25        145.62                40.56         0.572          pass              0.553             41.5                           0.367                4.04              0.387                                 ok            True                  False
  QCOM           81.48               27            1.64              2.17        188.23                63.33         0.567          pass              0.380             56.7                           0.594               -1.41              0.236                                 ok            True                  False
   LIN          100.00               13            1.19              4.43        527.89                20.88         0.554          pass              0.476              0.2                           0.034                2.43              0.043                                 ok            True                  False
  CSCO           90.00               10            1.92              1.63        120.61                35.64         0.553          pass              0.449             42.5                           0.615                1.47              0.304                                 ok            True                  False
  AMGN           90.00               10            1.65              4.19        361.59                21.45         0.547          pass              0.346              8.1                           0.243               -0.87             -0.074                                 ok            True                  False
  NXPI           83.33               18            2.73              5.58        289.87                55.03         0.529          pass              0.262             22.3                           0.477                2.13              0.407                                 ok            True                  False
  AVGO           82.61               23            2.03              5.69        397.53                49.47         0.520          pass              0.323             38.3                           0.683                5.21              0.794                                 ok            True                  False
  MPWR           80.95               21            3.88             36.71       1337.01                78.41         0.515          pass              0.201             16.9                           0.482               -0.80             -0.107                                 ok            True                  False
  KLAC           81.25               16            3.43              5.55        229.14               110.61         0.671          pass              0.239             32.9                           0.674              -19.68             -2.563 downtrend_blocked_slope_and_streak           False                  False
  AMAT           78.57               14            3.34             14.08        596.46                98.14         0.621          pass              0.213             41.4                           0.745              -16.16             -1.893 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-13T10:20:02.018219-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:15:05.926049-04:00 early_entry_1015 early_entry_shadow                   {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "entry_ask": 14.0, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 13.3, "hypothetical_budget": 13497.63, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 840.0, "option_spread_pct": 10.53, "option_volume": 123.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "matched_signals": 38, "recovery_stability_score": 0.761, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:10:04.827690-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "entry_ask": 15.1, "entry_bid": 12.2, "entry_mode": "early", "entry_option_price": 13.65, "hypothetical_budget": 13497.63, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 840.0, "option_spread_pct": 21.25, "option_volume": 123.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "matched_signals": 40, "recovery_stability_score": 0.769, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:00:02.015857-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:00:02.015857-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-07-13T09:55:05.995868-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-07-13T09:20:04.012010-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'empty': 63, 'saved': 30}
2026-07-10T15:10:08.910811-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-10T15:05:06.429039-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-07-10T15:00:09.226035-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713102002)

</details>

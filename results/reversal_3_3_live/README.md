# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 10:15:06 EDT`
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

- Cash: `$13,976.50`
- Equity: `$26,696.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$-1,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   1     96     13920.0                 12720.0         1.45           1.32       33.12         32.18          bid_ask_mid                       1.32                bid_ask_mid                    True         -1200.0                  -8.62         100.0               15              0.76         30.37           38.09                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   EXC           90.91               11            1.09              0.36         47.72                22.14         0.596          pass              0.368              3.7                           0.088                3.38              0.277                      ok            True                  False
   XEL          100.00               10            1.24              0.71         81.65                20.81         0.590          pass              0.460              0.5                           0.151                4.56              0.300                      ok            True                  False
  PAYX          100.00               18            1.39              1.04        105.91                31.56         0.553          pass              0.509              0.0                           0.190                6.75              0.867                      ok            True                  False
  MNST          100.00               17            0.96              0.66         97.32                16.38         0.541          pass              0.571             23.6                           0.237                5.82              0.581                      ok            True                  False
  BKNG           82.61               23            1.40              1.81        183.79                41.33         0.527          pass              0.269             20.1                           0.204                5.94              0.818                      ok            True                  False
   WBD           87.50                8            0.94              0.18         26.40                22.17         0.607          pass              0.382             40.5                           0.322                0.11             -0.097                      ok           False                  False
   KHC          100.00                2            2.78              0.49         25.16                36.79         0.592          pass              0.459              0.0                           0.170                8.09              1.239                      ok           False                  False
   PEP           80.00                5            1.83              1.85        143.43                27.18         0.575          pass              0.064              2.0                           0.051               -0.31             -0.037                      ok           False                  False
   ADP          100.00                9            1.89              3.20        240.90                30.79         0.569          pass              0.457              0.0                           0.177                8.83              1.077                      ok           False                  False
  CTAS           76.92               13            1.62              2.06        180.49                35.27         0.559          pass              0.102              8.7                           0.211                4.44              0.522                      ok           False                  False
  CPRT           88.89                9            2.32              0.49         29.80                43.39         0.552          pass              0.307              4.8                           0.093               -3.03             -0.349 downtrend_blocked_slope           False                  False
   KDP          100.00                1            3.12              0.73         32.99                28.43         0.539          pass              0.461              2.3                           0.067                5.62              0.904                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-07-06T10:15:06.215817-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:10:04.251643-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:05:02.304472-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRSK260821C00185000", "current_drop_pct": 0.57, "early_entry_score": 0.708, "early_reclaim_pct": 79.8, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 12.8, "hypothetical_budget": 6988.25, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 1.0, "option_spread_pct": null, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.708, "early_reclaim_pct": 79.8, "matched_signals": 37, "recovery_stability_score": 0.776, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:00:05.336949-04:00 early_entry_1000 early_entry_shadow                   {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.82, "early_entry_score": 0.749, "early_reclaim_pct": 70.7, "entry_ask": 21.9, "entry_bid": 17.1, "entry_mode": "early", "entry_option_price": 19.5, "hypothetical_budget": 6988.25, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 24.62, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 91.89, "ticker": "ROP", "timing_score": 0.399, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.749, "early_reclaim_pct": 70.7, "matched_signals": 37, "recovery_stability_score": 0.712, "success_rate": 91.89, "ticker": "ROP", "timing_score": 0.399, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T03:00:03.074522-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-07-04T02:55:10.939731-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:50:08.940118-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:45:08.118438-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:40:02.422082-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:35:05.961779-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706101506)

</details>

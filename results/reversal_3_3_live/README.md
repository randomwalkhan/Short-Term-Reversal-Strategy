# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 10:30:05 EDT`
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

- Cash: `$26,504.50`
- Equity: `$26,504.50`
- Realized PnL: `$16,504.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-06)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KDP     option         option KDP260821C00033000     96          2026-07-02         2026-07-06         1.45       1.305 -1392.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   WBD           91.67               12            0.81              0.15         26.42                22.17         0.594          pass              0.530             48.8                           0.503                0.25             -0.091                      ok            True                  False
   EXC           83.33               12            1.07              0.36         47.73                22.14         0.579          pass              0.211             17.1                           0.258                3.41              0.278                      ok            True                  False
  PAYX          100.00               16            1.50              1.12        105.87                31.56         0.558          pass              0.503              2.3                           0.048                6.63              0.862                      ok            True                  False
  CTAS           82.35               17            1.45              1.84        180.58                35.27         0.548          pass              0.242             26.0                           0.255                4.62              0.530                      ok            True                  False
  MNST          100.00               16            1.26              0.86         97.23                16.38         0.526          pass              0.539             15.5                           0.232                5.51              0.567                      ok            True                  False
  VRTX           90.00               10            1.81              6.70        525.17                28.87         0.521          pass              0.436             39.0                           0.554               14.80              1.359                      ok            True                  False
  BKNG           85.71               28            1.24              1.60        183.88                41.33         0.508          pass              0.411             29.4                           0.301                6.11              0.826                      ok            True                  False
   XEL          100.00                8            1.33              0.76         81.63                20.81         0.595          pass              0.499             13.1                           0.198                4.47              0.296                      ok           False                  False
   PEP           80.00                5            1.83              1.85        143.43                27.18         0.574          pass              0.078              7.0                           0.164               -0.31             -0.037                      ok           False                  False
   ADP          100.00                9            1.83              3.10        240.94                30.79         0.572          pass              0.483              8.8                           0.188                8.90              1.080                      ok           False                  False
   KHC          100.00                2            3.17              0.56         25.13                36.79         0.560          pass              0.475              6.4                           0.140                7.65              1.221                      ok           False                  False
  CPRT          100.00                4            2.85              0.60         29.75                43.39         0.559          pass              0.466              3.4                           0.162               -3.56             -0.374 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-07-06T10:30:05.295059-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:25:05.297833-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:20:05.672223-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:20:05.672223-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "KDP260821C00033000", "fill_price": 1.305, "pnl": -1392.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KDP"}
2026-07-06T10:15:06.215817-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:10:04.251643-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:05:02.304472-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRSK260821C00185000", "current_drop_pct": 0.57, "early_entry_score": 0.708, "early_reclaim_pct": 79.8, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 12.8, "hypothetical_budget": 6988.25, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 1.0, "option_spread_pct": null, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.708, "early_reclaim_pct": 79.8, "matched_signals": 37, "recovery_stability_score": 0.776, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:00:05.336949-04:00 early_entry_1000 early_entry_shadow                   {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.82, "early_entry_score": 0.749, "early_reclaim_pct": 70.7, "entry_ask": 21.9, "entry_bid": 17.1, "entry_mode": "early", "entry_option_price": 19.5, "hypothetical_budget": 6988.25, "hypothetical_contracts": 3, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 24.62, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 91.89, "ticker": "ROP", "timing_score": 0.399, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.749, "early_reclaim_pct": 70.7, "matched_signals": 37, "recovery_stability_score": 0.712, "success_rate": 91.89, "ticker": "ROP", "timing_score": 0.399, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T03:00:03.074522-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-07-04T02:55:10.939731-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706103005)

</details>

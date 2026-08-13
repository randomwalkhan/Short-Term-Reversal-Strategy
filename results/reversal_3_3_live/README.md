# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 09:40:07 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  INSM           86.96               46            0.54              0.50        132.06               107.72         0.731          pass              0.663             68.1                           0.499               29.63              3.874                       ok            True                  False
  FAST          100.00               19            0.82              0.30         52.09                25.01         0.585          pass              0.532              4.4                           0.125               10.99              1.181                       ok            True                  False
  BKNG           96.55               29            1.19              1.77        211.50                44.60         0.565          pass              0.629             15.4                           0.230                8.53              1.172                       ok            True                  False
   BKR           81.25               16            1.32              0.59         64.03                33.24         0.561          pass              0.261             43.9                           0.261                6.29              0.778                       ok            True                  False
  ISRG           86.49               37            0.32              0.90        400.89                69.94         0.676          pass              0.582             53.8                           0.333               13.32              1.338                       ok           False                  False
  DXCM           90.00               40            0.20              0.13         90.75                59.17         0.609          pass              0.709             60.5                           0.397               21.57              1.232                       ok           False                  False
  ABNB           95.65               46            0.06              0.08        180.06                64.05         0.608          pass              0.893             77.6                           0.419               17.63              2.249                       ok           False                  False
   ROP           97.44               39            0.06              0.16        395.16                44.32         0.593          pass              0.907             84.8                           0.550                1.48              0.203                       ok           False                  False
  DASH          100.00               44            0.21              0.32        212.35                48.36         0.534          pass              0.895             80.5                           0.442                9.56              1.055                       ok           False                  False
  ADSK           83.78               37            0.47              0.83        249.16                45.76         0.520          pass              0.586             84.3                           0.598                5.69              0.854                       ok           False                  False
  ROST           83.33               12            1.76              3.06        246.94                22.10         0.518          pass              0.226             24.0                           0.233               -3.44             -0.142 downtrend_blocked_streak           False                  False
   HON           92.68               41            0.18              0.30        235.21                35.57         0.512          pass              0.760             56.7                           0.330               -2.90             -0.581  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-12T16:10:05.737758-04:00      manage_1600                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "PYPL260918C00057500", "fill_price": 3.275, "pnl": 2945.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.96, "ticker": "PYPL"}
2026-08-12T15:10:02.859897-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T15:05:01.844432-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T15:00:05.838076-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T14:55:05.864031-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-12T14:50:05.779182-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"early_entry_score": 0.604, "option_liquidity_status": "low_volume", "option_open_interest": 178.0, "option_spread_pct": 8.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.806}
2026-08-12T14:50:05.779182-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-12", "training_samples": 5645, "window": 5}
2026-08-12T14:50:05.779182-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 17360.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 62, "early_entry_score": 0.819, "entry_mode": "regular", "entry_option_price": 2.8, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7246.0, "option_spread_pct": 5.71, "option_volume": 86.0, "success_rate": 93.94, "ticker": "PYPL", "timing_score": 0.657}
2026-08-12T12:00:04.666373-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T11:55:01.784821-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "BKNG260911C00210000", "current_drop_pct": 1.06, "early_entry_score": 0.858, "early_reclaim_pct": 95.4, "entry_ask": 8.3, "entry_bid": 7.3, "entry_mode": "early", "entry_option_price": 7.8, "hypothetical_budget": 17549.0, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 53.0, "option_spread_pct": 12.82, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 96.77, "ticker": "BKNG", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.858, "early_reclaim_pct": 95.4, "matched_signals": 31, "recovery_stability_score": 0.759, "success_rate": 96.77, "ticker": "BKNG", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813094007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813094007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813094007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813094007)

</details>

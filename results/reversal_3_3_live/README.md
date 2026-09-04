# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:00:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$37,600.60`
- Equity: `$78,685.60`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$4,207.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261016C00110000       2026-09-03                   1     99     36877.5                 41085.0         3.72           4.15      108.86        110.21          bid_ask_mid                       4.15                bid_ask_mid                    True          4207.5                  11.41         89.19               37              0.54         28.76           28.42                  36.36                2875.0          348.0               0.04                      ok
```

## Today's Closed Trades (2026-09-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           87.50               16            2.42              7.04        413.29                57.80         0.593          pass              0.331             10.7                           0.110                2.11              0.308                                 ok            True                  False
  AMGN          100.00               11            1.38              4.30        442.28                21.54         0.556          pass              0.560             32.5                           0.230               -0.31             -0.032                                 ok            True                  False
  MELI          100.00               30            0.98             13.72       1985.18                45.76         0.543          pass              0.653             21.8                           0.217                2.53              0.221                                 ok            True                  False
  PAYX          100.00               11            1.81              1.59        124.40                25.54         0.542          pass              0.562             33.8                           0.482               -1.34             -0.093                                 ok            True                  False
  NFLX           88.24               17            1.79              1.04         82.23                32.95         0.528          pass              0.319              0.0                           0.183                2.01              0.225                                 ok            True                  False
 CMCSA           92.59               27            0.64              0.12         26.60                25.91         0.522          pass              0.526              8.1                           0.225               -1.38             -0.197                                 ok            True                  False
    ZS          100.00               25            2.32              2.89        176.56                62.66         0.518          pass              0.755             67.6                           0.821               -4.44             -0.013                                 ok            True                  False
  WDAY           85.71               14            4.25              6.16        204.28                73.93         0.516          pass              0.290             19.8                           0.208               -0.94              0.274                                 ok            True                  False
  CHTR           90.91               44            0.52              0.55        151.15                61.35         0.510          pass              0.672             43.5                           0.310                0.29              0.037                                 ok            True                  False
   KHC           90.32               31            0.52              0.09         24.98                29.47         0.507          pass              0.466              0.0                           0.251               -2.70              0.036                                 ok            True                  False
  MNST           86.49               37            0.22              0.07         44.05               424.09         0.998          pass              0.686             77.9                           0.604               -7.96             -1.134 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                6            2.57              1.02         56.38                56.63         0.626          pass              0.539             25.5                           0.383              -10.06             -1.576 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-04T10:00:02.334638-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T00:00:05.130277-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
2026-09-03T15:10:05.000086-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.577, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.28, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "REGN", "timing_score": 0.533}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.72, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 85.0, "option_spread_pct": 12.16, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.542}
2026-09-03T14:50:04.996854-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-03", "training_samples": 5764, "window": 5}
2026-09-03T14:50:04.996854-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 36877.5, "asset_type": "option", "contract_symbol": "CSCO261016C00110000", "contracts": 99, "early_entry_score": 0.681, "entry_mode": "regular", "entry_option_price": 3.725, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2875.0, "option_spread_pct": 4.03, "option_volume": 348.0, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511}
2026-09-03T12:00:04.745572-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "DASH261016C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "entry_ask": 9.55, "entry_bid": 9.3, "entry_mode": "early", "entry_option_price": 9.425, "hypothetical_budget": 37239.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 365.0, "option_spread_pct": 2.65, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.852, "early_reclaim_pct": 70.1, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 100.0, "ticker": "DASH", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904100002)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:40:01 EDT`
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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               11            1.40              4.36        442.25                21.54         0.555          pass              0.557             31.6                           0.316               -0.33             -0.033                                 ok            True                  False
  PAYX          100.00               13            1.47              1.29        124.53                25.54         0.549          pass              0.614             46.3                           0.679               -1.00             -0.077                                 ok            True                  False
  MELI          100.00               35            0.52              7.27       1987.94                45.76         0.540          pass              0.796             58.6                           0.414                3.01              0.242                                 ok            True                  False
   WMT           85.71               35            0.57              0.43        108.23                40.07         0.533          pass              0.470             32.6                           0.193                3.95              0.307                                 ok            True                  False
  WDAY           85.71               21            3.45              5.00        204.78                73.93         0.520          pass              0.382             34.9                           0.616               -0.12              0.312                                 ok            True                  False
 CMCSA           92.00               25            0.92              0.17         26.58                25.91         0.514          pass              0.494              7.5                           0.153               -1.66             -0.209                                 ok            True                  False
  NFLX           80.00               10            2.51              1.45         82.05                32.95         0.514          pass              0.058              2.1                           0.122                1.26              0.192                                 ok            True                  False
   KDP           86.67               30            0.71              0.16         32.81                30.98         0.510          pass              0.435             24.2                           0.212                1.89              0.171                                 ok            True                  False
  CHTR           90.00               40            0.96              1.02        150.94                61.35         0.504          pass              0.534              5.5                           0.173               -0.17              0.017                                 ok            True                  False
  MNST           86.21               29            0.62              0.19         44.00               424.09         0.998          pass              0.500             36.0                           0.219               -8.34             -1.153 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                4            3.26              1.29         56.27                56.63         0.600          pass              0.477              5.6                           0.119              -10.69             -1.608 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.00               25            3.12              3.16        143.46               101.55         0.585          pass              0.316             52.5                           0.622               17.65              1.259                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-04T10:40:01.177649-04:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.77, "early_entry_score": 0.803, "early_reclaim_pct": 81.6, "entry_ask": 15.3, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 40580.3, "hypothetical_contracts": 29, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 25.0, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.803, "early_reclaim_pct": 81.6, "matched_signals": 38, "recovery_stability_score": 0.893, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:35:02.277988-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 1.06, "early_entry_score": 0.757, "early_reclaim_pct": 74.6, "entry_ask": 14.4, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.95, "hypothetical_budget": 40580.3, "hypothetical_contracts": 31, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 22.39, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.895, "shadow_only": true, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.757, "early_reclaim_pct": 74.6, "matched_signals": 36, "recovery_stability_score": 0.895, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:30:01.189639-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 82.8, "entry_ask": 13.9, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 12.55, "hypothetical_budget": 40580.3, "hypothetical_contracts": 32, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 21.51, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.942, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 82.8, "matched_signals": 38, "recovery_stability_score": 0.942, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:25:02.305265-04:00 early_entry_1025 early_entry_shadow   {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.79, "early_entry_score": 0.802, "early_reclaim_pct": 81.2, "entry_ask": 13.7, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 12.45, "hypothetical_budget": 40580.3, "hypothetical_contracts": 32, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 20.08, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.924, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.802, "early_reclaim_pct": 81.2, "matched_signals": 38, "recovery_stability_score": 0.924, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:20:02.325434-04:00 early_entry_1020 early_entry_shadow                                {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "entry_ask": 16.5, "entry_bid": 14.4, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 40580.3, "hypothetical_contracts": 26, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 158.0, "option_spread_pct": 13.59, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "matched_signals": 33, "recovery_stability_score": 0.831, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:15:04.189474-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CSCO261016C00110000", "fill_price": 4.4, "pnl": 6682.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.12, "ticker": "CSCO"}
2026-09-04T10:10:01.256246-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:05:05.442075-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:00:02.334638-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904104001)

</details>

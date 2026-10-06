# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 10:30:05 EDT`
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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           89.66               29            0.98             10.13       1475.55                53.63         0.581          pass              0.597             51.6                           0.315                6.30              0.804                                 ok            True                  False
  ABNB           82.61               23            1.42              1.63        163.37                40.56         0.532          pass              0.221              3.9                           0.210               -0.05              0.587                                 ok            True                  False
  DRAM           84.00               25            2.21              0.96         61.26                49.40         0.528          pass              0.261              0.4                           0.105               -5.21             -0.196                                 ok            True                  False
  AMAT           82.76               29            1.95              7.40        539.11                48.32         0.503          pass              0.255              1.6                           0.127               12.54              1.582                                 ok            True                  False
  META           84.62               39            0.22              1.13        741.42                55.50         0.591          pass              0.583             69.1                           0.536                0.50             -0.219                                 ok           False                  False
  INTC           88.89               36            1.36              1.10        115.72                74.54         0.564          pass              0.467              0.0                           0.163               -7.46             -0.739 downtrend_blocked_slope_and_streak           False                  False
  QCOM           90.24               41            0.30              0.37        180.63                57.17         0.558          pass              0.719             63.3                           0.433               -9.09             -1.090 downtrend_blocked_slope_and_streak           False                  False
  ASML           79.31               29            0.94             12.26       1854.60                40.48         0.539          pass              0.181              0.0                           0.183                5.40              0.778                                 ok           False                  False
    MU           92.50               40            0.33              2.49       1062.89                46.96         0.517          pass              0.824             79.7                           0.442               -3.26             -0.157                                 ok           False                  False
  TEAM          100.00               40            0.36              0.50        196.44                55.00         0.510          pass              0.850             66.4                           0.421                3.86              0.159                                 ok           False                  False
  AMGN           81.25               16            1.29              3.64        401.42                46.96         0.508          pass              0.189             21.8                           0.203               -3.04             -0.213           downtrend_blocked_streak           False                  False
  TMUS           89.19               37            0.20              0.24        164.54                30.04         0.505          pass              0.707             77.0                           0.715                1.17             -0.058                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-06T10:30:05.477700-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:25:05.769883-04:00 early_entry_1025 early_entry_shadow                                          {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "entry_ask": 13.6, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 13.33, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:20:05.384079-04:00 early_entry_1020 early_entry_shadow                                                 {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "entry_ask": 13.1, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 52573.4, "hypothetical_contracts": 42, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 9.6, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.723, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.723, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:15:05.337195-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:10:04.391057-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:05:04.347348-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "entry_ask": 4.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.8, "hypothetical_budget": 52573.4, "hypothetical_contracts": 138, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 21.05, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.784, "early_reclaim_pct": 66.7, "matched_signals": 34, "recovery_stability_score": 0.637, "success_rate": 94.12, "ticker": "BKR", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:00:02.462849-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T09:50:05.348208-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MRVL261120C00270000", "fill_price": 33.65, "pnl": 16560.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 37.63, "ticker": "MRVL"}
2026-10-06T00:00:06.226199-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-10-05T15:10:05.053706-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006103005)

</details>

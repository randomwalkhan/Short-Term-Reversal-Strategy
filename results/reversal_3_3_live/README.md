# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 11:00:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.77              1.95        156.30                99.69         0.685          pass              0.545              0.0                           0.170               19.10              2.142                                 ok            True                  False
    ZS           97.06               34            1.60              2.24        198.43                81.58         0.576          pass              0.694             25.4                           0.186                1.19              0.322                                 ok            True                  False
  PYPL           92.31               26            0.98              0.37         54.12                35.54         0.518          pass              0.491              1.6                           0.043               -0.11              0.212                                 ok            True                  False
   BKR           84.62               13            1.55              0.62         56.85                32.18         0.517          pass              0.368             57.8                           0.301               -0.86              0.077                                 ok            True                  False
   STX           87.50               32            1.14              7.36        918.35                53.46         0.507          pass              0.489             30.7                           0.203               18.13              1.860                                 ok            True                  False
  CRWD           89.13               46            0.30              0.55        259.02                71.98         0.588          pass              0.735             77.7                           0.445                6.59              0.828                                 ok           False                  False
   WBD           95.00               40            0.15              0.03         30.89                38.06         0.574          pass              0.842             61.5                           0.446               10.08              1.215                                 ok           False                  False
   TRI           87.50               32            1.01              0.69         97.04                56.59         0.573          pass              0.553             49.7                           0.426               -6.10             -0.306            downtrend_blocked_slope           False                  False
  AMGN           86.49               37            0.29              0.84        417.77                46.33         0.571          pass              0.633             74.1                           0.500               10.99              1.219                                 ok           False                  False
  CHTR           77.27               44            0.05              0.04        111.38                61.92         0.533          pass              0.535             93.9                           0.521              -21.15             -2.441 downtrend_blocked_slope_and_streak           False                  False
  CDNS           66.67               21            1.73              3.95        325.01                46.51         0.522          pass              0.292             55.6                           0.659               17.19              1.970                                 ok           False                  False
  PANW           68.18               22            2.95              8.11        388.61                69.78         0.519          pass              0.186             18.0                           0.241                1.44              0.397                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-29T11:00:04.441545-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "entry_ask": 2.4, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.325, "hypothetical_budget": 39379.15, "hypothetical_contracts": 169, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 6.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.862, "early_reclaim_pct": 87.8, "matched_signals": 34, "recovery_stability_score": 0.563, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.387, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.801, "early_reclaim_pct": 62.3, "matched_signals": 37, "recovery_stability_score": 0.581, "success_rate": 94.59, "ticker": "ORLY", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T10:55:05.493456-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:50:04.346665-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:45:06.219567-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:40:06.250418-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:35:05.394441-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:30:04.372650-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261120C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.866, "early_reclaim_pct": 68.9, "entry_ask": 21.9, "entry_bid": 19.6, "entry_mode": "early", "entry_option_price": 20.75, "hypothetical_budget": 39379.15, "hypothetical_contracts": 18, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 844.0, "option_spread_pct": 11.08, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.866, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.693, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-29T10:25:05.800774-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261120C00190000", "current_drop_pct": 0.53, "early_entry_score": 0.886, "early_reclaim_pct": 75.2, "entry_ask": 21.9, "entry_bid": 19.6, "entry_mode": "early", "entry_option_price": 20.75, "hypothetical_budget": 39379.15, "hypothetical_contracts": 18, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 844.0, "option_spread_pct": 11.08, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.603, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.886, "early_reclaim_pct": 75.2, "matched_signals": 41, "recovery_stability_score": 0.749, "success_rate": 97.56, "ticker": "ZS", "timing_score": 0.603, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-29T10:20:06.606039-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T10:15:06.005082-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929110004)

</details>

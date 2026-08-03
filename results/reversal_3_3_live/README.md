# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 10:50:01 EDT`
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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           94.44               18            0.90              0.39         62.14                33.81         0.599          pass              0.509              3.4                           0.162                2.46              0.527                                 ok            True                  False
   CSX           95.65               23            0.54              0.19         50.32                27.78         0.579          pass              0.683             46.0                           0.355                0.04             -0.062                                 ok            True                  False
  AMGN          100.00               11            1.81              4.88        383.07                25.80         0.531          pass              0.478              5.9                           0.169                3.85              0.629                                 ok            True                  False
  BKNG           90.91               33            0.74              0.99        192.47                45.18         0.518          pass              0.564             22.6                           0.287                6.70              1.168                                 ok            True                  False
  LRCX           89.19               37            0.07              0.15        292.96                90.68         0.617          pass              0.783             98.7                           0.855               -4.55             -1.289 downtrend_blocked_slope_and_streak           False                  False
  AAPL           95.00               20            1.16              2.51        307.84                37.33         0.589          pass              0.591             21.7                           0.267               -6.51             -0.349 downtrend_blocked_slope_and_streak           False                  False
  MNST           83.33                6            2.23              1.50         95.74                24.15         0.546          pass              0.144              0.0                           0.003               -1.28              0.181                                 ok           False                  False
   PEP           87.10               31            0.21              0.21        139.47                26.18         0.542          pass              0.383              0.0                           0.157                2.81              0.489                                 ok           False                  False
  GILD           85.71               28            0.66              0.61        129.95                32.59         0.540          pass              0.405             26.1                           0.233               -2.90             -0.056           downtrend_blocked_streak           False                  False
  CTAS           94.87               39            0.23              0.34        204.49                38.81         0.539          pass              0.724             26.7                           0.164                1.16              0.355                                 ok           False                  False
   KDP           85.71               28            0.40              0.09         31.08                33.11         0.539          pass              0.406             26.5                           0.223                1.82              0.459                                 ok           False                  False
  KLAC           87.88               33            0.86              1.11        182.35                69.24         0.534          pass              0.659             80.8                           0.765              -12.70             -2.271 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-03T10:50:01.989461-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:45:01.762482-04:00 early_entry_1045 early_entry_shadow  {"contract_symbol": "CSCO260918C00120000", "current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "entry_ask": 6.05, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 5.925, "hypothetical_budget": 17614.88, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 9412.0, "option_spread_pct": 4.22, "option_volume": 63.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.746, "shadow_only": true, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "matched_signals": 36, "recovery_stability_score": 0.746, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T10:40:04.670427-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:35:06.183056-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "FTNT260918C00165000", "current_drop_pct": 0.56, "early_entry_score": 0.794, "early_reclaim_pct": 64.5, "entry_ask": 10.25, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 17614.88, "hypothetical_contracts": 17, "matched_signals": 48, "option_liquidity_status": "ok", "option_open_interest": 1333.0, "option_spread_pct": 7.59, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 93.75, "ticker": "FTNT", "timing_score": 0.332, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.794, "early_reclaim_pct": 64.5, "matched_signals": 48, "recovery_stability_score": 0.646, "success_rate": 93.75, "ticker": "FTNT", "timing_score": 0.332, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T10:30:03.009484-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:25:02.838853-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:20:02.187581-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:15:04.011672-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:10:03.982772-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:05:02.768000-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803105001)

</details>

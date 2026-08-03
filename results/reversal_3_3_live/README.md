# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 11:10:01 EDT`
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
  MDLZ           95.24               21            0.58              0.25         62.20                33.81         0.599          pass              0.670             45.5                           0.381                2.79              0.541                                 ok            True                  False
  MNST           81.82               11            1.73              1.17         95.88                24.15         0.541          pass              0.176             22.3                           0.408               -0.78              0.204                                 ok            True                  False
  SOXL           80.00               35            0.91              0.73        114.41               178.56         0.688          pass              0.511             91.8                           0.905              -16.91             -4.122 downtrend_blocked_slope_and_streak           False                  False
  DRAM           75.76               33            0.84              0.30         50.24               111.30         0.635          pass              0.469             84.2                           0.741               -5.87             -1.685 downtrend_blocked_slope_and_streak           False                  False
  AAPL           94.12               17            1.28              2.77        307.72                37.33         0.600          pass              0.523             13.5                           0.189               -6.62             -0.354 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.24               34            0.63              1.30        292.46                90.68         0.596          pass              0.705             88.5                           0.852               -5.09             -1.314 downtrend_blocked_slope_and_streak           False                  False
    MU           79.41               34            0.85              4.87        820.94               109.24         0.581          pass              0.479             86.8                           0.769               -5.71             -1.757 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               34            0.01              0.01        139.56                26.18         0.535          pass              0.728             98.2                           0.539                3.02              0.498                                 ok           False                  False
  KLAC           85.71               28            1.42              1.82        182.04                69.24         0.525          pass              0.530             68.4                           0.755              -13.19             -2.297 downtrend_blocked_slope_and_streak           False                  False
   KDP           87.88               33            0.21              0.05         31.10                33.11         0.520          pass              0.607             63.9                           0.479                2.02              0.468                                 ok           False                  False
   CSX           97.14               35            0.26              0.09         50.36                27.78         0.518          pass              0.840             74.0                           0.697                0.32             -0.049                                 ok           False                  False
   EXC           96.77               31            0.22              0.07         45.79                22.49         0.514          pass              0.831             80.0                           0.364               -0.52             -0.109                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-08-03T11:10:01.942425-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:05:04.817699-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:00:04.955349-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:55:01.983630-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:50:01.989461-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:45:01.762482-04:00 early_entry_1045 early_entry_shadow  {"contract_symbol": "CSCO260918C00120000", "current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "entry_ask": 6.05, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 5.925, "hypothetical_budget": 17614.88, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 9412.0, "option_spread_pct": 4.22, "option_volume": 63.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.746, "shadow_only": true, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.678, "early_reclaim_pct": 73.7, "matched_signals": 36, "recovery_stability_score": 0.746, "success_rate": 88.89, "ticker": "CSCO", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T10:40:04.670427-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:35:06.183056-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "FTNT260918C00165000", "current_drop_pct": 0.56, "early_entry_score": 0.794, "early_reclaim_pct": 64.5, "entry_ask": 10.25, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 17614.88, "hypothetical_contracts": 17, "matched_signals": 48, "option_liquidity_status": "ok", "option_open_interest": 1333.0, "option_spread_pct": 7.59, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 93.75, "ticker": "FTNT", "timing_score": 0.332, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.794, "early_reclaim_pct": 64.5, "matched_signals": 48, "recovery_stability_score": 0.646, "success_rate": 93.75, "ticker": "FTNT", "timing_score": 0.332, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T10:30:03.009484-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T10:25:02.838853-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803111001)

</details>

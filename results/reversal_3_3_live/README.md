# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 11:05:03 EDT`
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

- Cash: `$23,958.10`
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23760.0         1.65           1.65       32.33         32.46          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0          87.5               16              1.99         38.72           37.89                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            1.86              1.63        124.18                86.77         0.592          pass              0.309             38.8                           0.271               17.56              1.556                                 ok            True                  False
  PAYX          100.00               16            1.16              1.02        125.20                25.34         0.519          pass              0.638             48.6                           0.558                1.37              0.229                                 ok            True                  False
    ZS          100.00               34            1.61              2.01        177.51                60.79         0.518          pass              0.750             46.1                           0.476               -4.93              0.118                                 ok            True                  False
  CSCO           89.19               37            0.57              0.44        109.55                36.37         0.514          pass              0.615             46.2                           0.372               -1.30             -0.065                                 ok            True                  False
  MNST           92.31               26            0.71              0.22         44.89               424.41         1.000          pass              0.710             58.4                           0.668               -5.82             -0.695            downtrend_blocked_slope           False                  False
  ABNB           93.33               30            0.70              0.89        182.16                64.48         0.666          pass              0.699             47.8                           0.445               -2.75             -0.272            downtrend_blocked_slope           False                  False
  SOXL           82.86               35            0.66              0.49        105.70                97.59         0.653          pass              0.567             86.1                           0.548              -12.86             -1.270            downtrend_blocked_slope           False                  False
   WDC           77.78               27            2.40              7.57        447.19                82.26         0.578          pass              0.222             17.0                           0.195               -4.86             -0.307 downtrend_blocked_slope_and_streak           False                  False
  CRWD           80.00                5            4.54              6.83        212.14                87.98         0.541          pass              0.086             10.7                           0.229                1.82              1.466                                 ok           False                  False
  MRVL           77.42               31            2.48              3.66        208.82                79.24         0.538          pass              0.266             24.2                           0.211              -13.53             -1.711 downtrend_blocked_slope_and_streak           False                  False
   HON           80.00               25            0.78              1.14        209.49                29.51         0.521          pass              0.152              0.0                           0.226               -6.03             -0.413 downtrend_blocked_slope_and_streak           False                  False
  INTU           92.68               41            0.22              0.54        344.70                46.23         0.508          pass              0.839             83.5                           0.474               -5.05             -0.551            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-02T11:05:03.505803-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:59:24.886569-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:40:01.550864-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ZS261002C00177500", "current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "entry_ask": 14.9, "entry_bid": 12.75, "entry_mode": "early", "entry_option_price": 13.825, "hypothetical_budget": 11979.05, "hypothetical_contracts": 8, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 13.0, "option_spread_pct": 15.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.839, "shadow_only": true, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.872, "early_reclaim_pct": 73.3, "matched_signals": 41, "recovery_stability_score": 0.839, "success_rate": 100.0, "ticker": "ZS", "timing_score": 0.525, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-02T10:35:02.301132-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:30:05.379361-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:25:02.267090-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:20:01.429455-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:15:02.415633-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:10:02.355086-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902110503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902110503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902110503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902110503)

</details>

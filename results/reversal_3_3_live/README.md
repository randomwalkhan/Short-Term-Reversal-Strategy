# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 10:50:05 EDT`
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

- Cash: `$1,421.80`
- Equity: `$142,736.80`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$5,045.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 75555.0          1.1           1.15       44.42         44.41          bid_ask_mid                       1.15                bid_ask_mid                    True          3285.0                   4.55          80.0               15              0.97         20.09           23.12                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 65760.0         20.0          20.55      220.60        219.66          bid_ask_mid                      20.55                bid_ask_mid                    True          1760.0                   2.75         100.0               12              3.08         70.90           74.77                  47.89                 302.0           39.0               0.10                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.44               18            0.91              0.22         34.89                25.67         0.556          pass              0.659             54.9                           0.660                6.15              0.541                                 ok            True                  False
 CMCSA           88.89               18            0.66              0.10         22.01                26.02         0.556          pass              0.390             14.7                           0.239                4.91              0.583                                 ok            True                  False
   KHC           82.35               17            1.59              0.28         24.61                34.80         0.553          pass              0.165              0.0                           0.228                8.50              0.973                                 ok            True                  False
   WMT           80.00               20            0.80              0.68        120.00                23.89         0.531          pass              0.168             16.1                           0.330                6.27              0.478                                 ok            True                  False
    ZS           91.18               34            0.96              1.75        259.70                57.14         0.524          pass              0.664             51.3                           0.498               12.81              1.873                                 ok            True                  False
  TEAM          100.00               27            1.68              2.63        222.29                43.78         0.520          pass              0.639             24.7                           0.361                5.59              0.868                                 ok            True                  False
  ABNB           83.33               18            1.61              1.93        170.22                25.32         0.502          pass              0.273             27.0                           0.403                1.64              0.136                                 ok            True                  False
  TMUS           88.10               42            0.03              0.03        146.92                64.06         0.634          pass              0.770             96.8                           0.697               -4.46             -0.672            downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.10              0.48         62.76                25.86         0.606          pass              0.288              9.2                           0.226                1.27              0.141                                 ok           False                  False
   ROP           76.92               13            1.51              4.67        439.65                39.00         0.566          pass              0.201             41.4                           0.545               18.07              2.014                                 ok           False                  False
   ADP          100.00                3            2.60              5.48        298.77                25.17         0.548          pass              0.455              0.0                           0.190                6.30              0.849                                 ok           False                  False
  LRCX           71.43               42            0.01              0.02        237.49                60.23         0.542          pass              0.553             99.5                           0.554              -21.13             -2.565 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-27T10:50:05.201521-04:00 early_entry_1050 early_entry_shadow                                                   {"contract_symbol": "GILD261218C00160000", "current_drop_pct": 0.66, "early_entry_score": 0.686, "early_reclaim_pct": 64.0, "entry_ask": 6.8, "entry_bid": 6.4, "entry_mode": "early", "entry_option_price": 6.6, "hypothetical_budget": 1421.8, "hypothetical_contracts": 2, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1422.0, "option_spread_pct": 6.06, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.686, "early_reclaim_pct": 64.0, "matched_signals": 33, "recovery_stability_score": 0.707, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-27T10:45:03.445212-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.99, "early_entry_score": 0.727, "early_reclaim_pct": 61.9, "entry_ask": 14.1, "entry_bid": 11.4, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.99, "early_entry_score": 0.727, "early_reclaim_pct": 61.9, "matched_signals": 37, "recovery_stability_score": 0.631, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:40:04.040794-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.81, "early_entry_score": 0.761, "early_reclaim_pct": 68.9, "entry_ask": 14.2, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 22.75, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.614, "shadow_only": true, "success_rate": 92.11, "ticker": "WDAY", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.761, "early_reclaim_pct": 68.9, "matched_signals": 38, "recovery_stability_score": 0.614, "success_rate": 92.11, "ticker": "WDAY", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:35:07.163044-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:30:04.056749-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:25:06.119259-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:20:06.240513-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:15:05.594224-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T10:10:04.139511-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "WDAY261127C00205000", "current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "entry_ask": 13.2, "entry_bid": 10.2, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 1421.8, "hypothetical_contracts": 1, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 25.64, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.729, "early_reclaim_pct": 62.5, "matched_signals": 37, "recovery_stability_score": 0.75, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-27T10:05:02.075117-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027105005)

</details>

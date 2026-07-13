# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 11:20:02 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   TXN           88.89               18            2.36              5.13        309.26                64.14         0.592          pass              0.462             37.6                           0.596                6.53              0.543                  ok            True                  False
  QCOM           82.76               29            1.22              1.61        188.47                63.33         0.581          pass              0.462             67.8                           0.612               -0.99              0.256                  ok            True                  False
   ADI           84.21               19            2.24              6.22        392.99                55.18         0.572          pass              0.282             17.5                           0.206               -1.28             -0.030                  ok            True                  False
  META           80.95               21            1.54              7.22        666.11                55.99         0.572          pass              0.250             31.2                           0.323               17.12              1.704                  ok            True                  False
  UPRO           88.00               25            1.09              1.11        145.68                40.56         0.558          pass              0.513             48.1                           0.447                4.19              0.393                  ok            True                  False
   LIN          100.00               12            1.29              4.79        527.74                20.88         0.553          pass              0.476              2.6                           0.190                2.32              0.038                  ok            True                  False
  CSCO           95.00               20            1.19              1.01        120.88                35.64         0.536          pass              0.713             64.3                           0.547                2.22              0.338                  ok            True                  False
   MAR           92.31               13            1.47              3.88        374.45                19.73         0.528          pass              0.480             26.2                           0.469               -1.15              0.039                  ok            True                  False
  NXPI           82.35               17            2.86              5.84        289.76                55.03         0.527          pass              0.218             18.6                           0.234                1.99              0.401                  ok            True                  False
  MPWR           80.95               21            3.81             36.04       1337.29                78.41         0.519          pass              0.206             18.4                           0.340               -0.73             -0.103                  ok            True                  False
  AVGO           80.95               21            2.29              6.40        397.23                49.47         0.516          pass              0.242             30.5                           0.232                4.93              0.782                  ok            True                  False
  ABNB           94.74               19            1.96              2.04        147.75                37.12         0.509          pass              0.623             39.8                           0.534               -0.99             -0.014                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-13T11:20:02.121903-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:15:04.147580-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:10:02.119516-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "SNPS260814C00445000", "current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "entry_ask": 27.0, "entry_bid": 20.8, "entry_mode": "early", "entry_option_price": 23.9, "hypothetical_budget": 13497.63, "hypothetical_contracts": 5, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 25.94, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "matched_signals": 39, "recovery_stability_score": 0.603, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T11:05:06.382767-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:00:04.971643-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:55:05.047187-04:00 early_entry_1055 early_entry_shadow                               {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "entry_ask": 16.1, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 15.1, "hypothetical_budget": 13497.63, "hypothetical_contracts": 8, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 840.0, "option_spread_pct": 13.25, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "matched_signals": 40, "recovery_stability_score": 0.645, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:50:02.084276-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:45:02.061748-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:40:04.044917-04:00 early_entry_1040 early_entry_shadow                                              {"contract_symbol": "CSCO260821C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "entry_ask": 7.1, "entry_bid": 6.95, "entry_mode": "early", "entry_option_price": 7.025, "hypothetical_budget": 13497.63, "hypothetical_contracts": 19, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 8106.0, "option_spread_pct": 2.14, "option_volume": 71.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.903, "shadow_only": true, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "matched_signals": 30, "recovery_stability_score": 0.903, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:35:02.047813-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713112002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713112002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713112002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713112002)

</details>

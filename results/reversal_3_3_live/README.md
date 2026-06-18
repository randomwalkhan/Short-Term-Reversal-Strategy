# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 10:55:03 EDT`
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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           94.12               17            1.09              0.47         60.66                21.28         0.542          pass              0.486              2.9                           0.117               -1.30             -0.164                                 ok            True                  False
  VRTX           93.33               15            1.70              5.47        456.65                24.55         0.505          pass              0.464              8.1                           0.176                2.14              0.294                                 ok            True                  False
    ZS           78.95               38            0.63              0.55        124.15               152.31         0.878          pass              0.522             82.6                           0.881               -8.62             -0.536 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.84              0.14         23.14                27.50         0.698          pass              0.551             27.2                           0.250                4.24              0.395                                 ok           False                  False
  INTU           76.32               38            1.02              1.92        268.26                98.62         0.677          pass              0.471             72.2                           0.664              -11.80             -1.255 downtrend_blocked_slope_and_streak           False                  False
   TRI           77.78               27            0.57              0.31         79.12                52.51         0.591          pass              0.410             79.3                           0.736               -8.09             -0.797 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.87              4.47        339.75                27.62         0.567          pass              0.189             14.5                           0.202               -2.99             -0.128           downtrend_blocked_streak           False                  False
  CRWD           88.10               42            0.06              0.27        682.84                64.33         0.553          pass              0.766             98.2                           0.944               -5.08              0.090                                 ok           False                  False
  GILD           85.71                7            1.97              1.73        124.71                29.17         0.550          pass              0.228              6.8                           0.134               -4.17             -0.252 downtrend_blocked_slope_and_streak           False                  False
  COST           66.67               15            1.08              7.27        962.47                23.27         0.539          pass              0.207             39.9                           0.509               -1.76             -0.052                                 ok           False                  False
  WDAY           78.79               33            1.48              1.26        121.29                69.08         0.536          pass              0.382             58.4                           0.494              -18.85             -2.096 downtrend_blocked_slope_and_streak           False                  False
   WMT           88.89               36            0.39              0.32        117.99                34.58         0.527          pass              0.616             51.1                           0.486               -0.06              0.034                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-18T10:55:03.314248-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:50:01.439897-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:45:03.283549-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:40:01.292114-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:35:03.329239-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:30:02.323229-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "entry_ask": 9.9, "entry_bid": 7.35, "entry_mode": "early", "entry_option_price": 8.625, "hypothetical_budget": 13257.25, "hypothetical_contracts": 15, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 29.57, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "matched_signals": 43, "recovery_stability_score": 0.694, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T10:25:02.315380-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:20:06.081546-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:15:06.113244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:10:05.150482-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618105503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618105503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618105503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618105503)

</details>

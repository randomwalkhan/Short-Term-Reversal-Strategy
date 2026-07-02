# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 11:20:05 EDT`
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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   WBD           90.91               11            0.80              0.15         26.75                21.87         0.621          pass              0.451             30.4                           0.301                1.35              0.117                      ok            True                  False
  ASML           95.24               21            2.56             32.98       1828.91                76.04         0.565          pass              0.677             49.0                           0.293               -3.85             -0.141                      ok            True                  False
  INTC           90.00               20            3.76              3.35        125.59               102.61         0.537          pass              0.426             13.1                           0.134                0.94             -0.208                      ok            True                  False
  PCAR           84.00               25            0.99              0.84        120.88                34.47         0.517          pass              0.323             21.6                           0.306                2.30              0.244                      ok            True                  False
    MU           92.86               14            4.24             30.62       1019.16               134.25         0.697          pass              0.502             20.8                           0.193               -5.24             -0.493 downtrend_blocked_slope           False                  False
  AVGO           78.26               23            1.48              3.84        367.70                71.90         0.680          pass              0.177              7.4                           0.194               -7.24             -0.908 downtrend_blocked_slope           False                  False
   TXN           89.47               19            1.85              3.86        296.76                67.74         0.621          pass              0.403              9.5                           0.205               -2.97             -0.891 downtrend_blocked_slope           False                  False
  UPRO           87.50               32            0.38              0.38        141.23                55.10         0.618          pass              0.560             50.5                           0.248                1.75              0.095                      ok           False                  False
   ADI           87.50               16            2.13              5.81        386.49                61.24         0.599          pass              0.331             10.4                           0.203               -8.15             -1.232 downtrend_blocked_slope           False                  False
  NXPI           86.67               15            2.47              4.83        277.11                63.41         0.565          pass              0.295              9.1                           0.201               -8.38             -1.361 downtrend_blocked_slope           False                  False
  DRAM           83.33                6            7.36              3.39         64.41               129.95         0.553          pass              0.167              7.5                           0.123              -12.77             -1.323 downtrend_blocked_slope           False                  False
  MPWR           84.21               19            3.35             31.26       1318.33                89.16         0.552          pass              0.240              4.2                           0.164              -10.99             -1.622 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-02T11:20:05.689456-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:15:06.544213-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "entry_ask": 14.1, "entry_bid": 13.35, "entry_mode": "early", "entry_option_price": 13.725, "hypothetical_budget": 13948.25, "hypothetical_contracts": 10, "matched_signals": 45, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.46, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "matched_signals": 45, "recovery_stability_score": 0.685, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:10:01.560535-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:05:04.703877-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:00:02.762100-04:00 early_entry_1100 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.51, "early_entry_score": 0.848, "early_reclaim_pct": 69.0, "entry_ask": 14.4, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 45, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 4.26, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.621, "shadow_only": true, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.848, "early_reclaim_pct": 69.0, "matched_signals": 45, "recovery_stability_score": 0.621, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T10:55:01.729347-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:50:04.749926-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:45:02.720384-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:40:05.626608-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:35:03.761213-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702112005)

</details>

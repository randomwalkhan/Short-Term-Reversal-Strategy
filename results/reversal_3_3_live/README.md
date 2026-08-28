# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 10:40:06 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.50              0.16         46.63               551.83         1.000          pass              0.641             21.7                           0.232               -0.76              0.159                      ok            True                  False
  AMGN          100.00               18            0.86              2.64        435.86                27.65         0.585          pass              0.581             23.1                           0.304                4.95              0.537                      ok            True                  False
  FAST          100.00               17            1.08              0.39         50.97                21.07         0.533          pass              0.605             34.9                           0.338               -0.85             -0.081                      ok            True                  False
  CSCO           84.38               32            1.05              0.83        111.80                41.41         0.533          pass              0.405             29.3                           0.479               -0.64             -0.020                      ok            True                  False
  REGN          100.00               13            1.45              8.20        804.20                24.94         0.529          pass              0.641             56.0                           0.318               -0.82             -0.023                      ok            True                  False
  VRTX           97.14               35            0.50              1.94        546.72                32.96         0.516          pass              0.828             70.0                           0.642                7.72              0.669                      ok            True                   True
  NVDA           86.67               30            1.14              1.81        227.20                42.92         0.515          pass              0.498             45.2                           0.562                0.10             -0.150                      ok            True                  False
  GILD          100.00               19            1.63              1.70        148.13                26.47         0.514          pass              0.533              7.3                           0.160                5.83              0.631                      ok            True                  False
    ZS           90.00               20            2.58              3.39        185.85                58.32         0.504          pass              0.428             14.6                           0.236               -0.62             -0.369                      ok            True                  False
  INSM           80.00               20            2.16              1.83        120.60               110.68         0.779          pass              0.259             38.2                           0.468               -4.02             -0.581 downtrend_blocked_slope           False                  False
  SOXL           79.41               34            2.50              2.15        122.13               111.92         0.640          pass              0.383             52.9                           0.783              -17.23             -2.059 downtrend_blocked_slope           False                  False
  DRAM           75.68               37            0.04              0.02         56.82                68.22         0.619          pass              0.538             98.8                           0.894               -0.90             -0.217                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-08-28T10:40:06.289047-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "entry_ask": 27.4, "entry_bid": 25.5, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 7.18, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.828, "early_reclaim_pct": 70.0, "matched_signals": 35, "recovery_stability_score": 0.642, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:35:02.085142-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:30:04.053969-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:25:02.074094-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:20:02.098332-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:15:03.828658-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:10:03.076583-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:05:04.075473-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:00:04.882804-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T09:20:06.065187-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828104006)

</details>

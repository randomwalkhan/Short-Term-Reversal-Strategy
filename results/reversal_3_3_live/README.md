# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:25:01 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC           97.06               34            0.69              0.59        120.64                85.20         0.636            pass              0.729             35.2                           0.201                3.56              1.070                      ok            True                  False
  CSCO           92.31               26            0.89              0.74        118.32                52.06         0.629            pass              0.604             35.3                           0.209                1.78              0.204                      ok            True                  False
  INSM           75.61               41            0.60              0.45        108.18               111.11         0.772            pass              0.435             52.6                           0.399               -6.83             -0.356 downtrend_blocked_slope           False                  False
  MELI           93.18               44            0.04              0.53       1695.30                61.27         0.603            pass              0.897             95.1                           0.726                5.44              0.825                      ok           False                  False
   AEP           75.00               16            0.44              0.40        127.59                25.60         0.596            pass              0.238             46.2                           0.389               -1.09              0.112                      ok           False                  False
  GOOG           87.50                8            1.87              5.06        383.95                41.01         0.548            pass              0.327             24.1                           0.279               -4.60             -0.353 downtrend_blocked_slope           False                  False
 GOOGL           87.50                8            2.07              5.65        387.71                41.30         0.542            pass              0.306             17.2                           0.229               -4.74             -0.347 downtrend_blocked_slope           False                  False
   TXN          100.00               32            0.27              0.59        315.70                35.59         0.526            pass              0.770             56.9                           0.435                2.25              0.549                      ok           False                  False
  AMGN           91.43               35            0.18              0.41        336.30                27.03         0.498 below_threshold              0.769             82.7                           0.738                0.65              0.287                      ok           False                  False
   CSX           73.33               15            1.22              0.39         45.64                23.65         0.498 below_threshold              0.197             38.1                           0.432               -1.46              0.012                      ok           False                  False
  CHTR           75.00               16            2.52              2.60        146.15                48.51         0.491 below_threshold              0.183             31.4                           0.474               -3.01              0.172                      ok           False                  False
  MSTR           83.33               36            1.50              1.59        150.96                63.23         0.483 below_threshold              0.409             33.0                           0.262              -20.11             -1.889 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-05-29T10:25:01.208564-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:25:01.208564-04:00 early_entry_1025 entry_candidate_skipped {"early_entry_score": 0.814, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 18.61, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.395}
2026-05-29T10:20:01.218195-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:20:01.218195-04:00 early_entry_1020 entry_candidate_skipped {"early_entry_score": 0.816, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 19.35, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.396}
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped       {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped        {"early_entry_score": 0.776, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 611.0, "option_spread_pct": 26.98, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "GILD", "timing_score": 0.366}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.817, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.95, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.397}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529102501)

</details>

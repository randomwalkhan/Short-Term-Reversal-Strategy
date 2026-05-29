# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:10:01 EDT`
Last processed slot: `manage_1000`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.81              0.67        118.35                52.06         0.634          pass              0.622             41.2                           0.274                1.86              0.208                                 ok            True                  False
  AMGN           88.46               26            0.60              1.41        335.87                27.03         0.528          pass              0.508             40.9                           0.284                0.22              0.267                                 ok            True                  False
  MDLZ           90.91               11            1.52              0.67         62.10                12.98         0.508          pass              0.452             34.5                           0.216                0.77              0.175                                 ok            True                  False
  INSM           74.36               39            0.66              0.50        108.15               111.11         0.779          pass              0.382             36.8                           0.359               -6.89             -0.359            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.61              0.55        127.53                25.60         0.598          pass              0.157             25.7                           0.246               -1.26              0.104                                 ok           False                  False
  REGN           90.00               40            0.18              0.77        621.19                44.05         0.534          pass              0.769             83.0                           0.511              -12.84             -1.047 downtrend_blocked_slope_and_streak           False                  False
   PEP           84.62               13            1.43              1.47        145.66                23.56         0.527          pass              0.261             21.8                           0.216               -3.01             -0.283            downtrend_blocked_slope           False                  False
   TXN          100.00               32            0.35              0.78        315.61                35.59         0.520          pass              0.726             42.6                           0.272                2.16              0.545                                 ok           False                  False
 GOOGL           87.50               16            1.56              4.26        388.31                41.30         0.518          pass              0.405             37.6                           0.581               -4.24             -0.323            downtrend_blocked_slope           False                  False
  SBUX           92.31               13            1.06              0.75        100.43                16.60         0.517          pass              0.598             66.0                           0.350               -5.77             -0.717            downtrend_blocked_slope           False                  False
  GOOG           89.47               19            1.41              3.82        384.48                41.01         0.503          pass              0.491             42.7                           0.626               -4.16             -0.332            downtrend_blocked_slope           False                  False
  MSTR           85.37               41            0.75              0.80        151.30                63.23         0.502          pass              0.593             66.4                           0.599              -19.51             -1.854            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped        {"early_entry_score": 0.776, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 611.0, "option_spread_pct": 26.98, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "GILD", "timing_score": 0.366}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.817, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.95, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.397}
2026-05-29T10:00:05.402847-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T09:20:06.125686-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                 {'saved': 92}
2026-05-28T15:10:10.028312-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T15:00:06.948836-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T14:55:06.010831-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529101001)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:15:06 EDT`
Last processed slot: `early_entry_1015`

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
  CSCO           92.31               26            0.77              0.64        118.37                52.06         0.637          pass              0.631             44.2                           0.267                1.90              0.210                                 ok            True                  False
  MDLZ           90.00               10            1.62              0.71         62.09                12.98         0.508          pass              0.409             30.3                           0.259                0.67              0.170                                 ok            True                  False
  INSM           70.59               34            1.13              0.85        108.00               111.11         0.776          pass              0.264              9.0                           0.261               -7.33             -0.380            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.69              0.62        127.50                25.60         0.593          pass              0.128             16.2                           0.171               -1.34              0.101                                 ok           False                  False
   PEP           91.67               12            1.48              1.52        145.64                23.56         0.539          pass              0.435             19.0                           0.198               -3.06             -0.285            downtrend_blocked_slope           False                  False
 GOOGL           90.00               10            1.94              5.30        387.86                41.30         0.539          pass              0.388             22.4                           0.344               -4.62             -0.341            downtrend_blocked_slope           False                  False
  REGN           90.24               41            0.10              0.45        621.33                44.05         0.533          pass              0.797             90.2                           0.586              -12.77             -1.044 downtrend_blocked_slope_and_streak           False                  False
  MSTR           85.37               41            0.35              0.37        151.48                63.23         0.531          pass              0.649             84.4                           0.639              -19.18             -1.836            downtrend_blocked_slope           False                  False
   TXN          100.00               31            0.40              0.89        315.57                35.59         0.524          pass              0.697             34.9                           0.252                2.11              0.543                                 ok           False                  False
  AMGN           89.66               29            0.43              1.02        336.04                27.03         0.520          pass              0.609             57.6                           0.421                0.40              0.275                                 ok           False                  False
  GOOG           85.71               14            1.71              4.63        384.13                41.01         0.514          pass              0.322             30.5                           0.420               -4.45             -0.346            downtrend_blocked_slope           False                  False
  SBUX           93.33               15            0.95              0.67        100.46                16.60         0.512          pass              0.649             69.5                           0.395               -5.66             -0.712            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped       {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped        {"early_entry_score": 0.776, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 611.0, "option_spread_pct": 26.98, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "GILD", "timing_score": 0.366}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.817, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.95, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.397}
2026-05-29T10:00:05.402847-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T09:20:06.125686-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                 {'saved': 92}
2026-05-28T15:10:10.028312-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529101506)

</details>

# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:20:06 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               22            2.80              2.37        119.60               109.00         0.618            pass              0.600             19.5                           0.159               23.73              3.065                      ok            True                  False
  TEAM           84.62               26            3.64              2.16         84.07               115.69         0.595            pass              0.396             35.6                           0.664               16.20              1.383                      ok            True                  False
  SNPS           97.14               35            0.63              2.25        512.25                43.23         0.549            pass              0.797             58.4                           0.706                5.98              0.708                      ok            True                  False
   ADP          100.00               11            2.20              3.29        212.40                33.54         0.549            pass              0.596             44.8                           0.339               -2.77             -0.099                      ok            True                  False
  KLAC           86.11               36            0.51              6.46       1808.58                48.58         0.523            pass              0.520             43.9                           0.278               -0.78              0.445                      ok            True                  False
  MCHP           80.00               25            1.27              0.87         97.33                50.72         0.517            pass              0.280             42.6                           0.210                6.98              0.732                      ok            True                  False
   XEL           88.89               27            0.66              0.37         79.74                27.12         0.505            pass              0.576             58.3                           0.646                0.70             -0.223                      ok            True                  False
  MSTR           90.32               31            2.28              2.95        183.16                75.69         0.503            pass              0.623             52.4                           0.766               13.92              1.264                      ok            True                  False
    ZS           83.33               42            0.57              0.58        145.92                59.81         0.502            pass              0.560             73.6                           0.765                7.88              1.117                      ok            True                  False
  MDLZ           85.19               27            0.64              0.28         61.58                23.07         0.500 below_threshold              0.461             53.0                           0.333                0.43              0.041                      ok            True                  False
  GILD           83.33               12            1.66              1.57        134.27                22.16         0.500            pass              0.210             19.1                           0.176                3.00              0.270                      ok            True                  False
  CHTR           63.64               11            3.52              3.64        146.36               118.13         0.753            pass              0.102              6.6                           0.289              -10.04             -1.399 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-13T10:20:06.278508-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.815, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 21.38, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.437}
2026-05-13T10:10:06.807841-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-13T10:05:05.859086-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513102006)

</details>

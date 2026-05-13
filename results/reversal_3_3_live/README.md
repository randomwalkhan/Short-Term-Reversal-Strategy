# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:15:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               22            2.69              2.27        119.64               109.00         0.624          pass              0.611             22.9                           0.175               23.87              3.070                                 ok            True                  False
  TEAM           84.62               26            3.58              2.13         84.09               115.69         0.599          pass              0.400             36.7                           0.600               16.27              1.386                                 ok            True                  False
  SNPS           97.14               35            0.61              2.18        512.28                43.23         0.550          pass              0.801             59.7                           0.673                6.00              0.709                                 ok            True                  False
   ADP          100.00               12            2.15              3.22        212.43                33.54         0.545          pass              0.606             46.0                           0.297               -2.72             -0.096                                 ok            True                  False
  ORLY           84.62               26            1.19              0.77         91.51                35.45         0.533          pass              0.312              9.5                           0.267               -1.03             -0.513                                 ok            True                  False
    ZS           82.50               40            0.66              0.68        145.88                59.81         0.508          pass              0.525             69.1                           0.751                7.77              1.112                                 ok            True                  False
   XEL           89.29               28            0.60              0.34         79.76                27.12         0.503          pass              0.605             62.2                           0.656                0.76             -0.220                                 ok            True                  False
  CHTR           66.67               12            3.25              3.37        146.48               118.13         0.763          pass              0.129             13.2                           0.249               -9.80             -1.387            downtrend_blocked_slope           False                  False
  NXPI           82.50               40            0.17              0.35        294.08                89.73         0.708          pass              0.440             34.2                           0.254                1.55              0.193                                 ok           False                  False
  INSM           78.38               37            0.84              0.69        115.71               110.65         0.597          pass              0.466             75.5                           0.464              -14.82             -2.841 downtrend_blocked_slope_and_streak           False                  False
  SHOP           80.95               21            2.52              1.76         99.08                84.62         0.572          pass              0.275             39.9                           0.685              -19.74             -2.529 downtrend_blocked_slope_and_streak           False                  False
  GEHC           72.97               37            0.75              0.33         62.15                57.10         0.559          pass              0.426             63.3                           0.728                3.93              0.367                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-13T10:15:05.895485-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.815, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 21.38, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.437}
2026-05-13T10:10:06.807841-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-13T10:05:05.859086-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-13T10:00:05.846029-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-12T15:10:04.189330-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513101505)

</details>

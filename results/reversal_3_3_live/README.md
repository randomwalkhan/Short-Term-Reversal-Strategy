# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:25:06 EDT`
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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            1.22              1.48        172.56               145.82         0.773          pass              0.416             62.1                           0.380               12.48             -0.498                      ok            True                  False
  INTC           90.91               11            4.22              3.51        117.45               113.85         0.671          pass              0.395             10.0                           0.220                3.94             -0.716                      ok            True                  False
  FTNT          100.00               31            1.12              1.01        129.57                70.74         0.636          pass              0.746             47.5                           0.376               19.06              1.772                      ok            True                  False
  SBUX           92.31               13            1.24              0.92        106.10                31.64         0.597          pass              0.554             48.7                           0.666                1.47              0.198                      ok            True                  False
  MNST           81.48               27            0.96              0.58         86.63                49.77         0.556          pass              0.453             81.4                           0.456               13.27              0.657                      ok            True                  False
 GOOGL           85.19               27            0.99              2.70        387.75                41.00         0.548          pass              0.410             34.6                           0.369               -3.25             -0.235                      ok            True                  False
  AMAT           82.35               34            0.76              2.27        425.88                55.19         0.546          pass              0.425             49.2                           0.355                3.16             -0.243                      ok            True                  False
   TXN           91.67               12            1.82              3.89        303.21                69.08         0.535          pass              0.433             18.5                           0.214                4.94              0.492                      ok            True                  False
  NVDA           82.35               17            2.04              3.19        222.10                44.60         0.526          pass              0.183              7.0                           0.214                3.51              0.319                      ok            True                  False
  ISRG           85.71               14            2.26              7.11        445.98                35.82         0.506          pass              0.307             25.8                           0.397               -3.22             -0.011                      ok            True                  False
    ZS           85.19               27            1.73              2.11        173.54                63.59         0.503          pass              0.433             43.6                           0.628               12.20              1.840                      ok            True                  False
  CHTR           89.36               47            0.24              0.24        144.51               113.96         0.749          pass              0.787             87.6                           0.698               -9.97             -0.928 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:25:06.196092-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped                   {"early_entry_score": 0.689, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.405}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped                  {"early_entry_score": 0.717, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.395}
2026-05-21T10:20:05.205283-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:20:05.205283-04:00 early_entry_1020 entry_candidate_skipped                 {"early_entry_score": 0.687, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1903.0, "option_spread_pct": 32.26, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.459}
2026-05-21T10:15:05.147516-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:15:05.147516-04:00 early_entry_1015 entry_candidate_skipped  {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 25.99, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                   {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped {"early_entry_score": 0.718, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.487}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                  {"early_entry_score": 0.806, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.634}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521102506)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:30:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  INTC           93.75               16            3.61              3.01        117.67               113.85         0.677          pass              0.552             25.7                           0.286                4.60             -0.687                  ok            True                  False
  FTNT          100.00               28            1.25              1.13        129.51                70.74         0.647          pass              0.709             41.3                           0.316               18.90              1.766                  ok            True                  False
  SBUX           92.31               13            1.23              0.91        106.11                31.64         0.598          pass              0.556             49.3                           0.694                1.49              0.199                  ok            True                  False
  MNST           81.48               27            0.96              0.58         86.63                49.77         0.556          pass              0.453             81.4                           0.438               13.27              0.657                  ok            True                  False
  AMAT           83.33               36            0.54              1.61        426.16                55.19         0.548          pass              0.509             63.9                           0.383                3.39             -0.233                  ok            True                  False
   TXN           91.67               12            1.89              4.03        303.15                69.08         0.531          pass              0.424             15.5                           0.165                4.86              0.489                  ok            True                  False
 GOOGL           88.89               36            0.55              1.48        388.27                41.00         0.521          pass              0.654             64.0                           0.662               -2.81             -0.215                  ok            True                  False
  NVDA           85.00               20            1.86              2.91        222.22                44.60         0.520          pass              0.308             18.8                           0.292                3.70              0.327                  ok            True                  False
    ZS           86.96               23            2.12              2.59        173.34                63.59         0.509          pass              0.415             30.8                           0.401               11.75              1.822                  ok            True                  False
  AVGO           91.67               36            0.57              1.67        417.04                40.33         0.507          pass              0.683             49.1                           0.297                0.68             -0.163                  ok            True                  False
  ISRG           85.71               14            2.25              7.08        445.99                35.82         0.507          pass              0.308             26.1                           0.400               -3.22             -0.011                  ok            True                  False
  SOXL           83.87               31            0.27              0.32        173.06               145.82         0.800          pass              0.599             91.8                           0.466               13.57             -0.454                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:30:05.185385-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:30:05.185385-04:00 early_entry_1030 entry_candidate_skipped                   {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.407}
2026-05-21T10:25:06.196092-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped                   {"early_entry_score": 0.689, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.405}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped                  {"early_entry_score": 0.717, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.395}
2026-05-21T10:20:05.205283-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:20:05.205283-04:00 early_entry_1020 entry_candidate_skipped                 {"early_entry_score": 0.687, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1903.0, "option_spread_pct": 32.26, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.459}
2026-05-21T10:15:05.147516-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:15:05.147516-04:00 early_entry_1015 entry_candidate_skipped  {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 25.99, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped {"early_entry_score": 0.718, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.487}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521103005)

</details>

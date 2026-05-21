# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:15:05 EDT`
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
  NXPI           81.25               32            0.80              1.73        309.41                91.65         0.710          pass              0.450             66.4                           0.758                6.02              0.307                  ok            True                  False
  INTC           94.74               19            3.31              2.76        117.78               113.85         0.682          pass              0.598             25.7                           0.339                4.93             -0.673                  ok            True                  False
  FTNT          100.00               32            1.07              0.97        129.58                70.74         0.633          pass              0.759             49.7                           0.540               19.12              1.774                  ok            True                  False
  SBUX           92.31               13            1.29              0.96        106.09                31.64         0.595          pass              0.548             46.8                           0.606                1.43              0.196                  ok            True                  False
  PAYX           94.74               19            0.51              0.34         94.77                29.35         0.565          pass              0.742             77.5                           0.845                1.47              0.258                  ok            True                  False
  MNST           82.14               28            0.82              0.50         86.67                49.77         0.559          pass              0.485             84.1                           0.650               13.43              0.663                  ok            True                  False
 GOOGL           83.33               24            1.14              3.11        387.58                41.00         0.556          pass              0.311             24.5                           0.241               -3.40             -0.242                  ok            True                  False
   ADP           94.12               34            0.53              0.81        220.34                38.26         0.527          pass              0.804             71.5                           0.777                2.54              0.455                  ok            True                   True
  NVDA           87.88               33            0.70              1.09        223.00                44.60         0.520          pass              0.566             50.2                           0.421                4.92              0.381                  ok            True                  False
   TXN           90.48               21            1.34              2.86        303.66                69.08         0.502          pass              0.523             40.2                           0.419                5.46              0.515                  ok            True                  False
    ZS           84.00               25            1.94              2.37        173.44                63.59         0.502          pass              0.368             36.9                           0.485               11.96              1.831                  ok            True                  False
  ISRG           84.62               13            2.41              7.57        445.78                35.82         0.502          pass              0.256             21.0                           0.373               -3.37             -0.018                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:15:05.147516-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:15:05.147516-04:00 early_entry_1015 entry_candidate_skipped  {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 25.99, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T10:10:05.107052-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                  {"early_entry_score": 0.691, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1903.0, "option_spread_pct": 73.17, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.46}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                   {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped {"early_entry_score": 0.718, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.487}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                  {"early_entry_score": 0.806, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.634}
2026-05-21T10:05:05.076526-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped  {"early_entry_score": 0.71, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.483}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped                  {"early_entry_score": 0.846, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521101505)

</details>

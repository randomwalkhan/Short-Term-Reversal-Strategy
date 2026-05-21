# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:00:05 EDT`
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
  INTC           96.43               28            1.56              1.29        118.41               113.85         0.727          pass              0.788             65.1                           0.780                6.83             -0.591                  ok            True                  False
  FTNT          100.00               32            1.03              0.94        129.60                70.74         0.635          pass              0.764             51.3                           0.466               19.16              1.776                  ok            True                  False
  MELI           91.67               36            0.83              9.63       1647.07                61.27         0.571          pass              0.726             61.5                           0.671              -12.44             -0.498                  ok            True                   True
  PAYX           92.86               14            1.09              0.72         94.61                29.35         0.560          pass              0.582             52.2                           0.643                0.89              0.231                  ok            True                  False
   ADP           91.30               23            1.23              1.90        219.88                38.26         0.553          pass              0.544             33.4                           0.439                1.82              0.423                  ok            True                  False
 GOOGL           86.67               30            0.80              2.18        387.97                41.00         0.544          pass              0.491             41.9                           0.511               -3.07             -0.227                  ok            True                  False
  MNST           86.11               36            0.62              0.38         86.72                49.77         0.524          pass              0.652             87.9                           0.674               13.65              0.672                  ok            True                  False
  FAST           95.00               20            1.10              0.34         43.54                21.35         0.520          pass              0.632             37.7                           0.518               -2.61             -0.126                  ok            True                  False
    ZS           82.35               17            2.68              3.27        173.05                63.59         0.508          pass              0.199             12.8                           0.237               11.12              1.796                  ok            True                  False
   TXN           91.30               23            1.07              2.27        303.91                69.08         0.507          pass              0.596             52.3                           0.535                5.75              0.527                  ok            True                  False
  ISRG           84.62               13            2.41              7.57        445.79                35.82         0.502          pass              0.256             21.1                           0.196               -3.37             -0.018                  ok            True                  False
  INSM           76.32               38            0.77              0.58        107.66               110.82         0.745          pass              0.345             27.8                           0.231                1.98              0.193                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:00:05.181059-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:00:05.181059-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 13.0, "option_spread_pct": 19.61, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.487}
2026-05-21T10:00:05.181059-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.726, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 36.96, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.571}
2026-05-21T09:20:03.993328-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 92}
2026-05-20T15:10:05.258354-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T15:05:01.057777-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T15:00:06.267185-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T14:55:06.339368-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T14:50:06.419995-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T14:50:06.419995-04:00       entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-20", "training_samples": 5043, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521100005)

</details>

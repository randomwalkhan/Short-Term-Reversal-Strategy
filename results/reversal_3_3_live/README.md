# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-12 15:35:10 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$27,308.25`
- Equity: `$27,308.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           93.10               29            1.26             14.05       1583.53                71.83         0.562          pass              0.640             36.0                           0.365                1.76             -0.369                                 ok            True                  False
  CSCO           93.10               29            0.75              0.64        121.56                43.07         0.549          pass              0.531              0.0                           0.250               -0.34             -0.482                                 ok            True                  False
  ASML           92.00               25            1.97             26.17       1888.27                60.86         0.502          pass              0.629             52.8                           0.322               14.34              1.277                                 ok            True                  False
  CPRT           88.00               25            1.18              0.26         30.95                31.00         0.500          pass              0.484             40.2                           0.368               -5.03             -0.139                                 ok            True                  False
  DRAM           91.67               24            0.20              0.09         65.08               107.49         0.754          pass              0.770             96.6                           0.582               -4.43             -0.768                                 ok           False                  False
  INTU           79.49               39            0.55              1.06        276.46               100.42         0.723          pass              0.515             83.0                           0.834              -22.15             -2.169 downtrend_blocked_slope_and_streak           False                  False
    MU           79.41               34            1.14              7.95        992.46               115.24         0.661          pass              0.441             71.7                           0.389               -4.92             -0.804                                 ok           False                  False
  AVGO           81.48               27            1.25              3.38        384.12                69.71         0.604          pass              0.344             43.6                           0.397              -17.23             -2.501            downtrend_blocked_slope           False                  False
  TEAM           85.71               35            1.23              0.77         88.87                85.01         0.567          pass              0.601             75.2                           0.766              -24.02             -2.614 downtrend_blocked_slope_and_streak           False                  False
  AAPL          100.00                9            1.78              3.67        294.06                23.83         0.533          pass              0.491             12.6                           0.330               -5.20             -0.829            downtrend_blocked_slope           False                  False
  CRWD           77.42               31            1.12              5.41        689.21                64.88         0.526          pass              0.321             42.9                           0.298              -12.58             -1.452 downtrend_blocked_slope_and_streak           False                  False
  CTAS          100.00                2            3.24              4.13        180.11                29.28         0.513          pass              0.495             14.5                           0.277                1.78              0.277                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                  detail
2026-06-12T15:10:11.830500-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T15:05:11.809096-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:50:07.527766-04:00   entry_1500           entry_skipped                                                                                                                                                            {"budget": 13654.13, "entry_cost": 15345.0, "reason": "insufficient_cash", "ticker": "ASML"}
2026-06-12T14:50:07.527766-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.73, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 0.0, "option_spread_pct": 7.0, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.565}
2026-06-12T14:50:07.527766-04:00   entry_1500          timing_overlay                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-12", "training_samples": 5261, "window": 5}
2026-06-12T13:30:06.922165-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                           {'saved': 93}
2026-06-11T16:00:02.840701-04:00  manage_1600                    exit                                                                       {"asset_type": "option", "contract_symbol": "PAYX260717C00100000", "fill_price": 4.725, "pnl": -1417.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-06-11T15:10:05.901456-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260612153510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260612153510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260612153510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260612153510)

</details>

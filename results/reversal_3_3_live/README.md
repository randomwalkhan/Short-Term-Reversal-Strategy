# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-12 15:50:10 EDT`
Last processed slot: `manage_1600`

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
    MU           80.00               35            1.05              7.29        992.75               115.24         0.661          pass              0.455             74.1                           0.419               -4.83             -0.799                                 ok            True                  False
  MPWR           93.75               32            0.86              9.53       1585.47                71.83         0.570          pass              0.740             56.6                           0.422                2.18             -0.350                                 ok            True                  False
  CSCO           93.10               29            0.79              0.67        121.54                43.07         0.544          pass              0.569             12.7                           0.239               -0.38             -0.484                                 ok            True                  False
  ASML           92.00               25            1.84             24.44       1889.01                60.86         0.511          pass              0.639             55.9                           0.337               14.49              1.283                                 ok            True                  False
  INTU           79.55               44            0.08              0.16        276.84               100.42         0.721          pass              0.564             97.4                           0.870              -21.79             -2.148 downtrend_blocked_slope_and_streak           False                  False
  AVGO           80.00               25            1.31              3.55        384.05                69.71         0.612          pass              0.284             40.8                           0.354              -17.28             -2.504            downtrend_blocked_slope           False                  False
  TEAM           87.50               40            0.86              0.54         88.97                85.01         0.561          pass              0.704             82.7                           0.802              -23.73             -2.597 downtrend_blocked_slope_and_streak           False                  False
  AAPL          100.00               10            1.55              3.21        294.25                23.83         0.541          pass              0.525             23.6                           0.409               -4.99             -0.819            downtrend_blocked_slope           False                  False
  CRWD           74.07               27            1.32              6.41        688.78                64.88         0.535          pass              0.264             32.3                           0.197              -12.76             -1.461 downtrend_blocked_slope_and_streak           False                  False
  NVDA           85.00               40            0.18              0.26        204.76                43.63         0.508          pass              0.619             78.3                           0.381               -8.75             -0.986            downtrend_blocked_slope           False                  False
  CTAS          100.00                2            3.34              4.25        180.06                29.28         0.508          pass              0.487             12.0                           0.198                1.68              0.272                                 ok           False                  False
  WDAY           86.84               38            0.78              0.71        130.22                70.45         0.504          pass              0.664             81.5                           0.804              -17.63             -1.888 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260612155010)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260612155010)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260612155010)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260612155010)

</details>

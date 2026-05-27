# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 09:45:02 EDT`
Last processed slot: `manual`

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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           84.62               26            2.56              4.05        224.01               148.29         0.645          pass              0.440             48.4                           0.304               27.50              2.178                                 ok            True                  False
  ASML           89.29               28            1.75             19.94       1623.48                54.27         0.528          pass              0.443              7.6                           0.162                5.43              0.589                                 ok            True                  False
  LRCX           83.33               30            1.05              2.37        321.66                57.65         0.513          pass              0.373             33.3                           0.271               10.39              0.980                                 ok            True                  False
  MRVL          100.00               27            1.37              1.99        207.41                65.55         0.501          pass              0.687             41.2                           0.322               24.87              2.007                                 ok            True                  False
  NXPI           90.00               40            0.18              0.43        332.49                92.16         0.648          pass              0.776             81.5                           0.396               12.86              1.249                                 ok           False                  False
  FTNT          100.00                7            3.25              3.04        132.66                66.88         0.630          pass              0.599             45.4                           0.406               13.82              1.438                                 ok           False                  False
  CSCO           94.59               37            0.20              0.17        118.26                52.88         0.594          pass              0.882             84.6                           0.645               18.93              1.410                                 ok           False                  False
   AEP           84.62               26            0.15              0.13        130.84                25.21         0.571          pass              0.549             87.3                           0.636               -0.93              0.175                                 ok           False                  False
  INTC           92.31               13            4.29              3.71        121.93                91.80         0.569          pass              0.439             11.3                           0.199               -1.99              0.338           downtrend_blocked_streak           False                  False
  SBUX           96.97               33            0.22              0.15        101.35                33.52         0.540          pass              0.856             82.9                           0.528               -4.49             -0.463 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.70               43            0.13              0.35        388.73                41.36         0.526          pass              0.801             87.6                           0.730                0.27             -0.301                                 ok           False                  False
  NVDA           85.71               21            1.58              2.37        213.84                40.94         0.526          pass              0.334             18.5                           0.207               -4.22             -0.667 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T09:20:01.591516-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
2026-05-26T12:00:02.390044-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527094502)

</details>

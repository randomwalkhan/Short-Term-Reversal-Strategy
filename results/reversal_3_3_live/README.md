# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 09:45:05 EDT`
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
  INTC          100.00               30            1.48              1.25        120.07               109.00         0.649          pass              0.749             50.1                           0.305               25.40              3.126                                 ok            True                  False
  TEAM           81.82               22            3.85              2.29         84.02               115.69         0.625          pass              0.191              0.0                           0.203               15.95              1.373                                 ok            True                  False
   ADP          100.00               10            2.30              3.44        212.33                33.54         0.549          pass              0.581             42.2                           0.279               -2.87             -0.104                                 ok            True                  False
  SNPS           96.67               30            1.29              4.63        511.23                43.23         0.545          pass              0.631             14.3                           0.236                5.27              0.678                                 ok            True                  False
    ZS           82.14               28            1.63              1.67        145.46                59.81         0.526          pass              0.302             24.2                           0.279                6.72              1.068                                 ok            True                  False
  MSTR           86.96               23            3.28              4.23        182.61                75.69         0.507          pass              0.337              4.9                           0.213               12.76              1.217                                 ok            True                  False
  CHTR           66.67               12            3.18              3.29        146.51               118.13         0.771          pass              0.098              2.4                           0.185               -9.73             -1.384            downtrend_blocked_slope           False                  False
 CMCSA           92.31               26            0.54              0.09         24.86                62.10         0.692          pass              0.695             63.5                           0.512               -7.46             -1.001 downtrend_blocked_slope_and_streak           False                  False
  INSM           75.76               33            1.30              1.06        115.55               110.65         0.590          pass              0.399             62.2                           0.350              -15.21             -2.862 downtrend_blocked_slope_and_streak           False                  False
  GEHC           64.29               28            1.26              0.55         62.05                57.10         0.571          pass              0.293             38.5                           0.434                3.39              0.344                                 ok           False                  False
  SHOP           86.67               15            3.84              2.68         98.69                84.62         0.546          pass              0.266              0.0                           0.183              -20.82             -2.590 downtrend_blocked_slope_and_streak           False                  False
  MSFT           81.25               16            1.51              4.32        405.92                32.80         0.545          pass              0.153              8.5                           0.129               -5.38             -0.236           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-12T15:10:04.189330-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:05:01.045921-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T15:00:02.256030-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:55:01.031417-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-12T14:50:01.032752-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T14:50:01.032752-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-12", "training_samples": 5014, "window": 5}
2026-05-12T12:00:02.098694-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:55:05.845380-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:50:02.083143-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-12T11:45:01.039711-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513094505)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 09:55:03 EDT`
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

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           90.91               22            0.82              1.94        335.65                27.03         0.546          pass              0.434              2.7                           0.128               -0.00              0.257                                 ok            True                  False
  MDLZ           90.91               11            1.57              0.69         62.10                12.98         0.505          pass              0.445             32.4                           0.200                0.72              0.172                                 ok            True                  False
  INSM           75.61               41            0.59              0.44        108.18               111.11         0.774          pass              0.410             44.3                           0.306               -6.82             -0.356            downtrend_blocked_slope           False                  False
  SHOP           84.44               45            0.29              0.23        114.93                84.44         0.626          pass              0.618             79.1                           0.431               17.74              1.402                                 ok           False                  False
  MELI           95.00               40            0.27              3.23       1694.15                61.27         0.617          pass              0.872             70.3                           0.577                5.20              0.814                                 ok           False                  False
   TRI           79.17               24            0.24              0.14         84.43                54.95         0.614          pass              0.417             87.4                           0.554                7.45              0.145                                 ok           False                  False
  CSCO           94.29               35            0.27              0.22        118.55                52.06         0.612          pass              0.851             80.7                           0.611                2.42              0.233                                 ok           False                  False
   AEP           82.61               23            0.29              0.26        127.65                25.60         0.571          pass              0.351             46.0                           0.321               -0.94              0.119                                 ok           False                  False
  MNST           95.56               45            0.24              0.15         87.93                49.61         0.554          pass              0.892             78.8                           0.549                2.28              0.183                                 ok           False                  False
  REGN           89.19               37            0.26              1.14        621.03                44.05         0.549          pass              0.705             75.0                           0.452              -12.91             -1.051 downtrend_blocked_slope_and_streak           False                  False
  MSTR           85.71               42            0.04              0.04        151.62                63.23         0.546          pass              0.702             98.3                           0.896              -18.93             -1.822            downtrend_blocked_slope           False                  False
   TXN          100.00               32            0.34              0.74        315.63                35.59         0.521          pass              0.736             45.6                           0.267                2.18              0.546                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-29T09:20:06.125686-04:00     data_refresh   data_refresh                                                                                                                                                                           {'saved': 92}
2026-05-28T15:10:10.028312-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:00:06.948836-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:55:06.010831-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:50:05.035990-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T14:50:05.035990-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-28", "training_samples": 5117, "window": 5}
2026-05-28T12:40:01.998163-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529095503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529095503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529095503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529095503)

</details>

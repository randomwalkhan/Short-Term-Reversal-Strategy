# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 09:30:03 EDT`
Last processed slot: `manage_0930`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.29               35            0.80              9.48       1691.47                61.27         0.614            pass              0.647             12.8                           0.210                4.64              0.790                                 ok            True                  False
  INSM           75.61               41            0.48              0.36        108.21               111.11         0.782            pass              0.367             29.7                           0.288               -6.72             -0.351            downtrend_blocked_slope           False                  False
  CSCO           93.33               30            0.43              0.36        118.49                52.06         0.640            pass              0.681             42.7                           0.356                2.25              0.225                                 ok           False                  False
   TRI           81.48               27            0.12              0.07         84.46                54.95         0.619            pass              0.452             79.2                           0.399                7.58              0.150                                 ok           False                  False
   AEP           82.61               23            0.25              0.22        127.66                25.60         0.574            pass              0.374             53.3                           0.367               -0.90              0.121                                 ok           False                  False
  MNST           95.65               46            0.16              0.10         87.95                49.61         0.552            pass              0.913             85.9                           0.560                2.37              0.187                                 ok           False                  False
  REGN           90.70               43            0.05              0.21        621.43                44.05         0.523            pass              0.824             95.3                           0.545              -12.73             -1.041 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.48               21            1.41              3.85        388.48                41.30         0.510            pass              0.404              0.0                           0.279               -4.10             -0.316            downtrend_blocked_slope           False                  False
  GOOG           88.89               18            1.56              4.21        384.31                41.01         0.510            pass              0.341              0.0                           0.276               -4.30             -0.338            downtrend_blocked_slope           False                  False
  COST           89.66               29            0.67              4.68       1001.68                24.99         0.492 below_threshold              0.526             31.0                           0.209               -4.25             -0.778 downtrend_blocked_slope_and_streak           False                  False
  MSTR           85.71               35            1.63              1.73        150.90                63.23         0.489 below_threshold              0.398             10.2                           0.090              -20.22             -1.895            downtrend_blocked_slope           False                  False
  PANW           90.24               41            0.16              0.29        257.64                44.02         0.486 below_threshold              0.766             81.3                           0.460                8.03              0.750                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529093003)

</details>

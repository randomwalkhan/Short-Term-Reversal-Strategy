# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 09:56:26 EDT`
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

- Cash: `$26,462.75`
- Equity: `$26,462.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               24            1.57              1.40        127.04                70.74         0.657            pass              0.605             15.4                           0.225               39.67              2.583                                 ok            True                  False
  PAYX           91.67               12            1.13              0.75         94.16                29.36         0.563            pass              0.575             64.6                           0.699                3.54              0.205                                 ok            True                  False
   WMT           90.00               10            1.44              1.35        133.62                20.68         0.535            pass              0.492             57.3                           0.322                1.87              0.330                                 ok            True                  False
 GOOGL           88.57               35            0.56              1.52        387.01                41.27         0.508            pass              0.446              0.0                           0.230               -3.15             -0.198                                 ok            True                  False
  SHOP           83.72               43            0.10              0.07        100.98                78.65         0.604            pass              0.643             94.4                           0.761               -4.30             -0.835 downtrend_blocked_slope_and_streak           False                  False
  TEAM           89.29               28            3.04              1.84         85.83               114.61         0.578            pass              0.547             40.4                           0.587               -5.42             -0.595 downtrend_blocked_slope_and_streak           False                  False
  CTSH           81.25               16            1.93              0.69         50.59                50.98         0.516            pass              0.275             49.9                           0.553               -2.10             -0.254           downtrend_blocked_streak           False                  False
  ADSK           84.62               13            2.25              3.85        242.51                38.52         0.504            pass              0.343             49.8                           0.589               -1.82             -0.196           downtrend_blocked_streak           False                  False
  SNPS           95.45               22            1.98              6.85        490.94                41.71         0.489 below_threshold              0.683             51.2                           0.657               -4.03             -0.421 downtrend_blocked_slope_and_streak           False                  False
  MSFT           83.33               24            1.11              3.24        416.03                29.51         0.488 below_threshold              0.304             24.4                           0.237               -0.28              0.057                                 ok           False                  False
   ADP           93.10               29            0.80              1.23        219.91                38.42         0.486 below_threshold              0.785             86.8                           0.763                5.54              0.476                                 ok           False                  False
  GOOG           89.19               37            0.57              1.53        384.24                41.08         0.483 below_threshold              0.473              0.0                           0.223               -3.15             -0.208           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                               detail
2026-05-20T09:18:59.431991-04:00     data_refresh   data_refresh                                                                                                                                                                        {'saved': 92}
2026-05-19T15:10:04.056831-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T15:05:05.027114-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T15:00:02.089036-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:55:06.057081-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:50:01.084215-04:00       entry_1500  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T14:50:01.084215-04:00       entry_1500 timing_overlay                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-19", "training_samples": 5044, "window": 5}
2026-05-19T12:20:01.028030-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "PANW260618C00250000", "fill_price": 13.7475, "pnl": -1374.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PANW"}
2026-05-19T12:00:03.873446-04:00 early_entry_1200  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520095626)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520095626)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520095626)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520095626)

</details>

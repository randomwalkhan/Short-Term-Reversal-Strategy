# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 09:38:40 EDT`
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
  FTNT          100.00               33            0.93              0.83        127.28                70.74         0.639            pass              0.767             49.8                           0.533               40.58              2.613                                 ok            True                  False
   WMT           93.75               16            1.04              0.97        133.78                20.68         0.526            pass              0.667             69.3                           0.429                2.29              0.349                                 ok            True                  False
  QCOM           91.89               37            0.26              0.36        195.46               100.64         0.690            pass              0.771             68.3                           0.358                1.31             -0.611                                 ok           False                  False
  SHOP           83.33               42            0.42              0.30        100.88                78.65         0.589            pass              0.576             76.1                           0.546               -4.60             -0.850 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.89               27            3.46              2.10         85.72               114.61         0.556            pass              0.502             32.1                           0.365               -5.83             -0.614 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.88               32            0.16              0.12        106.33                31.99         0.545            pass              0.849             82.6                           0.672                0.37              0.198                                 ok           False                  False
  PAYX           85.71                7            1.82              1.20         93.96                29.36         0.543            pass              0.335             42.9                           0.398                2.82              0.173                                 ok           False                  False
  AMGN           83.33               24            0.66              1.53        330.09                26.77         0.498 below_threshold              0.464             77.4                           0.476               -0.02             -0.000                                 ok           False                  False
   ADP           89.47               19            1.59              2.45        219.39                38.42         0.497 below_threshold              0.584             73.8                           0.411                4.70              0.440                                 ok           False                  False
  CTSH           72.73               11            2.68              0.96         50.47                50.98         0.488 below_threshold              0.146             30.1                           0.328               -2.86             -0.289           downtrend_blocked_streak           False                  False
   HON           87.88               33            0.32              0.49        216.94                24.50         0.487 below_threshold              0.605             64.2                           0.536                0.36              0.078                                 ok           False                  False
  MSFT           85.19               27            0.89              2.60        416.30                29.51         0.486 below_threshold              0.397             32.2                           0.275               -0.06              0.067                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520093840)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520093840)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520093840)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520093840)

</details>

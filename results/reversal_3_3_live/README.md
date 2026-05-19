# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 15:00:02 EDT`
Last processed slot: `entry_1500`

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

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19       13.550     12.1950 -1355.00       -10.0 stop_loss_hit_at_scan
  PANW     option         option PANW260618C00250000      9          2026-05-19         2026-05-19       15.275     13.7475 -1374.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  QCOM           89.47               19            1.89              2.70        202.48                99.05         0.676          pass              0.589             69.5                           0.636                7.09              0.237                                 ok            True                  False
  GOOG           80.00               10            1.89              5.21        390.88                40.55         0.569          pass              0.136             26.4                           0.196                0.36              0.013                                 ok            True                  False
 GOOGL           80.00               10            1.99              5.53        394.57                40.53         0.566          pass              0.138             27.0                           0.192                0.16              0.022                                 ok            True                  False
   KDP           86.36               22            1.10              0.23         29.33                33.71         0.556          pass              0.323              5.8                           0.192                0.64              0.213                                 ok            True                  False
  ASML           83.87               31            0.79              8.11       1468.91                50.95         0.543          pass              0.486             62.7                           0.505                1.24             -0.145                                 ok            True                  False
  SNPS           97.14               35            0.72              2.53        497.35                41.65         0.533          pass              0.782             54.0                           0.527               -1.53             -0.164                                 ok            True                  False
   ADP           93.33               30            0.82              1.28        222.39                37.99         0.527          pass              0.563              7.1                           0.150                4.99              0.440                                 ok            True                  False
  AVGO           88.89               18            2.26              6.66        417.86                42.85         0.509          pass              0.449             35.9                           0.263               -3.78             -0.118                                 ok            True                  False
  TTWO          100.00               19            1.72              2.91        240.91                33.10         0.500          pass              0.611             33.5                           0.391                6.67              1.027                                 ok            True                  False
  CHTR           89.58               48            0.21              0.21        141.12               112.84         0.706          pass              0.737             70.4                           0.401              -10.94             -1.375            downtrend_blocked_slope           False                  False
 CMCSA           84.00               25            0.66              0.12         24.88                60.09         0.663          pass              0.358             28.3                           0.384               -6.41             -0.693 downtrend_blocked_slope_and_streak           False                  False
  CSCO           85.71                7            1.93              1.60        118.19                49.96         0.639          pass              0.348             44.0                           0.446               23.64              2.944                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                               detail
2026-05-19T15:00:02.089036-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:55:06.057081-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:50:01.084215-04:00       entry_1500  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T14:50:01.084215-04:00       entry_1500 timing_overlay                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-19", "training_samples": 5044, "window": 5}
2026-05-19T12:20:01.028030-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "PANW260618C00250000", "fill_price": 13.7475, "pnl": -1374.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PANW"}
2026-05-19T12:00:03.873446-04:00 early_entry_1200  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:40:06.318992-04:00 early_entry_1140  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519150002)

</details>

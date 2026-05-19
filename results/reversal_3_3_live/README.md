# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 15:05:05 EDT`
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
  QCOM           89.47               19            1.91              2.72        202.47                99.05         0.675          pass              0.588             69.2                           0.660                7.08              0.236                                 ok            True                  False
  GOOG           80.00               10            1.91              5.25        390.86                40.55         0.568          pass              0.134             25.8                           0.195                0.35              0.012                                 ok            True                  False
 GOOGL           80.00               10            2.02              5.60        394.54                40.53         0.564          pass              0.135             26.1                           0.190                0.13              0.021                                 ok            True                  False
   KDP           86.36               22            1.27              0.26         29.32                33.71         0.544          pass              0.304              0.0                           0.229                0.47              0.205                                 ok            True                  False
  ASML           84.38               32            0.69              7.16       1469.32                50.95         0.543          pass              0.519             67.1                           0.521                1.33             -0.140                                 ok            True                  False
  SNPS           97.14               35            0.72              2.51        497.35                41.65         0.533          pass              0.783             54.3                           0.525               -1.53             -0.163                                 ok            True                  False
   ADP           93.33               30            0.84              1.31        222.38                37.99         0.525          pass              0.555              4.6                           0.115                4.97              0.439                                 ok            True                  False
  AVGO           89.47               19            2.21              6.50        417.93                42.85         0.507          pass              0.476             37.5                           0.393               -3.73             -0.115                                 ok            True                  False
  MDLZ           85.00               20            0.96              0.41         61.46                22.85         0.503          pass              0.358             36.0                           0.243               -0.51             -0.091                                 ok            True                  False
  CHTR           88.37               43            0.41              0.40        141.04               112.84         0.720          pass              0.622             42.2                           0.268              -11.12             -1.384            downtrend_blocked_slope           False                  False
 CMCSA           85.71               28            0.52              0.09         24.89                60.09         0.656          pass              0.468             43.5                           0.489               -6.27             -0.686 downtrend_blocked_slope_and_streak           False                  False
  CSCO           85.71                7            1.94              1.62        118.19                49.96         0.638          pass              0.347             43.5                           0.438               23.62              2.943                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                               detail
2026-05-19T15:05:05.027114-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T15:00:02.089036-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:55:06.057081-04:00       entry_1500   slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-19T14:50:01.084215-04:00       entry_1500  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T14:50:01.084215-04:00       entry_1500 timing_overlay                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-19", "training_samples": 5044, "window": 5}
2026-05-19T12:20:01.028030-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "PANW260618C00250000", "fill_price": 13.7475, "pnl": -1374.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PANW"}
2026-05-19T12:00:03.873446-04:00 early_entry_1200  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145  entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519150505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519150505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519150505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519150505)

</details>

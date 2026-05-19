# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 12:20:01 EDT`
Last processed slot: `manage_1230`

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
  SOXL           81.48               27            1.28              1.36        151.17               141.41         0.643          pass              0.482             88.4                           0.896                3.92              0.123                                 ok            True                  False
  GOOG           80.00               10            2.21              6.09        390.50                40.55         0.549          pass              0.097             13.9                           0.307                0.04             -0.002                                 ok            True                  False
 GOOGL           80.00               10            2.36              6.55        394.13                40.53         0.543          pass              0.095             13.5                           0.306               -0.22              0.005                                 ok            True                  False
  SNPS           96.77               31            1.00              3.50        496.93                41.65         0.541          pass              0.703             36.2                           0.448               -1.81             -0.177                                 ok            True                  False
  ASML           83.33               30            1.02             10.52       1467.88                50.95         0.533          pass              0.430             51.6                           0.684                1.00             -0.155                                 ok            True                  False
   KDP           90.91               33            0.56              0.12         29.38                33.71         0.527          pass              0.620             41.1                           0.277                1.19              0.238                                 ok            True                  False
  NVDA           87.88               33            0.65              1.02        221.88                44.74         0.518          pass              0.616             67.0                           0.555               12.40              1.141                                 ok            True                  False
  AVGO           88.89               18            2.28              6.72        417.83                42.85         0.508          pass              0.447             35.3                           0.527               -3.80             -0.119                                 ok            True                  False
  KLAC           81.48               27            1.39             17.12       1749.11                51.34         0.508          pass              0.393             63.0                           0.618               -0.05             -0.036                                 ok            True                  False
  INTC          100.00               34            0.43              0.33        108.03               114.00         0.733          pass              0.909             91.9                           0.890               -0.42             -0.402                                 ok           False                  False
  INSM           76.19               42            0.26              0.19        107.07               111.34         0.718          pass              0.533             87.1                           0.452              -23.35             -1.644 downtrend_blocked_slope_and_streak           False                  False
  QCOM          100.00                4            3.86              5.50        201.28                99.05         0.665          pass              0.580             37.7                           0.607                4.95              0.145                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                               detail
2026-05-19T12:20:01.028030-04:00      manage_1230          exit {"asset_type": "option", "contract_symbol": "PANW260618C00250000", "fill_price": 13.7475, "pnl": -1374.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PANW"}
2026-05-19T12:00:03.873446-04:00 early_entry_1200 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:55:04.964087-04:00 early_entry_1155 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:50:03.963905-04:00 early_entry_1150 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:45:02.013628-04:00 early_entry_1145 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:40:06.318992-04:00 early_entry_1140 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:35:01.898801-04:00 early_entry_1135 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:30:01.060546-04:00 early_entry_1130 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:25:05.065733-04:00 early_entry_1125 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-19T11:20:06.455937-04:00 early_entry_1120 entry_skipped                                                                                                                                                      {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519122001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519122001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519122001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519122001)

</details>

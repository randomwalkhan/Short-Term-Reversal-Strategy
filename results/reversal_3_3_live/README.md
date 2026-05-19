# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 12:40:01 EDT`
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
  GOOG           80.00               10            2.18              5.99        390.54                40.55         0.552          pass              0.101             15.3                           0.413                0.07             -0.000                                 ok            True                  False
 GOOGL           80.00               10            2.33              6.48        394.16                40.53         0.545          pass              0.098             14.5                           0.406               -0.19              0.006                                 ok            True                  False
   KDP           90.32               31            0.63              0.13         29.37                33.71         0.535          pass              0.571             33.9                           0.246                1.12              0.235                                 ok            True                  False
  SNPS           97.14               35            0.83              2.89        497.19                41.65         0.526          pass              0.761             47.4                           0.689               -1.63             -0.168                                 ok            True                  False
  TTWO          100.00               16            1.85              3.13        240.82                33.10         0.518          pass              0.532             13.4                           0.175                6.53              1.021                                 ok            True                  False
  AVGO           91.67               24            1.81              5.32        418.43                42.85         0.502          pass              0.601             48.8                           0.700               -3.34             -0.097                                 ok            True                  False
  INSM           76.19               42            0.21              0.15        107.08               111.34         0.721          pass              0.541             89.7                           0.482              -23.31             -1.642 downtrend_blocked_slope_and_streak           False                  False
  QCOM           87.50                8            2.93              4.17        201.85                99.05         0.679          pass              0.426             52.8                           0.763                5.97              0.189                                 ok           False                  False
 CMCSA           87.88               33            0.34              0.06         24.90                60.09         0.643          pass              0.546             39.3                           0.366               -6.10             -0.678 downtrend_blocked_slope_and_streak           False                  False
  CSCO           80.00                5            2.43              2.02        118.01                49.96         0.614          pass              0.149             29.3                           0.544               23.00              2.921                                 ok           False                  False
  MNST           63.64               11            1.93              1.20         88.03                49.83         0.605          pass              0.141             24.7                           0.534               14.55              1.473                                 ok           False                  False
  SHOP           78.79               33            1.35              0.97        101.97                78.89         0.594          pass              0.264             17.1                           0.274               -6.16             -0.984 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519124001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519124001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519124001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519124001)

</details>

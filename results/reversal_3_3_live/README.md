# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 16:00:10 EDT`
Last processed slot: `manage_1600`

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

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0      -10.00        stop_loss_hit_at_scan
  AVGO     option         option AVGO260717C00420000      4          2026-05-28         2026-05-28        31.25      35.950  1880.0       15.04 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.86               35            0.52              3.39        926.96               100.84         0.672          pass              0.580             90.0                           0.500               14.92              2.118                                 ok            True                  False
  INTC           97.14               35            0.76              0.64        121.49                92.16         0.622          pass              0.879             83.3                           0.710                0.47              0.794                                 ok            True                   True
  CSCO           92.31               26            0.86              0.72        119.36                51.65         0.617          pass              0.616             39.8                           0.408               16.46              0.869                                 ok            True                  False
  MNST           90.00               20            1.39              0.87         88.87                49.17         0.555          pass              0.447             19.5                           0.229                2.41              0.224                                 ok            True                  False
  MELI           93.18               44            0.08              0.92       1695.77                61.41         0.593          pass              0.885             91.3                           0.522                8.51              0.873                                 ok           False                  False
   AEP           71.43                7            1.42              1.29        129.02                25.33         0.565          pass              0.197             47.0                           0.474               -0.17              0.202                                 ok           False                  False
   XEL          100.00                6            2.19              1.24         80.47                25.49         0.564          pass              0.468              3.8                           0.224               -0.85              0.177                                 ok           False                  False
  ROST           83.33                6            2.69              4.40        231.59                38.54         0.549          pass              0.220             25.4                           0.551                7.29              1.129                                 ok           False                  False
  REGN           86.21               29            0.97              4.25        625.92                48.81         0.528          pass              0.398             17.8                           0.220              -13.51             -1.326 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.00               40            0.25              0.55        318.69                56.04         0.517          pass              0.795             92.3                           0.684                7.69              1.173                                 ok           False                  False
  COST           90.91               22            0.81              5.66       1001.26                24.84         0.516          pass              0.472             16.5                           0.153               -3.63             -0.544 downtrend_blocked_slope_and_streak           False                  False
  SBUX           91.67               12            1.32              0.94        101.69                33.41         0.501          pass              0.440             22.0                           0.292               -4.35             -0.552            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                  detail
2026-05-28T15:10:10.028312-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T15:00:06.948836-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:55:06.010831-04:00       entry_1500   slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-28T14:50:05.035990-04:00       entry_1500  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T14:50:05.035990-04:00       entry_1500 timing_overlay                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-28", "training_samples": 5117, "window": 5}
2026-05-28T12:40:01.998163-04:00      manage_1230           exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150  entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528160010)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528160010)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528160010)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528160010)

</details>

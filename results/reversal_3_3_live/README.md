# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:10:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26       30.350     36.1500  2320.0   19.110379 take_profit_day2_hit_at_scan
  SBUX     option         option SBUX260717C00105000     38          2026-05-22         2026-05-26        3.625      3.2625 -1377.5  -10.000000        stop_loss_hit_at_scan
  TTWO     option         option TTWO260717C00230000     15          2026-05-26         2026-05-26        9.800     11.3500  2325.0   15.816327 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           89.74               39            1.03              0.62         85.16               109.49         0.678          pass              0.744             74.3                           0.503               -3.17              0.032                                 ok            True                  False
  CSCO           90.00               10            1.74              1.46        119.78                52.25         0.650          pass              0.443             37.0                           0.562               19.85              1.889                                 ok            True                  False
  MELI           92.31               26            1.41             16.44       1657.37                60.80         0.594          pass              0.647             51.0                           0.662                5.37              0.702                                 ok            True                  False
   ADP          100.00               12            2.27              3.58        223.78                37.70         0.556          pass              0.499              9.9                           0.252                4.03              0.645                                 ok            True                  False
  PAYX           90.91               11            1.34              0.91         96.61                28.52         0.549          pass              0.519             55.5                           0.678                3.26              0.595                                 ok            True                  False
  CTSH           85.71               21            1.46              0.54         52.52                46.65         0.543          pass              0.440             53.3                           0.555                6.29              1.323                                 ok            True                  False
   ROP           85.71               14            1.80              4.13        325.17                26.18         0.523          pass              0.251              6.6                           0.179               -2.36              0.043                                 ok            True                  False
 CMCSA           84.21               19            1.07              0.19         25.12                20.74         0.501          pass              0.322             33.3                           0.316               -0.38              0.023                                 ok            True                  False
  INTU           78.57               14            3.76              8.43        316.33                90.56         0.620          pass              0.098              3.1                           0.163              -21.71             -2.290            downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.46              0.88         85.48                55.00         0.614          pass              0.231             45.4                           0.312               -4.46              0.099                                 ok           False                  False
   WMT           94.12               17            0.99              0.84        119.91                34.37         0.598          pass              0.559             25.3                           0.476               -6.67             -0.829 downtrend_blocked_slope_and_streak           False                  False
  SBUX           91.67               12            1.51              1.09        102.64                33.02         0.596          pass              0.482             32.5                           0.451               -3.39             -0.279            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:05:05.735209-04:00 early_entry_1105 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:00:04.326254-04:00 early_entry_1100 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:55:01.312359-04:00 early_entry_1055 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00 early_entry_1050 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260717C00230000", "fill_price": 11.35, "pnl": 2325.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.82, "ticker": "TTWO"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit      {"asset_type": "option", "contract_symbol": "SBUX260717C00105000", "fill_price": 3.2625, "pnl": -1377.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SBUX"}
2026-05-26T10:45:02.313357-04:00 early_entry_1045 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:40:05.315818-04:00 early_entry_1040 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:35:01.414005-04:00 early_entry_1035 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526111005)

</details>

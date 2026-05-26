# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 13:50:03 EDT`
Last processed slot: `manage_1400`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ASML           88.57               35            0.52              5.95       1630.35                54.77         0.572          pass              0.663             70.3                           0.566                3.74              0.377                      ok            True                  False
  MELI           93.94               33            1.07             12.47       1659.08                60.80         0.570          pass              0.771             62.9                           0.561                5.73              0.717                      ok            True                   True
   ADP          100.00               11            2.49              3.93        223.63                37.70         0.549          pass              0.465              1.1                           0.065                3.79              0.635                      ok            True                  False
  AMGN           85.00               20            0.85              2.01        338.44                27.24         0.546          pass              0.306             17.3                           0.367                2.85              0.216                      ok            True                  False
  CTSH           89.29               28            1.14              0.42         52.57                46.65         0.519          pass              0.610             63.6                           0.579                6.63              1.338                      ok            True                  False
   ROP           88.89               18            1.64              3.76        325.33                26.18         0.508          pass              0.401             20.0                           0.388               -2.20              0.051                      ok            True                  False
  MSFT           86.36               22            1.18              3.47        417.08                23.47         0.501          pass              0.332             10.8                           0.248                0.45              0.262                      ok            True                  False
  ROST           94.29               35            0.52              0.85        234.45                38.50         0.500          pass              0.798             66.7                           0.645                8.88              0.769                      ok            True                   True
  TEAM           91.30               46            0.05              0.03         85.41               109.49         0.695          pass              0.867             98.8                           0.660               -2.21              0.077                      ok           False                  False
   TRI           73.33               15            1.22              0.74         85.54                55.00         0.630          pass              0.259             54.3                           0.512               -4.22              0.110                      ok           False                  False
  CSCO           80.00                5            2.42              2.04        119.54                52.25         0.630          pass              0.100             12.2                           0.282               19.02              1.858                      ok           False                  False
  SBUX          100.00                8            1.79              1.29        102.56                33.02         0.617          pass              0.521             19.7                           0.282               -3.68             -0.292 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-26T12:00:02.390044-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:45:01.347976-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:40:05.359008-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:35:01.343425-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:30:01.341956-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526135003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526135003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526135003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526135003)

</details>

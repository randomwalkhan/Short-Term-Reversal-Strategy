# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 13:05:02 EDT`
Last processed slot: `manage_1300`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           88.57               35            0.57              6.57       1630.09                54.77         0.569            pass              0.654             67.3                           0.624                3.69              0.375                                 ok            True                  False
  MELI           94.29               35            0.95             11.05       1659.69                60.80         0.565            pass              0.805             67.1                           0.691                5.87              0.723                                 ok            True                   True
  AMGN           85.00               20            0.85              2.01        338.44                27.24         0.548            pass              0.275              6.8                           0.126                2.85              0.216                                 ok            True                  False
   ADP           93.33               15            2.06              3.25        223.92                37.70         0.539            pass              0.497             18.2                           0.251                4.25              0.655                                 ok            True                  False
   ROP           81.82               11            1.96              4.49        325.02                26.18         0.528            pass              0.122              4.5                           0.201               -2.52              0.036                                 ok            True                  False
  CTSH           88.46               26            1.21              0.45         52.56                46.65         0.527            pass              0.569             61.2                           0.533                6.55              1.335                                 ok            True                  False
  ROST           93.94               33            0.63              1.04        234.37                38.50         0.506            pass              0.754             59.5                           0.482                8.75              0.764                                 ok            True                  False
  MSFT           86.96               23            1.11              3.25        417.18                23.47         0.500 below_threshold              0.364             14.0                           0.123                0.52              0.266                                 ok            True                  False
  CSCO           80.00                5            2.45              2.07        119.52                52.25         0.628            pass              0.096             11.0                           0.157               18.98              1.856                                 ok           False                  False
  SBUX          100.00                8            1.82              1.31        102.55                33.02         0.615            pass              0.517             18.7                           0.212               -3.70             -0.293            downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.48              0.89         85.48                55.00         0.613            pass              0.229             44.8                           0.360               -4.47              0.099                                 ok           False                  False
   WMT           90.00               10            1.44              1.21        119.75                34.37         0.609            pass              0.348              6.9                           0.189               -7.09             -0.849 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526130502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526130502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526130502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526130502)

</details>

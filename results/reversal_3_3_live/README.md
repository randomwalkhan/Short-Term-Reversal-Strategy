# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:35:01 EDT`
Last processed slot: `manage_1130`

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
  TEAM           90.91               44            0.66              0.40         85.25               109.49         0.670          pass              0.808             83.5                           0.700               -2.81              0.049                                 ok            True                   True
  MELI           92.31               26            1.48             17.23       1657.03                60.80         0.589          pass              0.640             48.7                           0.654                5.30              0.699                                 ok            True                  False
  ASML           87.50               32            1.03             11.78       1627.85                54.77         0.565          pass              0.434             10.2                           0.182                3.21              0.354                                 ok            True                  False
  PAYX           90.91               11            1.30              0.88         96.62                28.52         0.552          pass              0.523             56.7                           0.681                3.29              0.597                                 ok            True                  False
   ADP           94.12               17            1.86              2.93        224.05                37.70         0.538          pass              0.555             26.1                           0.570                4.46              0.664                                 ok            True                  False
  AMGN           84.00               25            0.61              1.45        338.68                27.24         0.528          pass              0.328             22.8                           0.333                3.09              0.227                                 ok            True                  False
   ROP           81.82               11            1.98              4.54        325.00                26.18         0.526          pass              0.118              3.6                           0.130               -2.54              0.035                                 ok            True                  False
  CTSH           88.89               27            1.18              0.43         52.56                46.65         0.523          pass              0.590             62.4                           0.704                6.59              1.337                                 ok            True                  False
  ROST           94.12               34            0.55              0.91        234.42                38.50         0.505          pass              0.780             64.4                           0.549                8.84              0.767                                 ok            True                  False
  CSCO           83.33                6            1.88              1.58        119.73                52.25         0.659          pass              0.250             31.8                           0.422               19.68              1.883                                 ok           False                  False
  INTU           75.00               12            3.92              8.78        316.18                90.56         0.617          pass              0.085              3.5                           0.254              -21.84             -2.298            downtrend_blocked_slope           False                  False
   WMT           90.91               11            1.39              1.17        119.77                34.37         0.608          pass              0.363              1.5                           0.226               -7.05             -0.847 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-26T11:35:01.343425-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:30:01.341956-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:05:05.735209-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:00:04.326254-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T10:55:01.312359-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526113501)

</details>

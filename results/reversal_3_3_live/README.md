# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:45:01 EDT`
Last processed slot: `early_entry_1145`

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
  CSCO           81.82               11            1.72              1.45        119.79                52.25         0.634          pass              0.231             37.6                           0.617               19.87              1.890                      ok            True                  False
  MELI           92.31               26            1.45             16.88       1657.18                60.80         0.591          pass              0.643             49.7                           0.622                5.33              0.700                      ok            True                  False
  ASML           86.21               29            1.37             15.67       1626.18                54.77         0.560          pass              0.348              0.0                           0.150                2.85              0.338                      ok            True                  False
   ADP           93.75               16            1.90              3.00        224.03                37.70         0.542          pass              0.534             24.5                           0.586                4.42              0.662                      ok            True                  False
  PAYX           93.33               15            1.09              0.74         96.68                28.52         0.540          pass              0.634             63.6                           0.716                3.51              0.606                      ok            True                  False
  AMGN           84.62               26            0.56              1.34        338.73                27.24         0.524          pass              0.368             28.5                           0.332                3.14              0.229                      ok            True                  False
  CTSH           89.29               28            1.08              0.40         52.58                46.65         0.523          pass              0.616             65.5                           0.742                6.70              1.341                      ok            True                  False
   ROP           85.71               14            1.83              4.18        325.15                26.18         0.520          pass              0.265             11.2                           0.265               -2.38              0.042                      ok            True                  False
  ROST           94.12               34            0.55              0.91        234.42                38.50         0.505          pass              0.781             64.5                           0.536                8.84              0.768                      ok            True                  False
  TEAM           90.91               44            0.46              0.27         85.30               109.49         0.683          pass              0.825             88.6                           0.767               -2.61              0.058                      ok           False                  False
   TRI           73.33               15            1.26              0.76         85.54                55.00         0.627          pass              0.255             53.0                           0.562               -4.26              0.109                      ok           False                  False
  INTU           76.92               13            3.79              8.49        316.30                90.56         0.621          pass              0.102              6.6                           0.235              -21.73             -2.292 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-26T11:45:01.347976-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:40:05.359008-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:35:01.343425-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:30:01.341956-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:05:05.735209-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:00:04.326254-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526114501)

</details>

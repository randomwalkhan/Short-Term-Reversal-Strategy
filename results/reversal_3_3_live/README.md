# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-07 14:49:26 EDT`
Last processed slot: `manage_1430`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$27,583.50`
- Equity: `$27,583.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CRWD     option         option CRWD260618C00470000      3          2026-05-06         2026-05-07       33.025       51.55 5557.5   56.093868 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
   TXN           91.67               12            1.99              4.03        287.71                67.07         0.691            pass                1.02              0.495                                 ok            True
  INTC          100.00               19            3.21              2.54        111.92                95.68         0.652            pass               63.79              4.316                                 ok            True
  FAST           96.15               26            0.66              0.21         44.62                34.69         0.561            pass               -1.76             -0.070                                 ok            True
   XEL           90.00               30            0.50              0.28         80.43                28.12         0.515            pass                0.84              0.251                                 ok            True
  SBUX           86.67               15            1.97              1.47        105.81                31.94         0.512            pass                4.82              0.821                                 ok            True
 CMCSA           88.89               18            0.81              0.15         26.38                61.67         0.710            pass              -17.11             -1.134 downtrend_blocked_slope_and_streak           False
  NXPI           66.67                3            4.34              9.23        299.60                84.51         0.636            pass               20.41              2.653                                 ok           False
  GEHC           72.97               37            0.82              0.35         61.58                55.11         0.547            pass              -12.39             -1.577            downtrend_blocked_slope           False
  ROST          100.00                7            1.89              3.03        227.61                15.20         0.517            pass               -1.03              0.028                                 ok           False
   ADI           73.33               15            1.98              5.75        413.20                34.89         0.514            pass                0.88              0.350                                 ok           False
   CSX           71.43                7            1.84              0.59         45.33                28.34         0.505            pass               -3.12             -0.167                                 ok           False
   LIN           85.71               14            1.36              4.78        499.82                19.97         0.498 below_threshold               -2.56             -0.290            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-07T14:49:26.807112-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:40:04.362618-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:35:07.263877-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:30:09.464251-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:25:09.092318-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:10:05.300742-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:05:03.851776-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:00:03.857613-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:55:02.803994-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:40:10.073286-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507144926)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507144926)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507144926)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507144926)

</details>

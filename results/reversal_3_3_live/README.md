# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 14:15:05 EDT`
Last processed slot: `manual`

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

- Cash: `$29,983.50`
- Equity: `$29,983.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           84.21               19            4.36              2.82         91.16               115.49         0.609          pass               23.47              3.437                                 ok            True
  FAST           96.15               26            0.61              0.19         44.28                33.68         0.559          pass               -0.82             -0.066                                 ok            True
   XEL           95.65               23            0.75              0.42         80.25                27.43         0.530          pass                0.86              0.162                                 ok            True
    ZS           83.78               37            0.93              0.99        152.37                60.77         0.521          pass               11.72              1.197                                 ok            True
  ORLY           88.89               27            1.10              0.73         94.27                34.97         0.507          pass                0.44              0.229                                 ok            True
  ADSK           85.71               14            2.23              3.93        249.36                40.37         0.502          pass                3.37              0.625                                 ok            True
  CHTR           76.47               17            2.40              2.70        159.08               119.32         0.786          pass              -13.18             -1.233            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.55              0.47         26.04                61.43         0.662          pass               -7.22             -0.653 downtrend_blocked_slope_and_streak           False
  SHOP           85.00               20            2.94              2.30        110.75                82.33         0.586          pass              -13.81             -1.630 downtrend_blocked_slope_and_streak           False
  PYPL           92.59               27            1.01              0.33         46.08                42.03         0.547          pass               -9.36             -1.069 downtrend_blocked_slope_and_streak           False
  NFLX           88.57               35            0.82              0.51         88.04                43.15         0.536          pass               -5.31             -0.606            downtrend_blocked_slope           False
  MSFT           81.82               22            1.30              3.83        419.28                34.38         0.532          pass               -2.16             -0.277            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T14:10:04.922004-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T14:05:07.903857-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T14:00:06.476462-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T13:55:05.067818-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-08T13:40:04.672860-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:35:10.686912-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:30:04.901541-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:25:07.289550-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:10:09.442593-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T13:05:05.272156-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508141505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508141505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508141505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508141505)

</details>

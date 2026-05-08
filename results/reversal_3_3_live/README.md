# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 13:30:04 EDT`
Last processed slot: `manage_1330`

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
  FAST           95.83               24            0.92              0.29         44.24                33.68         0.551          pass               -1.13             -0.081                                 ok            True
   XEL           95.45               22            0.80              0.45         80.24                27.43         0.533          pass                0.81              0.159                                 ok            True
  MSFT           80.77               26            0.89              2.63        419.79                34.38         0.529          pass               -1.75             -0.258                                 ok            True
   ADP           84.21               19            1.19              1.79        213.32                38.09         0.523          pass                7.64              0.700                                 ok            True
    ZS           83.78               37            0.92              0.99        152.37                60.77         0.511          pass               11.72              1.197                                 ok            True
  ADSK           87.50               16            1.87              3.29        249.63                40.37         0.509          pass                3.75              0.642                                 ok            True
  CHTR           78.95               19            2.27              2.55        159.15               119.32         0.785          pass              -13.06             -1.227            downtrend_blocked_slope           False
 CMCSA           80.00                5            2.50              0.46         26.04                61.43         0.665          pass               -7.17             -0.650 downtrend_blocked_slope_and_streak           False
  TEAM           77.27               22            4.04              2.61         91.25               115.49         0.591          pass               23.89              3.452                                 ok           False
  SHOP           86.36               22            2.73              2.13        110.83                82.33         0.586          pass              -13.62             -1.620 downtrend_blocked_slope_and_streak           False
  ORLY           78.57               14            1.50              0.99         94.15                34.97         0.545          pass                0.03              0.211                                 ok           False
  PYPL           92.59               27            1.07              0.35         46.07                42.03         0.542          pass               -9.42             -1.072 downtrend_blocked_slope_and_streak           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-08T13:30:04.901541-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:25:07.289550-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-08T13:10:09.442593-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T13:05:05.272156-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T13:00:07.011484-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T12:55:09.634470-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-08T12:40:09.595901-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:35:05.338232-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:30:08.598241-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-08T12:25:05.406767-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508133004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508133004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508133004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508133004)

</details>

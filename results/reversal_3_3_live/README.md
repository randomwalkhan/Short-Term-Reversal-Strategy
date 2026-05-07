# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 14:30:09 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
 CMCSA           88.89               18            0.83              0.15         26.37                61.67            True
   TXN           85.71               14            1.63              3.30        288.02                67.07            True
  INTC          100.00               20            2.96              2.34        112.01                95.68            True
   XEL           92.00               25            0.67              0.38         80.39                28.12            True
  SBUX           87.50               16            1.72              1.28        105.89                31.94            True
  NXPI           66.67                3            4.09              8.70        299.82                84.51           False
  FAST           96.43               28            0.42              0.13         44.65                34.69           False
  GEHC           76.19               42            0.28              0.12         61.68                55.11           False
  ROST          100.00                5            2.18              3.50        227.41                15.20           False
   ADI           73.68               19            1.81              5.28        413.40                34.89           False
  ASML           80.00               25            1.96             21.21       1535.65                46.11           False
  GOOG           88.10               42            0.28              0.77        394.73                37.75           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-07T14:30:09.464251-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:25:09.092318-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:10:05.300742-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:05:03.851776-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:00:03.857613-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:55:02.803994-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:40:10.073286-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:35:04.908298-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:30:02.811193-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:25:01.880630-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507143009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507143009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507143009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507143009)

</details>

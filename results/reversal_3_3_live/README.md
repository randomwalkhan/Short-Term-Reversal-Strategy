# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 14:40:04 EDT`
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
 CMCSA           88.89               18            0.79              0.15         26.38                61.67            True
   TXN           91.67               12            1.94              3.93        287.76                67.07            True
  INTC          100.00               23            2.75              2.18        112.08                95.68            True
  FAST           96.30               27            0.56              0.18         44.63                34.69            True
   XEL           92.86               28            0.56              0.32         80.41                28.12            True
  SBUX           86.67               15            1.90              1.42        105.83                31.94            True
  NXPI           50.00                2            4.48              9.52        299.47                84.51           False
  GEHC           73.68               38            0.57              0.25         61.63                55.11           False
  ROST          100.00                6            2.03              3.26        227.51                15.20           False
   ADI           71.43               14            2.03              5.90        413.13                34.89           False
  ASML           80.77               26            1.81             19.57       1536.35                46.11           False
   LIN           85.71               14            1.43              5.02        499.72                19.97           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-07T14:40:04.362618-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:35:07.263877-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:30:09.464251-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:25:09.092318-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-07T14:10:05.300742-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:05:03.851776-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T14:00:03.857613-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:55:02.803994-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-07T13:40:10.073286-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-07T13:35:04.908298-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507144004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507144004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507144004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507144004)

</details>

# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 13:25:01 EDT`
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
  INTC          100.00               25            2.25              1.78        112.25                95.68            True
   XEL           92.86               28            0.58              0.33         80.41                28.12            True
  SBUX           90.91               22            1.27              0.95        106.03                31.94            True
  ASML           82.61               23            2.18             23.62       1534.62                46.11            True
   TXN           88.89                9            2.34              4.73        287.41                67.07           False
 CMCSA           90.00               30            0.40              0.07         26.41                61.67           False
  NXPI           66.67                3            4.32              9.18        299.62                84.51           False
  GEHC           76.19               42            0.25              0.11         61.69                55.11           False
  ROST          100.00                6            2.02              3.23        227.52                15.20           False
   ADI           73.33               15            2.01              5.84        413.16                34.89           False
   KDP           89.47               38            0.04              0.01         28.56                34.76           False
  GOOG           88.10               42            0.28              0.77        394.73                37.75           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                  detail
2026-05-07T13:25:01.880630-04:00 manage_1330 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T13:21:58.207270-04:00 manage_1330 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T11:05:05.932561-04:00 manage_1100 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T11:00:04.917667-04:00 manage_1100 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:55:01.919462-04:00 manage_1100 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:40:06.740458-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:35:01.914574-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:30:05.917191-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:25:01.892823-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:20:01.930498-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "CRWD260618C00470000", "fill_price": 51.55, "pnl": 5557.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 56.09, "ticker": "CRWD"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507132501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507132501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507132501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507132501)

</details>

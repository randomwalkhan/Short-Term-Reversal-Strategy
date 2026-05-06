# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-06 14:45:06 EDT`
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
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$22,026.00`
- Equity: `$22,026.00`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  TEAM     option         option TEAM260618C00090000     11          2026-05-05         2026-05-06         9.65       8.685 -1061.499958       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           89.19               37            0.92              1.02        157.79               118.74            True
  TEAM           82.14               28            3.54              2.29         91.37               119.37            True
   XEL           90.00               10            1.42              0.81         81.10                28.13            True
    ZS           80.77               26            1.89              1.87        140.56                69.30            True
  CRWD           80.95               21            1.93              6.43        473.78                50.97            True
  MSTR           87.18               39            1.35              1.77        186.14                66.92            True
  TMUS           86.21               29            0.78              1.06        193.89                36.92            True
   KDP           83.33               18            1.23              0.25         28.81                34.27            True
  PLTR           86.67               30            1.58              1.50        135.27                62.37            True
  PYPL           94.12               34            0.58              0.19         46.40                42.64            True
  PANW           86.11               36            0.69              0.89        183.60                45.58            True
  ADSK           80.00               10            3.24              5.66        247.01                46.09            True
```

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                              detail
2026-05-06T14:40:06.021703-04:00    manage_1430   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T14:35:04.878969-04:00    manage_1430   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T14:30:01.890640-04:00    manage_1430   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T14:25:05.857021-04:00    manage_1430   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T13:39:40.576601-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T11:37:18.444380-04:00    manage_1130   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T10:28:45.392607-04:00    manage_1030           exit                                                                                   {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 8.685, "pnl": -1061.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-05-06T09:35:01.127893-04:00    manage_0930   slot_skipped                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-06T00:00:03.652066-04:00   data_refresh   data_refresh                                                                                                                                                                                                                                                       {'saved': 99}
       2026-05-05T16:01:00-04:00 backfill_audit backfill_audit {"open_positions_after_backfill": 1, "reason": "Mac was offline; reconstructed missed 2026-05-05 ET afternoon slots using stock and option 1m bars clipped at each slot time", "slots": ["manage_1400", "manage_1430", "entry_1500", "manage_1530", "manage_1600"]}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506144506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506144506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506144506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506144506)

</details>

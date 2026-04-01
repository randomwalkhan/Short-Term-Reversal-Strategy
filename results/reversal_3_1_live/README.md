# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 12:00:03 EDT`
Last processed slot: `manage_1200`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart view: default display is trailing `1W`, with latest ET checkpoint annotation and return % axis

## Portfolio Snapshot

- Cash: `$9,742.50`
- Equity: `$9,742.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           93.33               30            0.95              0.64         95.85                24.42            True
   LIN           86.36               22            0.70              2.42        494.72                19.67            True
  MDLZ           85.71               14            0.95              0.38         57.48                24.77            True
   APP           85.37               41            0.85              2.36        396.99                76.97            True
   BKR           83.33               24            0.99              0.42         60.87                41.31            True
   PEP           82.35               17            0.81              0.88        154.91                18.57            True
   EXC           81.82               11            1.05              0.36         48.87                21.40            True
   TRI           81.40               43            0.83              0.52         89.76                41.71            True
  MELI           80.95               42            0.53              6.37       1726.29                41.66            True
 CMCSA           80.00               15            1.81              0.36         28.23                29.02            True
  FANG          100.00                1            3.95              5.47        195.45                24.73           False
  FTNT           93.88               49            0.13              0.08         81.69                30.40           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T12:00:03.162473-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:55:05.887264-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:40:05.886399-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:35:00.893892-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:30:03.989135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:25:05.883135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:10:02.909615-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:05:00.900882-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:00:05.880342-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:55:05.892151-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:10:03 EDT`
Last processed slot: `manage_1400`

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
   LIN           87.50               24            0.62              2.16        494.83                19.67            True
 CMCSA           86.36               22            1.23              0.24         28.28                29.02            True
  MDLZ           84.62               13            0.99              0.40         57.47                24.77            True
   EXC           84.21               19            0.60              0.21         48.93                21.40            True
   APP           83.33               36            1.34              3.75        396.39                76.97            True
   TRI           82.35               34            1.54              0.97         89.56                41.71            True
   BKR           80.00               20            1.36              0.58         60.80                41.31            True
   KDP          100.00                2            2.30              0.42         26.15                19.96           False
  FANG          100.00                1            4.58              6.34        195.07                24.73           False
  NFLX           95.00               40            0.49              0.33         95.98                24.42           False
  FTNT           93.33               45            0.49              0.28         81.60                30.40           False
  ABNB           93.18               44            0.10              0.09        126.24                37.55           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:55:00.878927-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:40:05.881728-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:35:05.876418-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:30:00.896240-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

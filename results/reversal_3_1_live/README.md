# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 13:50:05 EDT`
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
 CMCSA           88.46               26            1.04              0.21         28.29                29.02            True
   LIN           87.50               24            0.62              2.16        494.83                19.67            True
  MDLZ           85.71               14            0.94              0.38         57.48                24.77            True
   APP           83.33               36            1.26              3.50        396.50                76.97            True
   EXC           83.33               18            0.67              0.23         48.92                21.40            True
  VRSK           82.35               17            2.08              2.76        188.55                31.84            True
   BKR           81.82               22            1.24              0.53         60.82                41.31            True
   ADP           80.77               26            0.59              0.83        202.82                25.48            True
  PYPL           80.56               36            0.66              0.21         45.14                33.21            True
   KDP          100.00                2            2.11              0.39         26.16                19.96           False
  FANG          100.00                1            5.10              7.06        194.76                24.73           False
  NFLX           95.65               46            0.26              0.17         96.05                24.42           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T13:40:05.881728-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:35:05.876418-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:30:00.896240-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:00:05.896389-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:55:05.881294-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 13:30:00 EDT`
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
   LIN           88.89               27            0.54              1.88        494.96                19.67            True
   EXC           87.50               16            0.81              0.28         48.90                21.40            True
  CHTR           86.11               36            0.71              1.08        215.42                36.72            True
   APP           85.37               41            0.83              2.32        397.00                76.97            True
 CMCSA           84.21               19            1.52              0.30         28.25                29.02            True
   BKR           82.61               23            1.04              0.44         60.86                41.31            True
  VRSK           82.35               17            2.08              2.77        188.54                31.84            True
  MDLZ           81.82               11            1.14              0.46         57.44                24.77            True
   PEP           80.95               21            0.55              0.60        155.03                18.57            True
   ADP           80.00               25            0.63              0.90        202.79                25.48            True
  FANG          100.00                1            5.02              6.94        194.81                24.73           False
  NFLX           95.35               43            0.34              0.23         96.02                24.42           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T13:30:00.896240-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:00:05.896389-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:55:05.881294-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

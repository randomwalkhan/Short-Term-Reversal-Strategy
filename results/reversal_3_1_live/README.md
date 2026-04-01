# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 13:10:05 EDT`
Last processed slot: `manage_1300`

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
   LIN           88.46               26            0.61              2.11        494.86                19.67            True
   EXC           87.50               16            0.81              0.28         48.90                21.40            True
   BKR           86.21               29            0.80              0.34         60.90                41.31            True
  CHTR           85.71               35            1.00              1.51        215.23                36.72            True
  MDLZ           85.71               14            0.97              0.39         57.47                24.77            True
   APP           85.37               41            0.73              2.03        397.13                76.97            True
 CMCSA           81.25               16            1.71              0.34         28.23                29.02            True
   PEP           80.95               21            0.55              0.60        155.03                18.57            True
   ADP           80.77               26            0.54              0.77        202.85                25.48            True
  FANG          100.00                1            4.79              6.64        194.95                24.73           False
  NFLX           95.35               43            0.33              0.22         96.02                24.42           False
  COST           90.00               40            0.42              2.92        995.18                15.56           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:00:05.896389-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:55:05.881294-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:10:00.904829-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:05:05.895365-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

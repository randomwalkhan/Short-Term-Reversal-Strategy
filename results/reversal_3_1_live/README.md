# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 12:55:05 EDT`
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
   EXC           88.24               17            0.72              0.25         48.91                21.40            True
   APP           86.05               43            0.52              1.44        397.38                76.97            True
  CHTR           85.71               35            1.00              1.51        215.23                36.72            True
   BKR           85.71               28            0.85              0.36         60.89                41.31            True
   LIN           85.71               21            0.79              2.76        494.58                19.67            True
   PEP           83.33               18            0.66              0.72        154.98                18.57            True
  MDLZ           83.33               12            1.05              0.42         57.46                24.77            True
  PYPL           81.58               38            0.54              0.17         45.16                33.21            True
   TRI           81.40               43            0.77              0.49         89.77                41.71            True
 CMCSA           80.00               15            1.80              0.36         28.23                29.02            True
   KDP          100.00                2            2.15              0.40         26.16                19.96           False
  FANG          100.00                1            4.29              5.95        195.24                24.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T12:55:05.881294-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:10:00.904829-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:05:05.895365-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:00:03.162473-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:55:05.887264-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:40:05.886399-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

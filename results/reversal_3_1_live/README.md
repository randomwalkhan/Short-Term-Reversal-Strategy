# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 12:45:05 EDT`
Last processed slot: `manual_refresh`

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
   BKR           87.88               33            0.54              0.23         60.95                41.31            True
   LIN           85.71               21            0.77              2.69        494.61                19.67            True
  CHTR           84.38               32            1.24              1.87        215.08                36.72            True
   EXC           84.21               19            0.62              0.21         48.93                21.40            True
   PEP           83.33               18            0.76              0.83        154.94                18.57            True
  MDLZ           83.33               12            1.05              0.42         57.46                24.77            True
   TRI           82.05               39            1.09              0.69         89.69                41.71            True
 CMCSA           80.00               15            1.83              0.36         28.22                29.02            True
   KDP          100.00                2            2.11              0.39         26.16                19.96           False
  FANG          100.00                1            4.18              5.78        195.31                24.73           False
  NFLX           95.24               42            0.40              0.27         96.01                24.42           False
  COST           91.49               47            0.18              1.24        995.90                15.56           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:10:00.904829-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:05:05.895365-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:00:03.162473-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:55:05.887264-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:40:05.886399-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:35:00.893892-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

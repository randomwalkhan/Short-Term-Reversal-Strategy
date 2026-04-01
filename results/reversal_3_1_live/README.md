# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 13:40:05 EDT`
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
   LIN           87.50               24            0.62              2.16        494.84                19.67            True
   EXC           87.50               16            0.79              0.27         48.90                21.40            True
 CMCSA           85.71               21            1.25              0.25         28.27                29.02            True
   APP           85.37               41            0.94              2.62        396.88                76.97            True
  MDLZ           83.33               12            1.05              0.42         57.46                24.77            True
   BKR           81.82               22            1.13              0.48         60.84                41.31            True
  PYPL           81.58               38            0.56              0.18         45.15                33.21            True
   ADP           80.00               25            0.60              0.85        202.82                25.48            True
  VRSK           80.00               15            2.12              2.81        188.53                31.84            True
  FANG          100.00                1            5.12              7.09        194.75                24.73           False
  NFLX           95.35               43            0.35              0.23         96.02                24.42           False
  FTNT           94.23               52            0.06              0.04         81.70                30.40           False
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

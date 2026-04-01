# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 13:25:00 EDT`
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
   EXC           87.50               16            0.79              0.27         48.90                21.40            True
   LIN           86.36               22            0.71              2.46        494.71                19.67            True
  CHTR           86.11               36            0.70              1.05        215.43                36.72            True
   APP           85.37               41            0.89              2.48        396.94                76.97            True
 CMCSA           84.21               19            1.57              0.31         28.25                29.02            True
   BKR           83.33               24            0.97              0.41         60.87                41.31            True
  MDLZ           83.33               12            1.07              0.43         57.46                24.77            True
   ADP           80.00               25            0.59              0.84        202.82                25.48            True
  FANG          100.00                1            4.97              6.88        194.84                24.73           False
  NFLX           95.24               42            0.38              0.26         96.01                24.42           False
  COST           90.24               41            0.38              2.64        995.30                15.56           False
    EA           88.89               18            0.24              0.34        203.72                 7.29           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:00:05.896389-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:55:05.881294-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T12:40:05.874647-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:10:00.904829-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

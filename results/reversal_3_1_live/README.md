# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 11:05:00 EDT`
Last processed slot: `manage_1100`

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
  NFLX           93.75               32            0.89              0.60         95.86                24.42            True
  MDLZ           88.24               17            0.66              0.27         57.53                24.77            True
   LIN           86.36               22            0.71              2.47        494.70                19.67            True
   EXC           85.71               14            0.86              0.29         48.89                21.40            True
 CMCSA           84.21               19            1.52              0.30         28.25                29.02            True
   APP           83.78               37            1.18              3.30        396.59                76.97            True
   BKR           81.82               22            1.08              0.46         60.85                41.31            True
  WDAY           81.40               43            0.84              0.76        129.59                39.93            True
   TRI           81.40               43            0.82              0.52         89.76                41.71            True
  VRSK           80.00               20            1.89              2.51        188.65                31.84            True
   ADP           80.00               20            0.78              1.11        202.70                25.48            True
  FANG          100.00                6            3.26              4.52        195.85                24.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T11:05:00.900882-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:00:05.880342-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:55:05.892151-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:40:05.895881-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:35:05.886400-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:30:05.913021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

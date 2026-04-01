# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 11:15:05 EDT`
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
  NFLX           93.75               32            0.91              0.61         95.86                24.42            True
   LIN           88.46               26            0.59              2.06        494.88                19.67            True
  MDLZ           88.24               17            0.78              0.32         57.50                24.77            True
 CMCSA           85.71               21            1.34              0.27         28.27                29.02            True
   APP           84.21               38            1.05              2.91        396.75                76.97            True
   EXC           81.82               11            0.92              0.32         48.88                21.40            True
  WDAY           81.40               43            0.80              0.73        129.61                39.93            True
   TRI           81.40               43            0.76              0.48         89.78                41.71            True
   ADP           80.77               26            0.52              0.73        202.87                25.48            True
  MELI           80.49               41            0.79              9.52       1724.94                41.66            True
  CSGP           80.00               30            1.83              0.52         40.12                34.54            True
  CHTR           80.00               25            1.88              2.85        214.66                36.72            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T11:10:02.909615-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:05:00.900882-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:00:05.880342-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:55:05.892151-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:40:05.895881-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:35:05.886400-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:30:05.913021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

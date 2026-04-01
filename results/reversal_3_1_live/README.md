# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 11:25:05 EDT`
Last processed slot: `manage_1130`

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
  NFLX           92.31               26            1.11              0.75         95.80                24.42            True
  MDLZ           88.24               17            0.75              0.30         57.51                24.77            True
   LIN           85.71               21            0.76              2.64        494.63                19.67            True
   APP           84.21               38            1.04              2.88        396.76                76.97            True
 CMCSA           83.33               18            1.59              0.31         28.25                29.02            True
   PEP           83.33               18            0.76              0.83        154.94                18.57            True
   EXC           81.82               11            1.08              0.37         48.86                21.40            True
   TRI           81.40               43            0.89              0.56         89.74                41.71            True
  CSGP           81.25               32            1.78              0.50         40.12                34.54            True
  CHTR           80.00               25            1.87              2.83        214.67                36.72            True
  FANG          100.00                6            3.33              4.61        195.82                24.73           False
   XEL           93.75               32            0.01              0.01         79.44                18.50           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T11:25:05.883135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:10:02.909615-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:05:00.900882-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:00:05.880342-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:55:05.892151-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:40:05.895881-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:35:05.886400-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:30:05.913021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

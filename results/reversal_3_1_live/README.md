# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 11:10:02 EDT`
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
  NFLX           94.12               34            0.88              0.59         95.87                24.42            True
  MDLZ           86.67               15            0.88              0.35         57.49                24.77            True
   LIN           86.36               22            0.72              2.49        494.69                19.67            True
   APP           85.37               41            0.94              2.61        396.88                76.97            True
 CMCSA           84.21               19            1.50              0.30         28.25                29.02            True
   BKR           81.82               22            1.10              0.47         60.85                41.31            True
   EXC           81.82               11            0.99              0.34         48.87                21.40            True
   TRI           81.40               43            0.64              0.41         89.81                41.71            True
  WDAY           81.25               48            0.57              0.52        129.70                39.93            True
  CSGP           81.25               32            1.67              0.47         40.14                34.54            True
   ADP           80.77               26            0.53              0.76        202.85                25.48            True
  FANG          100.00                6            3.25              4.50        195.86                24.73           False
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

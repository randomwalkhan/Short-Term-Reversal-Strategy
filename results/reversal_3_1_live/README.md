# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:30:00 EDT`
Last processed slot: `manage_1430`

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
  NFLX           94.74               38            0.70              0.47         95.92                24.42            True
  FTNT           93.18               44            0.61              0.35         81.57                30.40            True
  ABNB           92.68               41            0.58              0.51        126.06                37.55            True
  MDLZ           86.67               15            0.87              0.35         57.49                24.77            True
 CMCSA           85.71               21            1.32              0.26         28.27                29.02            True
   LIN           85.71               21            0.79              2.73        494.59                19.67            True
   EXC           85.71               21            0.51              0.17         48.95                21.40            True
   TRI           83.33               36            1.23              0.78         89.65                41.71            True
   APP           81.25               32            2.36              6.57        395.18                76.97            True
   BKR           80.95               21            1.29              0.55         60.81                41.31            True
   KDP          100.00                2            2.58              0.48         26.13                19.96           False
  FANG          100.00                1            3.88              5.38        195.49                24.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T14:30:00.899928-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-01T14:25:05.884307-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:55:00.878927-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:40:05.881728-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:35:05.876418-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:30:00.896240-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

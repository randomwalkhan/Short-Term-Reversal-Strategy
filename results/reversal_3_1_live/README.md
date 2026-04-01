# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:15:01 EDT`
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
  NFLX           94.87               39            0.63              0.42         95.94                24.42            True
  FTNT           92.86               42            0.67              0.38         81.56                30.40            True
  MDLZ           86.67               15            0.88              0.36         57.49                24.77            True
   LIN           86.36               22            0.68              2.37        494.74                19.67            True
 CMCSA           85.71               21            1.36              0.27         28.26                29.02            True
   EXC           85.00               20            0.55              0.19         48.94                21.40            True
   APP           83.33               36            1.53              4.27        396.17                76.97            True
   BKR           80.95               21            1.33              0.57         60.81                41.31            True
   ADP           80.00               20            0.79              1.12        202.70                25.48            True
   KDP          100.00                2            2.49              0.46         26.13                19.96           False
  FANG          100.00                1            4.33              6.00        195.22                24.73           False
  ABNB           93.02               43            0.33              0.29        126.15                37.55           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:55:00.878927-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-01T13:40:05.881728-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:35:05.876418-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:30:00.896240-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:25:00.881126-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-01T13:10:05.888806-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-01T13:05:03.096526-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

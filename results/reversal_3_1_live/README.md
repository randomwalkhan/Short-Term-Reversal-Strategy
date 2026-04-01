# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 12:35:05 EDT`
Last processed slot: `manage_1230`

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
  NFLX           95.00               40            0.54              0.36         95.97                24.42            True
   LIN           88.46               26            0.57              1.97        494.92                19.67            True
   BKR           87.50               32            0.70              0.30         60.92                41.31            True
   APP           85.37               41            0.71              1.99        397.15                76.97            True
  MDLZ           84.62               13            1.01              0.41         57.46                24.77            True
  CHTR           83.87               31            1.26              1.91        215.06                36.72            True
   EXC           83.33               18            0.66              0.23         48.92                21.40            True
   TRI           81.82               44            0.56              0.35         89.83                41.71            True
 CMCSA           81.25               16            1.73              0.34         28.23                29.02            True
  FANG          100.00                1            4.35              6.02        195.21                24.73           False
  FTNT           94.23               52            0.09              0.05         81.70                30.40           False
  COST           91.49               47            0.17              1.18        995.92                15.56           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T12:35:05.909248-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:30:00.886617-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:25:05.886998-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-01T12:10:00.904829-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:05:05.895365-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T12:00:03.162473-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:55:05.887264-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-01T11:40:05.886399-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:35:00.893892-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:30:03.989135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

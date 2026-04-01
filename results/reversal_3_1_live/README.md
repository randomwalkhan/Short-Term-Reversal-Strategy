# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:20:05 EDT`
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
  NFLX           94.74               38            0.67              0.45         95.93                24.42            True
  ABNB           93.02               43            0.52              0.46        126.08                37.55            True
  FTNT           92.86               42            0.73              0.42         81.54                30.40            True
  PLTR           90.00               40            0.52              0.53        146.05                50.01            True
  MDLZ           86.67               15            0.85              0.34         57.49                24.77            True
 CMCSA           85.71               21            1.29              0.26         28.27                29.02            True
   EXC           85.71               21            0.51              0.17         48.95                21.40            True
   LIN           83.33               18            0.84              2.90        494.52                19.67            True
   APP           82.86               35            1.91              5.32        395.72                76.97            True
   TRI           81.82               33            1.67              1.05         89.53                41.71            True
   BKR           81.82               22            1.24              0.53         60.82                41.31            True
   ADP           80.00               20            0.78              1.11        202.70                25.48            True
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

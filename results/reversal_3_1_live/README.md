# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:35:05 EDT`
Last processed slot: `manage_1030`

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
  NFLX           96.00               25            1.14              0.77         95.79                24.42            True
   LIN           87.50               16            0.85              2.95        494.50                19.67            True
   TRI           83.78               37            1.14              0.72         89.67                41.71            True
   EXC           83.33               18            0.66              0.23         48.92                21.40            True
   APP           82.86               35            1.78              4.97        395.87                76.97            True
   PEP           82.35               17            0.77              0.84        154.93                18.57            True
  MELI           82.05               39            0.85             10.30       1724.61                41.66            True
  MDLZ           81.82               11            1.11              0.45         57.45                24.77            True
  FANG          100.00                7            3.06              4.23        195.98                24.73           False
  FTNT           94.23               52            0.04              0.02         81.71                30.40           False
  DXCM           94.23               52            0.00              0.00         62.80                32.83           False
   AEP           93.94               33            0.08              0.08        131.05                17.74           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-01T10:35:05.886400-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:30:05.913021-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                   {'saved': 99}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

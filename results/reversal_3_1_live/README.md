# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:25:05 EDT`
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
  NFLX           92.31               26            1.08              0.73         95.81                24.42            True
   LIN           86.67               15            0.95              3.31        494.34                19.67            True
   EXC           86.67               15            0.84              0.29         48.90                21.40            True
   PEP           84.62               13            0.91              0.99        154.86                18.57            True
  BKNG           84.21               38            0.67             19.82       4201.82                42.14            True
   TRI           83.78               37            1.16              0.73         89.67                41.71            True
   APP           83.33               36            1.58              4.39        396.12                76.97            True
  MELI           81.08               37            1.04             12.63       1723.61                41.66            True
   KDP          100.00                2            2.39              0.44         26.14                19.96           False
  FANG          100.00                1            3.92              5.43        195.46                24.73           False
   AEP           93.75               32            0.18              0.16        131.01                17.74           False
    EA           92.31               26            0.14              0.20        203.78                 7.29           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-01T10:25:05.888475-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                   {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                   {'saved': 99}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

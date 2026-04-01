# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:30:05 EDT`
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
  NFLX           93.33               30            0.94              0.63         95.85                24.42            True
   WMT           91.43               35            0.51              0.44        124.08                21.00            True
   LIN           85.71               21            0.74              2.57        494.66                19.67            True
   PEP           84.62               13            0.94              1.02        154.85                18.57            True
   APP           83.78               37            1.23              3.42        396.53                76.97            True
  MELI           82.05               39            0.84             10.16       1724.67                41.66            True
  ADSK           82.05               39            0.58              0.97        238.98                29.70            True
   EXC           81.82               11            0.91              0.31         48.89                21.40            True
   TRI           81.40               43            0.83              0.52         89.76                41.71            True
  VRSK           80.00               15            2.16              2.86        188.50                31.84            True
  FANG          100.00                2            3.75              5.19        195.57                24.73           False
   AEP           93.10               29            0.32              0.29        130.95                17.74           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-01T10:30:05.913021-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                   {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

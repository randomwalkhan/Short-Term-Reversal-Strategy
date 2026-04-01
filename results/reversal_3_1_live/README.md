# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:40:05 EDT`
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
  NFLX           93.10               29            1.05              0.71         95.82                24.42            True
   LIN           86.36               22            0.71              2.45        494.71                19.67            True
   EXC           83.33               18            0.71              0.25         48.91                21.40            True
   APP           82.86               35            1.86              5.19        395.78                76.97            True
  MDLZ           81.82               11            1.15              0.46         57.44                24.77            True
   TRI           81.40               43            0.73              0.46         89.78                41.71            True
  MELI           80.95               42            0.54              6.57       1726.21                41.66            True
  WDAY           80.49               41            1.27              1.15        129.43                39.93            True
  FANG          100.00                6            3.33              4.61        195.82                24.73           False
   AEP           93.75               32            0.19              0.17        131.01                17.74           False
   WMT           93.02               43            0.14              0.13        124.22                21.00           False
    EA           92.59               27            0.10              0.14        203.81                 7.29           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T10:40:05.895881-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:35:05.886400-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:30:05.913021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:25:05.888475-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:10:05.895127-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

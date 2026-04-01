# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:45:05 EDT`
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
  NFLX           93.10               29            1.05              0.71         95.82                24.42            True
   LIN           88.46               26            0.60              2.09        494.86                19.67            True
  MDLZ           88.24               17            0.68              0.27         57.52                24.77            True
   EXC           84.21               19            0.62              0.21         48.93                21.40            True
   APP           82.35               34            2.10              5.85        395.49                76.97            True
  WDAY           81.40               43            0.98              0.89        129.54                39.93            True
  MELI           80.95               42            0.52              6.32       1726.31                41.66            True
   ADP           80.00               20            0.87              1.23        202.65                25.48            True
  FANG          100.00                6            3.20              4.43        195.89                24.73           False
   AEP           94.29               35            0.05              0.05        131.06                17.74           False
    EA           93.55               31            0.07              0.10        203.83                 7.29           False
  PLTR           90.48               42            0.31              0.31        146.15                50.01           False
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

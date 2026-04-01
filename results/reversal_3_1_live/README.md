# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 11:45:05 EDT`
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
  NFLX           93.10               29            1.00              0.67         95.83                24.42            True
  MDLZ           86.67               15            0.82              0.33         57.50                24.77            True
 CMCSA           84.21               19            1.57              0.31         28.25                29.02            True
   PEP           83.33               18            0.75              0.82        154.94                18.57            True
   EXC           81.82               11            1.19              0.41         48.84                21.40            True
   TRI           81.40               43            0.63              0.40         89.81                41.71            True
  MELI           80.49               41            0.61              7.42       1725.84                41.66            True
  CHTR           80.00               25            1.91              2.89        214.64                36.72            True
   BKR           80.00               20            1.34              0.57         60.80                41.31            True
  FANG          100.00                5            3.38              4.68        195.79                24.73           False
   XEL           93.55               31            0.08              0.04         79.42                18.50           False
   AEP           93.10               29            0.27              0.25        130.97                17.74           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-01T11:40:05.886399-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:35:00.893892-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:30:03.989135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:25:05.883135-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-01T11:10:02.909615-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:05:00.900882-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T11:00:05.880342-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:55:05.892151-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-01T10:40:05.895881-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-01T10:35:05.886400-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

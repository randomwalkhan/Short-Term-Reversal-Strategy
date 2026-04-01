# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:50:00 EDT`
Last processed slot: `manage_1100`

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
  NFLX           93.10               29            1.01              0.68         95.83                24.42            True
  MDLZ           88.24               17            0.64              0.26         57.53                24.77            True
   EXC           84.21               19            0.57              0.20         48.94                21.40            True
   APP           83.33               36            1.45              4.05        396.27                76.97            True
  WDAY           81.40               43            0.95              0.86        129.55                39.93            True
  VRSK           80.00               15            2.21              2.94        188.47                31.84            True
 CMCSA           80.00               15            1.85              0.37         28.22                29.02            True
   BKR           80.00               15            1.55              0.66         60.77                41.31            True
  FANG          100.00                6            3.24              4.48        195.87                24.73           False
    EA           92.59               27            0.10              0.14        203.81                 7.29           False
  CTAS           91.11               45            0.07              0.08        169.11                28.13           False
  ALNY           88.00               50            0.44              1.03        330.45                36.48           False
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

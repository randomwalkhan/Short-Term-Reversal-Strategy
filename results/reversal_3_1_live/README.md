# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:15:05 EDT`
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
  NFLX           95.83               24            1.17              0.78         95.78                24.42            True
   LIN           87.50               16            0.86              2.97        494.49                19.67            True
  ALNY           86.96               46            0.74              1.70        330.16                36.48            True
   EXC           86.67               15            0.84              0.29         48.90                21.40            True
   TRI           83.78               37            1.18              0.74         89.66                41.71            True
   APP           83.33               36            1.37              3.83        396.36                76.97            True
  BKNG           82.86               35            0.97             28.69       4198.02                42.14            True
  CTSH           82.35               34            0.68              0.29         61.22                25.11            True
   PEP           81.82               11            1.19              1.29        154.74                18.57            True
  VRSK           80.00               15            2.15              2.86        188.51                31.84            True
  FANG          100.00                2            3.70              5.12        195.60                24.73           False
   KDP          100.00                1            2.96              0.55         26.10                19.96           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                    detail
2026-04-01T10:10:05.895127-04:00  manage_1000 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T10:05:05.886756-04:00  manage_1000 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                                                                                                                             {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped                                                                                                           {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                                                                                                                             {'saved': 99}
2026-03-31T16:00:05.906472-04:00  manage_1600         exit {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

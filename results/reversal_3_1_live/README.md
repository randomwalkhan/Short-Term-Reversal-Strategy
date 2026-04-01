# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:20:00 EDT`
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
  NFLX           95.83               24            1.19              0.80         95.78                24.42            True
   EXC           86.67               15            0.83              0.28         48.90                21.40            True
   LIN           85.71               14            1.02              3.54        494.24                19.67            True
   APP           83.33               36            1.41              3.93        396.31                76.97            True
   TRI           83.33               36            1.33              0.84         89.62                41.71            True
  BKNG           83.33               36            0.81             23.82       4200.11                42.14            True
  CTSH           83.33               36            0.64              0.27         61.23                25.11            True
   PEP           81.82               11            1.14              1.24        154.76                18.57            True
  FANG          100.00                1            3.89              5.39        195.48                24.73           False
   KDP          100.00                1            2.77              0.51         26.11                19.96           False
   AEP           93.75               32            0.20              0.18        131.00                17.74           False
  ABNB           93.18               44            0.06              0.06        126.26                37.55           False
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

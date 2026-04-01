# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:05:05 EDT`
Last processed slot: `manage_1000`

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
  NFLX           95.45               22            1.32              0.89         95.74                24.42            True
  ABNB           92.68               41            0.60              0.53        126.05                37.55            True
   LIN           86.36               22            0.69              2.41        494.73                19.67            True
 CMCSA           85.71               21            1.36              0.27         28.26                29.02            True
   PEP           84.62               13            0.95              1.03        154.85                18.57            True
  CTSH           83.87               31            0.93              0.40         61.18                25.11            True
   APP           83.33               36            1.26              3.50        396.50                76.97            True
  BKNG           82.35               34            1.24             36.41       4194.72                42.14            True
  MDLZ           81.82               11            1.09              0.44         57.45                24.77            True
   TRI           81.58               38            1.10              0.69         89.68                41.71            True
  ADSK           80.00               35            0.82              1.37        238.81                29.70            True
  FANG          100.00                9            2.77              3.83        196.15                24.73           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-04-01T10:05:05.886756-04:00  manage_1000 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T16:00:05.906472-04:00  manage_1600         exit                                         {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

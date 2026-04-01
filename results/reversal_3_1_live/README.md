# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 10:00:03 EDT`
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
  NFLX           95.45               22            1.31              0.88         95.74                24.42            True
  ABNB           93.94               33            0.89              0.79        125.94                37.55            True
  FTNT           93.33               45            0.53              0.30         81.59                30.40            True
 CMCSA           85.71               21            1.27              0.25         28.27                29.02            True
   LIN           85.71               21            0.79              2.75        494.58                19.67            True
   APP           83.33               36            1.55              4.32        396.15                76.97            True
  MDLZ           83.33               12            1.08              0.43         57.45                24.77            True
  CTSH           82.76               29            1.19              0.51         61.13                25.11            True
   TRI           82.05               39            1.04              0.66         89.70                41.71            True
   PEP           81.82               11            1.06              1.16        154.79                18.57            True
   ROP           81.40               43            0.50              1.25        353.33                20.64            True
   BKR           80.00               15            1.55              0.66         60.77                41.31            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-04-01T10:00:03.885645-04:00  manage_1000 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:55:03.975227-04:00  manage_1000 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:40:04.884111-04:00  manage_0930 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:35:00.954357-04:00  manage_0930 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T16:00:05.906472-04:00  manage_1600         exit                                         {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
2026-03-31T10:30:05.893788-04:00  manage_1030         exit                                          {"contract_symbol": "FANG260515C00200000", "pnl": 390.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 11.3, "ticker": "FANG"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

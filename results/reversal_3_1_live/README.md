# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:55:05 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$5,355.00`
- Equity: `$9,697.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$-45.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                  4.82       95.56         95.64           -45.0                  -1.03         94.87               39              0.58         41.74            40.8                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           95.00               40            0.50              0.34         95.97                24.42            True
  ABNB           93.94               33            1.06              0.94        125.88                37.55            True
  FTNT           93.18               44            0.62              0.36         81.57                30.40            True
  SHOP           86.67               45            0.57              0.47        118.42                49.70            True
  MDLZ           86.67               15            0.84              0.34         57.49                24.77            True
 CMCSA           85.71               21            1.37              0.27         28.26                29.02            True
   LIN           85.71               21            0.75              2.59        494.65                19.67            True
  BKNG           83.33               36            0.79             23.20       4200.38                42.14            True
   BKR           81.82               22            1.06              0.45         60.86                41.31            True
   TRI           81.25               32            1.68              1.06         89.53                41.71            True
  WDAY           80.49               41            1.02              0.93        129.52                39.93            True
  MELI           80.49               41            0.58              7.00       1726.02                41.66            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                            detail
2026-04-01T14:55:05.885525-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:50:05.934010-04:00  entry_1500        entry {"allocated_cash": 4387.5, "contract_symbol": "NFLX260508C00096000", "contracts": 9, "entry_option_price": 4.875, "matched_signals": 39, "success_rate": 94.87, "ticker": "NFLX"}
2026-04-01T14:40:05.889929-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:35:05.888067-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:30:00.899928-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:25:05.884307-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T13:55:00.878927-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 15:00:05 EDT`
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
- Equity: `$9,675.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$-67.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                   4.8       95.56         95.61           -67.5                  -1.54         94.87               39              0.58         41.74           40.92                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           95.00               40            0.54              0.36         95.96                24.42            True
  ABNB           93.75               32            1.16              1.02        125.84                37.55            True
  FTNT           93.18               44            0.56              0.32         81.58                30.40            True
  MDLZ           88.24               17            0.76              0.31         57.51                24.77            True
  SHOP           86.36               44            0.58              0.48        118.41                49.70            True
   LIN           86.36               22            0.68              2.35        494.75                19.67            True
 CMCSA           85.71               21            1.29              0.26         28.27                29.02            True
  BKNG           82.86               35            0.88             26.03       4199.17                42.14            True
   TRI           82.35               34            1.54              0.97         89.56                41.71            True
   BKR           81.82               22            1.06              0.45         60.86                41.31            True
  WDAY           81.40               43            0.89              0.81        129.57                39.93            True
  MELI           80.95               42            0.52              6.31       1726.31                41.66            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                            detail
2026-04-01T15:00:05.918391-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:55:05.885525-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:50:05.934010-04:00  entry_1500        entry {"allocated_cash": 4387.5, "contract_symbol": "NFLX260508C00096000", "contracts": 9, "entry_option_price": 4.875, "matched_signals": 39, "success_rate": 94.87, "ticker": "NFLX"}
2026-04-01T14:40:05.889929-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:35:05.888067-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:30:00.899928-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:25:05.884307-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

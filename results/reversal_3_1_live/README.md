# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 14:50:05 EDT`
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
- Equity: `$9,742.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                  4.88       95.56         95.51             0.0                    0.0         94.87               39              0.58         41.74           41.74                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           94.87               39            0.58              0.39         95.95                24.42            True
  ABNB           93.94               33            0.91              0.81        125.93                37.55            True
  FTNT           93.18               44            0.59              0.34         81.58                30.40            True
  MDLZ           88.24               17            0.75              0.30         57.51                24.77            True
  SHOP           86.36               44            0.64              0.53        118.39                49.70            True
   LIN           86.36               22            0.69              2.41        494.73                19.67            True
 CMCSA           85.71               21            1.36              0.27         28.26                29.02            True
  BKNG           85.00               40            0.61             18.00       4202.60                42.14            True
   BKR           83.33               24            0.95              0.41         60.88                41.31            True
   TRI           81.82               33            1.60              1.01         89.55                41.71            True
  MELI           80.95               42            0.56              6.78       1726.11                41.66            True
   APP           80.65               31            2.47              6.87        395.06                76.97            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                            detail
2026-04-01T14:50:05.934010-04:00  entry_1500        entry {"allocated_cash": 4387.5, "contract_symbol": "NFLX260508C00096000", "contracts": 9, "entry_option_price": 4.875, "matched_signals": 39, "success_rate": 94.87, "ticker": "NFLX"}
2026-04-01T14:40:05.889929-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:35:05.888067-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:30:00.899928-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:25:05.884307-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:10:03.897935-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:05:05.912655-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:00:05.891489-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T13:55:00.878927-04:00 manage_1400 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T13:40:05.881728-04:00 manage_1330 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

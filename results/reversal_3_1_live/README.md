# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 15:55:00 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$9,765.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$22.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                   4.9       95.56         95.64            22.5                   0.51         94.87               39              0.58         41.74           41.58                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           95.00               40            0.51              0.34         95.97                24.42            True
  ABNB           94.12               34            0.84              0.74        125.96                37.55            True
  FTNT           92.86               42            0.69              0.39         81.55                30.40            True
  DXCM           92.68               41            1.00              0.44         62.61                32.83            True
 CMCSA           88.00               25            1.15              0.23         28.28                29.02            True
  ALNY           86.96               46            0.76              1.76        330.14                36.48            True
  BKNG           83.33               36            0.83             24.33       4199.89                42.14            True
   BKR           83.33               24            1.00              0.43         60.87                41.31            True
  MDLZ           83.33               12            1.05              0.42         57.46                24.77            True
   APP           81.25               32            2.39              6.65        395.15                76.97            True
  CSGP           81.25               32            1.65              0.47         40.14                34.54            True
  ADSK           81.08               37            0.67              1.13        238.92                29.70            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                            detail
2026-04-01T15:55:00.975857-04:00 manage_1600 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:25:05.904161-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:10:05.885233-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:05:05.887661-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:00:05.918391-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:55:05.885525-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:50:05.934010-04:00  entry_1500        entry {"allocated_cash": 4387.5, "contract_symbol": "NFLX260508C00096000", "contracts": 9, "entry_option_price": 4.875, "matched_signals": 39, "success_rate": 94.87, "ticker": "NFLX"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

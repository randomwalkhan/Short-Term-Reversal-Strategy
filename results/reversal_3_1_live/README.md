# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 14:15:01 EDT`
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

- Cash: `$10,845.00`
- Equity: `$10,845.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.22               36            1.48              3.09        296.41                91.06            True
  UPRO           92.31               39            0.68              0.47         98.97                57.18            True
  MPWR           91.89               37            0.64              4.99       1117.37                56.57            True
  DXCM           89.74               39            1.11              0.48         62.16                31.67            True
  FAST           89.29               28            0.90              0.29         46.50                21.97            True
   MAR           88.89               27            1.02              2.37        332.44                28.45            True
  GILD           88.46               26            0.81              0.79        139.96                21.47            True
  ORLY           88.24               34            0.78              0.50         91.88                22.81            True
  CDNS           87.88               33            1.50              2.93        278.93                26.25            True
  KLAC           87.50               32            1.12             11.91       1514.74                56.48            True
  MCHP           85.29               34            0.93              0.43         65.20                45.66            True
  SOXL           85.29               34            0.82              0.30         52.13               138.72            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T14:10:05.893357-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T14:05:05.889867-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T14:00:05.896681-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T13:55:05.905247-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T13:40:05.899103-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:35:05.898186-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:30:05.883847-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:25:05.885731-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:10:05.901781-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T13:05:05.894561-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

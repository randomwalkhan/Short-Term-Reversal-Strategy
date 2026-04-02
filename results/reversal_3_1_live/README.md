# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 14:20:05 EDT`
Last processed slot: `manage_1430`

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
   WDC           97.22               36            1.46              3.04        296.43                91.06            True
  ABNB           92.50               40            0.67              0.59        124.94                36.75            True
  UPRO           92.31               39            0.66              0.46         98.97                57.18            True
  MPWR           91.89               37            0.57              4.49       1117.58                56.57            True
  DXCM           90.48               42            1.01              0.44         62.18                31.67            True
   MAR           89.29               28            0.96              2.23        332.50                28.45            True
  SNPS           89.13               46            0.52              1.45        396.12                35.88            True
  ORLY           88.57               35            0.74              0.48         91.90                22.81            True
  FAST           88.46               26            0.97              0.31         46.50                21.97            True
  GILD           88.46               26            0.80              0.78        139.96                21.47            True
  KLAC           87.50               32            1.13             11.98       1514.70                56.48            True
  CDNS           87.10               31            1.56              3.07        278.88                26.25            True
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

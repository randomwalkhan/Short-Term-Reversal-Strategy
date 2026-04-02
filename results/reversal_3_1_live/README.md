# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 12:25:05 EDT`
Last processed slot: `manage_1230`

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
   WDC           97.37               38            0.83              1.73        296.99                91.06            True
  MRVL           94.74               38            0.82              0.61        106.45                92.70            True
  ROST           92.59               27            0.59              0.90        219.56                21.27            True
  DXCM           91.11               45            0.80              0.35         62.22                31.67            True
  PCAR           90.00               40            0.59              0.49        117.44                23.75            True
  MPWR           90.00               30            1.54             12.10       1114.33                56.57            True
  AVGO           89.74               39            0.82              1.81        312.72                41.97            True
  UPRO           89.66               29            1.34              0.93         98.77                57.18            True
  CDNS           89.47               38            1.27              2.50        279.12                26.25            True
  GILD           88.46               26            0.67              0.65        140.02                21.47            True
   BKR           87.88               33            0.68              0.29         60.22                40.20            True
  SNPS           87.80               41            0.85              2.37        395.72                35.88            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                     detail
2026-04-02T12:25:05.909945-04:00 manage_1230 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T12:10:05.892027-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T12:05:05.882439-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T12:00:03.471000-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:55:05.888116-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:40:05.909108-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:35:01.344213-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:30:05.918886-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:25:05.883603-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:20:05.893680-04:00 manage_1130         exit {"contract_symbol": "NFLX260508C00096000", "pnl": 1102.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.13, "ticker": "NFLX"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

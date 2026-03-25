# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-24 15:30:03 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_only_filtered`
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every hour through `3:30 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed

## Portfolio Snapshot

- Cash: `$5,455.00`
- Equity: `$9,885.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-115.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   0               22.72                 22.15      318.55        319.14          -115.0                  -2.53         93.33               30              1.23         48.32           46.95                   39.5
```

## Today's Closed Trades (2026-03-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               19            0.56              0.88        222.63                23.58            True
  AVGO           93.33               30            1.30              2.94        321.25                39.50            True
  SBUX           93.33               15            1.45              0.96         93.42                29.88            True
    MU           92.86               28            2.00              5.67        401.92                68.53            True
  ABNB           92.59               27            1.38              1.28        132.04                36.74            True
  CTAS           88.89               18            1.15              1.46        180.59                24.07            True
  NFLX           88.24               17            1.82              1.19         92.87                53.50            True
  ORLY           86.67               30            0.89              0.55         88.46                20.87            True
  MNST           82.14               28            0.80              0.41         73.78                28.32            True
  SHOP           81.25               16            3.81              3.23        119.72                55.40            True
  IDXX           80.00               35            0.89              3.62        576.96                30.78            True
  PLTR           80.00               15            3.40              3.83        159.26                47.08            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
2026-03-24T13:30:05.751589-04:00  manage_1330 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-24T13:25:36.643365-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-23T20:59:15.901018-04:00       manual    pre_start                                                                                                                                                       {"start_date": "2026-03-24"}
```

## Equity Curve

![Reversal 3.0 Live Equity](../../assets/reversal_3_0_live_equity.png)

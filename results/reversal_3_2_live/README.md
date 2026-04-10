# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 15:25:06 EDT`
Last processed slot: `manage_1530`

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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,425.00`
- Equity: `$12,340.00`
- Realized PnL: `$2,235.00`
- Unrealized PnL: `$105.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260522C00235000       2026-04-10                   0          7      5810.0                  5915.0                 8.3                  8.45      234.53        234.63           105.0                   1.81         100.0               22              0.65         29.29            29.5                  23.67
```

## Today's Closed Trades (2026-04-10)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  REGN REGN260515C00765000          2026-04-09         2026-04-10                44.0               36.1 -790.0  -17.954545 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               22            0.61              1.01        235.63                23.67            True
  SBUX           94.29               35            0.63              0.43         96.74                40.73            True
  ROST           90.00               10            1.54              2.43        223.87                24.66            True
  SNPS           88.89               18            2.60              7.38        401.68                36.22            True
  ABNB           88.57               35            0.77              0.70        128.86                41.65            True
  SHOP           86.67               30            1.73              1.36        111.72                49.23            True
  TTWO           86.49               37            0.96              1.33        197.48                26.78            True
  PLTR           86.21               29            1.99              1.82        129.76                58.33            True
  CHTR           86.21               29            1.45              2.26        222.26                29.22            True
   CSX           85.71               21            0.87              0.26         42.38                21.51            True
   PEP           85.71               21            0.65              0.72        157.18                20.58            True
  DDOG           85.00               20            3.39              2.58        107.87                49.83            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-10T15:25:06.434467-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T15:10:06.450785-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T15:05:06.434805-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T15:00:06.450530-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:55:06.442916-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:50:01.462254-04:00  entry_1500        entry {"allocated_cash": 5810.0, "contract_symbol": "HON260522C00235000", "contracts": 7, "entry_option_price": 8.3, "matched_signals": 22, "success_rate": 100.0, "ticker": "HON"}
2026-04-10T14:40:06.463610-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:35:06.428666-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:30:06.426052-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:25:06.437702-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410152506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410152506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410152506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410152506)

</details>

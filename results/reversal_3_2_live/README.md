# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 15:05:06 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,425.00`
- Equity: `$12,375.00`
- Realized PnL: `$2,235.00`
- Unrealized PnL: `$140.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260522C00235000       2026-04-10                   0          7      5810.0                  5950.0                 8.3                   8.5      234.53        234.53           140.0                   2.41         100.0               22              0.65         29.29           29.98                  23.67
```

## Today's Closed Trades (2026-04-10)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  REGN REGN260515C00765000          2026-04-09         2026-04-10                44.0               36.1 -790.0  -17.954545 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               22            0.62              1.03        235.62                23.67            True
  SNPS           88.89               18            2.73              7.72        401.53                36.22            True
  ABNB           88.24               34            0.95              0.86        128.79                41.65            True
  TTWO           86.49               37            1.04              1.44        197.43                26.78            True
  PLTR           86.21               29            2.24              2.05        129.66                58.33            True
  CHTR           86.21               29            1.34              2.09        222.33                29.22            True
   CSX           85.71               21            0.84              0.25         42.38                21.51            True
  ROST           85.71               14            1.32              2.07        224.02                24.66            True
  SHOP           84.62               26            2.21              1.73        111.56                49.23            True
   BKR           83.87               31            0.86              0.38         63.26                35.49            True
  DDOG           83.33               18            3.90              2.98        107.70                49.83            True
  ISRG           82.93               41            0.77              2.45        453.89                22.96            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-10T15:05:06.434805-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T15:00:06.450530-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:55:06.442916-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:50:01.462254-04:00  entry_1500        entry {"allocated_cash": 5810.0, "contract_symbol": "HON260522C00235000", "contracts": 7, "entry_option_price": 8.3, "matched_signals": 22, "success_rate": 100.0, "ticker": "HON"}
2026-04-10T14:40:06.463610-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:35:06.428666-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:30:06.426052-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:25:06.437702-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:10:05.436380-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:05:04.428423-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410150506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410150506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410150506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410150506)

</details>

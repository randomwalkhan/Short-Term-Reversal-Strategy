# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 14:50:01 EDT`
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
- Equity: `$12,235.00`
- Realized PnL: `$2,235.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260522C00235000       2026-04-10                   0          7      5810.0                  5810.0                 8.3                   8.3      234.53        234.57             0.0                    0.0         100.0               22              0.65         29.29           29.29                  23.67
```

## Today's Closed Trades (2026-04-10)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  REGN REGN260515C00765000          2026-04-09         2026-04-10                44.0               36.1 -790.0  -17.954545 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               22            0.65              1.07        235.60                23.67            True
  ABNB           90.62               32            1.18              1.06        128.70                41.65            True
  ROST           89.47               19            1.18              1.86        224.11                24.66            True
  CHTR           88.57               35            0.95              1.49        222.59                29.22            True
  SNPS           88.24               17            2.92              8.26        401.30                36.22            True
  TTWO           85.71               35            1.26              1.74        197.30                26.78            True
   CSX           85.00               20            0.98              0.29         42.37                21.51            True
  DDOG           84.62               13            4.74              3.62        107.43                49.83            True
  SHOP           83.33               24            2.81              2.21        111.36                49.23            True
  PLTR           83.33               18            3.72              3.40        129.08                58.33            True
   EXC           83.33               12            1.16              0.40         49.27                21.05            True
  ODFL           82.86               35            0.71              1.04        209.06                37.04            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-10T14:50:01.462254-04:00  entry_1500        entry {"allocated_cash": 5810.0, "contract_symbol": "HON260522C00235000", "contracts": 7, "entry_option_price": 8.3, "matched_signals": 22, "success_rate": 100.0, "ticker": "HON"}
2026-04-10T14:40:06.463610-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:35:06.428666-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:30:06.426052-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:25:06.437702-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:10:05.436380-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:05:04.428423-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T14:00:06.425709-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T13:55:01.428998-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-10T13:40:01.464603-04:00 manage_1330 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410145001)

</details>

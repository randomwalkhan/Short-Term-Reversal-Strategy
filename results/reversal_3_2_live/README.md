# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 09:35:05 EDT`
Last processed slot: `manage_0930`

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
- Chart views: GitHub-native `1D / 1W / 1M`, default open panel is `1W`

## Portfolio Snapshot

- Cash: `$8,102.50`
- Equity: `$10,907.50`
- Realized PnL: `$845.00`
- Unrealized PnL: `$62.50`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   1               27.42                 28.05      294.77        301.48            62.5                   2.28         97.22               36              0.99         81.84             0.0                  91.06
```

## Today's Closed Trades (2026-04-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CDNS           90.91               44            0.60              1.18        278.21                25.28            True
  ORLY           87.88               33            0.79              0.51         91.20                22.90            True
  SNPS           87.80               41            0.78              2.16        395.03                35.67            True
  ASML           87.10               31            1.08              9.96       1312.96                51.28            True
  CTAS           86.67               30            0.68              0.83        173.99                28.60            True
  DDOG           85.19               27            2.28              1.92        119.54                49.88            True
  TMUS           84.00               25            0.78              1.11        200.93                22.45            True
  VRSK           83.72               43            0.51              0.66        184.80                33.36            True
  CTSH           83.33               30            1.10              0.48         62.33                26.11            True
  PANW           81.40               43            0.53              0.61        162.95                41.77            True
  TTWO           80.95               42            0.77              1.08        199.41                26.67            True
   ADP           80.00               20            0.89              1.27        203.47                24.00            True
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                                    detail
2026-04-06T09:35:05.895013-04:00 manage_0930  slot_skipped                           {"reason": "already_processed"}
       2026-04-03T16:00:00-04:00 manage_1600 market_closed {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:35:05.886679-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:30:05.889337-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:25:05.929228-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:10:05.887758-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png)

</details>

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 09:30:05 EDT`
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
   WDC WDC260501C00295000       2026-04-02                   1               27.42                 28.05      294.77        303.65            62.5                   2.28         97.22               36              0.99         81.84             0.0                  91.06
```

## Today's Closed Trades (2026-04-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               22            0.61              0.99        229.03                20.57            True
   XEL           93.33               15            0.82              0.46         80.54                19.13            True
  FAST           90.62               32            0.71              0.23         46.20                21.85            True
   MAR           89.29               28            0.97              2.25        330.97                27.74            True
   CSX           89.29               28            0.53              0.15         41.15                27.22            True
   KDP           88.89               18            0.55              0.10         25.27                19.41            True
  CTAS           87.88               33            0.52              0.64        174.07                28.60            True
  ORLY           87.50               32            0.80              0.51         91.20                22.90            True
  DDOG           85.19               27            2.45              2.06        119.48                49.88            True
   EXC           84.21               19            0.57              0.20         49.25                21.30            True
  IDXX           80.95               42            0.55              2.18        568.61                25.39            True
  FANG          100.00               30            0.15              0.21        193.79                28.70           False
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                                    detail
       2026-04-03T16:00:00-04:00 manage_1600 market_closed {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:35:05.886679-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:30:05.889337-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:25:05.929228-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:10:05.887758-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:00:05.892985-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
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

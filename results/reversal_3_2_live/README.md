# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 10:00:06 EDT`
Last processed slot: `manage_1000`

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
   WDC WDC260501C00295000       2026-04-02                   1               27.42                 28.05      294.77        309.18            62.5                   2.28         97.22               36              0.99         81.84             0.0                  91.06
```

## Today's Closed Trades (2026-04-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               22            0.61              0.97        229.03                20.57            True
  ASML           88.24               34            0.75              6.92       1314.27                51.28            True
  DDOG           85.19               27            2.38              2.00        119.50                49.88            True
  CTSH           84.21               38            0.53              0.23         62.44                26.11            True
   PEP           82.35               17            0.81              0.89        156.63                18.34            True
  TTWO           81.08               37            1.21              1.69        199.15                26.67            True
  PANW           80.95               42            0.62              0.71        162.91                41.77            True
   AEP           94.59               37            0.02              0.02        132.67                17.01           False
  FAST           92.86               42            0.35              0.11         46.25                21.85           False
  NVDA           92.50               40            0.26              0.32        177.25                36.70           False
  PCAR           91.49               47            0.04              0.04        118.30                23.40           False
  COST           90.70               43            0.31              2.18       1014.03                14.21           False
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                                    detail
2026-04-06T10:00:06.219713-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:55:02.509102-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:40:00.944679-04:00 manage_0930  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:35:05.895013-04:00 manage_0930  slot_skipped                           {"reason": "already_processed"}
       2026-04-03T16:00:00-04:00 manage_1600 market_closed {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:35:05.886679-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:30:05.889337-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
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

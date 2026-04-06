# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 10:15:05 EDT`
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
- Chart views: GitHub-native `1D / 1W / 1M`, default open panel is `1W`

## Portfolio Snapshot

- Cash: `$8,102.50`
- Equity: `$11,440.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$595.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   1               27.42                 33.38      294.77         311.5           595.0                   21.7         97.22               36              0.99         81.84            75.6                  91.06
```

## Today's Closed Trades (2026-04-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CDNS           90.91               44            0.64              1.24        278.19                25.28            True
  AVGO           89.74               39            0.79              1.73        313.81                41.04            True
  TSLA           84.62               39            0.52              1.30        360.03                42.35            True
  CTSH           83.78               37            0.61              0.27         62.43                26.11            True
  DDOG           82.61               23            2.80              2.36        119.35                49.88            True
  ASML           81.82               22            1.71             15.74       1310.49                51.28            True
  CRWD           81.40               43            0.56              1.57        398.45                42.36            True
   PEP           80.95               21            0.56              0.62        156.74                18.34            True
  PANW           80.49               41            0.81              0.92        162.81                41.77            True
  TTWO           80.00               30            1.51              2.11        198.96                26.67            True
  FANG          100.00               32            0.02              0.03        193.87                28.70           False
   HON          100.00               25            0.48              0.78        229.12                20.57           False
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                                    detail
2026-04-06T10:10:05.890008-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T10:05:05.886743-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T10:00:06.219713-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:55:02.509102-04:00 manage_1000  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:40:00.944679-04:00 manage_0930  slot_skipped                           {"reason": "already_processed"}
2026-04-06T09:35:05.895013-04:00 manage_0930  slot_skipped                           {"reason": "already_processed"}
       2026-04-03T16:00:00-04:00 manage_1600 market_closed {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
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

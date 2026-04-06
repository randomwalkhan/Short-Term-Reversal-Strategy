# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 10:10:05 EDT`
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
- Equity: `$11,317.50`
- Realized PnL: `$845.00`
- Unrealized PnL: `$472.50`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   1               27.42                 32.15      294.77        308.54           472.5                  17.23         97.22               36              0.99         81.84           77.32                  91.06
```

## Today's Closed Trades (2026-04-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               20            0.81              1.29        228.90                20.57            True
  MRVL           95.35               43            0.54              0.40        106.94                90.41            True
  NVDA           91.67               36            0.71              0.89        177.01                36.70            True
  AVGO           90.91               33            1.12              2.46        313.49                41.04            True
  CDNS           90.70               43            0.68              1.33        278.15                25.28            True
  SNPS           89.13               46            0.60              1.67        395.23                35.67            True
  FAST           88.89               27            0.95              0.31         46.17                21.85            True
  CTSH           83.87               31            1.02              0.45         62.35                26.11            True
  TSLA           83.78               37            0.71              1.79        359.82                42.35            True
  ASML           81.82               22            1.80             16.63       1310.10                51.28            True
   PEP           81.82               22            0.50              0.55        156.77                18.34            True
  MELI           80.95               42            0.63              7.62       1712.25                39.93            True
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

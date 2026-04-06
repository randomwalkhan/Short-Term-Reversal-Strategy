# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:30:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$11,440.00`
- Equity: `$11,440.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-06)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price   pnl  return_pct                  exit_reason
   WDC WDC260501C00295000          2026-04-02         2026-04-06              27.425             33.375 595.0   21.695533 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               24            0.57              0.92        229.06                20.57            True
  FTNT           92.68               41            0.78              0.45         82.34                30.26            True
  FAST           91.67               36            0.58              0.19         46.22                21.85            True
  CDNS           90.70               43            0.85              1.65        278.01                25.28            True
  AVGO           89.74               39            0.64              1.41        313.95                41.04            True
  SNPS           89.13               46            0.61              1.69        395.22                35.67            True
  ASML           85.19               27            1.39             12.80       1311.75                51.28            True
  TSLA           85.00               20            1.99              5.03        358.44                42.35            True
  TMUS           84.00               25            0.94              1.33        200.83                22.45            True
  CTSH           83.87               31            0.96              0.42         62.36                26.11            True
   PEP           83.33               18            0.74              0.82        156.66                18.34            True
  FANG          100.00               29            0.24              0.32        193.74                28.70           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:25:05.885117-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:10:05.890334-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:00:03.415712-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:55:05.885281-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:30:05.886948-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:25:05.896716-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
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

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:35:05 EDT`
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
   HON          100.00               23            0.59              0.94        229.05                20.57            True
  FTNT           93.02               43            0.67              0.38         82.37                30.26            True
  FAST           91.89               37            0.52              0.17         46.23                21.85            True
  CDNS           90.70               43            0.80              1.56        278.05                25.28            True
  AVGO           89.74               39            0.67              1.48        313.92                41.04            True
  SNPS           89.13               46            0.63              1.75        395.20                35.67            True
  TMUS           86.96               23            1.02              1.43        200.79                22.45            True
   LIN           85.19               27            0.50              1.76        501.85                19.40            True
  TSLA           85.00               20            2.20              5.56        358.21                42.35            True
  ASML           84.62               26            1.49             13.74       1311.34                51.28            True
  CTSH           83.87               31            0.88              0.38         62.38                26.11            True
   PEP           83.33               18            0.73              0.80        156.67                18.34            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:25:05.885117-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:10:05.890334-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:00:03.415712-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:55:05.885281-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:30:05.886948-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
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

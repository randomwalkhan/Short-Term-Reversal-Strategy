# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 13:05:05 EDT`
Last processed slot: `manage_1300`

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
   HON          100.00               20            0.82              1.32        228.88                20.57            True
  TSLA          100.00               13            3.35              8.46        356.96                42.35            True
  INTC           94.29               35            0.81              0.29         50.26                73.98            True
  FAST           90.62               32            0.72              0.23         46.20                21.85            True
  AVGO           89.74               39            0.65              1.43        313.94                41.04            True
  PLTR           87.50               40            0.67              0.70        148.16                50.29            True
   LIN           87.50               16            0.87              3.06        501.29                19.40            True
  ASML           86.67               30            1.24             11.43       1312.33                51.28            True
  TMUS           85.00               20            1.10              1.55        200.73                22.45            True
   PEP           84.21               19            0.67              0.73        156.70                18.34            True
  VRSK           82.93               41            0.57              0.74        184.76                33.36            True
  CTSH           82.35               34            0.69              0.30         62.41                26.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T13:05:05.883688-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:00:05.887824-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:55:05.885407-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:40:05.887169-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:35:05.882900-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:30:05.890457-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:25:05.881954-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:00:03.424842-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
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

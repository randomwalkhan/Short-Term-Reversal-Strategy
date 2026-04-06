# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 13:10:05 EDT`
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
   HON          100.00               19            0.95              1.53        228.79                20.57            True
  TSLA          100.00               11            3.60              9.08        356.70                42.35            True
  INTC           94.44               36            0.60              0.21         50.29                73.98            True
  FAST           90.00               30            0.86              0.28         46.18                21.85            True
  AVGO           89.74               39            0.87              1.93        313.72                41.04            True
  PLTR           87.50               40            0.78              0.81        148.11                50.29            True
  ASML           87.10               31            1.17             10.82       1312.59                51.28            True
   LIN           86.67               15            0.95              3.35        501.16                19.40            True
  TMUS           83.33               18            1.13              1.60        200.72                22.45            True
  CTSH           81.82               33            0.74              0.32         62.40                26.11            True
   PEP           80.95               21            0.57              0.62        156.74                18.34            True
  TTWO           80.77               26            1.74              2.44        198.83                26.67            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T13:10:05.894755-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:05:05.883688-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:00:05.887824-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:55:05.885407-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:40:05.887169-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:35:05.882900-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:30:05.890457-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:25:05.881954-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
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

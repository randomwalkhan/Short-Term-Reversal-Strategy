# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 12:40:05 EDT`
Last processed slot: `manage_1230`

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
   HON          100.00               21            0.71              1.13        228.96                20.57            True
  FAST           90.62               32            0.72              0.23         46.20                21.85            True
  AVGO           89.74               39            0.72              1.58        313.87                41.04            True
  ASML           87.10               31            1.12             10.33       1312.80                51.28            True
   EXC           85.71               21            0.52              0.18         49.25                21.30            True
   LIN           85.71               14            0.99              3.49        501.11                19.40            True
  TSLA           85.00               20            2.45              6.20        357.93                42.35            True
  CTSH           82.86               35            0.67              0.29         62.41                26.11            True
  TTWO           80.65               31            1.40              1.96        199.03                26.67            True
  DDOG           80.00               20            3.24              2.73        119.19                49.88            True
   PEP           80.00               20            0.60              0.66        156.73                18.34            True
  TMUS           80.00               15            1.29              1.81        200.62                22.45            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T12:40:05.887169-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:35:05.882900-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:30:05.890457-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:25:05.881954-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:00:03.424842-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:55:05.886057-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:40:05.882469-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
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

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 12:15:05 EDT`
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
   HON          100.00               22            0.70              1.12        228.97                20.57            True
  NFLX           95.00               40            0.50              0.35         98.51                27.07            True
  AVGO           90.00               40            0.53              1.17        314.05                41.04            True
  FAST           89.29               28            0.91              0.29         46.17                21.85            True
  CDNS           88.89               45            0.52              1.02        278.28                25.28            True
  ASML           87.10               31            1.09             10.07       1312.92                51.28            True
   LIN           85.71               14            0.98              3.45        501.12                19.40            True
  TSLA           85.00               20            2.24              5.65        358.17                42.35            True
  VRSK           83.72               43            0.54              0.70        184.78                33.36            True
  TMUS           83.33               18            1.13              1.59        200.72                22.45            True
  CTSH           82.35               34            0.72              0.31         62.41                26.11            True
   PEP           80.00               20            0.57              0.63        156.74                18.34            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:00:03.424842-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:55:05.886057-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:40:05.882469-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:25:05.885117-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:10:05.890334-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
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

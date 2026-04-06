# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 12:10:05 EDT`
Last processed slot: `manage_1200`

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
   HON          100.00               20            0.76              1.22        228.93                20.57            True
  NFLX           95.00               40            0.55              0.38         98.50                27.07            True
  AVGO           89.74               39            0.59              1.31        313.99                41.04            True
  CDNS           88.89               45            0.58              1.13        278.24                25.28            True
  FAST           88.46               26            1.00              0.33         46.16                21.85            True
  ASML           86.67               30            1.20             11.04       1312.50                51.28            True
   LIN           85.71               14            0.98              3.44        501.12                19.40            True
  TSLA           85.00               20            2.15              5.42        358.27                42.35            True
  TMUS           83.33               18            1.13              1.60        200.71                22.45            True
  VRSK           82.93               41            0.57              0.74        184.76                33.36            True
  CTSH           81.25               32            0.82              0.36         62.39                26.11            True
   PEP           80.00               20            0.63              0.69        156.71                18.34            True
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

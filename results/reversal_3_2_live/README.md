# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 12:30:05 EDT`
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
   HON          100.00               20            0.73              1.18        228.95                20.57            True
  FAST           90.62               32            0.73              0.24         46.20                21.85            True
  AVGO           89.74               39            0.66              1.45        313.93                41.04            True
  ASML           86.67               30            1.23             11.37       1312.36                51.28            True
   LIN           85.71               14            1.02              3.59        501.06                19.40            True
  TSLA           85.00               20            2.39              6.03        358.01                42.35            True
  TMUS           83.33               18            1.16              1.63        200.70                22.45            True
  CTSH           82.35               34            0.70              0.31         62.41                26.11            True
  CRWD           81.40               43            0.67              1.88        398.31                42.36            True
   PEP           80.00               20            0.59              0.64        156.73                18.34            True
  FANG          100.00               29            0.20              0.28        193.76                28.70           False
  NFLX           95.35               43            0.35              0.25         98.55                27.07           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T12:30:05.890457-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:25:05.881954-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:00:03.424842-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:55:05.886057-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:40:05.882469-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:25:05.885117-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
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

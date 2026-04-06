# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 13:20:05 EDT`
Last processed slot: `manage_1330`

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
   HON          100.00               12            1.28              2.06        228.57                20.57            True
 CMCSA           93.75               16            0.52              0.10         27.89                25.15            True
  NVDA           91.67               36            0.53              0.66        177.11                36.70            True
  FAST           90.00               30            0.86              0.28         46.18                21.85            True
  AVGO           89.19               37            0.98              2.16        313.63                41.04            True
  PLTR           87.18               39            0.96              1.00        148.03                50.29            True
  ASML           86.67               30            1.23             11.35       1312.37                51.28            True
  SHOP           86.36               44            0.62              0.51        118.03                46.39            True
   LIN           85.71               14            0.97              3.43        501.13                19.40            True
   PEP           84.21               19            0.68              0.75        156.69                18.34            True
  CRWD           81.40               43            0.57              1.60        398.43                42.36            True
  CTSH           81.25               32            0.83              0.36         62.38                26.11            True
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

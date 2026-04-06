# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 14:45:05 EDT`
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
   HON          100.00               19            0.85              1.36        228.87                20.57            True
   XEL           95.24               21            0.55              0.31         80.61                19.13            True
 CMCSA           90.00               10            0.88              0.17         27.86                25.15            True
  FAST           88.46               26            1.00              0.33         46.16                21.85            True
  ASML           87.10               31            1.09             10.09       1312.90                51.28            True
   LIN           85.71               14            1.00              3.51        501.09                19.40            True
  VRTX           85.37               41            0.59              1.81        437.93                40.20            True
  DDOG           85.19               27            2.50              2.11        119.46                49.88            True
  CTAS           85.19               27            0.89              1.09        173.87                28.60            True
  TSLA           84.21               19            2.58              6.52        357.80                42.35            True
   EXC           84.21               19            0.64              0.22         49.24                21.30            True
  TMUS           83.33               12            1.62              2.29        200.42                22.45            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T14:40:05.884687-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-06T14:35:05.889475-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-06T14:30:05.890964-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-06T14:25:05.885384-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-06T14:10:05.888996-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T14:05:05.887839-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T14:00:05.883215-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T13:55:05.882620-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T13:40:05.882912-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:35:05.888620-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
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

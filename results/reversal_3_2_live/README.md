# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 14:20:03 EDT`
Last processed slot: `manage_1430`

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
   HON          100.00               19            0.92              1.48        228.82                20.57            True
  TSLA          100.00               14            3.33              8.41        356.99                42.35            True
 CMCSA           93.33               15            0.65              0.13         27.88                25.15            True
  FAST           88.00               25            1.07              0.35         46.15                21.85            True
  ASML           87.10               31            1.11             10.20       1312.86                51.28            True
   LIN           86.67               15            0.91              3.19        501.23                19.40            True
  CTAS           86.21               29            0.77              0.94        173.94                28.60            True
  DDOG           85.19               27            2.45              2.06        119.48                49.88            True
  VRTX           84.62               39            0.73              2.25        437.75                40.20            True
   PEP           82.35               17            0.82              0.90        156.63                18.34            True
  TMUS           81.25               16            1.26              1.78        200.64                22.45            True
  TTWO           80.56               36            1.23              1.72        199.13                26.67            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T14:10:05.888996-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T14:05:05.887839-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T14:00:05.883215-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T13:55:05.882620-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-06T13:40:05.882912-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:35:05.888620-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:30:05.885486-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:25:05.887688-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:10:05.894755-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:05:05.883688-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
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

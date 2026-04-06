# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 13:45:05 EDT`
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
   HON          100.00               15            1.15              1.85        228.66                20.57            True
  TSLA          100.00               13            3.36              8.47        356.96                42.35            True
 CMCSA           93.33               15            0.66              0.13         27.87                25.15            True
   XEL           91.67               24            0.51              0.29         80.62                19.13            True
  AVGO           89.74               39            0.70              1.55        313.89                41.04            True
  FAST           88.46               26            1.04              0.34         46.16                21.85            True
  PLTR           87.50               40            0.65              0.68        148.17                50.29            True
  CTAS           87.50               32            0.58              0.71        174.04                28.60            True
  ASML           87.10               31            1.00              9.26       1313.26                51.28            True
   LIN           86.67               15            0.89              3.13        501.26                19.40            True
   EXC           85.00               20            0.54              0.19         49.25                21.30            True
  CTSH           83.78               37            0.56              0.25         62.43                26.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T13:40:05.882912-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:35:05.888620-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:30:05.885486-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:25:05.887688-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-06T13:10:05.894755-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:05:05.883688-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T13:00:05.887824-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:55:05.885407-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-06T12:40:05.887169-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:35:05.882900-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
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

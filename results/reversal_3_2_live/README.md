# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 12:35:05 EDT`
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
   HON          100.00               22            0.67              1.08        228.99                20.57            True
  FAST           90.91               33            0.69              0.22         46.20                21.85            True
  AVGO           89.74               39            0.70              1.54        313.89                41.04            True
  ASML           87.10               31            1.17             10.75       1312.62                51.28            True
   LIN           86.67               15            0.96              3.37        501.15                19.40            True
  TSLA           85.00               20            2.41              6.07        357.99                42.35            True
  TMUS           83.33               18            1.14              1.61        200.71                22.45            True
  CTSH           82.86               35            0.66              0.29         62.42                26.11            True
  TTWO           81.82               33            1.38              1.93        199.04                26.67            True
  CRWD           81.40               43            0.58              1.61        398.43                42.36            True
   PEP           80.00               20            0.61              0.67        156.72                18.34            True
  FANG          100.00               29            0.32              0.43        193.69                28.70           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T12:35:05.882900-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:30:05.890457-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:25:05.881954-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-06T12:10:05.895326-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:05:05.877929-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T12:00:03.424842-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:55:05.886057-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-06T11:40:05.882469-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
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

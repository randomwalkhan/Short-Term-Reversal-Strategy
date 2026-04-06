# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:40:05 EDT`
Last processed slot: `manage_1130`

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
   HON          100.00               22            0.65              1.04        229.01                20.57            True
  FTNT           93.48               46            0.53              0.31         82.40                30.26            True
  FAST           91.67               36            0.57              0.19         46.22                21.85            True
  CDNS           90.70               43            0.79              1.54        278.06                25.28            True
  SNPS           89.13               46            0.55              1.52        395.30                35.67            True
  TMUS           85.71               21            1.06              1.49        200.76                22.45            True
  ASML           85.19               27            1.39             12.83       1311.73                51.28            True
  TSLA           85.00               20            2.17              5.48        358.24                42.35            True
   LIN           85.00               20            0.73              2.58        501.49                19.40            True
   PEP           82.35               17            0.80              0.88        156.63                18.34            True
  CTSH           81.82               33            0.80              0.35         62.39                26.11            True
  FANG          100.00               29            0.36              0.48        193.67                28.70           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-06T11:40:05.882469-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:35:05.887081-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:30:05.877701-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:25:05.885117-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-06T11:10:05.890334-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T11:00:03.415712-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:55:05.885281-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
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

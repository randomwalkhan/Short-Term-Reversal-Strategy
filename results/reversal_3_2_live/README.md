# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:20:05 EDT`
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
   HON          100.00               22            0.63              1.01        229.02                20.57            True
  FTNT           93.02               43            0.67              0.39         82.36                30.26            True
  FAST           91.89               37            0.55              0.18         46.22                21.85            True
  CDNS           90.70               43            0.67              1.32        278.16                25.28            True
  AVGO           89.74               39            0.90              1.97        313.70                41.04            True
  ASML           85.19               27            1.42             13.07       1311.63                51.28            True
  TSLA           85.00               20            1.95              4.92        358.48                42.35            True
  TMUS           84.00               25            0.94              1.33        200.83                22.45            True
  CTSH           83.87               31            0.91              0.40         62.37                26.11            True
   PEP           83.33               18            0.75              0.83        156.65                18.34            True
  FANG          100.00               28            0.45              0.62        193.62                28.70           False
   XEL           93.75               32            0.02              0.01         80.74                19.13           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                 detail
2026-04-06T11:10:05.890334-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T11:00:03.415712-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:55:05.885281-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:30:05.886948-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:25:05.896716-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:20:05.891442-04:00 manage_1030         exit {"contract_symbol": "WDC260501C00295000", "pnl": 595.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.7, "ticker": "WDC"}
2026-04-06T10:10:05.890008-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
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

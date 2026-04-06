# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 10:50:05 EDT`
Last processed slot: `manage_1100`

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
   HON          100.00               21            0.71              1.14        228.96                20.57            True
  FTNT           93.02               43            0.65              0.38         82.37                30.26            True
  NVDA           91.67               36            0.63              0.78        177.06                36.70            True
  AVGO           91.18               34            1.08              2.38        313.53                41.04            True
  FAST           91.18               34            0.65              0.21         46.21                21.85            True
  CDNS           90.24               41            1.01              1.97        277.88                25.28            True
  CTSH           83.87               31            0.91              0.40         62.37                26.11            True
  TSLA           82.86               35            1.03              2.60        359.47                42.35            True
  ASML           80.95               21            1.83             16.91       1309.98                51.28            True
  MELI           80.00               35            1.18             14.14       1709.46                39.93            True
  NFLX           95.83               48            0.02              0.01         98.65                27.07           False
  COST           91.11               45            0.27              1.92       1014.14                14.21           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                 detail
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:30:05.886948-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:25:05.896716-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:20:05.891442-04:00 manage_1030         exit {"contract_symbol": "WDC260501C00295000", "pnl": 595.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.7, "ticker": "WDC"}
2026-04-06T10:10:05.890008-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:05:05.886743-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:00:06.219713-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T09:55:02.509102-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T09:40:00.944679-04:00 manage_0930 slot_skipped                                                                                                        {"reason": "already_processed"}
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

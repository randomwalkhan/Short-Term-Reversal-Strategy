# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 10:20:05 EDT`
Last processed slot: `manage_1030`

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
   HON          100.00               24            0.51              0.82        229.10                20.57            True
  AVGO           89.74               39            0.83              1.83        313.77                41.04            True
  ASML           84.00               25            1.51             13.96       1311.25                51.28            True
  CTSH           83.78               37            0.59              0.26         62.43                26.11            True
  CRWD           81.40               43            0.56              1.55        398.45                42.36            True
  DDOG           80.95               21            3.03              2.55        119.27                49.88            True
  TTWO           80.77               26            1.69              2.37        198.85                26.67            True
  PANW           80.00               40            0.88              1.01        162.78                41.77            True
  FANG          100.00               32            0.03              0.03        193.87                28.70           False
  FTNT           94.23               52            0.02              0.01         82.52                30.26           False
  FAST           93.02               43            0.26              0.08         46.26                21.85           False
  NVDA           92.50               40            0.24              0.29        177.26                36.70           False
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                                                                                                                 detail
2026-04-06T10:20:05.891442-04:00 manage_1030          exit {"contract_symbol": "WDC260501C00295000", "pnl": 595.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.7, "ticker": "WDC"}
2026-04-06T10:10:05.890008-04:00 manage_1000  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:05:05.886743-04:00 manage_1000  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:00:06.219713-04:00 manage_1000  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T09:55:02.509102-04:00 manage_1000  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T09:40:00.944679-04:00 manage_0930  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T09:35:05.895013-04:00 manage_0930  slot_skipped                                                                                                        {"reason": "already_processed"}
       2026-04-03T16:00:00-04:00 manage_1600 market_closed                                                                              {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                                                                                                        {"reason": "already_processed"}
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

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:05:06 EDT`
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
   HON          100.00               24            0.57              0.92        229.06                20.57            True
  CDNS           90.91               44            0.61              1.18        278.21                25.28            True
  AVGO           89.74               39            0.92              2.02        313.68                41.04            True
  TSLA           84.62               26            1.57              3.96        358.89                42.35            True
  TMUS           84.00               25            0.91              1.29        200.85                22.45            True
  ASML           82.61               23            1.65             15.24       1310.70                51.28            True
  MELI           82.05               39            0.91             10.89       1710.85                39.93            True
  CTSH           81.82               33            0.80              0.35         62.39                26.11            True
  FANG          100.00               29            0.27              0.37        193.72                28.70           False
  FTNT           93.48               46            0.47              0.27         82.41                30.26           False
  FAST           93.18               44            0.21              0.07         46.27                21.85           False
  NVDA           92.50               40            0.34              0.42        177.21                36.70           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                 detail
2026-04-06T11:05:06.304097-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T11:00:03.415712-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:55:05.885281-04:00 manage_1100 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:40:05.887120-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:35:05.885229-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:30:05.886948-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:25:05.896716-04:00 manage_1030 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:20:05.891442-04:00 manage_1030         exit {"contract_symbol": "WDC260501C00295000", "pnl": 595.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.7, "ticker": "WDC"}
2026-04-06T10:10:05.890008-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
2026-04-06T10:05:05.886743-04:00 manage_1000 slot_skipped                                                                                                        {"reason": "already_processed"}
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

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 11:15:05 EDT`
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
   HON          100.00               23            0.59              0.94        229.05                20.57            True
  FTNT           93.48               46            0.51              0.30         82.40                30.26            True
  FAST           91.89               37            0.53              0.17         46.23                21.85            True
  CDNS           90.91               44            0.60              1.18        278.22                25.28            True
  AVGO           89.74               39            0.89              1.96        313.71                41.04            True
  ASML           85.19               27            1.46             13.49       1311.45                51.28            True
   PEP           84.21               19            0.70              0.77        156.68                18.34            True
  TSLA           84.00               25            1.60              4.04        358.86                42.35            True
  TMUS           84.00               25            0.93              1.31        200.84                22.45            True
  CTSH           81.82               33            0.80              0.35         62.39                26.11            True
  FANG          100.00               28            0.49              0.67        193.59                28.70           False
  NFLX           95.83               48            0.05              0.03         98.65                27.07           False
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

# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-03 16:00:00 UTC-04:00`
Last processed slot: `manage_1600`

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

- Cash: `$8,102.50`
- Equity: `$10,827.50`
- Realized PnL: `$845.00`
- Unrealized PnL: `$-17.50`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   0               27.42                 27.25      294.77         294.2           -17.5                  -0.64         97.22               36              0.99         81.84           82.37                  91.06
```

## Today's Closed Trades (2026-04-03)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot    event_type                                                    detail
       2026-04-03T16:00:00-04:00 manage_1600 market_closed {"holiday_name": "Good Friday", "reason": "nyse_holiday"}
2026-04-02T16:00:05.925792-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:35:05.886679-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:30:05.889337-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:25:05.929228-04:00 manage_1530  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:10:05.887758-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
2026-04-02T15:00:05.892985-04:00  entry_1500  slot_skipped                           {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_1_live_equity_1d.png)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_1_live_equity_1m.png)

</details>

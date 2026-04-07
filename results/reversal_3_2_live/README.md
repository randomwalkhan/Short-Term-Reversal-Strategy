# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 14:15:05 EDT`
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

- Cash: `$10,320.00`
- Equity: `$10,320.00`
- Realized PnL: `$320.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-07)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price     pnl  return_pct           exit_reason
   HON HON260515C00230000          2026-04-06         2026-04-07                 7.4                5.8 -1120.0  -21.621622 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  MRVL           97.22               36            1.02              0.78        109.17                70.84            True
  NVDA           93.10               29            1.00              1.24        177.11                33.70            True
  UPRO           90.62               32            1.16              0.82        100.39                53.86            True
   LIN           90.00               10            1.44              5.03        497.32                19.02            True
  COST           90.00               10            1.20              8.58       1014.87                13.04            True
  ORLY           89.74               39            0.63              0.41         91.95                23.11            True
  PCAR           88.89               36            0.75              0.62        118.05                21.97            True
  ASML           88.57               35            0.70              6.42       1301.26                47.16            True
   KDP           88.24               17            0.70              0.13         25.65                20.32            True
  CTAS           87.88               33            0.59              0.71        171.39                28.73            True
  VRTX           87.80               41            0.56              1.71        433.57                40.01            True
  FAST           86.96               23            1.12              0.36         45.72                20.98            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T14:10:00.879771-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:05:03.892395-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:00:04.896209-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:55:00.552170-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:40:00.942700-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:35:03.883059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:30:05.887210-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:25:05.882654-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:10:04.926634-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T13:05:02.889424-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407141505)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407141505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407141505)

</details>

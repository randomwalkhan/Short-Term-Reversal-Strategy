# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 14:40:00 EDT`
Last processed slot: `manage_1430`

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
  REGN           97.14               35            0.71              3.81        761.41                25.24            True
  MRVL           96.67               30            1.46              1.12        109.03                70.84            True
  UPRO           92.59               27            1.59              1.12        100.26                53.86            True
  NVDA           92.59               27            1.18              1.47        177.01                33.70            True
  CDNS           91.11               45            0.66              1.29        278.84                25.26            True
  COST           90.91               11            1.16              8.25       1015.02                13.04            True
   LIN           90.00               10            1.36              4.74        497.44                19.02            True
  SNPS           88.89               45            0.61              1.71        396.34                35.70            True
  PCAR           88.24               34            0.84              0.69        118.02                21.97            True
  TSLA           88.24               17            3.25              8.04        349.38                42.33            True
   KDP           88.24               17            0.70              0.13         25.65                20.32            True
  VRTX           87.80               41            0.59              1.78        433.54                40.01            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T14:40:00.896832-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:35:00.890525-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:30:00.927122-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:25:01.881173-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:10:00.879771-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:05:03.892395-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:00:04.896209-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:55:00.552170-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:40:00.942700-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:35:03.883059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407144000)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407144000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407144000)

</details>

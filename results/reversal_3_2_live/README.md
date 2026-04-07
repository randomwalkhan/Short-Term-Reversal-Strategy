# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 14:35:00 EDT`
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
  REGN           97.37               38            0.54              2.88        761.80                25.24            True
  MRVL           97.06               34            1.21              0.93        109.11                70.84            True
  NVDA           92.59               27            1.08              1.34        177.07                33.70            True
  COST           91.67               12            1.13              8.09       1015.08                13.04            True
  UPRO           90.32               31            1.31              0.92        100.34                53.86            True
   LIN           90.00               10            1.39              4.85        497.39                19.02            True
   KDP           89.47               19            0.56              0.10         25.66                20.32            True
  SNPS           88.89               45            0.55              1.54        396.41                35.70            True
  ASML           88.57               35            0.71              6.51       1301.22                47.16            True
  ORLY           88.57               35            0.69              0.45         91.94                23.11            True
   CSX           88.46               26            0.58              0.17         41.41                24.91            True
  PCAR           88.24               34            0.81              0.67        118.03                21.97            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T14:35:00.890525-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:30:00.927122-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:25:01.881173-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-07T14:10:00.879771-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:05:03.892395-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T14:00:04.896209-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:55:00.552170-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:40:00.942700-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:35:03.883059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:30:05.887210-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407143500)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407143500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407143500)

</details>

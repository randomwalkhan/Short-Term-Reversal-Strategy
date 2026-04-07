# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 13:00:02 EDT`
Last processed slot: `manage_1300`

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
  REGN           96.77               31            1.10              5.89        760.51                25.24            True
  COST           95.24               21            0.87              6.18       1015.90                13.04            True
  NVDA           92.59               27            1.20              1.49        177.00                33.70            True
  UPRO           90.32               31            1.27              0.90        100.36                53.86            True
   LIN           90.00               10            1.49              5.22        497.23                19.02            True
  PCAR           89.47               38            0.63              0.52        118.10                21.97            True
  ABNB           89.29               28            1.53              1.36        126.23                36.80            True
  ASML           88.89               36            0.60              5.46       1301.67                47.16            True
  ORLY           88.57               35            0.69              0.45         91.94                23.11            True
  FAST           87.50               24            1.09              0.35         45.72                20.98            True
  MCHP           87.18               39            0.60              0.28         67.10                42.27            True
  KLAC           87.18               39            0.53              5.73       1537.61                45.70            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T13:00:02.895617-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:55:00.916656-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:40:05.895143-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:35:03.878614-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:30:00.912059-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:25:00.895869-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:10:05.880109-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-07T12:05:00.898216-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-07T12:00:02.896423-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-07T11:55:05.888145-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407130002)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407130002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407130002)

</details>

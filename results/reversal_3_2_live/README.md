# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 12:55:00 EDT`
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
  REGN           96.77               31            1.00              5.36        760.74                25.24            True
  NVDA           92.86               28            1.03              1.28        177.09                33.70            True
  COST           92.59               27            0.76              5.44       1016.22                13.04            True
  UPRO           90.62               32            1.24              0.88        100.36                53.86            True
  PCAR           90.24               41            0.53              0.44        118.13                21.97            True
   LIN           90.00               10            1.40              4.91        497.37                19.02            True
  ORLY           89.74               39            0.60              0.38         91.97                23.11            True
  ABNB           89.29               28            1.51              1.34        126.23                36.80            True
  FAST           87.50               24            1.09              0.35         45.72                20.98            True
  MCHP           87.18               39            0.58              0.27         67.10                42.27            True
  VRTX           86.67               30            1.25              3.80        432.67                40.01            True
  MDLZ           86.67               15            0.72              0.29         58.25                25.49            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                              detail
2026-04-07T12:55:00.916656-04:00 manage_1300 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:40:05.895143-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:35:03.878614-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:30:00.912059-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:25:00.895869-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:10:05.880109-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:05:00.898216-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:00:02.896423-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:55:05.888145-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:50:05.887768-04:00 manage_1200         exit {"contract_symbol": "HON260515C00230000", "pnl": -1120.0, "reason": "stop_loss_hit_at_scan", "return_pct": -21.62, "ticker": "HON"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407125500)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407125500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407125500)

</details>

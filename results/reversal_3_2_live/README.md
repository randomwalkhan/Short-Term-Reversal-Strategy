# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 12:45:02 EDT`
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
  REGN           96.77               31            1.06              5.64        760.62                25.24            True
  COST           96.00               25            0.81              5.81       1016.06                13.04            True
  NVDA           92.59               27            1.09              1.35        177.06                33.70            True
  UPRO           90.62               32            1.16              0.82        100.39                53.86            True
  PCAR           90.24               41            0.54              0.45        118.13                21.97            True
  ORLY           89.74               39            0.64              0.41         91.95                23.11            True
  ABNB           89.66               29            1.42              1.26        126.27                36.80            True
  VRTX           87.88               33            1.08              3.29        432.89                40.01            True
  MCHP           87.18               39            0.62              0.29         67.09                42.27            True
  FAST           86.96               23            1.16              0.37         45.71                20.98            True
  MDLZ           86.67               15            0.77              0.31         58.25                25.49            True
  CTAS           85.71               28            0.98              1.18        171.19                28.73            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                              detail
2026-04-07T12:40:05.895143-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:35:03.878614-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:30:00.912059-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:25:00.895869-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:10:05.880109-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:05:00.898216-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:00:02.896423-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:55:05.888145-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:50:05.887768-04:00 manage_1200         exit {"contract_symbol": "HON260515C00230000", "pnl": -1120.0, "reason": "stop_loss_hit_at_scan", "return_pct": -21.62, "ticker": "HON"}
2026-04-07T11:40:05.887766-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407124502)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407124502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407124502)

</details>

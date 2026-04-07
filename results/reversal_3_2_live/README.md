# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 12:30:00 EDT`
Last processed slot: `manage_1230`

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
  MRVL           97.22               36            0.98              0.75        109.19                70.84            True
  REGN           96.00               25            1.24              6.60        760.21                25.24            True
  COST           93.33               30            0.70              4.99       1016.41                13.04            True
  NVDA           92.31               26            1.24              1.54        176.98                33.70            True
  GILD           92.31               13            1.35              1.33        139.56                20.18            True
  CDNS           91.11               45            0.64              1.25        278.85                25.26            True
  ABNB           90.32               31            1.35              1.20        126.30                36.80            True
  ORLY           90.00               40            0.59              0.38         91.97                23.11            True
  UPRO           90.00               30            1.38              0.98        100.32                53.86            True
  PCAR           89.47               38            0.62              0.51        118.10                21.97            True
   KDP           89.47               19            0.56              0.10         25.66                20.32            True
  ASML           88.89               36            0.62              5.68       1301.57                47.16            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                              detail
2026-04-07T12:30:00.912059-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:25:00.895869-04:00 manage_1230 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:10:05.880109-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:05:00.898216-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:00:02.896423-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:55:05.888145-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:50:05.887768-04:00 manage_1200         exit {"contract_symbol": "HON260515C00230000", "pnl": -1120.0, "reason": "stop_loss_hit_at_scan", "return_pct": -21.62, "ticker": "HON"}
2026-04-07T11:40:05.887766-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:35:05.890463-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:30:02.894028-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407123000)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407123000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407123000)

</details>

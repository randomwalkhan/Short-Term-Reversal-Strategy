# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 12:15:04 EDT`
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
  TSLA          100.00               13            3.52              8.68        349.10                42.33            True
  MRVL           96.97               33            1.33              1.02        109.07                70.84            True
  REGN           95.65               23            1.33              7.09        760.00                25.24            True
  UPRO           92.59               27            1.61              1.13        100.25                53.86            True
  NVDA           92.00               25            1.32              1.64        176.94                33.70            True
  CDNS           90.91               44            0.83              1.62        278.70                25.26            True
  ABNB           90.32               31            1.29              1.15        126.32                36.80            True
  COST           90.32               31            0.65              4.62       1016.57                13.04            True
  ORLY           89.74               39            0.64              0.41         91.95                23.11            True
   KDP           89.47               19            0.55              0.10         25.66                20.32            True
  PCAR           89.19               37            0.73              0.60        118.06                21.97            True
  ASML           88.89               36            0.66              6.06       1301.41                47.16            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                              detail
2026-04-07T12:10:05.880109-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:05:00.898216-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T12:00:02.896423-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:55:05.888145-04:00 manage_1200 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:50:05.887768-04:00 manage_1200         exit {"contract_symbol": "HON260515C00230000", "pnl": -1120.0, "reason": "stop_loss_hit_at_scan", "return_pct": -21.62, "ticker": "HON"}
2026-04-07T11:40:05.887766-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:35:05.890463-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:30:02.894028-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:25:05.887847-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407121504)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407121504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407121504)

</details>

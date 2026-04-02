# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 14:40:05 EDT`
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

- Cash: `$10,845.00`
- Equity: `$10,845.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.30               37            0.85              1.77        296.97                91.06            True
  ASML           92.86               14            2.84             26.99       1348.19                52.01            True
  ABNB           92.50               40            0.67              0.59        124.94                36.75            True
   MAR           90.00               30            0.91              2.13        332.55                28.45            True
  DXCM           89.74               39            1.21              0.53         62.14                31.67            True
  ORLY           89.74               39            0.61              0.39         91.93                22.81            True
  SNPS           89.13               46            0.54              1.51        396.09                35.88            True
  KLAC           87.50               32            1.08             11.45       1514.93                56.48            True
  FAST           86.96               23            1.32              0.43         46.45                21.97            True
  GILD           86.96               23            0.94              0.92        139.91                21.47            True
  MCHP           86.49               37            0.70              0.32         65.24                45.66            True
  CDNS           86.21               29            1.75              3.42        278.72                26.25            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T14:40:05.911687-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-02T14:35:05.892322-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-02T14:30:05.929668-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-02T14:25:06.347985-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-02T14:10:05.893357-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T14:05:05.889867-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T14:00:05.896681-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T13:55:05.905247-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-02T13:40:05.899103-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:35:05.898186-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %. GitHub does not support true app-style toggles, so the dashboard uses collapsible `1D / 1W / 1M` sections instead.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.1 Live Equity 1D](../../assets/reversal_3_1_live_equity_1d.png)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.1 Live Equity 1M](../../assets/reversal_3_1_live_equity_1m.png)

</details>

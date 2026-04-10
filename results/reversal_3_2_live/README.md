# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 11:10:06 EDT`
Last processed slot: `manage_1100`

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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$8,625.00`
- Equity: `$12,695.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-330.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4070.0                44.0                  40.7      764.07        752.64          -330.0                   -7.5         100.0               21              1.48         48.92           53.01                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               15            1.98             10.65        763.29                26.14            True
  SBUX           94.44               36            0.55              0.37         96.76                40.73            True
  ROST           90.91               22            1.00              1.58        224.23                24.66            True
   WMT           90.91               11            1.61              1.46        128.50                24.68            True
  ABNB           90.32               31            1.29              1.16        128.66                41.65            True
  CDNS           90.00               10            3.49              6.86        278.07                29.62            True
  SNPS           88.89               18            2.68              7.60        401.59                36.22            True
   EXC           88.89               18            0.73              0.25         49.33                21.05            True
 CMCSA           88.89               18            0.57              0.11         28.26                24.06            True
  SHOP           88.64               44            0.54              0.42        112.13                49.23            True
  VRTX           88.46               26            1.32              4.12        444.98                28.30            True
  CHTR           87.88               33            1.07              1.67        222.51                29.22            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T11:10:06.432650-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:05:06.437501-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:00:06.440938-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:55:06.444820-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:30:06.417352-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410111006)

</details>

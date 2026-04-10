# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 10:45:05 EDT`
Last processed slot: `manual`

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
- Equity: `$12,685.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-340.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4060.0                44.0                  40.6      764.07        759.43          -340.0                  -7.73         100.0               21              1.48         48.92           48.98                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            1.12              6.00        765.28                26.14            True
   HON          100.00               25            0.56              0.92        235.67                23.67            True
  SNPS           90.48               21            2.42              6.86        401.91                36.22            True
  CDNS           90.00               10            3.64              7.16        277.94                29.62            True
  ROST           90.00               10            1.46              2.30        223.92                24.66            True
  VRTX           89.19               37            0.78              2.44        445.70                28.30            True
  CHTR           89.19               37            0.67              1.05        222.78                29.22            True
  BKNG           88.89               36            1.00              1.23        176.07                36.59            True
  DXCM           87.50               32            1.56              0.72         65.37                32.42            True
  INSM           87.10               31            1.54              1.73        158.85                51.90            True
  TTWO           86.49               37            0.98              1.36        197.47                26.78            True
  GILD           86.36               22            1.01              1.00        141.66                20.31            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:30:06.417352-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:00:05.430800-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:55:06.164206-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:40:06.426501-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:35:06.431602-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410104505)

</details>

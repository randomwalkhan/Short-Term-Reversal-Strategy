# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 12:15:00 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,636.99`
- Equity: `$13,371.74`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$13.82`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6734.75       746.77         748.31      746.77        748.31           13.82                   0.21         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   XEL           95.65               23            0.58              0.33         80.91                23.12            True
  FTNT           94.44               36            1.13              0.65         82.12                40.09            True
   LIN           92.31               13            1.38              4.81        497.16                18.78            True
   AEP           91.67               12            0.95              0.89        134.18                17.62            True
   TRI           82.22               45            0.95              0.62         92.80                39.83            True
  ADBE           81.82               33            1.40              2.44        247.11                38.98            True
  FANG          100.00                1            7.06              9.23        182.70                29.20           False
   ROP           91.11               45            0.18              0.45        361.69                23.28           False
  GILD           90.91               33            0.43              0.41        138.37                20.76           False
   PEP           87.88               33            0.13              0.15        158.32                20.28           False
  ALNY           85.71                7            3.26              7.31        317.00                45.49           False
  PAYX           85.37               41            0.39              0.25         92.02                31.23           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T12:10:05.868513-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:05:05.700509-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:00:02.894843-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:55:05.578809-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:40:00.700868-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:35:02.708343-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:30:05.729176-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:25:05.895658-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:10:00.820702-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-17T11:05:05.725954-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417121500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417121500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417121500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417121500)

</details>

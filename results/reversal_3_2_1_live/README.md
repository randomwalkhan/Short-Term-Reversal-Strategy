# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 12:25:05 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,636.99`
- Equity: `$13,366.24`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$8.32`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6729.26       746.77          747.7      746.77         747.7            8.32                   0.12         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   XEL           96.00               25            0.52              0.29         80.92                23.12            True
  FTNT           94.59               37            1.00              0.57         82.15                40.09            True
   AEP           94.44               18            0.80              0.75        134.24                17.62            True
   LIN           90.00               10            1.53              5.35        496.93                18.78            True
  ADBE           84.62               39            0.89              1.54        247.49                38.98            True
   TRI           82.61               46            0.55              0.36         92.92                39.83            True
   ADP           80.65               31            0.63              0.89        200.01                27.95            True
   BKR           80.00               25            1.09              0.46         60.40                34.01            True
  FANG          100.00                1            6.81              8.90        182.84                29.20           False
  GILD           91.67               36            0.25              0.24        138.45                20.76           False
   ROP           90.48               42            0.26              0.67        361.59                23.28           False
   PEP           87.88               33            0.18              0.20        158.29                20.28           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T12:25:05.728577-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:10:05.868513-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:05:05.700509-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:00:02.894843-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:55:05.578809-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:40:00.700868-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:35:02.708343-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:30:05.729176-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:25:05.895658-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:10:00.820702-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417122505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417122505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417122505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417122505)

</details>

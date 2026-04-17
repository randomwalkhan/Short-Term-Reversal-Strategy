# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 13:45:01 EDT`
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
- Equity: `$13,389.51`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$31.59`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6752.52       746.77         750.28      746.77        750.28           31.59                   0.47         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   AEP           95.24               21            0.61              0.57        134.32                17.62            True
  FTNT           93.94               33            1.33              0.77         82.07                40.09            True
  GILD           88.46               26            0.64              0.62        138.29                20.76            True
   ROP           88.24               34            0.57              1.46        361.26                23.28            True
   LIN           87.50               24            0.63              2.21        498.27                18.78            True
   PEP           86.36               22            0.87              0.96        157.97                20.28            True
  PAYX           85.00               40            0.53              0.34         91.98                31.23            True
   BKR           84.38               32            0.81              0.34         60.45                34.01            True
   TRI           83.33               42            1.07              0.70         92.77                39.83            True
  ADBE           82.86               35            1.17              2.04        247.28                38.98            True
  CSGP           80.95               42            0.82              0.23         39.94                39.11            True
   ADP           80.65               31            0.65              0.92        200.00                27.95            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T13:40:05.864078-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-17T13:35:05.720352-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-17T13:30:05.887852-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-17T13:25:05.730626-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-17T13:10:05.750112-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T13:05:05.919019-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T13:00:01.731689-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T12:55:03.722354-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T12:40:00.714662-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:35:00.699894-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417134501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417134501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417134501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417134501)

</details>

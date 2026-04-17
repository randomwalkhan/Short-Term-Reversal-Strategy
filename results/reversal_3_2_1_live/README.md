# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 14:45:00 EDT`
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
- Equity: `$13,372.50`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$14.58`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6735.51       746.77         748.39      746.77        748.39           14.58                   0.22         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC           94.59               37            0.76              0.36         68.34                74.40            True
  FTNT           93.75               32            1.39              0.80         82.06                40.09            True
   AEP           92.00               25            0.55              0.52        134.34                17.62            True
  GILD           90.00               30            0.56              0.55        138.32                20.76            True
   LIN           90.00               20            0.95              3.32        497.80                18.78            True
   ROP           88.24               34            0.53              1.34        361.30                23.28            True
   PEP           85.71               21            0.89              0.99        157.96                20.28            True
   BKR           84.38               32            0.81              0.34         60.45                34.01            True
  PAYX           83.33               36            0.78              0.50         91.91                31.23            True
   TRI           82.61               46            0.64              0.42         92.89                39.83            True
   CEG           82.35               34            1.15              2.41        298.11                57.36            True
  ADBE           80.65               31            1.57              2.73        246.98                38.98            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T14:40:05.721864-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-17T14:35:05.695089-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-17T14:30:04.813251-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-17T14:25:05.697715-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-17T14:10:00.716098-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-17T14:05:00.716620-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-17T14:00:01.661535-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-17T13:55:05.710439-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-17T13:40:05.864078-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-17T13:35:05.720352-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417144500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417144500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417144500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417144500)

</details>

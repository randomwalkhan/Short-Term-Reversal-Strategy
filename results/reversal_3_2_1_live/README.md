# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 13:15:05 EDT`
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
- Equity: `$13,417.77`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$59.85`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6780.78       746.77         753.42      746.77        753.42           59.85                   0.89         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   AEP           94.74               19            0.74              0.69        134.26                17.62            True
  FTNT           94.59               37            1.04              0.60         82.14                40.09            True
   LIN           88.89               18            1.06              3.70        497.64                18.78            True
   ROP           88.24               34            0.53              1.34        361.30                23.28            True
   TRI           84.62               39            1.24              0.81         92.72                39.83            True
   BKR           83.87               31            0.84              0.36         60.45                34.01            True
  ADBE           83.78               37            1.01              1.75        247.41                38.98            True
   CEG           82.35               34            1.26              2.64        298.01                57.36            True
  TEAM           80.56               36            2.40              1.15         68.24                72.52            True
  WDAY           80.00               40            1.28              1.12        124.39                54.23            True
  FANG          100.00                2            4.88              6.38        183.92                29.20           False
   XEL           93.94               33            0.27              0.15         80.98                23.12           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T13:10:05.750112-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T13:05:05.919019-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T13:00:01.731689-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T12:55:03.722354-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-17T12:40:00.714662-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:35:00.699894-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:30:05.713324-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:25:05.728577-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:10:05.868513-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:05:05.700509-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417131505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417131505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417131505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417131505)

</details>

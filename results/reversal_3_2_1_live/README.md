# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 12:30:05 EDT`
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
- Equity: `$13,368.45`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$10.53`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6731.46       746.77         747.94      746.77        747.94           10.53                   0.16         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           94.74               38            0.89              0.51         82.18                40.09            True
   AEP           93.75               16            0.84              0.79        134.22                17.62            True
   LIN           90.00               10            1.56              5.44        496.89                18.78            True
  ADBE           84.62               39            0.80              1.38        247.56                38.98            True
   BKR           84.38               32            0.83              0.35         60.45                34.01            True
  WDAY           80.00               40            1.17              1.02        124.43                54.23            True
  TEAM           80.00               35            2.66              1.28         68.18                72.52            True
  FANG          100.00                1            6.58              8.60        182.96                29.20           False
   XEL           92.59               27            0.41              0.24         80.95                23.12           False
  GILD           91.18               34            0.38              0.37        138.39                20.76           False
   ROP           91.11               45            0.17              0.44        361.69                23.28           False
   PEP           87.88               33            0.22              0.25        158.27                20.28           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T12:30:05.713324-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:25:05.728577-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-17T12:10:05.868513-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:05:05.700509-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T12:00:02.894843-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:55:05.578809-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-17T11:40:00.700868-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:35:02.708343-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:30:05.729176-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:25:05.895658-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417123005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417123005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417123005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417123005)

</details>

# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 09:35:02 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$6,851.31`
- Equity: `$12,093.93`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-45.66`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   1     23     5288.28                 5242.62       229.93         227.94      229.93        227.94          -45.66                  -0.86         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               30            1.14              6.00        746.84                22.94            True
   HON          100.00               24            0.77              1.24        229.21                21.89            True
  COST           92.00               25            0.91              6.36        995.11                18.83            True
  QCOM           91.43               35            0.64              0.61        137.26                21.00            True
   XEL           91.30               23            0.61              0.34         80.17                19.06            True
  ALNY           90.91               22            2.26              4.91        308.84                46.90            True
  ORLY           90.24               41            0.64              0.41         92.65                22.94            True
  TMUS           87.50               24            1.07              1.48        197.73                22.76            True
   LIN           87.50               24            0.73              2.55        497.06                19.90            True
   KDP           86.96               23            0.75              0.14         26.44                19.93            True
   PEP           86.67               15            1.10              1.21        156.47                19.06            True
  DXCM           86.36               44            0.65              0.29         64.49                35.89            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                         detail
2026-04-21T09:35:02.420022-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T09:30:06.425372-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T09:25:06.429302-04:00  manage_0930 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-21T00:00:06.440855-04:00 data_refresh data_refresh                                                                                                                                                  {'saved': 99}
2026-04-20T16:10:06.425591-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:05:05.426426-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:00:06.436506-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:55:06.432735-04:00  manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:50:06.460350-04:00  manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 748.9, "pnl": 19.17, "reason": "time_exit_at_4pm_scan", "return_pct": 0.29, "ticker": "REGN"}
2026-04-20T15:40:03.007489-04:00  manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421093502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421093502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421093502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421093502)

</details>

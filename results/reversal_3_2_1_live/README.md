# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 10:20:06 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$12,060.12`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-79.47`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   1     23     5288.28                 5208.81       229.93         226.47      229.93        226.47          -79.47                   -1.5         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.94              4.94        747.29                22.94            True
   HON          100.00               11            1.42              2.29        228.76                21.89            True
  NFLX           96.67               30            0.91              0.60         94.57                46.83            True
   XEL           91.67               24            0.57              0.32         80.18                19.06            True
  ALNY           90.32               31            1.53              3.33        309.51                46.90            True
  GILD           90.00               10            1.87              1.77        135.11                18.88            True
  VRTX           89.74               39            0.61              1.87        438.38                26.84            True
  ASML           89.19               37            0.58              6.00       1473.93                54.76            True
  TMUS           86.36               22            1.12              1.55        197.69                22.76            True
   PEP           86.36               22            0.79              0.87        156.62                19.06            True
  DXCM           84.62               39            1.02              0.46         64.42                35.89            True
   APP           84.62               39            0.82              2.83        489.75                75.05            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-21T10:10:06.423835-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-21T10:05:03.425370-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-21T10:00:01.768732-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-21T09:55:02.363892-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-21T09:40:06.428759-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-21T09:35:02.420022-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-21T09:30:06.425372-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-21T09:25:06.429302-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-21T00:00:06.440855-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-20T16:10:06.425591-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421102006)

</details>

# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 09:55:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$539.49`
- Equity: `$13,200.15`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$-157.77`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-16                   2      9     6720.93                 6720.66       746.77         746.74      746.77        746.74           -0.27                  -0.00        100.00               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260529C00068000       2026-04-17                   1      9     6097.50                 5940.00         6.78           6.60       68.04         66.13         -157.50                  -2.58         94.59               37              0.66         72.85            3.13                  74.40                 143.0           74.0               0.04                                       ok
```

## Today's Closed Trades (2026-04-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               35            0.63              3.31        749.15                23.07            True
   WDC           97.37               38            0.77              2.01        371.66                78.62            True
  NFLX           95.65               23            1.24              0.85         96.95                45.70            True
  INTC           95.45               22            3.27              1.57         67.83                74.75            True
   STX           94.29               35            1.74              6.65        544.90                70.39            True
  AVGO           93.94               33            1.09              3.09        405.21                45.93            True
  ALNY           92.11               38            1.07              2.33        308.66                46.89            True
  NVDA           91.67               36            0.77              1.09        201.21                35.90            True
  SBUX           90.91               22            1.16              0.81         99.65                34.23            True
  GILD           87.50               24            0.94              0.90        137.25                20.86            True
  AMAT           86.11               36            0.71              1.98        396.09                56.13            True
 GOOGL           84.62               39            0.52              1.25        341.15                37.74            True
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-04-20T09:55:05.914542-04:00    manage_1000  slot_skipped             {"reason": "already_processed"}
2026-04-20T09:40:05.897388-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-20T09:35:04.897856-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-20T03:00:01.932213-04:00   data_refresh  data_refresh                               {'saved': 99}
2026-04-18T02:55:04.895909-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:50:05.754604-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:45:05.704328-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:40:05.886237-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:35:05.896361-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:30:05.930649-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420095505)

</details>

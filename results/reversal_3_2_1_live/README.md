# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 09:30:02 EDT`
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

- Cash: `$539.49`
- Equity: `$13,200.33`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$-157.59`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-16                   2      9     6720.93                 6720.84       746.77         746.76      746.77        746.76           -0.09                  -0.00        100.00               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260529C00068000       2026-04-17                   1      9     6097.50                 5940.00         6.78           6.60       68.04         67.88         -157.50                  -2.58         94.59               37              0.66         72.85             0.0                  74.40                 143.0           74.0               0.04                                       ok
```

## Today's Closed Trades (2026-04-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  UPRO           92.11               38            0.65              0.57        124.98                56.64            True
  NVDA           91.67               24            1.46              2.06        200.80                35.90            True
  SBUX           91.67               24            1.08              0.76         99.67                34.23            True
  BKNG           89.74               39            0.74              0.99        191.58                38.41            True
   MAR           89.19               37            0.55              1.47        377.30                31.36            True
  DDOG           85.71               35            1.01              0.90        126.23                63.81            True
   EXC           85.71               21            0.72              0.24         46.92                20.08            True
  MDLZ           85.71               21            0.56              0.22         57.15                18.44            True
  INSM           85.37               41            0.80              0.80        144.14                56.82            True
  CTSH           84.62               39            0.67              0.29         61.18                28.79            True
  DASH           82.93               41            0.89              1.14        183.40                50.41            True
  ODFL           82.86               35            0.65              0.99        217.34                29.30            True
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-04-20T03:00:01.932213-04:00   data_refresh  data_refresh                               {'saved': 99}
2026-04-18T02:55:04.895909-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:50:05.754604-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:45:05.704328-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:40:05.886237-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:35:05.896361-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:30:05.930649-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:25:05.591206-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:20:00.526829-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-18T02:15:06.161975-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420093002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420093002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420093002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420093002)

</details>

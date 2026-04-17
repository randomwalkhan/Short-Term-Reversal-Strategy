# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 09:30:03 EDT`
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

- Cash: `$6,636.99`
- Equity: `$13,431.09`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$73.17`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                  6794.1       746.77          754.9      746.77         754.9           73.17                   1.09         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TMUS           86.96               23            0.98              1.35        196.54                22.97            True
  FANG          100.00                1            5.29              6.91        183.69                29.20           False
   EXC          100.00                1            3.12              1.04         47.14                21.57           False
   XEL           93.94               33            0.28              0.16         80.98                23.12           False
   WMT           93.62               47            0.00              0.00        124.82                24.34           False
  COST           91.11               45            0.22              1.55        986.55                18.46           False
   LIN           86.21               29            0.48              1.66        498.51                18.78           False
  AXON           66.67               30            2.26              6.37        399.45                78.78           False
  NFLX             NaN                0            9.29              7.01        104.79                27.33           False
  AAPL             NaN                0            0.00              0.00        267.07                21.13           False
  ABNB             NaN                0            0.00              0.00        140.40                39.01           False
  ADBE             NaN                0            0.00              0.00        253.91                38.98           False
```

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-17T09:30:03.716817-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T09:25:00.715536-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T00:00:06.568918-04:00   data_refresh data_refresh                   {'saved': 99}
2026-04-16T22:07:23.247621-04:00 share_ext_2205 slot_skipped {"reason": "already_processed"}
2026-04-16T21:57:45.188264-04:00 share_ext_2155 slot_skipped {"reason": "already_processed"}
2026-04-16T16:10:06.586169-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T16:05:06.429687-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T16:00:06.436019-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T15:55:05.424408-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T15:40:06.417370-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417093003)

</details>

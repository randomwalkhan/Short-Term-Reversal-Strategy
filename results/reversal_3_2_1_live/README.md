# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 09:35:05 EDT`
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
- Equity: `$13,438.92`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$81.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6801.93       746.77         755.77      746.77        755.77            81.0                   1.21         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WMT           92.31               26            0.81              0.71        124.52                24.34            True
   LIN           87.50               24            0.73              2.55        498.13                18.78            True
  TMUS           86.36               22            1.04              1.43        196.51                22.97            True
  VRSK           80.95               42            0.68              0.85        177.95                37.32            True
  FANG          100.00                1            6.20              8.10        183.18                29.20           False
   EXC          100.00                1            3.03              1.01         47.16                21.57           False
  CHTR           93.48               46            0.21              0.35        235.82                36.79           False
 CMCSA           92.86               28            0.19              0.04         29.33                20.38           False
  MDLZ           92.86               28            0.18              0.07         57.04                18.42           False
  COST           90.48               42            0.41              2.85        985.99                18.46           False
   AEP           88.89                9            1.27              1.20        134.05                17.62           False
   AMD           86.05               43            0.15              0.30        278.13                54.30           False
```

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-17T09:35:05.702550-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T09:30:03.716817-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T09:25:00.715536-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T00:00:06.568918-04:00   data_refresh data_refresh                   {'saved': 99}
2026-04-16T22:07:23.247621-04:00 share_ext_2205 slot_skipped {"reason": "already_processed"}
2026-04-16T21:57:45.188264-04:00 share_ext_2155 slot_skipped {"reason": "already_processed"}
2026-04-16T16:10:06.586169-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T16:05:06.429687-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T16:00:06.436019-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-16T15:55:05.424408-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417093505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417093505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417093505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417093505)

</details>

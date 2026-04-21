# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 10:15:06 EDT`
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

- Cash: `$6,851.31`
- Equity: `$12,075.07`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-64.52`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   1     23     5288.28                 5223.76       229.93         227.12      229.93        227.12          -64.52                  -1.22         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               23            1.33              6.98        746.42                22.94            True
   HON          100.00               20            1.06              1.71        229.01                21.89            True
  NFLX           97.06               34            0.76              0.50         94.61                46.83            True
   XEL           94.44               18            0.80              0.45         80.13                19.06            True
  ASML           89.19               37            0.57              5.90       1473.97                54.76            True
  VRTX           88.89               36            0.88              2.70        438.02                26.84            True
  ALNY           88.89               27            1.72              3.75        309.33                46.90            True
   PEP           87.50               24            0.73              0.81        156.64                19.06            True
  DXCM           85.37               41            0.96              0.43         64.43                35.89            True
  AAPL           85.19               27            1.00              1.92        272.23                22.37            True
   APP           84.62               39            0.68              2.33        489.96                75.05            True
  TMUS           84.21               19            1.30              1.80        197.59                22.76            True
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

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421101506)

</details>

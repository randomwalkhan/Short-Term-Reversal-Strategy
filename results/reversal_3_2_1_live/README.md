# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 15:35:00 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$13,115.82`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$-242.10`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-16                   1      9     6720.93                 6748.83       746.77         749.87      746.77        749.87            27.9                   0.42        100.00               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260529C00068000       2026-04-17                   0      9     6097.50                 5827.50         6.78           6.48       68.04         67.89          -270.0                  -4.43         94.59               37              0.66         72.85           70.36                  74.40                 143.0           74.0               0.04                                       ok
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           94.74               38            0.98              0.57         82.16                40.09            True
  INTC           94.44               36            0.80              0.39         68.33                74.40            True
   AEP           94.44               18            0.75              0.71        134.26                17.62            True
   LIN           92.31               13            1.41              4.92        497.11                18.78            True
   PEP           86.96               23            0.83              0.92        157.99                20.28            True
  PAYX           84.21               38            0.64              0.41         91.95                31.23            True
   CEG           82.35               34            1.28              2.67        297.99                57.36            True
  WDAY           81.82               44            0.69              0.60        124.61                54.23            True
   BKR           80.77               26            1.02              0.43         60.41                34.01            True
  ADBE           80.65               31            1.56              2.71        247.00                38.98            True
  FANG          100.00                3            3.80              4.96        184.52                29.20           False
   XEL           94.44               36            0.01              0.01         81.05                23.12           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                  detail
2026-04-17T15:35:00.771718-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T15:30:05.693150-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T15:25:05.763304-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T15:10:05.708534-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T15:05:05.702166-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T15:00:03.706216-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:55:03.734020-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:50:05.923182-04:00  entry_1500        entry {"allocated_cash": 6097.5, "asset_type": "option", "contract_symbol": "INTC260529C00068000", "contracts": 9, "entry_option_price": 6.775, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 143.0, "option_spread_pct": 3.69, "option_volume": 74.0, "success_rate": 94.59, "ticker": "INTC"}
2026-04-17T14:40:05.721864-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:35:05.695089-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417153500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417153500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417153500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417153500)

</details>

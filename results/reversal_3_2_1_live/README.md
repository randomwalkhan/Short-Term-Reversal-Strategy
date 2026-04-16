# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 11:05:06 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$7,327.92`
- Equity: `$13,897.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-450.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6570.0          3.9           3.65      231.34        231.08          -450.0                  -6.41         100.0               22              0.82         27.49           27.56                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               34            0.62              3.25        752.54                24.02            True
   WDC           97.06               34            1.04              2.66        363.86                79.90            True
  MRVL           96.67               30            1.40              1.32        134.04                70.04            True
  ROST           92.59               27            0.58              0.91        223.76                24.88            True
  ALNY           92.31               26            1.85              4.32        331.54                43.40            True
  ASML           90.91               11            3.62             37.58       1465.66                53.24            True
  GILD           88.46               26            0.65              0.64        139.50                21.89            True
  ISRG           86.67               15            1.99              6.52        465.57                23.09            True
  KLAC           86.49               37            0.86             10.56       1743.58                51.26            True
  AMAT           86.11               36            0.79              2.18        393.33                56.17            True
  TSLA           84.38               32            1.23              3.39        390.50                50.86            True
  AAPL           83.33               18            1.45              2.71        265.27                21.71            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T11:05:06.423912-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T11:00:06.429305-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:55:06.426923-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:40:06.719835-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:35:06.428424-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:30:06.538163-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:25:06.584595-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:10:06.432406-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T10:05:06.442845-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T10:00:05.433710-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416110506)

</details>

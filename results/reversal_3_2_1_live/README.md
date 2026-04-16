# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 12:55:06 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$14,257.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-90.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6930.0          3.9           3.85      231.34        230.84           -90.0                  -1.28         100.0               22              0.82         27.49           28.83                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               34            0.61              3.23        752.55                24.02            True
   HON          100.00               26            0.59              0.96        231.78                23.34            True
   WDC           96.97               33            2.15              5.50        362.64                79.90            True
   STX           94.59               37            0.81              2.94        518.34                74.63            True
   AEP           92.31               13            0.91              0.85        134.02                19.19            True
  ASML           90.00               10            3.86             40.08       1464.59                53.24            True
  ALNY           88.89               27            1.80              4.20        331.59                43.40            True
  GILD           86.96               23            0.91              0.89        139.39                21.89            True
  KLAC           86.21               29            1.46             17.87       1740.45                51.26            True
  ROST           85.71               14            1.31              2.05        223.27                24.88            True
  AMAT           84.38               32            1.12              3.09        392.94                56.17            True
  AAPL           84.00               25            1.08              2.01        265.57                21.71            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T12:55:06.561781-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T12:40:06.434016-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:35:06.484289-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:30:06.422606-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:25:06.428963-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:10:06.550009-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T12:05:06.425148-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T12:00:03.440674-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T11:55:06.424438-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T11:40:06.426554-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416125506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416125506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416125506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416125506)

</details>

# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 13:30:06 EDT`
Last processed slot: `manage_1330`

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
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6570.0          3.9           3.65      231.34        230.43          -450.0                  -6.41         100.0               22              0.82         27.49           28.44                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.72              3.79        752.31                24.02            True
   HON          100.00               22            0.76              1.23        231.66                23.34            True
   WDC           96.97               33            1.37              3.50        363.50                79.90            True
   AEP           92.31               13            0.89              0.84        134.03                19.19            True
  ALNY           90.91               22            2.14              4.99        331.25                43.40            True
  ASML           90.91               11            3.79             39.31       1464.92                53.24            True
  ROST           90.48               21            1.05              1.65        223.44                24.88            True
  VRTX           88.24               34            0.95              2.94        440.44                27.87            True
  KLAC           87.50               32            1.32             16.18       1741.17                51.26            True
  GILD           86.96               23            0.94              0.92        139.37                21.89            True
  AMAT           84.38               32            1.08              2.97        392.99                56.17            True
  AAPL           84.00               25            1.07              2.00        265.57                21.71            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T13:30:06.517067-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:25:06.427978-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:10:06.436244-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T13:05:06.432138-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T13:00:06.440375-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T12:55:06.561781-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T12:40:06.434016-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:35:06.484289-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:30:06.422606-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:25:06.428963-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416133006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416133006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416133006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416133006)

</details>

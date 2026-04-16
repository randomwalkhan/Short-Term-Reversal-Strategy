# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 13:45:01 EDT`
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

- Cash: `$7,327.92`
- Equity: `$13,627.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6300.0          3.9            3.5      231.34        230.07          -720.0                 -10.26         100.0               22              0.82         27.49           28.09                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               34            0.61              3.23        752.55                24.02            True
   HON          100.00               22            0.79              1.28        231.64                23.34            True
   WDC           96.97               33            1.52              3.88        363.34                79.90            True
   AEP           92.31               26            0.57              0.54        134.16                19.19            True
  ROST           90.48               21            1.04              1.63        223.45                24.88            True
  VRTX           90.32               31            1.07              3.29        440.29                27.87            True
  ASML           90.00               10            3.88             40.29       1464.50                53.24            True
  ALNY           89.47               19            2.34              5.47        331.05                43.40            True
  GILD           86.96               23            0.89              0.87        139.40                21.89            True
  KLAC           86.67               30            1.34             16.36       1741.10                51.26            True
  AAPL           84.62               26            1.05              1.97        265.59                21.71            True
   EXC           84.62               13            1.20              0.40         47.71                22.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T13:40:06.445455-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:35:06.443919-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:30:06.517067-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:25:06.427978-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:10:06.436244-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T13:05:06.432138-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T13:00:06.440375-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T12:55:06.561781-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T12:40:06.434016-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:35:06.484289-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416134501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416134501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416134501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416134501)

</details>

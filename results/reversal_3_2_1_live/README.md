# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 14:10:06 EDT`
Last processed slot: `manage_1400`

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
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6300.0          3.9            3.5      231.34        229.66          -720.0                 -10.26         100.0               22              0.82         27.49           29.07                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               28            1.05              5.55        751.55                24.02            True
   HON          100.00               22            0.93              1.52        231.54                23.34            True
  MRVL           97.22               36            0.79              0.74        134.28                70.04            True
   WDC           96.77               31            2.55              6.51        362.21                79.90            True
  NVDA           91.67               36            0.60              0.84        198.51                36.33            True
  GILD           91.67               12            1.35              1.32        139.20                21.89            True
  ORLY           90.48               42            0.52              0.34         93.45                23.50            True
  VRTX           86.36               22            1.67              5.17        439.49                27.87            True
  KLAC           85.19               27            1.74             21.24       1739.01                51.26            True
 GOOGL           84.62               39            0.54              1.27        336.57                37.85            True
  AAPL           84.62               26            0.94              1.75        265.68                21.71            True
   EXC           84.62               13            1.10              0.37         47.72                22.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T14:10:06.435946-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T14:05:06.594374-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T14:00:06.440718-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T13:55:06.472928-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-16T13:40:06.445455-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:35:06.443919-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:30:06.517067-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:25:06.427978-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-16T13:10:06.436244-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-16T13:05:06.432138-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416141006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416141006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416141006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416141006)

</details>

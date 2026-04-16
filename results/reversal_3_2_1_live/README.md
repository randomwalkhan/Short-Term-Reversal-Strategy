# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 12:25:06 EDT`
Last processed slot: `manage_1230`

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
- Equity: `$14,077.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-270.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6750.0          3.9           3.75      231.34         231.6          -270.0                  -3.85         100.0               22              0.82         27.49           27.26                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               31            0.79              4.15        752.15                24.02            True
   WDC           96.55               29            2.89              7.38        361.84                79.90            True
   AEP           94.74               19            0.73              0.69        134.10                19.19            True
   STX           94.59               37            1.07              3.91        517.93                74.63            True
  ALNY           91.67               24            1.92              4.47        331.47                43.40            True
  ASML           90.91               11            3.74             38.82       1465.13                53.24            True
  GILD           88.46               26            0.80              0.78        139.43                21.89            True
  KLAC           86.21               29            1.49             18.28       1740.28                51.26            True
  ROST           85.71               14            1.33              2.09        223.26                24.88            True
  AAPL           84.62               26            0.98              1.83        265.64                21.71            True
  ISRG           84.62               13            2.03              6.64        465.51                23.09            True
   EXC           84.62               13            1.19              0.40         47.71                22.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T12:25:06.428963-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-16T12:10:06.550009-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T12:05:06.425148-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T12:00:03.440674-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T11:55:06.424438-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-16T11:40:06.426554-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:35:06.442645-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:30:06.450119-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:25:06.517654-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:10:06.436313-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416122506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416122506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416122506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416122506)

</details>

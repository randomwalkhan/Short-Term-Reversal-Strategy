# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 11:50:06 EDT`
Last processed slot: `manage_1200`

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
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6930.0          3.9           3.85      231.34        231.49           -90.0                  -1.28         100.0               22              0.82         27.49           27.82                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               34            0.58              3.07        752.61                24.02            True
  MRVL           97.22               36            0.89              0.84        134.24                70.04            True
   WDC           96.97               33            2.06              5.26        362.74                79.90            True
   STX           94.74               38            0.68              2.48        518.54                74.63            True
  ASML           91.67               12            3.32             34.41       1467.02                53.24            True
  ROST           90.91               22            0.89              1.39        223.55                24.88            True
  ALNY           88.89               27            1.81              4.22        331.58                43.40            True
  GILD           88.46               26            0.76              0.74        139.45                21.89            True
   EXC           86.96               23            0.55              0.19         47.80                22.11            True
  ISRG           86.67               15            2.01              6.59        465.54                23.09            True
  KLAC           86.21               29            1.38             16.92       1740.86                51.26            True
  AMAT           86.11               36            0.89              2.45        393.21                56.17            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T11:40:06.426554-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:35:06.442645-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:30:06.450119-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:25:06.517654-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:10:06.436313-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T11:05:06.423912-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T11:00:06.429305-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:55:06.426923-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:40:06.719835-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:35:06.428424-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416115006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416115006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416115006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416115006)

</details>

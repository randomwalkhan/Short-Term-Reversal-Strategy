# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 11:35:06 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$13,987.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  6660.0          3.9            3.7      231.34        230.88          -360.0                  -5.13         100.0               22              0.82         27.49           27.84                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.66              3.47        752.44                24.02            True
   HON          100.00               27            0.55              0.89        231.81                23.34            True
   WDC           96.97               33            1.60              4.08        363.25                79.90            True
  MRVL           96.97               33            1.05              0.99        134.17                70.04            True
  ASML           93.33               15            2.96             30.69       1468.62                53.24            True
  ROST           92.00               25            0.82              1.28        223.60                24.88            True
  ALNY           91.30               23            1.96              4.58        331.43                43.40            True
  GILD           87.50               24            0.87              0.85        139.40                21.89            True
  KLAC           87.18               39            0.75              9.22       1744.16                51.26            True
  AMAT           87.18               39            0.54              1.48        393.62                56.17            True
   EXC           86.96               23            0.55              0.19         47.80                22.11            True
  ISRG           84.62               13            2.05              6.73        465.48                23.09            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T11:35:06.442645-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:30:06.450119-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:25:06.517654-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-16T11:10:06.436313-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T11:05:06.423912-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T11:00:06.429305-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:55:06.426923-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-16T10:40:06.719835-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:35:06.428424-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:30:06.538163-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416113506)

</details>

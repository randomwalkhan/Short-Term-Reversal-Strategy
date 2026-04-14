# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 13:25:06 EDT`
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

- Cash: `$7,229.00`
- Equity: `$13,255.32`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$110.32`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6026.32        739.5         753.29       739.5        753.29          110.32                   1.86         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.85              2.45        188.05                30.53            True
  COST           95.45               22            0.90              6.17        978.21                19.04            True
  INTC           94.12               17            3.98              1.82         64.42                75.15            True
  MPWR           91.43               35            0.86              8.22       1368.71                58.48            True
  ORLY           90.70               43            0.54              0.36         93.86                24.40            True
  AMAT           86.84               38            0.53              1.48        395.10                56.21            True
  TMUS           82.35               17            1.28              1.73        191.69                20.34            True
  WDAY           81.08               37            1.33              1.12        119.44                50.72            True
  CSCO           80.00               20            0.56              0.32         82.21                28.38            True
   HON          100.00               27            0.47              0.77        233.31                23.77           False
   LIN          100.00                3            2.56              9.13        504.96                18.23           False
  FTNT           96.00               50            0.15              0.08         78.71                38.32           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T13:25:06.439003-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:10:06.425309-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T13:05:06.417007-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T13:00:06.426810-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T12:55:06.432298-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T12:40:06.432068-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:35:06.424201-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:30:06.429134-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:25:06.421645-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:10:06.438728-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414132506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414132506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414132506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414132506)

</details>

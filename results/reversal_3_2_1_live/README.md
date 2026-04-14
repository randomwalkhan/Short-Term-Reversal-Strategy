# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 12:45:06 EDT`
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

- Cash: `$7,229.00`
- Equity: `$13,281.24`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$136.24`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6052.24        739.5         756.53       739.5        756.53          136.24                    2.3         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               15            1.95              2.58        187.99                30.53            True
  COST           93.10               29            0.72              4.96        978.72                19.04            True
  INTC           91.67               12            4.65              2.12         64.29                75.15            True
  FAST           91.67               12            2.20              0.71         45.50                37.61            True
  MPWR           90.91               33            1.10             10.57       1367.70                58.48            True
  AMAT           86.11               36            0.69              1.91        394.91                56.21            True
  WDAY           82.05               39            1.08              0.91        119.53                50.72            True
  CRWD           81.40               43            0.59              1.67        401.52                60.69            True
  TMUS           81.25               16            1.48              2.00        191.57                20.34            True
  PANW           80.49               41            0.74              0.84        162.18                56.05            True
  CSCO           80.00               20            0.76              0.44         82.16                28.38            True
   HON          100.00               27            0.49              0.80        233.30                23.77           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T12:40:06.432068-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:35:06.424201-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:30:06.429134-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:25:06.421645-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-14T12:10:06.438728-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T12:05:06.429215-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T12:00:03.430403-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T11:55:05.428677-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T11:40:02.417003-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-14T11:35:06.429798-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414124506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414124506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414124506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414124506)

</details>

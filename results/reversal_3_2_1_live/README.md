# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 14:10:06 EDT`
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

- Cash: `$7,229.00`
- Equity: `$13,259.80`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$114.80`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                  6030.8        739.5         753.85       739.5        753.85           114.8                   1.94         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.69              2.24        188.14                30.53            True
  FTNT           95.35               43            0.70              0.38         78.58                38.32            True
  INTC           95.24               21            3.50              1.60         64.51                75.15            True
  FAST           92.86               14            1.98              0.63         45.53                37.61            True
  MPWR           91.18               34            1.01              9.74       1368.05                58.48            True
  COST           91.18               34            0.57              3.94        979.16                19.04            True
  CTSH           85.00               40            0.53              0.22         60.43                30.13            True
  WDAY           80.00               30            2.00              1.68        119.20                50.72            True
  PCAR           80.00               20            1.41              1.25        126.84                27.21            True
  TMUS           80.00               15            1.55              2.09        191.53                20.34            True
   HON          100.00               27            0.46              0.75        233.32                23.77           False
   LIN          100.00                3            2.37              8.45        505.25                18.23           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T14:10:06.428517-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T14:05:06.440824-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T14:00:05.431636-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T13:55:04.952325-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T13:40:06.435598-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:35:06.418066-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:30:06.417621-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:25:06.439003-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:10:06.425309-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T13:05:06.417007-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414141006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414141006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414141006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414141006)

</details>

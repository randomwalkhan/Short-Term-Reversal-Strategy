# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 12:35:00 EDT`
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

- Cash: `$1,069.00`
- Equity: `$13,482.44`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$337.44`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6475.00          8.8           9.25      186.41        186.82          315.00                   5.11         100.0               20              1.42         38.05           40.47                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5938.44        739.5         742.30      739.50        742.30           22.44                   0.38         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               18            1.75              9.24        751.55                24.04            True
   HON          100.00               14            1.29              2.11        232.34                23.78            True
   WDC           96.67               30            2.78              7.13        363.16                85.18            True
  ALNY           92.31               26            1.90              4.51        337.48                42.77            True
   AEP           92.00               25            0.58              0.55        135.23                19.01            True
  MPWR           91.18               34            1.26             11.99       1358.28                58.76            True
  VRTX           90.32               31            1.02              3.16        442.92                27.91            True
   WMT           90.32               31            0.62              0.55        124.82                26.20            True
   MAR           88.89               36            0.74              1.90        365.88                29.18            True
   PEP           88.24               17            0.95              1.04        155.28                20.04            True
  FAST           87.50               16            1.66              0.52         44.40                38.71            True
   EXC           87.50               16            0.85              0.29         48.49                21.52            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-15T12:35:00.710440-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:30:04.719379-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:25:01.751378-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:10:03.719067-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:05:05.700528-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:00:03.446556-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:55:03.708914-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:40:00.698299-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:35:03.700134-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:30:05.709566-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415123500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415123500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415123500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415123500)

</details>

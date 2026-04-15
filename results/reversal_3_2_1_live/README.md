# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 12:30:04 EDT`
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
- Equity: `$13,418.16`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$273.16`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6405.00          8.8           9.15      186.41        187.03          245.00                   3.98         100.0               20              1.42         38.05           39.08                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5944.16        739.5         743.02      739.50        743.02           28.16                   0.48         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               19            1.68              8.90        751.70                24.04            True
   HON          100.00               11            1.39              2.27        232.27                23.78            True
   WDC           96.88               32            2.47              6.34        363.50                85.18            True
  FTNT           95.45               44            0.71              0.39         78.53                37.90            True
   AEP           93.33               15            0.83              0.79        135.13                19.01            True
   WMT           93.10               29            0.76              0.67        124.76                26.20            True
  ALNY           91.30               23            1.97              4.69        337.40                42.77            True
  MPWR           91.18               34            1.24             11.84       1358.34                58.76            True
   LIN           90.00               20            0.96              3.35        498.25                19.38            True
   STX           88.89               18            4.23             15.78        526.68                74.84            True
  VRTX           88.46               26            1.28              3.99        442.57                27.91            True
   MAR           88.24               34            0.84              2.15        365.78                29.18            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-15T12:30:04.719379-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:25:01.751378-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:10:03.719067-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:05:05.700528-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:00:03.446556-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:55:03.708914-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:40:00.698299-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:35:03.700134-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:30:05.709566-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:25:03.719640-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415123004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415123004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415123004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415123004)

</details>

# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 12:45:00 EDT`
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

- Cash: `$1,069.00`
- Equity: `$13,457.72`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$312.72`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6440.00          8.8           9.20      186.41        187.43          280.00                   4.55         100.0               20              1.42         38.05           38.49                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5948.72        739.5         743.59      739.50        743.59           32.72                   0.55         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               19            1.58              8.34        751.93                24.04            True
   HON          100.00               17            1.21              1.97        232.39                23.78            True
   WDC           96.30               27            3.38              8.67        362.50                85.18            True
  FTNT           95.65               46            0.57              0.32         78.56                37.90            True
   XEL           91.67               12            0.94              0.52         79.61                20.57            True
  MPWR           90.32               31            1.61             15.33       1356.85                58.76            True
  ALNY           90.00               30            1.58              3.76        337.80                42.77            True
   EXC           88.89               18            0.77              0.26         48.50                21.52            True
   MAR           88.57               35            0.78              2.01        365.84                29.18            True
  VRTX           88.00               25            1.32              4.12        442.52                27.91            True
  DXCM           87.50               40            0.98              0.43         62.76                31.26            True
  GILD           87.50               24            0.85              0.83        140.09                21.91            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-15T12:40:05.426776-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:35:00.710440-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:30:04.719379-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:25:01.751378-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:10:03.719067-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:05:05.700528-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:00:03.446556-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:55:03.708914-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:40:00.698299-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:35:03.700134-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415124500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415124500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415124500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415124500)

</details>

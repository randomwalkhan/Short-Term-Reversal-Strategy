# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 12:20:04 EDT`
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
- Equity: `$13,528.72`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$383.72`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6545.00          8.8           9.35      186.41        186.87          385.00                   6.25         100.0               20              1.42         38.05           40.42                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5914.72        739.5         739.34      739.50        739.34           -1.28                  -0.02         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               14            2.11             11.17        750.72                24.04            True
   HON          100.00               11            1.42              2.31        232.25                23.78            True
   WDC           96.97               33            2.31              5.92        363.68                85.18            True
  FTNT           95.65               46            0.64              0.35         78.55                37.90            True
   AEP           94.44               18            0.73              0.69        135.17                19.01            True
  FAST           92.31               13            2.05              0.64         44.35                38.71            True
  MPWR           91.43               35            0.94              9.00       1359.56                58.76            True
  ALNY           90.91               22            2.13              5.07        337.24                42.77            True
   WMT           90.48               21            1.05              0.92        124.66                26.20            True
  VRTX           90.32               31            1.07              3.33        442.85                27.91            True
   LIN           90.00               20            0.89              3.11        498.35                19.38            True
  CTAS           89.47               38            0.51              0.63        175.87                29.17            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-15T12:10:03.719067-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:05:05.700528-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:00:03.446556-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:55:03.708914-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T11:40:00.698299-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:35:03.700134-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:30:05.709566-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:25:03.719640-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-15T11:10:01.922344-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T11:05:03.774531-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415122004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415122004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415122004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415122004)

</details>

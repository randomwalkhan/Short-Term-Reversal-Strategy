# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 12:30:01 EDT`
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

- Cash: `$7,080.20`
- Equity: `$12,982.72`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$28.73`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   2     26     5873.79                 5902.52       225.91         227.02      225.91        227.02           28.73                   0.49         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           97.50               40            0.53              0.35         93.09                46.34            True
  SHOP           92.86               14            4.67              4.31        130.11                53.34            True
  NVDA           91.67               36            0.66              0.94        202.10                33.17            True
  DDOG           88.89               27            2.29              2.12        131.23                58.97            True
  QCOM           88.89               27            1.05              1.00        135.64                21.23            True
  ABNB           88.24               34            0.97              0.98        143.76                37.26            True
  TSLA           86.96               23            1.97              5.34        385.22                48.19            True
  DXCM           86.67               45            0.79              0.35         63.26                37.31            True
  SNPS           85.71               14            3.28             10.95        472.57                42.64            True
  ASML           84.38               32            0.97              9.80       1439.46                53.38            True
   ADP           83.33               12            2.42              3.42        200.22                26.51            True
  ORLY           81.25               16            1.64              1.08         93.46                22.27            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-23T12:30:01.242610-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:25:03.186227-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:10:04.189589-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:05:01.187665-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:00:03.198539-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:55:01.249277-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:50:01.202591-04:00 manage_1200         exit {"asset_type": "option", "contract_symbol": "INTC260618C00065000", "fill_price": 8.675, "pnl": 980.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "INTC"}
2026-04-23T11:40:01.234723-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:35:01.179247-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:30:04.126054-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423123001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423123001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423123001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423123001)

</details>

# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 12:45:01 EDT`
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

- Cash: `$7,080.20`
- Equity: `$12,985.32`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$31.33`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   2     26     5873.79                 5905.12       225.91         227.12      225.91        227.12           31.33                   0.53         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           97.30               37            0.66              0.43         93.06                46.34            True
  SHOP           92.86               14            4.73              4.37        130.09                53.34            True
  DDOG           88.89               27            2.50              2.32        131.15                58.97            True
  QCOM           88.46               26            1.11              1.06        135.62                21.23            True
  ABNB           86.84               38            0.69              0.70        143.88                37.26            True
  DXCM           86.67               45            0.66              0.29         63.28                37.31            True
  ASML           85.71               35            0.67              6.80       1440.75                53.38            True
  TSLA           85.71               21            2.60              7.04        384.49                48.19            True
  SNPS           83.33               12            3.38             11.29        472.42                42.64            True
   ADP           83.33               12            2.43              3.43        200.22                26.51            True
  INSM           81.58               38            0.91              0.92        144.09                48.16            True
   HON          100.00                6            2.45              3.77        218.35                25.23           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-23T12:40:04.311160-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:35:04.168358-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:30:01.242610-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:25:03.186227-04:00 manage_1230 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:10:04.189589-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:05:01.187665-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T12:00:03.198539-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:55:01.249277-04:00 manage_1200 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-23T11:50:01.202591-04:00 manage_1200         exit {"asset_type": "option", "contract_symbol": "INTC260618C00065000", "fill_price": 8.675, "pnl": 980.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "INTC"}
2026-04-23T11:40:01.234723-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423124501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423124501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423124501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423124501)

</details>

# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 14:45:05 EDT`
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
- Equity: `$12,972.84`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$18.85`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   2     26     5873.79                 5892.64       225.91         226.64      225.91        226.64           18.85                   0.32         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA           93.33               15            3.54              9.60        383.40                48.19            True
  NVDA           91.67               24            1.56              2.20        201.56                33.17            True
  UPRO           90.32               31            1.20              1.06        125.24                53.56            True
  DDOG           87.50               24            2.99              2.76        130.96                58.97            True
  ABNB           87.50               24            1.67              1.69        143.46                37.26            True
  ORLY           86.67               30            1.01              0.66         93.64                22.27            True
  DXCM           86.49               37            1.30              0.58         63.16                37.31            True
  CSCO           86.36               22            1.00              0.63         89.53                27.83            True
  ISRG           84.62               39            0.60              2.02        482.76                37.51            True
  BKNG           84.00               25            1.95              2.45        178.35                44.00            True
    MU           82.86               35            1.35              4.61        485.51                79.49            True
  QCOM           81.25               16            1.79              1.70        135.34                21.23            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:35:04.153865-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T14:00:03.244541-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T13:55:06.322619-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T13:40:04.214984-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-23T13:35:01.289230-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423144505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423144505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423144505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423144505)

</details>

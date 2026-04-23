# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 14:30:04 EDT`
Last processed slot: `manage_1430`

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
- Equity: `$12,971.02`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$17.03`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   2     26     5873.79                 5890.82       225.91         226.57      225.91        226.57           17.03                   0.29         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NVDA           95.65               23            1.58              2.24        201.54                33.17            True
  TSLA           94.12               17            3.33              9.03        383.64                48.19            True
  UPRO           91.18               34            0.93              0.82        125.34                53.56            True
  ABNB           89.29               28            1.53              1.55        143.52                37.26            True
  ORLY           88.57               35            0.83              0.55         93.69                22.27            True
  DDOG           88.46               26            2.86              2.65        131.01                58.97            True
  CSCO           86.96               23            0.85              0.53         89.57                27.83            True
  BKNG           85.19               27            1.81              2.28        178.42                44.00            True
  DXCM           84.62               39            1.10              0.49         63.20                37.31            True
  QCOM           83.33               18            1.63              1.55        135.40                21.23            True
    MU           82.86               35            1.61              5.50        485.12                79.49            True
   WBD           80.95               21            0.71              0.14         27.27                 7.69            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T14:00:03.244541-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T13:55:06.322619-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-23T13:40:04.214984-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-23T13:35:01.289230-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-23T13:30:04.040854-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-23T13:25:03.137208-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423143004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423143004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423143004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423143004)

</details>

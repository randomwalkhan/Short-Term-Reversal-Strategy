# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 15:55:00 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$7,327.92`
- Equity: `$14,707.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   0     18      7020.0                  7380.0          3.9            4.1      231.34        232.15           360.0                   5.13         100.0               22              0.82         27.49           27.65                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price         pnl  return_pct                  exit_reason
  FANG     option         option FANG260515C00185000      7          2026-04-14         2026-04-15          8.8    10.35000 1085.000000   17.613636 take_profit_day1_hit_at_scan
  REGN      share share_fallback                REGN      8          2026-04-13         2026-04-15        739.5   754.23999  117.919922    1.993237        time_exit_at_4pm_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.30               37            0.72              1.84        365.43                85.18            True
   AEP           94.12               17            0.80              0.75        135.14                19.01            True
   STX           92.59               27            2.63              9.82        529.23                74.84            True
  MPWR           91.67               36            0.87              8.32       1359.85                58.76            True
  VRTX           89.74               39            0.52              1.62        443.59                27.91            True
  ALNY           88.89               27            1.66              3.94        337.72                42.77            True
   MAR           88.57               35            0.79              2.04        365.83                29.18            True
  AMAT           87.18               39            0.53              1.46        395.02                56.23            True
   CSX           86.96               23            0.79              0.23         42.41                21.52            True
   WBD           84.85               33            0.53              0.10         27.33                 9.25            True
   TXN           83.33               30            1.13              1.73        218.13                31.27            True
  ASML           83.33               24            2.27             24.12       1507.96                52.27            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                           detail
2026-04-15T15:55:00.685389-04:00 manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:50:05.921508-04:00 manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 754.24, "pnl": 117.92, "reason": "time_exit_at_4pm_scan", "return_pct": 1.99, "ticker": "REGN"}
2026-04-15T15:40:05.911045-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:35:05.907365-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:30:05.900838-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:25:04.898383-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:10:01.074432-04:00  entry_1500 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:05:05.906794-04:00  entry_1500 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:00:05.949066-04:00  entry_1500 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T14:55:00.892312-04:00  entry_1500 slot_skipped                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415155500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415155500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415155500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415155500)

</details>

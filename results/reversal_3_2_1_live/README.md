# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 17:45:00 EDT`
Last processed slot: `share_ext_1745`

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
- Equity: `$14,977.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$630.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   0     18      7020.0                  7650.0          3.9           4.25      231.34         234.0           630.0                   8.97         100.0               22              0.82         27.49           28.39                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price         pnl  return_pct                  exit_reason
  FANG     option         option FANG260515C00185000      7          2026-04-14         2026-04-15          8.8    10.35000 1085.000000   17.613636 take_profit_day1_hit_at_scan
  REGN      share share_fallback                REGN      8          2026-04-13         2026-04-15        739.5   754.23999  117.919922    1.993237        time_exit_at_4pm_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                           detail
2026-04-15T16:10:06.073164-04:00 manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T16:05:06.125049-04:00 manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T16:00:04.897355-04:00 manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:55:00.685389-04:00 manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:50:05.921508-04:00 manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 754.24, "pnl": 117.92, "reason": "time_exit_at_4pm_scan", "return_pct": 1.99, "ticker": "REGN"}
2026-04-15T15:40:05.911045-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:35:05.907365-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:30:05.900838-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:25:04.898383-04:00 manage_1530 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:10:01.074432-04:00  entry_1500 slot_skipped                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415174500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415174500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415174500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415174500)

</details>

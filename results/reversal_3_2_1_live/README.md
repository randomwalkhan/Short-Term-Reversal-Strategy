# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 23:40:06 EDT`
Last processed slot: `share_ext_2340`

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

- Cash: `$6,851.31`
- Equity: `$12,141.08`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$1.49`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   0     23     5288.28                 5289.77       229.93         229.99      229.93        229.99            1.49                   0.03         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20      6.77500    5.400000 -1237.500000  -20.295203 stop_loss_hit_at_scan
  REGN      share share_fallback                REGN      9          2026-04-16         2026-04-20    746.77002  748.900024    19.170044    0.285229 time_exit_at_4pm_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                         detail
2026-04-20T16:10:06.425591-04:00 manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:05:05.426426-04:00 manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T16:00:06.436506-04:00 manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:55:06.432735-04:00 manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:50:06.460350-04:00 manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 748.9, "pnl": 19.17, "reason": "time_exit_at_4pm_scan", "return_pct": 0.29, "ticker": "REGN"}
2026-04-20T15:40:03.007489-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:35:05.448312-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:30:05.898034-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:25:06.452583-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:10:06.433548-04:00  entry_1500 slot_skipped                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420234006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420234006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420234006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420234006)

</details>

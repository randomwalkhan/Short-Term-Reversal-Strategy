# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 14:45:05 EDT`
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

- Cash: `$8,314.00`
- Equity: `$14,304.16`
- Realized PnL: `$4,230.00`
- Unrealized PnL: `$74.16`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   2      8      5916.0                 5990.16        739.5         748.77       739.5        748.77           74.16                   1.25         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  FANG     option         option FANG260515C00185000      7          2026-04-14         2026-04-15          8.8       10.35 1085.0   17.613636 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.89              4.72        753.49                24.04            True
   HON          100.00               22            0.91              1.48        232.61                23.78            True
   WDC           97.14               35            0.94              2.42        365.18                85.18            True
  MRVL           96.77               31            1.26              1.18        133.29                70.60            True
   AEP           94.12               17            0.76              0.72        135.15                19.01            True
  ALNY           92.86               42            0.98              2.34        338.41                42.77            True
   STX           91.67               24            3.14             11.72        528.42                74.84            True
  FAST           89.66               29            0.92              0.29         44.50                38.71            True
   EXC           89.47               19            0.73              0.25         48.51                21.52            True
   MAR           88.89               36            0.70              1.81        365.93                29.18            True
  MPWR           88.46               26            2.19             20.94       1354.45                58.76            True
  GILD           88.46               26            0.70              0.69        140.15                21.91            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                  detail
2026-04-15T14:40:01.721975-04:00 manage_1430 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:35:00.735526-04:00 manage_1430 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:30:01.739266-04:00 manage_1430 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:25:01.819991-04:00 manage_1430 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:10:00.708048-04:00 manage_1400 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:05:00.755308-04:00 manage_1400 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T14:00:00.656760-04:00 manage_1400 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T13:55:00.758652-04:00 manage_1400 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-04-15T13:50:00.792014-04:00 manage_1400         exit {"asset_type": "option", "contract_symbol": "FANG260515C00185000", "fill_price": 10.35, "pnl": 1085.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.61, "ticker": "FANG"}
2026-04-15T13:40:03.714737-04:00 manage_1330 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415144505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415144505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415144505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415144505)

</details>

# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-30 15:45:01 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$8,357.50`
- Equity: `$15,007.50`
- Realized PnL: `$5,567.50`
- Unrealized PnL: `$-560.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260618C00095000       2026-04-30                   0      7      7210.0                  6650.0         10.3            9.5       94.02         93.89          -560.0                  -7.77         100.0               38              0.77         78.24           72.13                   91.3               17799.0         2068.0               0.01                      ok
```

## Today's Closed Trades (2026-04-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CRWD     option         option CRWD260618C00450000      2          2026-04-29         2026-04-30         36.2      30.175 -1205.0  -16.643646 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               37            0.87              0.58         94.50                91.30            True
  FANG          100.00               25            0.64              0.92        204.93                33.59            True
  TMUS           83.33               24            1.24              1.72        197.43                38.48            True
  AXON           84.78               46            0.05              0.13        400.48                68.68           False
  WDAY           85.11               47            0.13              0.12        122.38                63.16           False
  CRWD           78.26               23            1.67              5.29        450.11                53.11           False
  INTU           79.31               29            1.40              3.89        393.41                55.07           False
  CDNS           97.50               40            0.24              0.56        329.71                53.49           False
  PANW           81.25               32            1.04              1.32        180.98                47.73           False
    ZS           76.19               21            3.06              2.88        133.49                64.71           False
  FTNT           91.30               23            1.75              1.05         85.66                38.28           False
  MSFT          100.00                1            3.67             10.91        419.78                29.73           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-04-30T15:40:04.338512-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T15:35:01.528764-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T15:30:05.829979-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T15:25:05.342773-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T15:10:03.423192-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T15:04:22.001854-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T14:48:57.081711-04:00  entry_1500          entry {"allocated_cash": 7210.0, "asset_type": "option", "contract_symbol": "INTC260618C00095000", "contracts": 7, "entry_option_price": 10.3, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 17799.0, "option_spread_pct": 0.97, "option_volume": 2068.0, "success_rate": 100.0, "ticker": "INTC", "timing_score": 0.639}
2026-04-30T14:48:57.081711-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-30", "training_samples": 5506, "window": 5}
2026-04-30T14:32:17.011087-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-04-30T14:06:17.032910-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260430154501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260430154501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260430154501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260430154501)

</details>

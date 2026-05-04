# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-04 14:50:09 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$9,067.50`
- Equity: `$17,667.50`
- Realized PnL: `$7,667.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CHTR     option         option CHTR260618C00175000       2026-05-04                   0     10      8600.0                  8600.0          8.6            8.6      169.93        169.83             0.0                    0.0         88.89               36              1.06         46.31           46.31                 118.68                 169.0           21.0               0.07                      ok
```

## Today's Closed Trades (2026-05-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           88.89               36            1.06              1.27        171.20               118.68            True
  INTC          100.00               20            3.07              2.14         98.69                90.80            True
  SOXL           82.14               28            2.48              2.26        129.43                93.95            True
  AXON           84.62               39            0.77              2.18        401.38                68.18            True
  ISRG           94.12               17            1.64              5.26        455.52                36.31            True
   KDP           81.25               16            1.36              0.28         28.97                34.45            True
   WMT           89.47               19            1.19              1.10        131.13                27.95            True
  NFLX           88.24               34            0.77              0.49         91.85                43.43            True
   CSX           80.95               21            1.09              0.34         44.95                28.27            True
  MPWR           87.50               24            1.79             19.85       1574.97                53.29            True
   ADI           81.25               32            0.61              1.70        396.96                38.53            True
  TMUS           85.71               28            1.01              1.39        195.47                37.34            True
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                        detail
2026-05-04T14:50:09.604154-04:00  entry_1500          entry {"allocated_cash": 8600.0, "asset_type": "option", "contract_symbol": "CHTR260618C00175000", "contracts": 10, "entry_option_price": 8.6, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 6.98, "option_volume": 21.0, "success_rate": 88.89, "ticker": "CHTR", "timing_score": 0.733}
2026-05-04T14:50:09.604154-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                  {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-04", "training_samples": 5525, "window": 5}
2026-05-04T14:40:09.470745-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:35:09.922061-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:30:09.366130-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:25:09.855763-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:10:09.093734-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:05:09.193507-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:00:08.800470-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T13:55:10.029925-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260504145009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260504145009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260504145009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260504145009)

</details>

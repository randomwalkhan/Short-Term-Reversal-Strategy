# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-04 15:55:09 EDT`
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
- Equity: `$16,717.50`
- Realized PnL: `$7,667.50`
- Unrealized PnL: `$-950.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CHTR     option         option CHTR260618C00175000       2026-05-04                   0     10      8600.0                  7650.0          8.6           7.65      169.93        165.29          -950.0                 -11.05         88.89               36              1.06         46.31           50.92                 118.68                 169.0           21.0               0.07                      ok
```

## Today's Closed Trades (2026-05-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
 CMCSA           90.48               21            0.70              0.13         27.11                61.39            True
  INTC          100.00               17            3.71              2.59         98.50                90.80            True
  SOXL           82.14               28            2.42              2.21        129.46                93.95            True
  NFLX           86.36               22            1.19              0.77         91.73                43.43            True
  MPWR           91.18               34            0.55              6.10       1580.86                53.29            True
   KDP           85.00               20            1.03              0.21         29.00                34.45            True
  ISRG           95.65               23            1.28              4.09        456.03                36.31            True
   WMT           90.48               21            1.14              1.05        131.15                27.95            True
  MRVL          100.00               31            0.93              1.08        164.49                47.49            True
  AVGO           91.67               24            1.56              4.60        419.31                41.07            True
  AXON           81.25               32            1.87              5.28        400.05                68.18            True
  TMUS           85.71               28            1.01              1.39        195.46                37.34            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                        detail
2026-05-04T15:55:09.975943-04:00 manage_1600 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:40:09.372943-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:35:09.467002-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:30:09.346876-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:25:09.552870-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:10:09.065840-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:05:09.667886-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T15:00:09.508232-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:55:09.604545-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-04T14:50:09.604154-04:00  entry_1500        entry {"allocated_cash": 8600.0, "asset_type": "option", "contract_symbol": "CHTR260618C00175000", "contracts": 10, "entry_option_price": 8.6, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 6.98, "option_volume": 21.0, "success_rate": 88.89, "ticker": "CHTR", "timing_score": 0.733}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260504155509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260504155509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260504155509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260504155509)

</details>

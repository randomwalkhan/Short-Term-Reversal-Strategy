# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 14:55:06 EDT`
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

- Cash: `$8,255.50`
- Equity: `$13,975.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$-70.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00280000       2026-04-24                   0      4      5790.0                  5720.0        14.48           14.3      276.91        277.16           -70.0                  -1.21         80.95               21              1.88         37.37           36.62                  66.99                1259.0          219.0               0.04                      ok
```

## Today's Closed Trades (2026-04-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  NVDA     option         option NVDA260618C00200000      5          2026-04-23         2026-04-24       12.325      14.475 1075.0   17.444219 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           82.61               23            1.80              3.55        280.71                66.99            True
  FAST           88.46               26            1.19              0.38         45.29                38.70            True
  MRVL           97.22               36            0.91              1.05        165.11                67.12            True
   WMT           83.33               12            1.74              1.61        131.34                24.33            True
  MSTR           80.95               42            0.64              0.77        172.14                74.46            True
   CSX           87.50               24            0.91              0.29         46.05                27.21            True
  MDLZ           82.61               23            0.61              0.25         57.60                22.00            True
  FANG          100.00               31            0.50              0.69        195.30                34.00            True
  AAPL           81.82               22            1.24              2.38        272.41                25.85            True
  NFLX           95.00               40            0.46              0.30         92.69                46.09           False
   ADI           83.78               37            0.42              1.19        403.37                40.58           False
   APP           82.35               34            1.35              4.30        452.33                77.03           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                         detail
2026-04-24T14:55:06.115782-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:50:06.282476-04:00  entry_1500          entry {"allocated_cash": 5790.0, "asset_type": "option", "contract_symbol": "TXN260618C00280000", "contracts": 4, "entry_option_price": 14.475, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 1259.0, "option_spread_pct": 3.8, "option_volume": 219.0, "success_rate": 80.95, "ticker": "TXN", "timing_score": 0.579}
2026-04-24T14:50:06.282476-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-24", "training_samples": 5461, "window": 5}
2026-04-24T14:40:02.156742-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:35:05.332979-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:30:02.109645-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:25:02.113704-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:10:02.102094-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:05:04.100469-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-24T14:00:02.276536-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424145506)

</details>

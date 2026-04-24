# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 16:00:02 EDT`
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

- Cash: `$8,255.50`
- Equity: `$13,835.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$-210.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00280000       2026-04-24                   0      4      5790.0                  5580.0        14.48          13.95      276.91        277.14          -210.0                  -3.63         80.95               21              1.88         37.37           35.92                  66.99                1259.0          219.0               0.04                      ok
```

## Today's Closed Trades (2026-04-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  NVDA     option         option NVDA260618C00200000      5          2026-04-23         2026-04-24       12.325      14.475 1075.0   17.444219 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           81.82               22            1.80              3.56        280.70                66.99            True
  FAST           82.35               17            1.72              0.55         45.22                38.70            True
  MRVL           97.22               36            0.76              0.88        165.18                67.12            True
   WMT           84.62               13            1.60              1.48        131.40                24.33            True
   ADI           82.14               28            1.08              3.06        402.57                40.58            True
  SBUX           93.33               30            0.89              0.62         99.27                31.25            True
  MSTR           80.95               42            0.84              1.01        172.03                74.46            True
   APP           82.86               35            1.16              3.69        452.59                77.03            True
  FANG          100.00               31            0.40              0.55        195.36                34.00           False
   CSX           70.00               10            1.71              0.55         45.94                27.21           False
  NFLX           95.24               42            0.42              0.27         92.70                46.09           False
   STX           95.12               41            0.23              0.96        587.21                63.32           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T16:00:02.171187-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-24T15:55:02.149717-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-24T15:40:01.121969-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-24T15:35:01.140975-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-24T15:30:01.137261-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-24T15:25:01.130783-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-24T15:10:01.134952-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-24T15:05:01.122254-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-24T15:00:04.108388-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-24T14:55:06.115782-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424160002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424160002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424160002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424160002)

</details>

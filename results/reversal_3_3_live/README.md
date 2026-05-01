# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 10:20:05 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$16,530.00`
- Realized PnL: `$5,567.50`
- Unrealized PnL: `$962.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260618C00095000       2026-04-30                   1      7      7210.0                  8172.5         10.3          11.68       94.02         98.77           962.5                  13.35         100.0               38              0.77         78.24           68.45                   91.3               17799.0         2068.0               0.01                      ok
```

## Today's Closed Trades (2026-05-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           84.38               32            0.74              1.46        280.45                67.79            True
  FANG          100.00               16            1.69              2.43        204.59                30.31            True
   ADI           80.77               26            1.01              2.83        401.05                38.22            True
  NXPI           68.75               16            2.51              5.17        291.37                84.73           False
  AXON           84.44               45            0.36              1.03        401.32                68.71           False
   ADP           77.78               18            1.21              1.80        211.17                37.35           False
   KDP           88.89               36            0.10              0.02         29.39                34.77           False
  ASML           87.50               40            0.10              1.02       1438.55                47.82           False
  ORLY           89.66               29            1.02              0.71         99.10                32.49           False
  INTU           84.44               45            0.16              0.43        388.32                55.12           False
   CSX           88.89               36            0.29              0.09         45.39                28.16           False
   AMD           87.80               41            0.09              0.22        354.39                60.73           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-01T10:10:01.610571-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T10:05:01.725672-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T10:00:02.530062-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T09:55:01.544131-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T09:40:04.657745-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T09:35:01.597283-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T09:30:01.556101-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T09:25:01.559161-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T00:00:02.455342-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-30T16:10:06.514467-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501102005)

</details>

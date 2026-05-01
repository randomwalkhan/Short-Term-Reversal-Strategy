# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 09:30:01 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$15,644.50`
- Realized PnL: `$5,567.50`
- Unrealized PnL: `$77.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260618C00095000       2026-04-30                   1      7      7210.0                  7287.0         10.3          10.41       94.02         94.19            77.0                   1.07         100.0               38              0.77         78.24            0.78                   91.3               17799.0         2068.0               0.01                      ok
```

## Today's Closed Trades (2026-05-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               37            0.70              0.46         94.28                90.68            True
   TXN           82.14               28            1.29              2.54        279.99                67.79            True
  SOXL           80.00               25            3.05              2.72        125.89                94.60            True
  QCOM           85.00               20            1.50              1.88        178.77                62.29            True
  FANG          100.00               24            0.75              1.08        205.17                30.31            True
  ASML           83.87               31            0.78              7.85       1435.63                47.82            True
  MCHP           84.38               32            0.80              0.52         92.69                46.58            True
  NXPI           76.67               30            0.97              1.99        292.74                84.73           False
   ADP           77.78               18            1.45              2.18        214.12                37.35           False
   ADI           79.17               24            1.23              3.46        400.77                38.22           False
   KDP           88.89               36            0.07              0.01         29.39                34.77           False
   CEG           90.00               40            0.38              0.83        312.64                46.55           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-01T09:30:01.556101-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T09:25:01.559161-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T00:00:02.455342-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-30T16:10:06.514467-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-30T16:05:04.468898-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-30T16:00:02.362386-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-30T15:55:01.138813-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-30T15:40:04.338512-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-30T15:35:01.528764-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-30T15:30:05.829979-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501093001)

</details>

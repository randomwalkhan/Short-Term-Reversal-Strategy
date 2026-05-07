# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 10:05:04 EDT`
Last processed slot: `manage_1000`

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
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$12,118.50`
- Equity: `$26,158.50`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$4,132.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00470000       2026-05-06                   1      3      9907.5                 14040.0        33.02           46.8      466.99        497.68          4132.5                  41.71         80.95               21               2.0         52.84            50.4                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               35            0.61              0.48        112.80                95.68            True
   TXN           90.00               10            2.22              4.51        287.51                67.07            True
  QCOM           93.75               32            0.73              0.98        192.24                72.73            True
   KDP           82.35               17            1.38              0.28         28.44                34.76            True
  ASML           82.14               28            1.16             12.53       1539.37                46.11            True
    MU           85.71               35            0.80              3.75        665.19                62.30            True
  MSTR           88.24               34            2.21              2.88        185.58                67.05            True
   ADI           81.48               27            1.03              3.00        414.37                34.89            True
  NXPI           64.29               14            2.95              6.26        300.87                84.51           False
  SBUX          100.00                6            2.63              1.96        105.60                31.94           False
   CEG           86.67               30            1.46              3.29        321.37                45.75           False
 GOOGL           88.89               45            0.13              0.36        397.67                37.42           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-07T10:05:04.033139-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T10:00:03.903840-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T09:55:02.556058-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T09:40:01.922571-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:35:01.914408-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:30:01.925048-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:25:01.894252-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T00:00:03.858471-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-06T16:10:02.677283-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-06T16:05:02.443108-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507100504)

</details>

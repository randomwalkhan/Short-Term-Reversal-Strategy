# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 10:15:01 EDT`
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
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$12,118.50`
- Equity: `$28,048.50`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$6,022.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00470000       2026-05-06                   1      3      9907.5                 15930.0        33.02           53.1      466.99        496.75          6022.5                  60.79         80.95               21               2.0         52.84           57.89                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   KDP           80.00               10            1.80              0.36         28.41                34.76            True
  ASML           82.76               29            0.98             10.61       1540.19                46.11            True
  MSTR           89.19               37            1.78              2.32        185.82                67.05            True
   TXN           88.89                9            2.57              5.22        287.20                67.07           False
  NXPI           69.23               13            3.17              6.73        300.67                84.51           False
  GEHC           76.19               42            0.27              0.12         61.69                55.11           False
  SBUX          100.00                5            2.94              2.19        105.50                31.94           False
 GOOGL           88.10               42            0.26              0.73        397.51                37.42           False
  GOOG           88.10               42            0.31              0.86        394.69                37.75           False
   ADI           76.19               21            1.66              4.83        413.59                34.89           False
  PCAR           73.68               19            1.51              1.23        115.98                31.28           False
   CEG           89.74               39            0.68              1.53        322.12                45.75           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-07T10:10:04.036694-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T10:05:04.033139-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T10:00:03.903840-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T09:55:02.556058-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-07T09:40:01.922571-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:35:01.914408-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:30:01.925048-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:25:01.894252-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T00:00:03.858471-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-06T16:10:02.677283-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507101501)

</details>

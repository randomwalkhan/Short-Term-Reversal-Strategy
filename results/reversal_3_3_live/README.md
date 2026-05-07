# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 09:50:01 EDT`
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
- Equity: `$21,829.50`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$-196.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00470000       2026-05-06                   1      3      9907.5                  9711.0        33.02          32.37      466.99        497.51          -196.5                  -1.98         80.95               21               2.0         52.84             0.0                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           91.67               12            1.95              3.95        287.75                67.07            True
  INTC          100.00               29            1.71              1.35        112.43                95.68            True
  QCOM           90.48               21            1.41              1.91        191.85                72.73            True
   KDP           83.33               18            1.28              0.26         28.45                34.76            True
  ASML           83.87               31            0.81              8.74       1541.00                46.11            True
   XEL           92.86               28            0.57              0.32         80.41                28.12            True
  MSTR           87.88               33            2.41              3.15        185.47                67.05            True
   ADI           80.00               30            0.70              2.02        414.79                34.89            True
  NXPI           68.42               19            2.37              5.03        301.40                84.51           False
  SBUX          100.00                6            2.63              1.96        105.60                31.94           False
   CEG           90.70               43            0.19              0.42        322.60                45.75           False
 GOOGL           87.50               40            0.41              1.15        397.33                37.42           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-07T09:40:01.922571-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:35:01.914408-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:30:01.925048-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T09:25:01.894252-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-07T00:00:03.858471-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-06T16:10:02.677283-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-06T16:05:02.443108-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-06T16:00:08.490329-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-06T15:55:02.698208-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-06T15:40:03.512361-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507095001)

</details>

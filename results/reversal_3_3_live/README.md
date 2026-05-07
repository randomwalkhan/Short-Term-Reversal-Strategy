# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 09:40:01 EDT`
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
  CRWD     option         option CRWD260618C00470000       2026-05-06                   1      3      9907.5                  9711.0        33.02          32.37      466.99        494.95          -196.5                  -1.98         80.95               21               2.0         52.84             0.0                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               29            1.68              1.33        112.44                95.68            True
   TXN           90.91               22            1.26              2.55        288.35                67.07            True
  QCOM           87.50               16            1.80              2.43        191.62                72.73            True
   XEL           95.65               23            0.73              0.41         80.37                28.12            True
   KDP           83.33               18            1.12              0.22         28.46                34.76            True
  SBUX          100.00               11            2.14              1.60        105.76                31.94            True
  MSTR           89.19               37            1.80              2.35        185.81                67.05            True
  NXPI           77.42               31            0.96              2.03        302.68                84.51           False
 CMCSA           91.67               36            0.04              0.01         26.44                61.67           False
  ASML           86.11               36            0.45              4.86       1542.66                46.11           False
   ADI           81.25               32            0.62              1.82        414.88                34.89           False
  MCHP           83.33               30            1.06              0.77        102.64                46.15           False
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

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507094001)

</details>

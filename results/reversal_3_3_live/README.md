# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-06 15:35:07 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$21,906.00`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$-120.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00470000       2026-05-06                   0      3      9907.5                  9787.5        33.02          32.62      466.99        467.22          -120.0                  -1.21         80.95               21               2.0         52.84           52.44                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  TEAM     option         option TEAM260618C00090000     11          2026-05-05         2026-05-06         9.65       8.685 -1061.499958       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           88.57               35            1.17              1.29        157.68               118.74            True
    ZS           82.61               23            2.17              2.15        140.44                69.30            True
  MSTR           87.80               41            0.89              1.16        186.40                66.92            True
   XEL           94.44               18            0.91              0.52         81.23                28.13            True
  SHOP           86.96               23            2.50              1.89        106.81                83.08            True
  CRWD           80.95               21            1.95              6.52        473.74                50.97            True
   KDP           85.00               20            1.02              0.21         28.83                34.27            True
  TEAM           78.26               23            3.93              2.54         91.26               119.37           False
  SNPS           97.56               41            0.32              1.11        502.03                50.17           False
  ADBE           76.47               17            2.30              4.11        253.86                46.79           False
   ADP           78.95               19            1.46              2.16        209.68                37.68           False
   BKR           61.54               13            1.65              0.78         67.45                35.93           False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                         detail
2026-05-06T15:35:07.469158-04:00 manage_1530            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T15:30:02.784375-04:00 manage_1530            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T15:25:01.987747-04:00 manage_1530            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T15:10:01.990575-04:00  entry_1500            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T15:05:02.040467-04:00  entry_1500            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T15:00:04.914832-04:00  entry_1500            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T14:55:01.390762-04:00  entry_1500            slot_skipped                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-06T14:50:06.542235-04:00  entry_1500 entry_candidate_skipped               {"option_liquidity_status": "wide_spread", "option_open_interest": 634.0, "option_spread_pct": 18.18, "option_volume": 128.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.574}
2026-05-06T14:50:06.542235-04:00  entry_1500          timing_overlay                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-06", "training_samples": 5546, "window": 5}
2026-05-06T14:50:06.542235-04:00  entry_1500 entry_candidate_skipped {"option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 18.0, "option_spread_pct": 7.47, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.738}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506153507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506153507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506153507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506153507)

</details>

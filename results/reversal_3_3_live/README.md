# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-06 15:30:02 EDT`
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
  CRWD     option         option CRWD260618C00470000       2026-05-06                   0      3      9907.5                  9787.5        33.02          32.62      466.99        466.14          -120.0                  -1.21         80.95               21               2.0         52.84           53.23                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  TEAM     option         option TEAM260618C00090000     11          2026-05-05         2026-05-06         9.65       8.685 -1061.499958       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           88.89               36            1.07              1.18        157.72               118.74            True
    ZS           80.95               21            2.28              2.26        140.39                69.30            True
   XEL           93.33               15            1.04              0.60         81.19                28.13            True
  SHOP           86.96               23            2.49              1.88        106.81                83.08            True
  MSTR           87.50               40            1.22              1.60        186.22                66.92            True
   KDP           83.33               18            1.12              0.23         28.82                34.27            True
  CRWD           80.95               21            2.12              7.07        473.50                50.97            True
  PANW           86.49               37            0.65              0.83        183.62                45.58            True
  TMUS           85.71               35            0.65              0.89        193.97                36.92            True
 CMCSA           91.67               36            0.02              0.00         26.46                61.75           False
  TEAM           78.26               23            3.97              2.57         91.25               119.37           False
  SNPS           97.56               41            0.30              1.04        502.06                50.17           False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                                    detail
2026-05-06T15:30:02.784375-04:00 manage_1530            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T15:25:01.987747-04:00 manage_1530            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T15:10:01.990575-04:00  entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T15:05:02.040467-04:00  entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T15:00:04.914832-04:00  entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T14:55:01.390762-04:00  entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-05-06T14:50:06.542235-04:00  entry_1500 entry_candidate_skipped            {"option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 18.0, "option_spread_pct": 7.47, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.738}
2026-05-06T14:50:06.542235-04:00  entry_1500          timing_overlay                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-06", "training_samples": 5546, "window": 5}
2026-05-06T14:50:06.542235-04:00  entry_1500 entry_candidate_skipped                          {"option_liquidity_status": "wide_spread", "option_open_interest": 634.0, "option_spread_pct": 18.18, "option_volume": 128.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.574}
2026-05-06T14:50:06.542235-04:00  entry_1500 entry_candidate_skipped {"option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 17.0, "option_spread_pct": 15.09, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ZS", "timing_score": 0.549}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506153002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506153002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506153002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506153002)

</details>

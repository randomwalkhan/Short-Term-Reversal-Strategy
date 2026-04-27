# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 17:05:07 EDT`
Last processed slot: `share_ext_1705`

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

- Cash: `$6,573.50`
- Equity: `$13,073.50`
- Realized PnL: `$3,125.50`
- Unrealized PnL: `$-52.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode           instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
 CMCSA     option         option CMCSA260618C00027500       2026-04-27                   0     52      6552.0                  6500.0         1.26           1.25       27.36          27.5           -52.0                  -0.79         91.67               24              0.55         32.42           31.01                  60.91                 871.0           87.0               0.03                      ok
```

## Today's Closed Trades (2026-04-27)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct           exit_reason
   TXN     option         option TXN260618C00280000      4          2026-04-24         2026-04-27       14.475      12.175 -920.0  -15.889465 stop_loss_hit_at_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T16:10:05.210604-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-27T16:05:09.393931-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-27T16:00:09.657283-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-27T15:55:07.763445-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-27T15:40:07.694980-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-27T15:35:07.539962-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-27T15:30:04.079813-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-27T15:25:07.581352-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-27T15:10:04.191055-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-27T15:05:07.808930-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427170507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427170507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427170507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427170507)

</details>

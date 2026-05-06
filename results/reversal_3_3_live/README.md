# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-06 15:55:02 EDT`
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
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$12,118.50`
- Equity: `$21,831.00`
- Realized PnL: `$12,026.00`
- Unrealized PnL: `$-195.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00470000       2026-05-06                   0      3      9907.5                  9712.5        33.02          32.38      466.99        468.16          -195.0                  -1.97         80.95               21               2.0         52.84           51.29                  50.97                3216.0          255.0               0.05                      ok
```

## Today's Closed Trades (2026-05-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  TEAM     option         option TEAM260618C00090000     11          2026-05-05         2026-05-06         9.65       8.685 -1061.499958       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           89.19               37            0.98              1.09        157.76               118.74            True
   XEL           91.67               12            1.13              0.64         81.17                28.13            True
    ZS           81.48               27            1.85              1.83        140.58                69.30            True
  SHOP           89.66               29            1.84              1.39        107.02                83.08            True
  CRWD           80.95               21            1.97              6.57        473.72                50.97            True
  ADSK           83.33               12            2.79              4.87        247.34                46.09            True
   KDP           82.35               17            1.37              0.28         28.80                34.27            True
  TMUS           84.85               33            0.68              0.93        193.95                36.92            True
 CMCSA           91.18               34            0.09              0.02         26.45                61.75           False
  TEAM           78.26               23            3.90              2.52         91.27               119.37           False
    EA           85.71               14            0.41              0.58        201.32                 4.03           False
  ADBE           77.78               18            2.19              3.91        253.94                46.79           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-06T15:55:02.698208-04:00 manage_1600 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:40:03.512361-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:35:07.469158-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:30:02.784375-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:25:01.987747-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:10:01.990575-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:05:02.040467-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T15:00:04.914832-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T14:55:01.390762-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T14:50:06.542235-04:00  entry_1500        entry {"allocated_cash": 9907.5, "asset_type": "option", "contract_symbol": "CRWD260618C00470000", "contracts": 3, "entry_option_price": 33.025, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 3216.0, "option_spread_pct": 4.69, "option_volume": 255.0, "success_rate": 80.95, "ticker": "CRWD", "timing_score": 0.537}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506155502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506155502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506155502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506155502)

</details>

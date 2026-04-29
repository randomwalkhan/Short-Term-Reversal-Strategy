# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 14:55:05 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$9,532.50`
- Equity: `$16,752.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$-20.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00450000       2026-04-29                   0      2      7240.0                  7220.0         36.2           36.1      452.38        452.33           -20.0                  -0.28          85.0               40              0.57         51.94           51.98                   53.3                2047.0          316.0               0.03                      ok
```

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  AXON           80.00               35            1.25              3.54        404.79                69.13            True
   CSX           80.00               15            1.27              0.40         45.06                28.77            True
  SNPS           94.44               36            0.75              2.56        482.79                50.93            True
  FAST           84.62               13            2.23              0.70         44.38                39.66            True
  CRWD           85.00               40            0.67              2.13        454.08                53.30            True
 CMCSA          100.00                1            3.54              0.69         27.36                60.29           False
   XEL           88.89                9            1.46              0.81         79.13                20.53           False
    ZS           83.33               48            0.37              0.36        135.92                65.17           False
  INTU           72.00               25            1.97              5.53        398.01                55.13           False
  SHOP           95.56               45            0.20              0.17        121.98                56.59           False
  AMAT           86.84               38            0.23              0.61        380.60                49.43           False
  NFLX           91.30               46            0.10              0.06         92.27                46.23           False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                                                                                                                                                                         detail
2026-04-29T14:55:05.139248-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:50:04.147895-04:00  entry_1500                   entry {"allocated_cash": 7240.0, "asset_type": "option", "contract_symbol": "CRWD260618C00450000", "contracts": 2, "entry_option_price": 36.2, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 2047.0, "option_spread_pct": 3.04, "option_volume": 316.0, "success_rate": 85.0, "ticker": "CRWD", "timing_score": 0.528}
2026-04-29T14:50:04.147895-04:00  entry_1500 entry_candidate_skipped                                                                                                                                                                 {"option_liquidity_status": "low_volume", "option_open_interest": 229.0, "option_spread_pct": 11.07, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "AXON", "timing_score": 0.536}
2026-04-29T14:50:04.147895-04:00  entry_1500          timing_overlay                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-29", "training_samples": 5504, "window": 5}
2026-04-29T14:40:03.710393-04:00 manage_1430            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:35:04.143140-04:00 manage_1430            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:30:01.439060-04:00 manage_1430            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:25:04.993410-04:00 manage_1430            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:10:06.997817-04:00 manage_1400            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:05:05.131403-04:00 manage_1400            slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429145505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429145505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429145505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429145505)

</details>

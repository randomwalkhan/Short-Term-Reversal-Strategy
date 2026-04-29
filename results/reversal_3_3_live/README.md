# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 15:55:03 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$9,532.50`
- Equity: `$16,957.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$185.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00450000       2026-04-29                   0      2      7240.0                  7425.0         36.2          37.12      452.38        452.35           185.0                   2.56          85.0               40              0.57         51.94           53.54                   53.3                2047.0          316.0               0.03                      ok
```

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
    ZS           81.08               37            0.94              0.90        135.69                65.17            True
  FAST           85.71               14            2.13              0.67         44.39                39.66            True
   CSX           80.00               15            1.20              0.38         45.07                28.77            True
  SNPS           94.87               39            0.53              1.80        483.12                50.93            True
   XEL           94.74               19            0.88              0.49         79.27                20.53            True
  CRWD           85.00               40            0.64              2.04        454.11                53.30            True
   AEP           95.00               20            0.86              0.82        135.24                15.27            True
  SHOP           95.12               41            0.64              0.55        121.81                56.59            True
   HON           88.89               18            1.28              1.91        212.11                25.70            True
  ISRG          100.00               11            2.73              8.92        462.82                36.73            True
 CMCSA          100.00                2            3.02              0.58         27.40                60.29           False
  INTU           75.00               28            1.60              4.49        398.46                55.13           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                         detail
2026-04-29T15:55:03.440219-04:00 manage_1600 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:40:05.909113-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:35:01.161957-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:30:01.150324-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:25:02.112734-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:10:01.145829-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:05:05.153851-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T15:00:05.120623-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:55:05.139248-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-04-29T14:50:04.147895-04:00  entry_1500        entry {"allocated_cash": 7240.0, "asset_type": "option", "contract_symbol": "CRWD260618C00450000", "contracts": 2, "entry_option_price": 36.2, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 2047.0, "option_spread_pct": 3.04, "option_volume": 316.0, "success_rate": 85.0, "ticker": "CRWD", "timing_score": 0.528}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429155503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429155503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429155503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429155503)

</details>

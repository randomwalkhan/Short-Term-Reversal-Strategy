# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 10:45:01 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$8,357.50`
- Equity: `$17,807.50`
- Realized PnL: `$5,567.50`
- Unrealized PnL: `$2,240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260618C00095000       2026-04-30                   1      7      7210.0                  9450.0         10.3           13.5       94.02         99.09          2240.0                  31.07         100.0               38              0.77         78.24           80.36                   91.3               17799.0         2068.0               0.01                      ok
```

## Today's Closed Trades (2026-05-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ORLY           83.33               18            1.34              0.93         99.00                32.49            True
  FANG          100.00               22            1.29              1.86        204.83                30.31            True
   ADP           81.48               27            0.76              1.13        211.46                37.35            True
   ADI           80.77               26            1.09              3.06        400.95                38.22            True
  NXPI           65.00               20            1.73              3.55        292.07                84.73           False
   TXN           83.33               36            0.46              0.90        280.69                67.79           False
  FAST           97.06               34            0.13              0.04         44.91                40.12           False
  AXON           84.78               46            0.27              0.75        401.44                68.71           False
   KDP           86.21               29            0.49              0.10         29.36                34.77           False
  ASML           86.84               38            0.28              2.79       1437.79                47.82           False
   CSX           91.43               35            0.37              0.12         45.38                28.16           False
   AMD           86.49               37            0.51              1.27        353.94                60.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-01T10:40:01.653941-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-01T10:35:06.610528-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-01T10:30:01.556728-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-01T10:25:01.530323-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-05-01T10:10:01.610571-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T10:05:01.725672-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T10:00:02.530062-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T09:55:01.544131-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-01T09:40:04.657745-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-01T09:35:01.597283-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501104501)

</details>

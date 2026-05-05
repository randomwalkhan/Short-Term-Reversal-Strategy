# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-05 12:10:06 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$23,087.50`
- Equity: `$23,087.50`
- Realized PnL: `$13,087.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00095000      8          2026-05-04         2026-05-05         10.7      17.475 5420.0   63.317757 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TEAM           85.71               35            2.37              1.55         92.53               121.39            True
  META           86.96               23            1.52              6.48        607.69                47.41            True
    ZS           84.09               44            0.52              0.52        141.98                69.57            True
  MSFT           82.61               23            0.99              2.88        412.39                34.18            True
  MDLZ           84.21               19            0.94              0.40         61.21                26.22            True
  PANW           86.84               38            0.55              0.71        184.25                48.03            True
  CHTR           71.43                7            3.69              4.27        163.51               118.91           False
 CMCSA           75.00                4            2.27              0.43         26.89                61.32           False
   TXN           84.62               39            0.02              0.04        280.87                67.78           False
  FAST           96.88               32            0.25              0.08         44.85                39.95           False
  GEHC           78.95               38            0.45              0.19         60.92                59.35           False
   KDP           87.50               32            0.26              0.05         28.85                34.67           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-05T12:10:06.308673-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-05T12:05:06.304003-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-05T12:00:06.748217-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-05T11:55:05.945498-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-05T11:40:06.303988-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:35:06.313311-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:33:04.017063-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:30:06.314731-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:25:06.295587-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-05T11:10:06.308576-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260505121006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260505121006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260505121006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260505121006)

</details>

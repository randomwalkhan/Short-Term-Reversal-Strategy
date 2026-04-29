# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 12:45:11 EDT`
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

- Cash: `$16,772.50`
- Equity: `$16,772.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
    ZS           83.33               30            1.51              1.44        135.45                65.17            True
  SNPS           94.74               19            2.28              7.72        480.58                50.93            True
  FAST           83.33               18            1.67              0.52         44.45                39.66            True
  WDAY           83.72               43            0.89              0.76        120.86                63.12            True
  CDNS           92.00               25            1.77              4.04        323.61                53.80            True
   CSX           85.00               20            1.07              0.34         45.08                28.77            True
  ADSK           85.71               28            1.29              2.13        233.94                45.23            True
 CMCSA          100.00                7            1.50              0.29         27.53                60.29           False
  CHTR           80.00                5            4.09              4.96        170.89               113.02           False
  ASML           87.18               39            0.20              1.94       1383.73                50.71           False
  MSFT           75.00               12            1.67              5.02        427.10                30.07           False
  INTU           74.07               27            1.73              4.84        398.30                55.13           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-29T12:40:11.745307-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:35:07.057965-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:30:04.773295-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:25:04.979686-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:10:08.034825-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T12:05:04.313090-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T12:00:06.336773-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T11:55:05.214410-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T11:40:04.893859-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-29T11:35:04.084627-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429124511)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429124511)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429124511)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429124511)

</details>

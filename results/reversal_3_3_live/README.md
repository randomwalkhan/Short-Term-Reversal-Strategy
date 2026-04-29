# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 14:10:06 EDT`
Last processed slot: `manage_1400`

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
   KDP           87.50               24            0.68              0.14         28.76                36.44            True
    ZS           82.86               35            1.30              1.24        135.54                65.17            True
  CRWD           81.48               27            1.51              4.82        452.92                53.30            True
  SNPS           96.15               26            1.76              5.96        481.33                50.93            True
  FAST           86.67               15            2.08              0.65         44.40                39.66            True
  SHOP           93.75               32            1.33              1.13        121.56                56.59            True
   CSX           87.50               24            0.87              0.28         45.11                28.77            True
  CDNS           94.74               38            0.76              1.73        324.60                53.80            True
   HON           84.62               13            1.45              2.17        212.00                25.70            True
   XEL           92.00               25            0.67              0.37         79.32                20.53            True
  ADSK           88.57               35            0.86              1.42        234.24                45.23            True
  UPRO           90.32               31            1.18              1.04        125.25                42.06            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-29T14:10:06.997817-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T14:05:05.131403-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T14:00:12.028983-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T13:55:05.166783-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-29T13:40:10.019029-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:35:08.054699-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:30:12.365677-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:25:10.874925-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:10:07.449671-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T13:05:10.681495-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429141006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429141006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429141006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429141006)

</details>

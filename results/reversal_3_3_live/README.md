# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 10:50:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$13,125.50`
- Equity: `$13,125.50`
- Realized PnL: `$3,125.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-27)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct           exit_reason
   TXN     option         option TXN260618C00280000      4          2026-04-24         2026-04-27       14.475      12.175 -920.0  -15.889465 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           91.89               37            0.88              1.11        179.66               113.10            True
   KDP           84.21               19            1.10              0.22         29.12                32.43            True
   MAR           86.36               22            1.21              3.10        365.82                31.82            True
   WMT           86.96               23            1.01              0.92        129.53                25.05            True
  AVGO           91.67               24            1.74              5.16        420.55                42.01            True
  ROST           96.55               29            0.55              0.87        226.04                25.80            True
   TXN           77.78                9            2.77              5.38        274.86                67.06           False
  UPRO           92.68               41            0.13              0.11        126.94                48.54           False
  TEAM           82.00               50            0.33              0.16         71.48                79.96           False
  SHOP           95.56               45            0.20              0.17        125.76                57.21           False
    ZS           81.63               49            0.18              0.17        135.43                69.32           False
  CSCO           86.67               30            0.29              0.18         88.93                28.51           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-27T10:40:05.458641-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:35:01.494241-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:30:01.499388-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:25:04.454229-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:20:02.444364-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00280000", "fill_price": 12.175, "pnl": -920.0, "reason": "stop_loss_hit_at_scan", "return_pct": -15.89, "ticker": "TXN"}
2026-04-27T10:10:05.431763-04:00 manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:05:01.450003-04:00 manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:00:06.086949-04:00 manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:55:04.282451-04:00 manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:40:04.365918-04:00 manage_0930 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427105001)

</details>

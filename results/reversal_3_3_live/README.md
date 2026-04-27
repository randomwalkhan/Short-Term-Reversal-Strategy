# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 10:20:02 EDT`
Last processed slot: `manage_1030`

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
  CHTR           91.89               37            0.84              1.06        179.68               113.10            True
   KDP           85.71               14            1.64              0.34         29.08                32.43            True
   WMT           86.96               23            0.97              0.88        129.54                25.05            True
  KLAC           85.00               20            2.27             30.76       1921.82                47.17            True
  AAPL           85.00               20            1.28              2.43        270.02                26.22            True
   HON          100.00               21            1.09              1.62        212.46                25.73            True
   MAR           88.89               27            1.07              2.74        365.97                31.82            True
   TXN           77.78                9            2.77              5.37        274.87                67.06           False
 CMCSA           93.33               30            0.18              0.03         27.50                60.91           False
  UPRO           92.50               40            0.22              0.20        126.91                48.54           False
   ADI           71.43               14            2.12              5.93        397.03                38.91           False
  SHOP           95.45               44            0.41              0.36        125.68                57.21           False
```

## Recent Events

```text
                    timestamp_et           slot   event_type                                                                                                                                                                           detail
2026-04-27T10:20:02.444364-04:00    manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00280000", "fill_price": 12.175, "pnl": -920.0, "reason": "stop_loss_hit_at_scan", "return_pct": -15.89, "ticker": "TXN"}
2026-04-27T10:10:05.431763-04:00    manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:05:01.450003-04:00    manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:00:06.086949-04:00    manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:55:04.282451-04:00    manage_1000 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:40:04.365918-04:00    manage_0930 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:35:01.383848-04:00    manage_0930 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:30:01.445280-04:00    manage_0930 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T09:25:03.410352-04:00    manage_0930 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T02:43:32.046615-04:00 share_ext_0240 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427102002)

</details>

# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 14:20:04 EDT`
Last processed slot: `manage_1430`

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
   KDP           83.33               12            1.76              0.36         29.07                32.43            True
   WDC           97.44               39            0.71              2.01        403.14                62.15            True
   WMT           84.62               13            1.58              1.43        129.31                25.05            True
  SHOP           94.12               34            1.26              1.11        125.35                57.21            True
  AVGO           91.67               24            1.62              4.78        420.71                42.01            True
   MAR           83.33               12            2.11              5.42        364.83                31.82            True
  CSCO           82.35               17            1.26              0.79         88.67                28.51            True
  ASML           81.82               22            2.35             23.97       1447.43                51.44            True
  ISRG           86.67               15            2.12              7.17        479.15                37.71            True
   TXN           66.67                6            3.27              6.34        274.45                67.06           False
 CMCSA           93.33               30            0.22              0.04         27.50                60.91           False
  CHTR           70.00               10            3.02              3.81        178.50               113.10           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T14:10:01.492312-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-27T14:05:03.452029-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-27T14:00:05.386547-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-27T13:55:01.507336-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-27T13:40:01.413909-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:35:05.278374-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:30:03.802245-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:25:05.720735-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:10:08.731273-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T13:05:09.458541-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427142004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427142004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427142004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427142004)

</details>

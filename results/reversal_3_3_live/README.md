# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-04 14:45:09 EDT`
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

- Cash: `$17,667.50`
- Equity: `$17,667.50`
- Realized PnL: `$7,667.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           88.57               35            1.13              1.35        171.16               118.68            True
 CMCSA           88.00               25            0.52              0.10         27.12                61.39            True
  INTC          100.00               20            3.25              2.26         98.64                90.80            True
  AXON           84.62               39            0.77              2.17        401.38                68.18            True
   WMT           88.24               17            1.29              1.19        131.09                27.95            True
  ISRG           94.12               17            1.70              5.44        455.45                36.31            True
   KDP           81.25               16            1.39              0.28         28.97                34.45            True
  NFLX           87.50               32            0.84              0.54         91.83                43.43            True
  MRVL          100.00               35            0.58              0.66        164.66                47.49            True
   CSX           80.95               21            1.09              0.34         44.95                28.27            True
  TMUS           84.62               26            1.10              1.51        195.41                37.34            True
   ADI           81.25               32            0.60              1.68        396.97                38.53            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-04T14:40:09.470745-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-04T14:35:09.922061-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-04T14:30:09.366130-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-04T14:25:09.855763-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-05-04T14:10:09.093734-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T14:05:09.193507-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T14:00:08.800470-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T13:55:10.029925-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T13:40:09.680336-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-04T13:35:08.919053-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260504144509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260504144509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260504144509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260504144509)

</details>

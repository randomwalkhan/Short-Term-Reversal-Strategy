# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-04 14:20:09 EDT`
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
  CHTR           84.62               26            1.56              1.87        170.94               118.68            True
 CMCSA           90.48               21            0.72              0.14         27.11                61.39            True
  INTC          100.00               24            2.70              1.88         98.80                90.80            True
  SOXL           82.14               28            2.11              1.93        129.57                93.95            True
  NFLX           88.00               25            1.09              0.70         91.76                43.43            True
  AXON           85.37               41            0.69              1.96        401.47                68.18            True
  ISRG           94.44               18            1.58              5.07        455.61                36.31            True
   KDP           82.35               17            1.31              0.27         28.98                34.45            True
   WMT           89.47               19            1.18              1.08        131.14                27.95            True
  MRVL          100.00               36            0.54              0.63        164.68                47.49            True
  TMUS           84.00               25            1.16              1.60        195.38                37.34            True
  MPWR           89.29               28            1.46             16.17       1576.55                53.29            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-04T14:10:09.093734-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T14:05:09.193507-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T14:00:08.800470-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T13:55:10.029925-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-04T13:40:09.680336-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-04T13:35:08.919053-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-04T13:30:06.628773-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-04T09:28:28.007436-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-04T09:20:06.330074-04:00 data_refresh data_refresh                   {'saved': 99}
2026-05-01T14:10:01.750184-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260504142009)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260504142009)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260504142009)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260504142009)

</details>

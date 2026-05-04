# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-04 12:30:26 EDT`
Last processed slot: `manage_1230`

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
  INTC          100.00               24            2.58              1.80         98.84                90.80            True
  AXON           82.86               35            1.22              3.43        400.84                68.18            True
  ISRG           94.12               17            1.63              5.24        455.54                36.31            True
   WMT           88.24               17            1.30              1.20        131.09                27.95            True
   KDP           86.36               22            0.95              0.19         29.01                34.45            True
   ADP           84.00               25            0.91              1.37        213.62                37.25            True
   AEP           92.31               13            1.21              1.16        136.41                16.88            True
  MRVL          100.00               31            0.98              1.13        164.46                47.49            True
  MPWR           90.00               30            1.08             11.96       1578.35                53.29            True
  NFLX           89.19               37            0.67              0.43         91.88                43.43            True
  ORLY           86.67               15            1.75              1.19         96.14                34.19            True
  TMUS           85.71               28            0.98              1.34        195.48                37.34            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-04T09:28:28.007436-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-04T09:20:06.330074-04:00 data_refresh data_refresh                   {'saved': 99}
2026-05-01T14:10:01.750184-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T14:05:02.593188-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T14:00:02.753183-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:55:05.465592-04:00  manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:40:06.684351-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:35:01.746076-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:30:03.675917-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:25:02.795278-04:00  manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260504123026)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260504123026)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260504123026)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260504123026)

</details>

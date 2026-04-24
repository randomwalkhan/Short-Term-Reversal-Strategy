# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 10:40:05 EDT`
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

- Cash: `$14,045.50`
- Equity: `$14,045.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  NVDA     option         option NVDA260618C00200000      5          2026-04-23         2026-04-24       12.325      14.475 1075.0   17.444219 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           81.82               11            2.60              5.14        280.03                66.99            True
   WMT           88.89               18            1.20              1.11        131.56                24.33            True
  DDOG           89.29               28            1.81              1.62        127.16                60.38            True
  MSTR           80.95               42            0.59              0.71        172.16                74.46            True
  PLTR           89.47               38            0.93              0.92        141.18                64.15            True
   CSX           87.50               24            0.76              0.24         46.08                27.21            True
   HON          100.00               10            1.67              2.51        213.26                25.71            True
  AVGO           93.33               30            1.24              3.65        418.37                44.94            True
  CRWD           73.91               23            1.93              6.01        442.82                59.30           False
  NFLX           95.00               40            0.46              0.30         92.69                46.09           False
    ZS           76.32               38            0.93              0.86        132.60                69.17           False
  AXON           71.43               35            1.40              3.84        391.00                71.24           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                   detail
2026-04-24T10:40:05.045051-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:35:02.034739-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:30:05.226988-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:25:05.335841-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:20:01.416891-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "NVDA260618C00200000", "fill_price": 14.475, "pnl": 1075.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.44, "ticker": "NVDA"}
2026-04-24T10:10:06.140592-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:05:05.170858-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:00:03.243449-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T09:55:04.947426-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T09:40:04.006761-04:00 manage_0930 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424104005)

</details>

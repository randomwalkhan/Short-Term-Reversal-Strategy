# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 10:45:01 EDT`
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
   WMT           87.50               16            1.34              1.24        131.50                24.33            True
  PLTR           89.74               39            0.61              0.61        141.31                64.15            True
  DDOG           86.67               30            1.48              1.32        127.29                60.38            True
   HON          100.00               12            1.46              2.20        213.40                25.71            True
   CSX           86.96               23            0.96              0.31         46.05                27.21            True
  FAST           92.31               39            0.53              0.17         45.38                38.70            True
   TXN           75.00                8            2.86              5.65        279.81                66.99           False
  AXON           74.36               39            0.84              2.30        391.66                71.24           False
  CRWD           73.33               30            1.45              4.51        443.46                59.30           False
  MSTR           81.40               43            0.38              0.45        172.28                74.46           False
  NFLX           95.24               42            0.41              0.27         92.70                46.09           False
    ZS           79.17               48            0.40              0.37        132.81                69.17           False
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

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424104501)

</details>

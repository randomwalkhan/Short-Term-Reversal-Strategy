# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 11:05:04 EDT`
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
  NFLX           92.86               28            0.97              0.63         92.55                46.09            True
   WMT           87.50               16            1.39              1.28        131.48                24.33            True
  PLTR           89.74               39            0.61              0.60        141.31                64.15            True
  FAST           90.91               33            0.73              0.23         45.35                38.70            True
   CSX           86.96               23            0.91              0.30         46.05                27.21            True
  DDOG           86.11               36            1.10              0.99        127.44                60.38            True
  SBUX           92.86               28            0.95              0.67         99.25                31.25            True
  MRVL           96.15               26            1.98              2.29        164.58                67.12            True
   ADI           82.35               34            0.65              1.84        403.09                40.58            True
   TXN           60.00                5            3.42              6.76        279.33                66.99           False
  AXON           73.68               38            0.95              2.62        391.52                71.24           False
    ZS           75.61               41            0.83              0.78        132.64                69.17           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                   detail
2026-04-24T11:05:04.237988-04:00 manage_1100 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T11:00:06.205625-04:00 manage_1100 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:55:02.045514-04:00 manage_1100 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:40:05.045051-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:35:02.034739-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:30:05.226988-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:25:05.335841-04:00 manage_1030 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:20:01.416891-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "NVDA260618C00200000", "fill_price": 14.475, "pnl": 1075.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.44, "ticker": "NVDA"}
2026-04-24T10:10:06.140592-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
2026-04-24T10:05:05.170858-04:00 manage_1000 slot_skipped                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424110504)

</details>

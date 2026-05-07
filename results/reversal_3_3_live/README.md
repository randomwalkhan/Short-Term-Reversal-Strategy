# Reversal 3.3.1 Live Paper Test

Latest checkpoint (ET): `2026-05-07 10:55:01 EDT`
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
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$27,583.50`
- Equity: `$27,583.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CRWD     option         option CRWD260618C00470000      3          2026-05-06         2026-05-07       33.025       51.55 5557.5   56.093868 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           90.91               11            2.20              4.46        287.53                67.07            True
   KDP           83.33               12            1.77              0.35         28.41                34.76            True
  SOXL           82.14               28            2.51              2.91        164.60                95.28            True
  MSTR           88.24               34            2.31              3.02        185.53                67.05            True
  ROST           92.86               14            1.35              2.16        227.98                15.20            True
  NXPI           64.29               14            2.76              5.86        301.04                84.51           False
  SBUX          100.00                9            2.37              1.76        105.68                31.94           False
  ASML           86.84               38            0.31              3.35       1543.31                46.11           False
 GOOGL           88.37               43            0.21              0.59        397.57                37.42           False
  GOOG           88.10               42            0.28              0.77        394.74                37.75           False
   ADI           78.26               23            1.47              4.29        413.82                34.89           False
   CEG           89.74               39            0.60              1.36        322.20                45.75           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                  detail
2026-05-07T10:55:01.919462-04:00 manage_1100 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:40:06.740458-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:35:01.914574-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:30:05.917191-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:25:01.892823-04:00 manage_1030 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:20:01.930498-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "CRWD260618C00470000", "fill_price": 51.55, "pnl": 5557.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 56.09, "ticker": "CRWD"}
2026-05-07T10:10:04.036694-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:05:04.033139-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T10:00:03.903840-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
2026-05-07T09:55:02.556058-04:00 manage_1000 slot_skipped                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260507105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260507105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260507105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260507105501)

</details>

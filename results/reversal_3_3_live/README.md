# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 11:15:04 EDT`
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

- Cash: `$16,772.50`
- Equity: `$16,772.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CDNS          100.00               12            2.77              6.31        322.63                53.80            True
  SNPS           94.74               19            2.27              7.69        480.60                50.93            True
  FAST           86.36               22            1.44              0.45         44.48                39.66            True
   XEL           95.24               21            0.83              0.46         79.28                20.53            True
  ADSK           85.71               28            1.26              2.08        233.96                45.23            True
  WDAY           82.93               41            1.13              0.96        120.77                63.12            True
  DDOG           90.00               30            1.40              1.29        131.00                52.25            True
   CSX           88.00               25            0.78              0.25         45.12                28.77            True
  SHOP           93.75               32            1.34              1.14        121.56                56.59            True
 CMCSA          100.00                7            1.63              0.31         27.52                60.29           False
  CHTR           80.00                5            4.14              5.01        170.87               113.02           False
  CRWD           79.17               24            1.64              5.23        452.75                53.30           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-29T11:10:03.826422-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T11:05:04.165460-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T11:00:04.760456-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:55:04.247793-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:40:05.649444-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:35:07.394496-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:30:03.700381-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:25:04.185468-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:20:03.810424-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "INTC260529C00084000", "fill_price": 8.85, "pnl": 1775.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.09, "ticker": "INTC"}
2026-04-29T10:10:03.767251-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429111504)

</details>

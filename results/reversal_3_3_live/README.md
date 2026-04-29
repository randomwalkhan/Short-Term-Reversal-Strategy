# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 10:30:03 EDT`
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
  SNPS           92.86               28            1.53              5.19        481.67                50.93            True
  FAST           86.96               23            1.41              0.44         44.49                39.66            True
   XEL           95.24               21            0.84              0.47         79.28                20.53            True
  CDNS           88.24               17            2.51              5.72        322.89                53.80            True
  CRWD           82.35               34            1.13              3.61        453.44                53.30            True
  SHOP           93.55               31            1.47              1.26        121.51                56.59            True
  ADSK           88.89               36            0.81              1.33        234.28                45.23            True
   PEP           83.33               12            1.36              1.49        155.65                18.45            True
 CMCSA          100.00                8            1.43              0.28         27.53                60.29           False
  CHTR           75.00               12            2.73              3.31        171.60               113.02           False
  INTU           72.00               25            1.90              5.32        398.10                55.13           False
    ZS           77.27               22            2.68              2.55        134.98                65.17           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-29T10:30:03.700381-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:25:04.185468-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:20:03.810424-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "INTC260529C00084000", "fill_price": 8.85, "pnl": 1775.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.09, "ticker": "INTC"}
2026-04-29T10:10:03.767251-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:05:08.240355-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:00:04.620825-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:55:04.061412-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:40:03.886159-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:35:04.233499-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:30:03.967315-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429103003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429103003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429103003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429103003)

</details>

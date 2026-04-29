# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 10:50:08 EDT`
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
  CDNS          100.00               12            2.82              6.41        322.59                53.80            True
   XEL           92.31               13            1.14              0.64         79.21                20.53            True
   KDP           87.50               24            0.75              0.15         28.76                36.44            True
  SNPS           95.65               23            2.06              6.97        480.90                50.93            True
  FAST           81.25               16            1.85              0.58         44.43                39.66            True
  CRWD           82.35               34            1.15              3.65        453.43                53.30            True
  ADSK           87.50               32            0.94              1.54        234.19                45.23            True
  SHOP           93.55               31            1.43              1.22        121.53                56.59            True
 CMCSA          100.00                7            1.54              0.30         27.52                60.29           False
  CHTR           62.50                8            3.17              3.84        171.37               113.02           False
  INTU           72.00               25            2.01              5.62        397.97                55.13           False
    ZS           77.27               22            2.78              2.65        134.94                65.17           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-04-29T10:40:05.649444-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:35:07.394496-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:30:03.700381-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:25:04.185468-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:20:03.810424-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "INTC260529C00084000", "fill_price": 8.85, "pnl": 1775.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.09, "ticker": "INTC"}
2026-04-29T10:10:03.767251-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:05:08.240355-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T10:00:04.620825-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:55:04.061412-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-04-29T09:40:03.886159-04:00 manage_0930 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429105008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429105008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429105008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429105008)

</details>

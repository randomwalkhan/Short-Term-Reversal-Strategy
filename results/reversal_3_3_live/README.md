# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-30 12:46:51 EDT`
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

- Cash: `$15,567.50`
- Equity: `$15,567.50`
- Realized PnL: `$5,567.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CRWD     option         option CRWD260618C00450000      2          2026-04-29         2026-04-30         36.2      30.175 -1205.0  -16.643646 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NXPI           80.00               35            0.79              1.60        288.56                85.25            True
  INTC          100.00               33            1.42              0.94         94.35                91.30            True
  AXON           82.86               35            1.15              3.21        399.16                68.68            True
  CDNS           97.06               34            1.11              2.56        328.85                53.49            True
  WDAY           81.58               38            1.45              1.24        121.90                63.16            True
  FTNT           87.50               16            2.11              1.27         85.56                38.28            True
  PLTR           90.24               41            0.06              0.06        137.95                55.72           False
  SNPS           97.67               43            0.03              0.10        481.18                50.55           False
  CRWD           77.27               22            1.94              6.15        449.75                53.11           False
  INTU           70.00               20            2.42              6.68        392.22                55.07           False
  SHOP           95.00               40            0.94              0.80        120.92                52.79           False
  PANW           76.00               25            1.59              2.03        180.67                47.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                              detail
2026-04-30T12:30:16.917018-04:00 manage_1230 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:35:01.336447-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:30:02.465737-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:25:26.566050-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:02:03.888950-04:00 manage_1100         exit {"asset_type": "option", "contract_symbol": "CRWD260618C00450000", "fill_price": 30.175, "pnl": -1205.0, "reason": "stop_loss_hit_at_scan", "return_pct": -16.64, "ticker": "CRWD"}
2026-04-30T10:25:03.253231-04:00 manage_1030 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T09:30:01.723685-04:00 manage_0930 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T09:27:16.860657-04:00 manage_0930 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-29T16:10:01.130102-04:00 manage_1600 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-29T16:05:02.179548-04:00 manage_1600 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260430124651)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260430124651)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260430124651)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260430124651)

</details>

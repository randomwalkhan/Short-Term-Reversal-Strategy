# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-30 14:32:17 EDT`
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
  CDNS           97.30               37            0.61              1.40        329.35                53.49            True
  WDAY           83.72               43            0.90              0.77        122.10                63.16            True
  TMUS           80.95               21            1.52              2.11        197.26                38.48            True
  FTNT           88.89               18            1.96              1.18         85.60                38.28            True
  INTC          100.00               47            0.02              0.01         94.74                91.30           False
  SNPS           97.56               41            0.24              0.81        480.87                50.55           False
  AXON           84.78               46            0.29              0.82        400.19                68.68           False
  INTU           73.91               23            2.09              5.79        392.60                55.07           False
  CRWD           76.19               21            2.18              6.89        449.43                53.11           False
  PANW           79.31               29            1.31              1.67        180.83                47.73           False
   ADP           72.22               18            1.21              1.82        214.28                37.07           False
    ZS           75.00               20            3.11              2.94        133.47                64.71           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                              detail
2026-04-30T14:32:17.011087-04:00 manage_1430 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T14:06:17.032910-04:00 manage_1400 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T13:31:16.977135-04:00 manage_1330 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T12:30:16.917018-04:00 manage_1230 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:35:01.336447-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:30:02.465737-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:25:26.566050-04:00 manage_1130 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T11:02:03.888950-04:00 manage_1100         exit {"asset_type": "option", "contract_symbol": "CRWD260618C00450000", "fill_price": 30.175, "pnl": -1205.0, "reason": "stop_loss_hit_at_scan", "return_pct": -16.64, "ticker": "CRWD"}
2026-04-30T10:25:03.253231-04:00 manage_1030 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-04-30T09:30:01.723685-04:00 manage_0930 slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260430143217)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260430143217)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260430143217)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260430143217)

</details>

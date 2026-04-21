# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 14:00:05 EDT`
Last processed slot: `manage_1400`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$11,973.99`
- Equity: `$11,973.99`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-21)

```text
ticker asset_type execution_mode instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price        pnl  return_pct           exit_reason
   HON      share share_fallback        HON     23          2026-04-20         2026-04-21   229.925003  222.725006 -165.59993   -3.131455 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
 CMCSA          100.00               14            0.94              0.20         29.65                20.07            True
  ROST           96.15               26            0.75              1.20        227.74                25.78            True
  SHOP           93.55               31            1.65              1.56        134.47                55.61            True
  NVDA           92.86               28            1.14              1.62        201.37                32.81            True
  NFLX           92.86               14            1.83              1.22         94.31                46.83            True
  ALNY           92.00               25            1.90              4.14        309.16                46.90            True
  QCOM           91.43               35            0.65              0.63        137.25                21.00            True
   MAR           90.62               32            0.90              2.38        377.70                30.20            True
  UPRO           90.32               31            1.08              0.94        124.09                53.04            True
  TMUS           88.46               26            0.87              1.20        197.84                22.76            True
  SBUX           88.24               17            1.70              1.18         98.45                31.75            True
  ASML           87.50               32            0.97             10.03       1472.20                54.76            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T14:00:05.726262-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T13:55:05.880707-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T13:40:06.427254-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:35:04.423627-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:30:05.435338-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:25:05.440820-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:10:05.422037-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T13:05:05.441291-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T13:00:06.440016-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T12:55:06.441117-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421140005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421140005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421140005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421140005)

</details>

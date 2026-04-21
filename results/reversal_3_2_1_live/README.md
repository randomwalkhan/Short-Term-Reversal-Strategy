# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 13:25:05 EDT`
Last processed slot: `manage_1330`

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
  ROST           95.45               22            0.88              1.40        227.65                25.78            True
  UPRO           92.59               27            1.64              1.43        123.88                53.04            True
  NVDA           92.31               26            1.29              1.82        201.28                32.81            True
  SHOP           92.00               25            2.56              2.42        134.10                55.61            True
  NFLX           90.91               11            2.08              1.38         94.24                46.83            True
  QCOM           90.62               32            0.81              0.78        137.18                21.00            True
   LIN           89.29               28            0.57              1.98        497.30                19.90            True
  ALNY           88.89               27            1.84              4.00        309.22                46.90            True
   MAR           88.89               27            1.10              2.90        377.48                30.20            True
  CTAS           88.24               34            0.70              0.87        178.32                25.35            True
  TMUS           87.50               32            0.63              0.87        197.99                22.76            True
  SBUX           87.50               16            1.94              1.34         98.37                31.75            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T13:25:05.440820-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:10:05.422037-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T13:05:05.441291-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T13:00:06.440016-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T12:55:06.441117-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-21T12:40:06.441688-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:35:06.426815-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:30:06.440383-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:25:04.435579-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:10:04.433255-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421132505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421132505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421132505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421132505)

</details>

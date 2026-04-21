# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 12:50:05 EDT`
Last processed slot: `manage_1300`

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
  REGN          100.00               37            0.54              2.82        748.20                22.94            True
  SHOP           94.12               34            1.35              1.27        134.59                55.61            True
  NVDA           93.55               31            0.93              1.32        201.50                32.81            True
  ALNY           93.18               44            0.69              1.51        310.29                46.90            True
  NFLX           92.31               13            2.00              1.33         94.26                46.83            True
  QCOM           91.89               37            0.57              0.55        137.28                21.00            True
  UPRO           91.18               34            0.93              0.81        124.14                53.04            True
   XEL           90.00               10            1.15              0.64         80.04                19.06            True
  SBUX           89.47               19            1.50              1.04         98.50                31.75            True
  TMUS           88.46               26            0.86              1.19        197.85                22.76            True
   MAR           88.24               34            0.83              2.20        377.78                30.20            True
   LIN           88.00               25            0.68              2.37        497.14                19.90            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T12:40:06.441688-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:35:06.426815-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:30:06.440383-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:25:04.435579-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:10:04.433255-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T12:05:06.438436-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T12:00:03.430397-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T11:55:06.424584-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T11:40:06.419812-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-21T11:35:05.427020-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421125005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421125005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421125005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421125005)

</details>

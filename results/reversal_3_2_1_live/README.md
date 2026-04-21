# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 12:30:06 EDT`
Last processed slot: `manage_1230`

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
  SHOP           94.44               36            1.31              1.24        134.61                55.61            True
  NFLX           94.12               17            1.67              1.11         94.36                46.83            True
  NVDA           93.33               30            0.97              1.36        201.48                32.81            True
  ALNY           92.11               38            1.05              2.30        309.96                46.90            True
  UPRO           91.43               35            0.85              0.74        124.17                53.04            True
   XEL           90.91               11            1.08              0.61         80.06                19.06            True
   LIN           90.00               20            0.95              3.30        496.74                19.90            True
  SBUX           88.89               18            1.52              1.05         98.50                31.75            True
  TMUS           88.46               26            0.85              1.18        197.85                22.76            True
   MAR           88.24               34            0.83              2.19        377.78                30.20            True
  CTAS           87.88               33            0.80              1.00        178.26                25.35            True
  ASML           87.50               32            1.00             10.34       1472.07                54.76            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T12:30:06.440383-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:25:04.435579-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-21T12:10:04.433255-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T12:05:06.438436-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T12:00:03.430397-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T11:55:06.424584-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-21T11:40:06.419812-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-21T11:35:05.427020-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-21T11:30:03.385825-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-21T11:25:05.699661-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421123006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421123006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421123006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421123006)

</details>

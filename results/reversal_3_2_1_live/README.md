# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 14:25:05 EDT`
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
  ROST           94.12               17            1.19              1.90        227.43                25.78            True
  SHOP           92.86               28            2.06              1.95        134.30                55.61            True
  UPRO           92.86               28            1.51              1.31        123.93                53.04            True
  NVDA           92.86               28            1.11              1.57        201.39                32.81            True
  NFLX           92.86               14            1.86              1.24         94.30                46.83            True
  QCOM           90.91               33            0.81              0.78        137.19                21.00            True
  ALNY           90.91               22            2.11              4.59        308.97                46.90            True
   MAR           88.89               27            1.11              2.94        377.46                30.20            True
  SBUX           88.24               17            1.78              1.23         98.42                31.75            True
   CSX           88.00               25            0.65              0.20         43.62                16.22            True
  ASML           87.50               32            1.08             11.18       1471.71                54.76            True
   LIN           86.67               30            0.52              1.81        497.37                19.90            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T14:25:05.717035-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-21T14:10:02.597542-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T14:05:05.877097-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T14:00:05.726262-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T13:55:05.880707-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-21T13:40:06.427254-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:35:04.423627-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:30:05.435338-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:25:05.440820-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-21T13:10:05.422037-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421142505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421142505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421142505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421142505)

</details>

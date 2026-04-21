# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 11:20:06 EDT`
Last processed slot: `manage_1130`

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
  REGN          100.00               23            1.45              7.62        746.14                22.94            True
  SHOP           95.45               44            0.55              0.53        134.91                55.61            True
   AEP           94.74               19            0.71              0.66        133.00                13.52            True
  NFLX           94.44               18            1.42              0.94         94.43                46.83            True
  ROST           94.44               18            1.17              1.87        227.45                25.78            True
  QCOM           90.91               33            0.80              0.77        137.19                21.00            True
  VRTX           90.00               40            0.55              1.69        438.46                26.84            True
  ALNY           88.89               27            1.69              3.67        309.37                46.90            True
  ISRG           88.89               18            1.65              5.38        463.29                25.78            True
  TMUS           88.46               26            0.89              1.23        197.83                22.76            True
  SBUX           88.24               17            1.65              1.14         98.46                31.75            True
   LIN           88.00               25            0.64              2.23        497.19                19.90            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                           detail
2026-04-21T11:20:06.439324-04:00 manage_1130         exit {"asset_type": "share", "contract_symbol": "HON", "fill_price": 222.725, "pnl": -165.6, "reason": "stop_loss_hit_at_scan", "return_pct": -3.13, "ticker": "HON"}
2026-04-21T11:10:03.434849-04:00 manage_1100 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T11:05:05.426636-04:00 manage_1100 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T11:00:06.434483-04:00 manage_1100 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:55:06.432974-04:00 manage_1100 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:40:06.436848-04:00 manage_1030 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:35:05.440766-04:00 manage_1030 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:30:05.716181-04:00 manage_1030 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:25:06.438286-04:00 manage_1030 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-21T10:10:06.423835-04:00 manage_1000 slot_skipped                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421112006)

</details>

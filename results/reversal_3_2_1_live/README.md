# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 14:55:03 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$539.49`
- Equity: `$13,284.48`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$-73.44`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-16                   1      9     6720.93                 6737.49       746.77         748.61      746.77        748.61           16.56                   0.25        100.00               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260529C00068000       2026-04-17                   0      9     6097.50                 6007.50         6.78           6.68       68.04         68.09          -90.00                  -1.48         94.59               37              0.66         72.85           71.34                  74.40                 143.0           74.0               0.04                                       ok
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   AEP           95.83               24            0.59              0.55        134.32                17.62            True
  INTC           94.59               37            0.69              0.33         68.36                74.40            True
  FTNT           93.33               30            1.47              0.85         82.04                40.09            True
   ROP           88.24               34            0.53              1.35        361.30                23.28            True
   PEP           88.24               17            0.97              1.07        157.92                20.28            True
   LIN           86.67               15            1.14              3.98        497.52                18.78            True
  TTWO           86.05               43            0.56              0.83        213.57                32.46            True
   CEG           83.33               36            1.07              2.25        298.18                57.36            True
  ADSK           82.93               41            0.52              0.89        242.78                43.74            True
  PAYX           82.86               35            0.99              0.64         91.86                31.23            True
  ADBE           82.76               29            1.84              3.20        246.79                38.98            True
   TRI           82.61               46            0.60              0.39         92.90                39.83            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                  detail
2026-04-17T14:55:03.734020-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:50:05.923182-04:00  entry_1500        entry {"allocated_cash": 6097.5, "asset_type": "option", "contract_symbol": "INTC260529C00068000", "contracts": 9, "entry_option_price": 6.775, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 143.0, "option_spread_pct": 3.69, "option_volume": 74.0, "success_rate": 94.59, "ticker": "INTC"}
2026-04-17T14:40:05.721864-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:35:05.695089-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:30:04.813251-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:25:05.697715-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:10:00.716098-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:05:00.716620-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T14:00:01.661535-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-17T13:55:05.710439-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417145503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417145503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417145503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417145503)

</details>
